"""
Credit: Isaac List
Modified: June 27, 2019

This simple app takes three inputs 
a, b, c in the form ax^2 + bx + c, 
and outputs the resulting x values
in the console.  
"""

import math
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

# define window
class MainWindow(Gtk.Window):
    """Extend Gtk.Window"""

    def __init__(self):
        """Build the application window"""
        Gtk.Window.__init__(self, title="Quadratic Solver")
        self.set_border_width(10)
        self.set_default_size(200, 100)

        # layout
        vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 8)
        self.add(vbox)

        # Practicing your ABC's
        self.A = Gtk.Entry()
        self.B = Gtk.Entry()
        self.C = Gtk.Entry()
        entries = [self.A, self.B, self.C]
        characters = ["A", "B", "C"]

        # Build the inputs
        for index in range(len(characters)):
            hbox = Gtk.Box(spacing = 8)
            # Don't use this index thing
            label = Gtk.Label(characters[index])

            hbox.pack_start(label, True, True, 0)
            # Don't use this index thing
            hbox.pack_start(entries[index], True, True, 0)

            vbox.pack_start(hbox, True, True, 0)

        # Submit Button
        self.submit_button = Gtk.Button(label = "Calculate")
        self.submit_button.connect("clicked", self.calculate)
        vbox.pack_start(self.submit_button, True, True, 0)

        # Answer field
        self.answer_field = Gtk.Label("")        
        vbox.pack_start(self.answer_field, True, True, 0)

    
    def display_answer(self, result):
        """Display the results in the window"""
        self.answer_field = Gtk.Label()

    # Run this when button clicked
    def calculate(self, widget):
        """Calculate the quadratic formula"""
        # read in results
        A = float(self.A.get_text())
        B = float(self.B.get_text())
        C = float(self.C.get_text())
        
        # calculate result
        result_1 = (-B + math.  sqrt((B**2)-(4*A*C))) / (2*A)
        result_2 = (-B - math.sqrt((B**2)-(4*A*C))) / (2*A)
    	
        # format result
        result = f"x = {result_1}, {result_2}"
        display_answer(result)
        

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
