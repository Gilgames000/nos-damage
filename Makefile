.PHONY: install
.PHONY: run
.PHONY: gui


SRC = src/main/python
PYTHON = venv/bin/python
PIP = venv/bin/pip
UIS = $(wildcard $(SRC)/gui/*.ui)
PYS = $(patsubst $(SRC)/gui/%.ui, $(SRC)/gui/%.py, $(UIS))

install :
	$(PIP) install -r requirements.txt

run :
	$(PYTHON) src/main/python/main.py

gui : $(PYS)

$(SRC)/gui/%.py: $(SRC)/gui/%.ui
	pyside2-uic $< -o $@
