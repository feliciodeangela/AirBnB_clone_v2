#!/usr/binpython3
"""Module to distribute compressed content to web servers"""
from fabric.api import run, put, env
from os.path import isfile
env.hosts = ['100.25.180.71', '100.24.205.214']
"""env.user = ['ubuntu']
env.key_filename = ['~/.ssh/school']"""


def do_deploy(archive_path):
    """Function to send content to servers"""
    if isfile(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        arch = archive_path.split('/')[1].split('.')[0]
        run('mkdir -p /data/web_static/releases/{}'.format(arch))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/'.format(arch))
        run('rm -f /tmp/{}.tgz /data/web_static/current'.format(arch))
        run('mv /data/web_static/releases/{}/web_static/*'
            ' /data/web_static/releases/{}/'.format(arch))
        run('rm -fr /data/web_static/releases/{}/web_static'.format(arch))
        run('ln -fs /data/web_static/{}/'
            ' /data/web_static/current'.format(arch))
        return True
    except:
        return False
