#!/usr/bin/python3
"""Fabric script for full deployment - packing and deploying web_static"""

from fabric.api import env, put, run, local, runs_once
from datetime import datetime
import os


env.hosts = ['54.204.136.7', '44.201.166.17']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


@runs_once
def do_pack():
    """
    Compress web_static folder into a .tgz archive

    Returns:
        str: Path to the created archive if successful
        None: If archive creation failed
    """
    try:
        # Create versions directory if it doesn't exist
        if not os.path.exists('versions'):
            os.makedirs('versions')

        # Generate timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{timestamp}.tgz"
        archive_path = f"versions/{archive_name}"

        print(f"Packing web_static to {archive_path}")

        # Create the archive
        result = local(f"tar -cvzf {archive_path} web_static", capture=False)

        # Check if command was successful
        if result.succeeded:
            # Get file size
            file_size = os.path.getsize(archive_path)
            print(f"web_static packed: {archive_path} -> {file_size}Bytes")
            return archive_path
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None


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


def deploy():
    """
    Full deployment: pack and deploy web_static

    Returns:
        bool: Result of do_deploy operation
    """
    # Pack the web_static folder
    archive_path = do_pack()

    # Return False if packing failed
    if archive_path is None:
        return False

    # Deploy the archive
    return do_deploy(archive_path)
