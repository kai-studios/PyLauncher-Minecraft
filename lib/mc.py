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

def launch(version, username):
    """Запуск Minecraft в оффлайн режиме."""
    options = {
        "username": username,
        "uuid": generate_uuid(username),
        "token": ""
    }

    command = mll.command.get_minecraft_command(version, dir(), options)

    subprocess.Popen(command, cwd=mc.dir())

