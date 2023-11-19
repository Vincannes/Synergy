#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os
import logging

from app.syhub.core import constants as cst


def create_log(name="Syngergy"):
    _login_info = logging.DEBUG if eval(os.environ.get(cst.Variables.SYN_DEBUG)) else logging.INFO

    logger = logging.getLogger(name)
    logger.setLevel(_login_info)

    ch = logging.StreamHandler()
    ch.setLevel(_login_info)

    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger

