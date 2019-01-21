.PHONY: gui


GUI = gui
SRC = $(wildcard $(GUI)/*.ui)
PYS = $(patsubst $(GUI)/%.ui, $(GUI)/%.py, $(SRC))

gui : $(PYS)

$(GUI)/%.py: $(GUI)/%.ui
	pyside2-uic $< -o $@
