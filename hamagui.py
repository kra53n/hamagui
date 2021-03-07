import requests
import subprocess
from os import remove


URL_SITE = "https://www.vpn.net/installers/"
OPTIONS = {
    "linux": {
        32: {
            "tgz": "logmein-hamachi-2.1.0.203-x86.tgz",
        },
        64: {
            "tgz": "logmein-hamachi-2.1.0.203-x64.tgz",
        }
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


class Gui:
    pass


if __name__ == "__main__":
    Install.install("linux", 64)
