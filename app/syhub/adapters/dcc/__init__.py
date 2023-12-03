#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

def get_current_engine_wrapper():
    try:
        from .nuke_wrapper import NukeWrapper
        return NukeWrapper
    except ImportError:
        pass

    try:
        from .maya_wrapper import MayaWrapper
        return MayaWrapper
    except ImportError:
        pass

    try:
        from .houdini_wrapper import HoudiniWrapper
        return HoudiniWrapper
    except ImportError:
        pass

    raise ValueError("Cannot import any DCC Wrapper.")
