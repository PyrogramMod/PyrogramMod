import os
import sys

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomHook(BuildHookInterface):
    def initialize(self, version, build_data):
        if self.target_name not in {"wheel", "install"}:
            return

        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

        try:
            from compiler.api.compiler import start as compile_api
            from compiler.errors.compiler import start as compile_errors
        except ImportError as e:
            raise RuntimeError("Could not import compiler.") from e

        try:
            compile_api()
        except Exception as e:
            raise RuntimeError("Could not compile compiler.") from e

        try:
            compile_errors()
        except Exception as e:
            raise RuntimeError("Could not compile errors.") from e
