#!/usr/bin/python3
"""fabric script that generates a tgz archive"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """generate a tgz archive from web_static folder"""
    time = datetime.now()
    t_s = time.strftime("%Y%m%d%H%M%S")
    try:
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static_{}\
              .tgz web_static".format(t_s))
        file_path = ("versions/web_static_{}.tgz".format(t_s))
        file_size = os.path.getsize(file_path)
        print(f'web_static packed: versions/web_static_{t_s}.tgz -> {file_size}')
    except Exception:
        return (None)
