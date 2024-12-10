VENV_DIR := .venv

FLIT := $(VENV_DIR)/bin/flit
PIP := $(VENV_DIR)/bin/pip
PYTHON := $(VENV_DIR)/bin/python3

.PHONY: run
run:
	$(PYTHON) -m camera_server

.PHONY: clean
clean:
	rm -rf \
		oe-* \
		camera_server/__pycache__ \
		$(VENV_DIR)

.PHONY: install
install: $(VENV_DIR)
	command -v flit >/dev/null || $(PIP) install flit
	$(FLIT) install

$(VENV_DIR):
	python3 -m venv $(VENV_DIR)
