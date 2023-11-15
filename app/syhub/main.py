#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os
import sys
from PySide2 import QtWidgets

from app.resources.style import style
from app.syhub.interfaces.synergy_ui import Synergy


def run():
    app = QtWidgets.QApplication(sys.argv)
    style.dark(app)
    w = Synergy()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    os.environ["SYN_ROOT_PATH"] = "D:\\Desk\\python\\Synergy\\app"
    os.environ["SYN_PROJECTS_FILE_STRUCTURE"] = "D:\\Desk\\python\\Projects"
    run()
