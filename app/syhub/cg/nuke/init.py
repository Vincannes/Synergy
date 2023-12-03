#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import os
import sys
import nuke
from pprint import pprint

# Import Synergy modules
from app.syhub.cg.scripts import syn_create_folders, custom_save
from app.syhub.adapters.tank_wrapper import TankWrapper

_write_before_render = "syn_create_folders.create_folder(nuke.thisNode().knob('file').value())"
nuke.knobDefault("Write.beforeRender", _write_before_render)


