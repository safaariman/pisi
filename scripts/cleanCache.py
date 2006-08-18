#!/usr/bin/python

import os
import sys
import string
import pisi.util as util

def findUnneededFiles():
    listdir = os.listdir("/var/cache/pisi/packages")
    listdir.sort()

    dict = {}
    for file in listdir:
        name, version = util.parse_package_name(file)
        dict[name] = version

    for file in dict:
        listdir.remove("%s-%s" % (file, dict[file]))

    return listdir

def usage(msg):
    print """
Error: %s

Usage:
    cleanCache --dry-run    (Shows unneeded files)
    cleanCache --clean      (Removes unneeded files)
    """ % msg

    sys.exit(1)

if __name__ == "__main__":
    try:
        sys.argv[1]
    except IndexError:
        usage("Unsufficient arguments...")

    if sys.argv[1] == "--dry-run":
        for i in findUnneededFiles():
            if os.path.exists("/var/cache/pisi/packages/%s" % i):
                print i
    elif sys.argv[1] == "--clean":
        for i in findUnneededFiles():
            if os.path.exists("/var/cache/pisi/packages/%s" % i):
                try:
                    os.remove("/var/cache/pisi/packages/%s" % i)
                except OSError:
                    usage("Permission denied...")
    else:
        usage("No command given...")