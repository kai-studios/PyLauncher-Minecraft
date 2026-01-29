import sys
import minecraft_launcher_lib as mll
import lib.mc as mc

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

    mc.launch(version, username)

if __name__ == "__main__":
    create_launcher()

