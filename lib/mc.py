import minecraft_launcher_lib as mll
import uuid
import subprocess

def dir(md=None):
    """return minecraft install (memoized)"""
    if md == None:
        md = mll.utils.get_minecraft_directory() 
    return md

def generate_uuid(username,id=None):
    """Генерация UUID для оффлайн режима."""
    if id == None:
        id = str(uuid.uuid3(uuid.NAMESPACE_DNS, username))
    return id

def version_ids(ids=None):
    if ids == None:
        versions = mll.utils.get_available_versions(dir())
        ids = [v["id"] for v in versions]
    return ids

def command(version,options={}):
    return mll.command.get_minecraft_command(version, dir(), options)

def launch(version, username):
    """Запуск Minecraft в оффлайн режиме."""
    options = {
        "username": username,
        "uuid": generate_uuid(username),
        "token": ""
    }

    subprocess.Popen(command(version, options), cwd=dir())

def install_version(version):
    mll.install.install_minecraft_version(version, dir())

