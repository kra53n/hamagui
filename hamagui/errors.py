import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class OsError(Gtk.Dialog):
    def __init__(self):
        Gtk.Dialog.__init__(
            self,
            title="OsError",
            flags=0,
        )
        self.add_buttons(
            Gtk.STOCK_OK,
            Gtk.ResponseType.OK,
        )

        message = "If you see this Error you have not Gnu/Linux.\n"
        message += "Hamagui is only for it"
        label = Gtk.Label(label=message)

        box = self.get_content_area()
        box.add(label)
        self.show_all()


class InstallError(Gtk.Dialog):
    def __init__(self):
        Gtk.Dialog.__init__(
                self,
                title="InstallError",
                flags=0,
        )
        self.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK,
            Gtk.ResponseType.OK,
        )

        message = "You do not have files of hamachi "
        message += "or they in another place.\n"
        message += "Put theme to this directory or "
        message += "Click `OK` to auto install this files"
        label = Gtk.Label(label=message)

        box = self.get_content_area()
        box.add(label)
        self.show_all()
