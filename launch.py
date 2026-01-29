import sys
import lib.mc as mc
import minecraft_launcher_lib as mll

def usage():
    exit("Usage: {} <username> [version] (default: {})".format(sys.argv[0],mc.version_ids()[0]))

def create_launcher():
    if len(sys.argv) < 3:
        usage()

    username = sys.argv[1]
    version = sys.argv[2]

    if not username.strip():
        usage()

    if not version:
        usage()

    if version not in mc.version_ids():
        mc.install_version(version)

    try: 
        mc.command(version)
    except mll.exceptions.VersionNotFound:
        mc.install_version(version)

    mc.launch(version, username)

if __name__ == "__main__":
    create_launcher()

