VENV_DIR := .venv
PIP := $(VENV_DIR)/bin/pip

.PHONY: run
run:
	FLASK_APP=web_server:app flask run --debugger --host 0.0.0.0

.PHONY: clean
clean:
	rm -rf web_server/__pycache__ $(VENV_DIR)

.PHONY: install
install: $(VENV_DIR)
	command -v flit >/dev/null || $(PIP) install flit
	flit install

$(VENV_DIR):
	python3 -m venv $(VENV_DIR)
