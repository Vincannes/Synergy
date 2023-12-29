#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import maya.cmds as cmds

import syn_menu
from app.syhub import main


syn_menu.prod_menu()

# run syn_hub at opening
main.run_dcc()
