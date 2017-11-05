# A very, very simple text editor.
# Made with Python and GTK3 (via gobject)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

# define window
class MainWindow(Gtk.Window):

    # set up window contents
    def __init__(self):
        Gtk.Window.__init__(self, title="Text Editor")

        # Create HeaderBar
        headerbar = Gtk.HeaderBar()
        headerbar.set_show_close_button(True)
        headerbar.props.title = "Text Editor"
        self.set_titlebar(headerbar)

        open_button = Gtk.Button(label="Open")
        open_button.connect("clicked", self.on_open_clicked)
        headerbar.pack_start(open_button)

        save_button = Gtk.Button(label="Save")
        save_button.connect("clicked", self.on_save_clicked)
        headerbar.pack_start(save_button)

        # Add text typing area
        self.add(Gtk.TextView())

    def on_open_clicked(self, widget):
        print("open")

    def on_save_clicked(self, widget):
        print("save")

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
