import requests
import subprocess

from os import remove
from os import uname
from os import walk
from os import getcwd
from os import rename
from os import rmdir
import os.path


URL_SITE_DL = "https://www.vpn.net/installers/"
OPTIONS = {
    "linux": {
        32: {
            "tgz": "logmein-hamachi-2.1.0.203-x86.tgz",
        },
        64: {
            "tgz": "logmein-hamachi-2.1.0.203-x64.tgz",
        },
    },
}


def get_os_information():
    """
    Return os name and type of architecture
    """
    inf = list(uname())
    if inf[4] == "x86_64":
        inf[4] = 64
    if inf[4] == "64":
        inf[4] = 32
    return inf[0].lower(), inf[4]

def execute_command(command, path=None):
    pass

class Install:
    def download(os, bit):
        url = URL_SITE_DL + OPTIONS[os][bit]["tgz"]
        r = requests.get(url, allow_redirects=True)
        open(OPTIONS[os][bit]["tgz"], "wb").write(r.content)

    def remove_files(from_dir, to_dir):
        """
        Recursivly remove all files
        """
        for root, dirs, files in walk(from_dir):
            for file in files:
                rename(os.path.join(root, file), os.path.join(to_dir, file))

    def extract(os, bit):
        from sys import exit
        dir_name = OPTIONS[os][bit]["tgz"]
        dir_path = getcwd() + "/" + dir_name[:-4]
        subprocess.run(["tar", "--extract", "-f", dir_name])
        Install.remove_files(dir_path, getcwd())


    def install(os, bit):
        Install.download(os, bit)
        Install.extract(os, bit)
        remove(OPTIONS[os][bit]["tgz"])
        rmdir(OPTIONS[os][bit]["tgz"][:-4])
        

if __name__ == "__main__":
    #print(get_os_information())
    Install.install("linux", 64)
    #path = "/home/kra53n/Рабочий стол/hamagui/logmein-hamachi-2.1.0.203-x64/"
    #path = "/logmein-hamachi-2.1.0.203-x64/"
    #Commands.execute_install_sh("/home/kra53n/Рабочий стол/hamagui/logmein-hamachi-2.1.0.203-x64/")
    #Commands.init_hamachi(path)
    #Commands.kill_hamachi_process()
