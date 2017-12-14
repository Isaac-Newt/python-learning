import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

# define window
class MainWindow(Gtk.Window):

    # set up window contents
    def __init__(self):
        Gtk.Window.__init__(self, title="Entry Example")
        self.set_border_width(20)
        self.set_default_size(200, 100)

        # Layout
        vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        self.add(vbox)

        # Create entry text box
        self.entry = Gtk.Entry()
        self.entry.set_text("hello world")
        vbox.pack_start(self.entry, True, True, 0)

        # Create container for options
        hbox = Gtk.Box(spacing = 6)
        vbox.pack_start(hbox, True, True, 0)

        # Options

        # Editable Checkbutton
        self.check_editable = Gtk.CheckButton("Editable")
        self.check_editable.connect("toggled", self.on_editable_toggled)
        self.check_editable.set_active(True)
        hbox.pack_start(self.check_editable, True, True, 0)

        # Show/hide search icon Checkbutton
        self.icon = Gtk.CheckButton("Icon")
        self.icon.connect("toggled", self.on_icon_toggled)
        self.icon.set_active(False)
        hbox.pack_start(self.icon, True, True, 0)

    # Functions

    # Editable toggle
    def on_editable_toggled(self, button):
        # Gets value of the checkbox
        value = button.get_active()
        # Sets editable attribute of entry element based on value
        self.entry.set_editable(value)

    # Icon toggle
    def on_icon_toggled(self, button):
        if button.get_active():
            icon_name = "system-search-symbolic"
        else:
            icon_name = None
        self.entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY,
            icon_name)

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
