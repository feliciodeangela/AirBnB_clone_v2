#!/usr/bin/python3
"""Module for packing and deploying the static content"""
from fabric.api import local
from datetime import datetime
from fabric.api import run, put, env
from os.path import isfile
env.hosts = ['100.25.180.71', '100.24.205.214']


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


def do_deploy(archive_path):
    """Function to send content to servers"""
    if isfile(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        arch = archive_path.split('/')[1].split('.')[0]
        main_dir = '/data/web_static/releases'
        run('mkdir -p {0}/{1}/'.format(main_dir, arch))
        run('tar -xzf /tmp/{1}.tgz -C {0}/{1}/'.format(main_dir, arch))
        run('rm -f /tmp/{}.tgz /data/web_static/current'.format(arch))
        run('mv {0}/{1}/web_static/* {0}/{1}/'.format(main_dir, arch))
        run('rm -fr {0}/{1}/web_static'.format(main_dir, arch))
        run('ln -fs {0}/{1}/ /data/web_static/current'.format(main_dir, arch))
        return True
    except Exception:
        return False


def deploy():
    """Deploy in one step"""
    path = do_pack()
    do_deploy(path)


if __name__ == "__main__":
    deploy
