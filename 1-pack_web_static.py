#!/usr/bin/python3
''' we are generating a tgz archive'''

from fabric.api import *


@runs_once
def do_pack():
    ''' using theweb_static folder'''
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(path))

    if result.failed:  # if any exception give None
        return None
    return path
