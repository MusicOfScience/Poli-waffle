PYTHON ?= python

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt -r requirements-dev.txt

test:
	PYTHONPATH=. pytest -q

manifest:
	PYTHONPATH=. $(PYTHON) scripts/ingest_reference.py

build-interim:
	PYTHONPATH=. $(PYTHON) scripts/build_interim_tables.py

check-raw:
	PYTHONPATH=. $(PYTHON) scripts/check_raw_layout.py

run:
	streamlit run streamlit_app.py
