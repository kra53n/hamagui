import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class WarningKillHamachid(Gtk.Dialog):
    def __init__(self):
        Gtk.Dialog.__init__(
            self,
            title="KillHamachid",
            flags=0,
        )
        self.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK,
            Gtk.ResponseType.OK,
        )

        label = Gtk.Label(label="Do you want kill hamachid process?")

        box = self.get_content_area()
        box.add(label)
        self.show_all()

class WarningRemoveHamachiFiles(Gtk.Dialog):
    def __init__(self):
        Gtk.Dialog.__init__(
            self,
            title="RemoveHamachiFiles",
            flags=0,
        )
        self.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK,
            Gtk.ResponseType.OK,
        )

        label = Gtk.Label(label="Do you want remove hamachi files?")

        box = self.get_content_area()
        box.add(label)
        self.show_all()
