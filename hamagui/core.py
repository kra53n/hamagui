import requests
import subprocess
import os.path
from pathlib import Path
from itertools import chain
from os import remove, uname, walk, getcwd, rename, rmdir, system

from constants import URL_SITE_DL, SYSTEM_BITS_OPTIONS, HAMACHI_FILES


def get_os_information():
    """
    Return os name and type of architecture
    """
    inf = list(uname())
    system_bits = {"x86_64": 64, "64": 32}
    return inf[0].lower(), system_bits[inf[4]]


class Install:
    def __init__(self):
        os, bit = get_os_information()
        self.install(os, bit)

    def download(self, os, bit):
        url = URL_SITE_DL + SYSTEM_BITS_OPTIONS[os][bit]["tgz"]
        r = requests.get(url, allow_redirects=True)
        open(SYSTEM_BITS_OPTIONS[os][bit]["tgz"], "wb").write(r.content)

    def move_files(self, from_dir, to_dir):
        """
        Recursivly remove all files
        """
        for root, dirs, files in walk(from_dir):
            for file in files:
                rename(os.path.join(root, file), os.path.join(to_dir, file))

    def extract(self, os, bit):
        dir_name = SYSTEM_BITS_OPTIONS[os][bit]["tgz"]
        dir_path = str(Path(getcwd()) / dir_name[:-4])
        subprocess.run(["tar", "--extract", "-f", dir_name])
        self.move_files(dir_path, getcwd())

    def install(self, os, bit):
        self.download(os, bit)
        self.extract(os, bit)
        remove(SYSTEM_BITS_OPTIONS[os][bit]["tgz"])
        rmdir(SYSTEM_BITS_OPTIONS[os][bit]["tgz"][:-4])


class Mana:
    """
    Manipultaion with hamachi or just `Mana`
    """
    def __init__(self, hamachi_files=HAMACHI_FILES):
        # hamachid - it`s main file of hamachi
        # Be careful with it beacause of unknowing of considering in this file
        self.hamachid = "hamachid"
        self.hamachi_files = hamachi_files

    def delete_files(self):
        """delete all files from pwd of hamachi"""
        for file in self.hamachi_files:
            remove(file)

    def check_hamachid(self, path):
        """
        Check existing of hamachi.
        If exist then return 1 else return 0.
        Arguments:
            1) path - path where situated hamachid
        """
        return self.hamachid in chain.from_iterable(map(lambda x: x[2], walk(path)))

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
        """Power off hamachid"""
        system("killall {}".format(self.hamachid))
        return 1

    def __get_hamachi_inf(self):
        """Get information from `hamachi`"""
        return subprocess.Popen(["hamachi"], stdout=subprocess.PIPE).communicate()

    def __get_hamachi_list(self):
        return subprocess.Popen(["hamachi", "list"], stdout=subprocess.PIPE).communicate()

    def __get_from_text(self, text, word, cut_spaces=1):
        """
        From `text` function catch word and return information
        that situated after this word.
        For example: from `status: offline` it will return offline.
        Arguments:
            3) cut_signs - it`s bool argument. If it `1`
            it will sign `:` and " ", if `0` not.
        """
        text = text.decode("utf-8")
        text_len = len(text)
        word_len = len(word)
        # from what place begin reading
        begin = 0
        catch = None
        # catg information of the word parameter
        while (text_len - begin) >= word_len:
            if text[begin:begin+word_len] == word:
                end = begin+word_len
                while text[end] != "\n":
                    end += 1
                catch = text[begin+word_len:end]
                break
            begin += 1
        # remove `:` and spaces
        catch = catch.replace(":", "")
        if cut_spaces:
            catch = catch.replace(" ", "")
        return catch
    
    def __get_from_text_between_symbols(self, text, sym1, sym2):
        """
        Parse text from string between two symbols
        """
        pos = 0
        inf = []
        poss = []
        text = text[0].decode("utf-8")
        while len(text) > pos:
            if text[pos] == sym1 or text[pos] == sym2:
                poss.append(pos)
            pos += 1
        for i in range(0, len(poss), 2):
            inf.append(text[poss[i]+1:poss[i+1]])
        return inf
    
    def __return_first_part(self, string):
        """
        It returns first part of sentence
        For example we have `  cut    this`, we will get only `cut`
        """
        return string[:string.index(" ")]

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
            self.__get_from_text(inf, "address", cut_spaces=0)
        )
        data["client id"] = data["client id"].replace("-", ".")
        data["list"] = self.__get_from_text_between_symbols(
            self.__get_hamachi_list(), "[", "]"
        )
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
