.PHONY: gui


GUI = src/main/python/gui
SRC = $(wildcard $(GUI)/*.ui)
PYS = $(patsubst $(GUI)/%.ui, $(GUI)/%.py, $(SRC))

gui : $(PYS)

$(GUI)/%.py: $(GUI)/%.ui
	pyside2-uic $< -o $@
