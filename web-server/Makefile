VENV_DIR := .venv

FLASK := $(VENV_DIR)/bin/flask
FLIT := $(VENV_DIR)/bin/flit
PIP := $(VENV_DIR)/bin/pip

.PHONY: run
run:
	FLASK_APP=web_server:app $(FLASK) run --reload --debugger --host 0.0.0.0

.PHONY: clean
clean:
	rm -rf \
		oe-* \
		web_server/__pycache__ \
		$(VENV_DIR)

.PHONY: install
install: $(VENV_DIR)
	command -v flit >/dev/null || $(PIP) install flit
	$(FLIT) install

$(VENV_DIR):
	python3 -m venv $(VENV_DIR)
