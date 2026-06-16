#!/usr/bin/python3
"""Fabric script that distributes an archive to web servers."""
import os
from fabric.api import env, put, run


env.hosts = ['54.204.136.7', '44.201.166.17']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distribute an archive to the web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        folder_name = archive_filename.replace('.tgz', '')
        release_dir = '/data/web_static/releases/{}/'.format(folder_name)

        put(archive_path, '/tmp/{}'.format(archive_filename))
        run('mkdir -p {}'.format(release_dir))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_dir))
        run('rm /tmp/{}'.format(archive_filename))
        run('mv {}web_static/* {}'.format(release_dir, release_dir))
        run('rm -rf {}web_static'.format(release_dir))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_dir))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Error during deployment: {}".format(e))
        return False
