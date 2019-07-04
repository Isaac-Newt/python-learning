"""
Credits: Isaac List
Updated: July 2019
License: MPL2

A basic GUI front-end to a Morse Code decoder project,
built using GTK (Python GObject).
"""

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL
# was not distributed with this file, You can obtain
# one at https://mozilla.org/MPL/2.0/.

# GTK
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Morse
from resources.morse import Coder


class MainWindow(Gtk.Window):
    """Create an application window"""

    def __init__(self):
        """Initialize Application"""
        # Create morse code tree
        # Should fix this path, as it's based on the root of the current terminal view.
        self.morse_coder = Coder("Morse Code Transcriber/resources/morse.txt")

        # Window title
        Gtk.Window.__init__(self, title="Morse Code Generator")

        # Window padding
        self.set_border_width(10)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)

        # Build the Stack
        self.initialize_stack()

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

    def initialize_stack(self):
        """Build the stack and its contents"""
        # Setup stack
        self.main_area = Gtk.Stack()
        self.main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.main_area.set_transition_duration(250)

        # Create stack pages
        self.create_first_stack()
        # self.create_second_stack()

    def create_first_stack(self):
        """Build the first stack (text to morse)"""
        self.letters_to_morse = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        # Input form
        self.text_input = Gtk.Entry()
        input_box = self.build_text_box("Enter Text:", self.text_input)
        self.letters_to_morse.pack_start(input_box, True, True, 0)

        # Submit button
        self.submit_button = Gtk.Button(label="Convert")
        self.submit_button.connect("clicked", self.display_morse)
        self.letters_to_morse.pack_start(self.submit_button, True, True, 0)

        # Output area
        self.morse_output = Gtk.Entry()
        self.morse_output.set_editable(False)
        output_box = self.build_text_box("Morse Transcription:", self.morse_output)
        self.letters_to_morse.pack_start(output_box, True, True, 0)

        # add_titled for section labels.  2nd item = ID, third = section label
        self.main_area.add_titled(self.letters_to_morse, "let_to_mor", "To Morse Code")

    def build_text_box(self, label: str, box_function):
        """Create a Gtk.Entry() element (i.e. text box)"""
        hbox = Gtk.Box(spacing=8)
        box_label = Gtk.Label(label)
        hbox.pack_start(box_label, True, True, 0)
        hbox.pack_start(box_function, True, True, 0)
        return hbox

    def to_morse(self, input_text: str):
        """Convert text to Morse Code"""
        code_string = self.morse_coder.encode(input_text)
        return code_string

    def display_morse(self, input_text):
        """Display converted text in the output box"""
        input_text = self.text_input.get_text()
        input_text = input_text.lower()
        print(input_text)
        morse_string = self.to_morse(input_text)
        self.morse_output.set_text(morse_string)
        


WINDOW = MainWindow()
WINDOW.connect("delete-event", Gtk.main_quit)
WINDOW.show_all()
Gtk.main()
