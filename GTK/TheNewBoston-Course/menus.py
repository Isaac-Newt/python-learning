import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

# define window
class MainWindow(Gtk.Window):

    # set up window contents
    def __init__(self):
        Gtk.Window.__init__(self, title="Fake Menus")
        layout = Gtk.Box()
        self.add(layout)

        # Create menubar container
        main_menubar = Gtk.MenuBar()

        # Add menus to menubar

        # File menu
        file_menu = Gtk.Menu()
        file_menu_dropdown = Gtk.MenuItem("File")
        # Items
        file_new = Gtk.MenuItem("New")
        file_open = Gtk.MenuItem("Open")
        file_quit = Gtk.MenuItem("Quit")
        # Build
        file_menu_dropdown.set_submenu(file_menu)
        file_menu.append(file_new)
        file_menu.append(file_open)
        # Separator
        file_menu.append(Gtk.SeparatorMenuItem())
        file_menu.append(file_quit)

        main_menubar.append(file_menu_dropdown)
        layout.pack_start(main_menubar, True, True, 0)

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
