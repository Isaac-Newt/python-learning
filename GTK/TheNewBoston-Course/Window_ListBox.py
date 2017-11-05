# This will create a window with a ListBox.
# This ListBox will contain _______________

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# define window
class MainWindow(Gtk.Window):

    # set up window contents
    def __init__(self):
        # window title
        Gtk.Window.__init__(self, title="Cheeseburger Factory")
        # Set border for window internals
        self.set_border_width(10)

        # Create ListBox
        listbox = Gtk.ListBox()
        # Limit selection to items in list
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)

        # Add listbox to window
        self.add(listbox)

        # Add elements to listbox

        # Add row to list
        row_1 = Gtk.ListBoxRow()
        # Create box for more flexibility in layout, esp. spacing
        box_1 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 100)
        # Clean up
        row_1.add(box_1)

        # Checkbox
        label = Gtk.Label("Check for cheese on your burger")
        checkbox = Gtk.CheckButton()
        box_1.pack_start(label, True, True, 0)
        box_1.pack_start(checkbox, True, True, 0)
        listbox.add(row_1)

        # Add second row to list
        row_2 = Gtk.ListBoxRow()
        box_2 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 100)
        row_2.add(box_2)

        # Toggle Switch
        label = Gtk.Label("Start Making the Burger")
        toggle = Gtk.Switch()
        box_2.pack_start(label, True, True, 0)
        box_2.pack_start(toggle, True, True, 0)
        listbox.add(row_2)

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
