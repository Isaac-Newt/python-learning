# This will create a window with a "tabbed" UI.
# In GTK, stackswitcher = section headers,
# stack = contents. This will have 2 stacks,
#one with a checkbox, the other with a large label.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# define window
class MainWindow(Gtk.Window):

    # set up window contents
    def __init__(self):
        # window title
        Gtk.Window.__init__(self, title="Switcher")
        # Padding
        self.set_border_width(10)
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)

        # Stack
        main_area = Gtk.Stack()
        main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        main_area.set_transition_duration(500)

        # Checkbox
        checkbox = Gtk.CheckButton("Do Not Check This Box!")
        # add_titled for section labels.  2nd item = ID, thrid = section label
        main_area.add_titled(checkbox, "checkbutton_name", "checkbox")

        # Label
        label = Gtk.Label()
        label.set_markup("<big>This Text Is HUGE!</big>")
        main_area.add_titled(label, "label_name", "big label")

        # StackSwitcher (Tabs)
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(main_area)
        box.pack_start(stack_switcher, True, True, 0)
        box.pack_start(main_area, True, True, 0)

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
