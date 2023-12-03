#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import os
import nuke
# from PySide2.

from app.syhub import main
# from app.syhub.cg.scripts import custom_save

NUKE_MENU = nuke.menu("Nuke")


def prod_menu():
    prodMenuName = f"PROD-{os.environ.get('PROD', 'Menu')}"
    top_menu = NUKE_MENU.findItem(prodMenuName)

    if not top_menu:
        top_menu = NUKE_MENU.addMenu(prodMenuName)


# Override Ctrl+S
fileMenu = nuke.menu('Nuke').findItem('File')
fileMenu.addCommand("&Save", "custom_save.customSave(nuke.root().name())", "Ctrl+S")
print("lalalalal")
prod_menu()
main.run_dcc()
