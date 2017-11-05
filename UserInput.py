# This demonstrates text input by immitating
# a login form.  It displays the entered text
# in the console when the button is clicked.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

# define window
class MainWindow(Gtk.Window):

    # set up window contents
    def __init__(self):
        Gtk.Window.__init__(self, title="Fake login screen")
        self.set_border_width(10)
        self.set_default_size(200, 100)

        # layout
        vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 8)
        self.add(vbox)

        # Username
        self.username = Gtk.Entry()
        self.username.set_text("username")
        vbox.pack_start(self.username, True, True, 0)

        # Password
        self.password = Gtk.Entry()
        self.password.set_text("password")
        # Make password into dots
        self.password.set_visibility(False)
        vbox.pack_start(self.password, True, True, 0)

        # Submit Button
        self.button = Gtk.Button(label = "Sign In")
        self.button.connect("clicked", self.sign_in)
        vbox.pack_start(self.button, True, True, 0)

    # Run this when button clicked
    def sign_in(self, widget):
    	# print username
    	print(self.username.get_text())
    	# print password
    	print(self.password.get_text())

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
