#!/usr/bin/python3
"""distribute an archive to my web servers"""
from fabric.api import run, env, put
import os
from fabric.contrib import files

env.hosts = ['100.26.221.230', '54.165.22.24']

def do_deploy(archive_path):
    """deploys an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    label = tmp.split('/')[1]
    path = data_path + label

    try:
        put(archive_path, '/tmp')
        run('sudo mkdir -p {}'.format(path))
        run('sudo tar -xzf /tmp/{}.tgz -C {}'.format(label, path))
        run('sudo rm -f /tmp/{}.tgz'.format(label))
        run('sudo mv {}/web_static/* {}/'.format(path, path))
        run('sudo rm -rf {}/web_static'.format(path))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(path))

        return True
    except:
        return False
