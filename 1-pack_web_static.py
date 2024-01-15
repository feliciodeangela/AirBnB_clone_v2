#!/usr/bin/python3
"""Module for packing the static content"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Function to create the compressed file"""
    local("mkdir -p versions")
    time = datetime.now()
    date = time.strftime('%Y%m%d%H%M%S')
    pth = "versions/web_static_{}.tgz".format(date)
    done = local("tar -cvzf {} web_static".format(pth))
    if done is not None:
        return pth
    else:
        return None
