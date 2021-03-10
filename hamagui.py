import requests
import subprocess
from os import remove
from tkinter import Tk


# NOTE:
# Commands class can be done easyier. So goal make it more understable


URL_SITE = "https://www.vpn.net/installers/"
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


class Install:
    def download(os, bit):
        url = URL_SITE + OPTIONS[os][bit]["tgz"]
        r = requests.get(url, allow_redirects=True)
        open(OPTIONS[os][bit]["tgz"], "wb").write(r.content)

    def extract(os, bit):
        subprocess.run(["tar", "--extract", "-f", OPTIONS[os][bit]["tgz"]])


    def install(os, bit):
        Install.download(os, bit)
        Install.extract(os, bit)
        remove(OPTIONS[os][bit]["tgz"])


class Commands:
    def execute_install_sh(path):
        """
        Install install.sh file
        """
        name = "install.sh"
        subprocess.run(["sh", "{}".format(path+name)])

    def init_hamachi(path):
        name = "hamachid"
        subprocess.run([".{}".format(path+name)])

    def kill_hamachi_process():
        subprocess.run(["killall", "hamachid"])


class Gui:
    def __init__(self):
        pass


if __name__ == "__main__":
    Install.install("linux", 64)
    #path = "/home/kra53n/Рабочий стол/hamagui/logmein-hamachi-2.1.0.203-x64/"
    path = "/logmein-hamachi-2.1.0.203-x64/"
    Commands.execute_install_sh("/home/kra53n/Рабочий стол/hamagui/logmein-hamachi-2.1.0.203-x64/")
    Commands.init_hamachi(path)
    #Commands.kill_hamachi_process()
