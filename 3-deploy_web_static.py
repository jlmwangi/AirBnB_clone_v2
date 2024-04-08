#!/usr/bin/python3
#creates and distributes an archive to my web servers
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

env.hosts = ['100.26.221.230', '54.165.22.24']

def deploy():
    """distribute an archive"""
    archive_path = do_pack()
    if not archive_path:
        return False

    value = do_deploy(archive_path)

    return value
