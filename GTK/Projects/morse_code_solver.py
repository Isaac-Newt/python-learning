"""
Credits: Isaac List
Modified: June 30 2019
"""

# This Source Code Form is subject to the terms of the 
# Mozilla Public License, v. 2.0. If a copy of the MPL 
# was not distributed with this file, You can obtain 
# one at https://mozilla.org/MPL/2.0/.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    """Create an application window"""

    def __init__(self):
        """Initialize Window Contents"""

        # Window title
        Gtk.Window.__init__(self, title="Morse Code Generator")

        # Window padding
        self.set_border_width(10)
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)

        # Stack
        self.main_area = Gtk.Stack()
        self.main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.main_area.set_transition_duration(500)

        self.create_first_stack()

        """
        Morse to Letters Stack
        """

        # Label
        label = Gtk.Label()
        label.set_markup("<big>This Text Is HUGE!</big>")

        # Label the second stack
        self.main_area.add_titled(label, "label_name", "big label")

        # StackSwitcher (Tabs)
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(self.main_area)
        box.pack_start(stack_switcher, True, True, 0)
        box.pack_start(self.main_area, True, True, 0)

    def create_first_stack(self):
        self.letters_to_morse = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing = 8)

        # Input form
        hbox1 = Gtk.Box(spacing = 8)
        label = Gtk.Label("Enter Text:")
        self.letter_input = Gtk.Entry()
        hbox1.pack_start(label, True, True, 0)
        hbox1.pack_start(self.letter_input, True, True, 0)

        self.letters_to_morse.pack_start(hbox1, True, True, 0)

        # Submit button
        self.submit_button = Gtk.Button(label = "Convert")
        self.submit_button.connect("clicked", self.to_morse)
        self.letters_to_morse.pack_start(self.submit_button, True, True, 0)

        # Output area
        hbox2 = Gtk.Box(spacing = 8)
        label = Gtk.Label("Morse Transcription:")
        self.morse_output = Gtk.Entry()
        self.morse_output.set_editable(False)
        hbox2.pack_start(label, True, True, 0)
        hbox2.pack_start(self.morse_output, True, True, 0)

        self.letters_to_morse.pack_start(hbox2, True, True, 0)

        # add_titled for section labels.  2nd item = ID, third = section label
        self.main_area.add_titled(self.letters_to_morse, "let_to_mor", "To Morse Code")
    
    def to_morse(self, input):
        """Convert text to Morse Code"""
        print("text to morse")



window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
