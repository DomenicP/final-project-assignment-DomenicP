.PHONY: run
run:
	flask --app web_server:app run --debug --host 0.0.0.0

.PHONY: clean
clean:
	rm -rf web_server/__pycache__ .venv

.PHONY: install
install:
	[ -d .venv ] || python3 -m venv .venv
	.venv/bin/pip install -r requirements.lock

.PHONY: lock
lock:
	.venv/bin/pip install -r requirements.txt
	.venv/bin/pip freeze > requirements.lock
