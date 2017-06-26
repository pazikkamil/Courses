FOLDER = venv
PYVERSION = $(shell python -V 3>&1 | sed 's/Python //g' | cut -c 1)

ifneq ($(PYVERSION), 3)
	PYTHON = python3
endif

all:
	mkdir $(FOLDER)
	$(PYTHON) -m venv $(FOLDER) 

