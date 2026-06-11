#!/usr/bin/python3
"""Fabric script for full deployment - packing and deploying web_static"""
import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ['54.204.136.7', '44.201.166.17']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


@runs_once
def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder"""
    if not os.path.exists("versions"):
        os.makedirs("versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    print("Packing web_static to {}".format(archive_path))
    result = local("tar -cvzf {} web_static".format(archive_path),
                   capture=False)

    if result.failed:
        return None

    size = os.path.getsize(archive_path)
    print("web_static packed: {} -> {}Bytes".format(archive_path, size))
    return archive_path


def do_deploy(archive_path):
    """Distribute an archive to the web servers"""
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


def deploy():
    """Create and distribute an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
