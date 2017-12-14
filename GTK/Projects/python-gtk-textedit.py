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
        # Set window size
        self.set_border_width(10)
        self.set_default_size(500, 400)

        # Add grid
        self.grid = Gtk.Grid()
        self.add(self.grid)

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

        # Create scrolled window
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 1, 3, 1)

        # Add text typing area
        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        # Set text to wrap after words
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        scrolledwindow.add(self.textview)

    def on_open_clicked(self, widget):
        print("open")

    def on_save_clicked(self, widget):
        print("save")
        self.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), True)
        filename = savechooser.get_filename()
        print(filename, 'selected.')

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
