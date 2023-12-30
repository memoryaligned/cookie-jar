.PHONY: clean data lint requirements sync_package_to_repo

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_REPO = {{ cookiecutter.python_repo }}
PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON = ./venv/bin/python3 

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies and set up the environment
setup: requirements pre-commit alembic.ini
	@echo ""
	@echo "###################################################################"
	@echo "to source your environment to use it:"
	@echo "  source ./venv/bin/activate"
	@echo "###################################################################"

.git/hooks/pre-commit:
	@git init .

pre-commit: .git/hooks/pre-commit
	@pre-commit install
	@pre-commit

venv:
	python3 -m venv venv

requirements: venv
	$(PYTHON) -m pip install -U pip setuptools wheel
	$(PYTHON) -m pip install -e .[dev]

## Clean the project temporary files
clean:
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
	@rm -rf ./build ./dist

## Run the linter against the scripts
lint:
	$(PYTHON) -m flake8 scripts
	$(PYTHON) -m blake scripts

## Upload Data to the python module repository
sync_package_to_repo:
	twine --repository-url $(PYTHON_REPO) upload dist/* 

## Serve the documentation locally
serve_doc: requirements
	$(PYTHON) -m mkdocs serve

build_doc: requirements
	$(PYTHON) -m mkdocs build

alembic.ini:
	$(PYTHON) -m alembic init alembic

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

## Build the project deliverables
dist: build_doc
	-mkdir dist
	cd build && tar czf ../dist/docs.tar.gz docs

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
