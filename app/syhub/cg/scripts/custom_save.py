#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
from app.syhub.adapters import dcc
from app.syhub.adapters.disk_wrapper import get_user
from app.syhub.adapters.tank_wrapper import TankWrapper


def customSave(currentFile=None):
    """
    Prevent scene overwriting from an other artist.
    Protect only for scenes in the pipeline.
    """
    dcc_wrapper = dcc.get_current_engine_wrapper()
    current_user = get_user(currentFile)
    file_user = get_user(currentFile)

    try:
        tk = TankWrapper()
        template = tk.get_template_from_path(currentFile)
    except:
        template = None

    # ignore for scenes out of pipe
    if not template:
        dcc_wrapper.save()
        return

    # so let's add an exception
    isSceneProtected = template.name()
    if file_user != current_user and isSceneProtected:
        dcc_wrapper.message("You are not allowed to overwrite {0}'s scene ".format(file_user))
        return
    dcc_wrapper.save()
