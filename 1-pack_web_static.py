#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the web_static folder."""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder."""
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
