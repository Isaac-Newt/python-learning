# This demonstrates text input by immitating
# a login form.  It displays the entered text
# in the console when the button is clicked.

import math
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

# define window
class MainWindow(Gtk.Window):

    # set up window contents
    def __init__(self):
        Gtk.Window.__init__(self, title="Quadratics")
        self.set_border_width(10)
        self.set_default_size(200, 100)

        # layout
        vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 8)
        self.add(vbox)

        # A
        self.A = Gtk.Entry()
        self.A.set_text("A")
        vbox.pack_start(self.A, True, True, 0)

        # B
        self.B = Gtk.Entry()
        self.B.set_text("B")
        vbox.pack_start(self.B, True, True, 0)
        
        # C
        self.C = Gtk.Entry()
        self.C.set_text("C")
        vbox.pack_start(self.C, True, True, 0)

        # Submit Button
        self.button = Gtk.Button(label = "Calculate")
        self.button.connect("clicked", self.calculate)
        vbox.pack_start(self.button, True, True, 0)

    # Run this when button clicked
    def calculate(self, widget):
        # read in results
        A = float(self.A.get_text())
        B = float(self.B.get_text())
        C = float(self.C.get_text())
        
        # calculate result
        result_1 = (-B + math.  sqrt((B**2)-(4*A*C))) / (2*A)
        result_2 = (-B - math.sqrt((B**2)-(4*A*C))) / (2*A)
    	
        # print results
        print("x = ", end = '')
        print(str(result_1), ",", str(result_2), sep = '')

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
