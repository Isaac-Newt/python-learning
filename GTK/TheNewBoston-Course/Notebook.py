# This produces a window with a "notebook"
# (Tabbed) UI.  Notebook = everything (including
# tabs), Pages = content of tabs

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

# define window
class MainWindow(Gtk.Window):

    # set up window contents
    def __init__(self):
        Gtk.Window.__init__(self, title="Notebook Example")
        self.set_border_width(10)
        self.set_default_size(500, 400)

        # Create Notebook
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # First Page
        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label("Here's stuff that's in the main area."))
        self.notebook.append_page(self.page1, Gtk.Label("First Tab Text"))

        # Second Page
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label("Hello from page two."))
        icon = Gtk.Image.new_from_icon_name("gnome-dev-cdrom-audio", Gtk.IconSize.MENU)
        self.notebook.append_page(self.page2, icon)

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
