#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os
import sys
from pprint import pprint

from PySide2 import QtWidgets

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.syhub.core import constants
from app.syhub.core.vars import set_vars
from app.resources.style import style
from app.syhub.interfaces.synergy_ui import Synergy


def run():
    app = QtWidgets.QApplication(sys.argv)
    style.dark(app)
    w = Synergy()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    set_vars()
    os.environ[constants.Variables.SYN_DEBUG] = "1"
    run()
