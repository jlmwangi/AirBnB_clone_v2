#!/usr/bin/python3
"""distribute an archive to my web servers"""
from fabric.api import rn, env, put
import os
from fabric.contrib import files

env.hosts = ['100.26.221.230', '54.165.22.24']

def do_deploy(archive_path):
    """deploys an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    arc_path = '/data/web_static/releases/'
    temp= archive_path.split('.')[0]
    label = temp.split('/')[1]
    path = arc_path + name

    try:
        put(archive_path, 'temp')
        run('sudo mkdir -p {}'.format(path))
        run('sudo tar -fzx /temp/{}.tgz -C {}'.format(label, path))
        run('sudo rm -f /temp/{}.tgz'.format(label))
        run('sudo mv {}/web_static/* {}/'.format(path, path))
        run('sudo rm -rf {}/web_static'.format(path))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(path))

        return True
    except:
        return False
