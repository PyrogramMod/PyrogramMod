VENV := venv
PYTHON := $(VENV)/bin/python
ifeq ($(OS),Windows_NT)
    PYTHON := $(VENV)/Scripts/python.exe
endif

HOST := $(shell ifconfig | grep "inet " | tail -1 | cut -d\  -f2 2>/dev/null || echo "127.0.0.1")
TAG := v$(shell grep -E '__version__ = ".*"' pyrogram/__init__.py | cut -d\" -f2)

RM := rm -rf

NUM_CORES := $(shell $(PYTHON) -c "import os; print(os.cpu_count())")

.PHONY: venv clean-build clean-api clean api build docs clean-docs tag dtag

venv:
	$(RM) $(VENV)
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install -U pip wheel setuptools
	$(PYTHON) -m pip install -U -r requirements.txt -r dev-requirements.txt
	@echo "Created venv with $$($(PYTHON) --version)"

clean-build:
	$(RM) *.egg-info build dist

clean-api:
	$(RM) pyrogram/errors/exceptions pyrogram/raw/all.py pyrogram/raw/base pyrogram/raw/functions pyrogram/raw/types

clean-pyc:
	find . -name "*.pyc" -exec $(RM) {} + || true
	find . -name "__pycache__" -exec $(RM) {} + || true

clean-ds_store:
	find . -name ".DS_Store" -exec $(RM) {} \;

clean: clean-build clean-api clean-pyc clean-ds_store clean-docs

clean-docs:
	$(RM) docs/build
	$(RM) docs/source/api/bound-methods docs/source/api/methods docs/source/api/types docs/source/telegram

api:
	cd compiler/api && ../../$(PYTHON) compiler.py
	cd compiler/errors && ../../$(PYTHON) compiler.py

docs:
	make clean-docs
	cd compiler/docs && ../../$(PYTHON) compiler.py
	$(PYTHON) -m sphinx -b html "docs/source" "docs/build/html" -j$(NUM_CORES)

build:
	make clean
	$(PYTHON) setup.py sdist
	$(PYTHON) setup.py bdist_wheel

tag:
	git tag $(TAG)
	git push origin $(TAG)

dtag:
	git tag -d $(TAG)
	git push origin -d $(TAG)

tagall:
	echo "Creating automatic tags for all version bumps..."
	for hash in $$(git log --grep="Bump version\|Version bump\|v[0-9]\+\.[0-9]\+\.[0-9]\+" --format="%H"); do \
	    msg=$$(git log -1 --format="%s" $$hash); \
	    versions=$$(echo "$$msg" | grep -o "v[0-9]\+\.[0-9]\+\.[0-9]\+"); \
	    for version in $$versions; do \
	        if [ -n "$$version" ]; then \
	            if git show-ref --tags --quiet --verify "refs/tags/$$version"; then \
	                echo "Tag $$version already exists, skipping."; \
	            else \
	                echo "Creating tag $$version for commit $$hash"; \
	                git tag -a "$$version" "$$hash" -m "Automatic tag $$version"; \
	            fi; \
	        fi; \
	    done; \
	done
	echo "Pushing all tags to the remote..."
	git push origin --tags