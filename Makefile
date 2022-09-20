PROJ_PTH=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))
APP_PATH = inv
LINT_PATHS = $(APP_PATH)

%:
	@:

lint:
	python -m autoflake --in-place --recursive --ignore-init-module-imports --remove-duplicate-keys --remove-unused-variables --remove-all-unused-imports $(LINT_PATHS)
	python -m black $(LINT_PATHS)
	python -m isort $(LINT_PATHS)
	python -m mypy $(APP_PATH) --ignore-missing-imports
