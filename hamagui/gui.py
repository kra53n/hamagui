import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from core import Mana
mana = Mana()

# print(dir(Gtk.Switch()))


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hamagui")
        space_size = 12

        grid = Gtk.Grid()
        self.add(grid)

        label = Gtk.Label(label="Status", expand=1)
        self.label_status = Gtk.Label(label="Offline", expand=1)
        self.button_status = Gtk.Button(label="Online", expand=1)
        grid.add(label)
        grid.attach(self.label_status, 1, 0, 1, 1)
        grid.attach(self.button_status, 2, 0, 1, 1)

        label = Gtk.Label(label="Nickname", expand=1)
        self.entry_nickname = Gtk.Entry(placeholder_text="Krai53n", expand=1)
        self.button_nickname = Gtk.Button(label="Apply", expand=1)
        grid.attach(label, 0, 1, 1, 1)
        grid.attach(self.entry_nickname, 1, 1, 1, 1)
        grid.attach(self.button_nickname, 2, 1, 1, 1)

        label = Gtk.Label(label="Client ID", expand=1)
        self.label_client_id = Gtk.Label(label="234.234.234", expand=1)
        self.button_client_id = Gtk.Button(label="Copy", expand=1)
        grid.attach(label, 0, 2, 1, 1)
        grid.attach(self.label_client_id, 1, 2, 1, 1)
        grid.attach(self.button_client_id, 2, 2, 1, 1)


        label = Gtk.Label(label="Address", expand=1)
        self.label_address = Gtk.Label(label="234.234.45", expand=1)
        self.button_address = Gtk.Button(label="Copy", expand=1)
        grid.attach(label, 0, 3, 1, 1)
        grid.attach(self.label_address, 1, 3, 1, 1)
        grid.attach(self.button_address, 2, 3, 1, 1)

        label = Gtk.Label(label="To join", expand=1)
        self.entry_join = Gtk.Entry(placeholder_text="kryakryakrya", expand=1)
        self.button_join = Gtk.Button(label="Join", expand=1)
        grid.attach(label, 0, 4, 1, 1)
        grid.attach(self.entry_join, 1, 4, 1, 1)
        grid.attach(self.button_join, 2, 4, 1, 1)


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.connect("destroy", Gtk.main_quit)
    main_window.show_all()
    Gtk.main()
