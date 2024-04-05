#!/usr/bin/python3
"""fabric script that generates a tgz archive"""
from fabric.api import local
import time

def do_pack():
    """generate a tgz archive from web_static folder"""
    t.s = time.strptime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czf versions/web_static_{:s}.tgz web_static".format(t.s))
        return ("web_static_{:s}.tgz".format(t.s))
    except:
        return (None)
