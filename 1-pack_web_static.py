#!/usr/bin/python3
"""Fabric script to pack web_static folder into a .tgz archive"""

from fabric.api import local
from datetime import datetime
import os


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
