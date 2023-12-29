#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import os
import nuke

from app.syhub import main


NUKE_MENU = nuke.menu("Nuke")


def prod_menu():
    prodMenuName = f"PROD-{os.environ.get('PROD', 'Menu')}"
    top_menu = NUKE_MENU.findItem(prodMenuName)

    if not top_menu:
        top_menu = NUKE_MENU.addMenu(prodMenuName)


# Override Ctrl+S
fileMenu = nuke.menu('Nuke').findItem('File')
fileMenu.addCommand("&Save", "custom_save.customSave(nuke.root().name())", "Ctrl+S")

prod_menu()

# run syn_hub at opening
main.run_dcc()
