# This will create a window with 2 buttons
# When clicked, the buttons will each print
# a message.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# define window
class MainWindow(Gtk.Window):

    # set up window contents
    def __init__(self):
        # window title
        Gtk.Window.__init__(self, title="Bacon or Tuna?")
        
        # Create Box (container to put widgets into)
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)
        
        # Bacon Button
        self.bacon_button = Gtk.Button(label="bacon")
        self.bacon_button.connect("clicked", self.button_clicked)
        # add items in box from left to right, with options
        self.box.pack_start(self.bacon_button, True, True, 0) 
        
        # Tuna Button
        self.tuna_button = Gtk.Button(label="tuna")
        self.tuna_button.connect("clicked", self.button_clicked)
        # add items in box from left to right, with options
        self.box.pack_start(self.tuna_button, True, True, 0) 
        
    # define button clicked action
    def button_clicked(self, widget):
        name = widget.get_properties("label")[0]
        print("you clicked " + name)
        
window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
