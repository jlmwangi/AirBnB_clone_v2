#!/usr/bin/python3
#creates and distributes an archive to my web servers
from fabric.api import local, env, put, run
from fabric.contrib import files
from datetime import datetime
import os

env.hosts = ['100.26.221.230', '54.165.22.24']

def do_pack():
    """generate a tgz archive from web_static folder"""
    time = datetime.now()
    t_s = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}\
              .tgz web_static/".format(t_s))
        file_path = ("versions/web_static_{}.tgz".format(t_s))
        file_size = os.path.getsize(file_path)
        print(f'web_static packed: versions/web_static_{t_s}.tgz -> {file_size}')
    except Exception:
        return (None)

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
        run('mkdir -p {}'.format(path))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(label, path))
        run('rm -f /tmp/{}.tgz'.format(label))
        run('mv {}/web_static/* {}/'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(path))

        return True
    except:
        return False

def deploy():
    """distribute an archive"""
    archive_path = do_pack()
    if not archive_path:
        return False

    value = do_deploy(archive_path)

    return value

deploy()
