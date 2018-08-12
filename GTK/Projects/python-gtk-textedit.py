# A very, very simple text editor.
# Made with Python and GTK3 (via gobject)

# Import GTK
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

# Import OS (File management)
import os

# define window
class MainWindow(Gtk.Window):

    # set up window contents
    def __init__(self):
        Gtk.Window.__init__(self, title="Text Editor")
        # Set window size
        self.set_border_width(10)
        self.set_default_size(500, 400)

        # Add gridut
        self.grid = Gtk.Grid()
        self.add(self.grid)

        # Create HeaderBar
        headerbar = Gtk.HeaderBar()
        headerbar.set_show_close_button(True)
        headerbar.props.title = "Text Editor"
        self.set_titlebar(headerbar)

        # Set up buttons
        open_button = Gtk.Button(label="Open")
        open_button.connect("clicked", self.on_open_clicked)
        headerbar.pack_start(open_button)

        save_button = Gtk.Button(label="Save")
        save_button.connect("clicked", self.on_save_clicked)
        headerbar.pack_start(save_button)

        about_button = Gtk.Button("About")
        about_button.connect("clicked", self.on_about_clicked)
        headerbar.pack_start(about_button)

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

    # About Dialog actions
    def on_about_clicked(self, widget):
        Dialog = Popup(self)
        response = Dialog.run()

        if response == Gtk.ResponseType.OK:
            print("You clicked ok")
        elif response == Gtk.ResponseType.CANCEL:
            print("You clicked cancel")

        Dialog.destroy()

class Popup(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Popup Title", parent, Gtk.DialogFlags.MODAL,
            ("Custom Cancel Text", Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_border_width(10)
        self.set_default_size(200, 250)

        area = self.get_content_area()
        area.add(Gtk.Label("This is descriptive text for the about Dialog"))
        self.show_all()

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
