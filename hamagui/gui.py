import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from core import Mana
mana = Mana()


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hamagui")
        space_size = 12

        self.box_status = Gtk.Box(spacing=space_size)
        self.label_status = Gtk.Label(label="Status")
        self.label_status_show = Gtk.Label(label="online")
        self.button_status = Gtk.Button(label="offline")

        self.box_nickname = Gtk.Box(spacing=space_size)
        self.label_nickname = Gtk.Label(label="Nickname")
        self.entry_nickname = Gtk.Entry()
        self.button_nickname = Gtk.Button()

        self.box_client_id = Gtk.Box(spacing=space_size)
        self.label_client_id = Gtk.Label(label="Client ID")
        self.label_client_id_show = Gtk.Label()
        self.button_client_id = Gtk.Button(label="Copy")

        self.box_address = Gtk.Box(spacing=space_size)
        self.label_address = Gtk.Label(label="Client ID")
        self.label_address_show = Gtk.Label()
        self.button_address = Gtk.Button()

        self.box_to_join = Gtk.Box(spacing=space_size)
        self.label_to_join = Gtk.Label(label="To join")
        self.entry_to_join = Gtk.Button()
        self.button_to_join = Gtk.Label(label="Join")


        self.add(self.box_status)
        self.box_status.pack_start(self.label_status, 1, 1, 0)
        self.box_status.pack_start(self.label_status_show, 1, 1, 0)
        self.box_status.pack_start(self.button_status, 1, 1, 0)

        self.add(self.box_nickname)
        self.box_status.pack_start(self.label_nickname, 1, 1, 0)
        self.box_status.pack_start(self.entry_nickname, 1, 1, 0)
        self.box_status.pack_start(self.button_nickname, 1, 1, 0)


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.connect("destroy", Gtk.main_quit)
    main_window.show_all()
    Gtk.main()
