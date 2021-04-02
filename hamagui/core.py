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
        system("killall {}".format(self.hamachid))
        return 1

    def __get_hamachi_inf(self):
        """
        Get information from `hamachi`
        """
        return subprocess.Popen(
            ["hamachi"],
            stdout=subprocess.PIPE,
        ).communicate()

    def __get_from_text(self, text, word, cut_spaces=1):
        """
        From `text` function catch word and return information
        that situated after this word.

        For example: from `status: offline` it will return offline

        Arguments:
            3) cut_signs - it`s bool argument. If it `1`
            it will sign `:` and " ", if `0` not
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
        if cut_spaces:
            catch = catch.replace(" ", "")
        return catch
    
    def __return_first_part(self, string):
        """
        It return first part of sentence
        For example we have `cut    this`, we will get only `cut`
        """
        string = string.lstrip()
        end = 0
        while string[end] != " ":
            end += 1
        return string[:end]

    def hamachi_inf(self):
        """
        Sort hamachi information
        """
        inf = self.__get_hamachi_inf()[0]
        data = {}
        parameters = (
            "status",
            "client id",
            "nickname",
        )

        for p in parameters:
            data[p] = self.__get_from_text(inf, p)
        data["address"] = self.__return_first_part(
            self.__get_from_text(inf,"address", cut_spaces=0)
        )
        data["client id"] = data["client id"].replace("-", ".")
        return data
    
    def logged_in(self):
        subprocess.run(["hamachi", "login"])
    
    def logged_off(self):
        """
        Go to offline mode
        """
        subprocess.run(["hamachi", "logoff"])
    
    def set_nickname(self, nickname):
        """
        To set nickname user must be in `logged in`
        If nicknames are simular then return 0
        """
        # check user nickname
        data = self.hamachi_inf()
        if data["nickname"] == nickname:
            return 0
        if data["status"] != "logged in":
            self.logged_in()
        subprocess.run(["hamachi", "set-nick", nickname])
    
    def join_network(self, id):
        subprocess.run(["hamachi", "join", id])

if __name__ == "__main__":
    from time import sleep
    #Install.install("linux", 64)
    #sleep(0.2)
    mana = Mana()
    #mana.logged_off()
    #mana.set_nickname("kryakraykrya")
    #mana.run_insall_sh()
    #mana.power_on_hamachid()
    #sleep(0.2)
    print(mana.hamachi_inf())
    #mana.power_off_hamachid()
    #system("./rmfs")
