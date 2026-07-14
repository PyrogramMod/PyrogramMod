#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import csv
from pathlib import Path
import re
import requests  # requests==2.28.1
import sys

if len(sys.argv) != 2:
    sys.exit(1)


def clean_message(message):
    message = (
        message.replace(" &raquo;", "")
        .replace("&raquo;", "")
        .replace("&laquo;", "")
        .replace(" »", "")
        .replace("»", "")
        .replace("«", "")
    )
    return " ".join(message.split())


if sys.argv[1] == "sort":
    for p in Path("source").glob("*.tsv"):
        with open(p) as f:
            reader = csv.reader(f, delimiter="\t")
            dct = {}

            for row in reader:
                if not row:
                    continue

                key = row[0].strip()
                value = clean_message(row[1]) if len(row) > 1 else ""

                if not key or key == "id":
                    continue

                if len(key) > 60 or any(ch in key for ch in "[]()`;{}"):
                    continue

                dct[key] = value

            keys = sorted(dct)

        with open(p, "w") as f:
            f.write("id\tmessage\n")

            for i, item in enumerate(keys, start=1):
                f.write(f"{item}\t{dct[item]}")

                if i != len(keys):
                    f.write("\n")

elif sys.argv[1] == "scrape":
    base_url = "https://core.telegram.org"

    errors_json_url = base_url + "/api/errors.json"

    try:
        response = requests.get(errors_json_url)
        response.raise_for_status()
        errors_data = response.json()
    except (requests.exceptions.RequestException, ValueError):
        try:
            page = requests.get(base_url + "/api/errors")
            page.raise_for_status()
            match = re.search(r'<a href="([^"]*\.json)"', page.text)
            if not match:
                sys.exit("Link to errors JSON not found on the errors page.")

            response = requests.get(base_url + match.group(1))
            response.raise_for_status()
            errors_data = response.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            sys.exit(f"Error fetching errors JSON: {e}")

    error_categories = errors_data.get("errors", [])
    if not error_categories:
        sys.exit("No error categories found in JSON.")

    source_dir = Path("source/")
    source_dir.mkdir(exist_ok=True)

    for error_type in error_categories:
        data_dict = {}

        for tsv_path in source_dir.glob(f"{error_type}*.tsv"):
            with open(tsv_path, 'r') as tsv_file:
                reader = csv.DictReader(tsv_file, delimiter='\t')
                for row in reader:
                    key = (row.get('id') or "").strip()
                    message = clean_message(row.get('message') or "")

                    if not key or key == "id":
                        continue

                    if len(key) > 60 or any(ch in key for ch in "[]()`;{}"):
                        continue

                    data_dict[key] = message

        error_details = errors_data["errors"].get(error_type, {})
        descriptions = errors_data["descriptions"]

        for error_code in error_details:
            if error_code.endswith("_*"):
                continue

            description = descriptions.get(error_code, "")
            if description:
                processed_description = clean_message(
                    description.replace("%d", "{value}")
                    .replace("\"", "'")
                    .replace("](/api/", f"]({base_url}/api/")
                )
                data_dict[error_code.replace("_%d", "_X")] = processed_description

        sorted_keys = sorted(data_dict.keys())

        for tsv_path in source_dir.glob(f"{error_type}*.tsv"):
            print(f"Writing to {tsv_path}")
            with open(tsv_path, 'w', newline='') as tsv_file:
                writer = csv.writer(tsv_file, delimiter='\t')
                writer.writerow(["id", "message"])
                writer.writerows([(key, data_dict[key]) for key in sorted_keys])
