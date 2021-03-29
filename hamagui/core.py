import requests
import subprocess

from os import remove
from os import uname
from os import walk
from os import getcwd
from os import rename
from os import rmdir
from os import system
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


class Install:
    def download(os, bit):
        url = URL_SITE_DL + OPTIONS[os][bit]["tgz"]
        r = requests.get(url, allow_redirects=True)
        open(OPTIONS[os][bit]["tgz"], "wb").write(r.content)

    def move_files(from_dir, to_dir):
        """
        Recursivly remove all files
        """
        for root, dirs, files in walk(from_dir):
            for file in files:
                rename(os.path.join(root, file), os.path.join(to_dir, file))

    def extract(os, bit):
        dir_name = OPTIONS[os][bit]["tgz"]
        dir_path = getcwd() + "/" + dir_name[:-4]
        subprocess.run(["tar", "--extract", "-f", dir_name])
        Install.move_files(dir_path, getcwd())

    def install(os, bit):
        Install.download(os, bit)
        Install.extract(os, bit)
        remove(OPTIONS[os][bit]["tgz"])
        rmdir(OPTIONS[os][bit]["tgz"][:-4])


class Mana:
    """
    Manipultaion with hamachi or just `Mana`
    """
    def __init__(self):
        # hamachid - it`s main file of hamachi
        # Be careful with it beacause of unknowing of considering in this file
        self.hamachid = "hamachid"

    def run_insall_sh(self):
        """
        Run install.sh script
        """
        system("./install.sh")
        return 1

    def power_on_hamachid(self):
        """
        Power on hamachid
        hamachid - it`s main file of hamachi
        Be careful with it beacause of unknowing of considering in this file
        """
        system("./{}".format(self.hamachid))
        return 1
    
    def power_off_hamachid(self):
        """
        Power off hamachid
        """
        system("killall", self.hamachid)
        return 1

    def __get_hamachi_inf(self):
        """
        Get information from `hamachi`
        """
        return subprocess.Popen(
            ["hamachi"],
            stdout=subprocess.PIPE,
        ).communicate()

    def __get_from_text(self, text, word):
        """
        From `text` function catch word and return information
        that situated after this word.

        For example: from `status: offline` it will return offline
        """
        text = text.decode("utf-8")
        len_text = len(text)
        len_word = len(word)
        # from what place begin reading
        begin = 0
        catch = None
        # catg information of the word parameter
        while (len_text - begin) >= len_word:
            if text[begin:begin+len_word] == word:
                end = begin+len_word
                while text[end] != "\n":
                    end += 1
                catch = text[begin+len_word:end]
                break
            begin += 1
        # remove `:` and spaces
        catch = catch.replace(":", "")
        catch = catch.replace(" ", "")
        return catch

    def hamachi_inf(self):
        """
        Sort hamachi information
        """
        # TODO: avoid --> 'address': '25.103.11.9226209b1967b5c'
        inf = self.__get_hamachi_inf()[0]
        data = {}
        parameters = (
            "status",
            "client id",
            "address",
            "nickname",
        )
        for p in parameters:
            data[p] = self.__get_from_text(inf, p)
        return data

if __name__ == "__main__":
    #Install.install("linux", 64)
    mana = Mana()
    #mana.run_insall_sh()
    #mana.power_on_hamachid()
    print(mana.hamachi_inf())