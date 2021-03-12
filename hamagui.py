import requests
import subprocess

from os import remove
from os import uname

from tkinter import Tk


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

    def extract(os, bit):
        subprocess.run(["tar", "--extract", "-f", OPTIONS[os][bit]["tgz"]])


    def install(os, bit):
        Install.download(os, bit)
        Install.extract(os, bit)
        remove(OPTIONS[os][bit]["tgz"])


class Gui:
    def __init__(self):
        pass


if __name__ == "__main__":
    print(get_os_information())
    #Install.install("linux", 64)
    #path = "/home/kra53n/Рабочий стол/hamagui/logmein-hamachi-2.1.0.203-x64/"
    #path = "/logmein-hamachi-2.1.0.203-x64/"
    #Commands.execute_install_sh("/home/kra53n/Рабочий стол/hamagui/logmein-hamachi-2.1.0.203-x64/")
    #Commands.init_hamachi(path)
    #Commands.kill_hamachi_process()