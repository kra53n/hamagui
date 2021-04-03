import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ListBoxWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ListBox")
        self.set_border_width = 50
        
        box_outer = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
        )
        self.add(box_outer)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, 1, 1, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, 1, 1, 0)

        label1 = Gtk.Label(label="Automatic Date&Time", xalign=0)
        label2 = Gtk.Label(label="Requires internter access", xalign=0)
        vbox.pack_start(label1, 1, 1, 0)
        vbox.pack_start(label2, 1, 1, 0)

        switch = Gtk.Switch()
        switch.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switch,  0, 1, 0)
        
        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label(label="Enable Automatic Update", xalign=0)
        check = Gtk.CheckButton()
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(check, False, False, True)

        listbox.add(row)



if __name__ == "__main__":
    win = ListBoxWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()