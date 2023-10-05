#!/usr/bin/python3
"""
This distributes archive to your web servers through
the use of Fabric
"""

from fabric.api import env, put, run, local
from datetime import datetime
from os.path import exists

env.hosts = ['18.207.3.198', '54.84.150.136']
env.user = 'ubuntu'  # SSH username used
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
    Distribution of archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Uploading archive in tmp dir of web servers
        put(archive_path, "/tmp/")

        archive_filename = archive_path.split("/")[-1].split(".")[0]

        # folder for the new version done
        run("mkdir -p /data/web_static/releases/{}/".format(archive_filename))

        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(archive_filename, archive_filename))

        # Deleting archive from my servers
        run("rm /tmp/{}.tgz".format(archive_filename))

        # Removing symbolic link thats there
        run("rm -f /data/web_static/current")

        # Creating new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_filename))

        print("New version deployed!")
        return True

    except Exception as e:
        return False
