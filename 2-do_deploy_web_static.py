#!/usr/bin/python3
"""Fabric script to deploy web_static archive to web servers"""

from fabric.api import env, put, run
import os


env.hosts = ['54.204.136.7', '44.201.166.17']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distribute archive to web servers

    Args:
        archive_path (str): Path to the archive to deploy

    Returns:
        bool: True if all operations successful, False otherwise
    """
    # Check if archive exists
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract archive filename without path
        archive_filename = os.path.basename(archive_path)
        # Remove .tgz extension to get the folder name
        folder_name = archive_filename.replace('.tgz', '')

        # Upload archive to /tmp/
        put(archive_path, f'/tmp/{archive_filename}')

        # Create release folder
        run(f'mkdir -p /data/web_static/releases/{folder_name}/')

        # Extract archive
        run(f'tar -xzf /tmp/{archive_filename} -C /data/web_static/releases/{folder_name}/')

        # Remove archive from server
        run(f'rm /tmp/{archive_filename}')

        # Move contents from web_static subfolder to release folder
        run(f'mv /data/web_static/releases/{folder_name}/web_static/* /data/web_static/releases/{folder_name}/')

        # Remove the empty web_static folder
        run(f'rm -rf /data/web_static/releases/{folder_name}/web_static')

        # Delete the old symbolic link
        run('rm -rf /data/web_static/current')

        # Create new symbolic link
        run(f'ln -s /data/web_static/releases/{folder_name}/ /data/web_static/current')

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Error during deployment: {e}")
        return False
