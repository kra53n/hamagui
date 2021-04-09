import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

from os import getcwd
from time import sleep

from errors import OsError
from errors import InstallError

from core import Mana
from core import Install
from core import get_os_information
mana = Mana()


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hamagui")
        space_size = 12

        grid = Gtk.Grid()
        self.add(grid)

        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

        label = Gtk.Label(label="Status", expand=1)
        self.label_status = Gtk.Label(expand=1)
        self.button_status = Gtk.Button(expand=1)
        self.button_status.connect("clicked", self.button_status_clicked)
        grid.add(label)
        grid.attach(self.label_status, 1, 0, 1, 1)
        grid.attach(self.button_status, 2, 0, 1, 1)

        label = Gtk.Label(label="Nickname", expand=1)
        self.entry_nickname = Gtk.Entry(placeholder_text="Krai53n", expand=1)
        self.button_nickname = Gtk.Button(label="Apply", expand=1)
        self.button_nickname.connect("clicked", self.button_nickname_clicked)
        grid.attach(label, 0, 1, 1, 1)
        grid.attach(self.entry_nickname, 1, 1, 1, 1)
        grid.attach(self.button_nickname, 2, 1, 1, 1)

        label = Gtk.Label(label="Client ID", expand=1)
        self.label_client_id = Gtk.Label(label="234.234.234", expand=1)
        self.button_client_id = Gtk.Button(label="Copy", expand=1)
        self.button_client_id.connect("clicked", self.button_client_id_clicked)
        grid.attach(label, 0, 2, 1, 1)
        grid.attach(self.label_client_id, 1, 2, 1, 1)
        grid.attach(self.button_client_id, 2, 2, 1, 1)


        label = Gtk.Label(label="Address", expand=1)
        self.label_address = Gtk.Label(label="234.234.45", expand=1)
        self.button_address = Gtk.Button(label="Copy", expand=1)
        self.button_address.connect("clicked", self.button_address_clicked)
        grid.attach(label, 0, 3, 1, 1)
        grid.attach(self.label_address, 1, 3, 1, 1)
        grid.attach(self.button_address, 2, 3, 1, 1)

        label = Gtk.Label(label="To join", expand=1)
        self.entry_join = Gtk.Entry(placeholder_text="kryakryakrya", expand=1)
        self.button_join = Gtk.Button(label="Join", expand=1)
        self.button_join.connect("clicked", self.button_join_clicked)
        grid.attach(label, 0, 4, 1, 1)
        grid.attach(self.entry_join, 1, 4, 1, 1)
        grid.attach(self.button_join, 2, 4, 1, 1)

        self.update()

    def get_status(self):
        status = mana.hamachi_inf()["status"]
        if status == "offline":
            return "offline", "online"
        if status != "offline":
            return "online", "offline"
    
    def update(self):
        """
        Update all possible elements of Gui
        """
        self.label_status.props.label = self.get_status()[0]
        self.button_status.props.label = self.get_status()[1]
        self.entry_nickname.props.placeholder_text = mana.hamachi_inf()["nickname"]
        self.label_client_id.props.label = mana.hamachi_inf()["client id"]
        self.label_address.props.label = mana.hamachi_inf()["address"]
        try:
            self.entry_join.props.placeholder_text = mana.hamachi_inf()["list"][-1]
        except IndexError:
            self.entry_join.props.placeholder_text = ""

    def button_status_clicked(self, button):
        label = self.label_status.get_label()
        if label == "online":
            mana.logged_off()
        if label == "offline":
            mana.logged_in()
        self.update()

    def button_nickname_clicked(self, button):
        text = self.entry_nickname.get_text()
        if text:
            mana.set_nickname(self.entry_nickname.get_text())
        self.update()

    def button_client_id_clicked(self, button):
        self.clipboard.set_text(self.label_client_id.get_label(), -1)
        self.update()

    def button_address_clicked(self, button):
        self.clipboard.set_text(self.label_address.get_label(), -1)
        self.update()

    def button_join_clicked(self, button):
        text = self.entry_join.get_text()
        if text:
            mana.join_network(text)
        self.update()

def run_main_window():
    main_window = MainWindow()
    main_window.connect("destroy", Gtk.main_quit)
    main_window.show_all()
    Gtk.main()

def main():
    if get_os_information()[0] != "linux":
        OsError().run()
        return 0

    install = False
    if not mana.check_hamachid(getcwd()):
        dialog = InstallError()
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            install = True
            dialog.destroy()
        if response == Gtk.ResponseType.CANCEL:
            return 0
    if install:
        Install()

    try:
        run_main_window()
    except AttributeError:
        # if hamachid is not run
        mana.power_on_hamachid()
        sleep(0.1)
        run_main_window()


if __name__ == "__main__":
    main()
