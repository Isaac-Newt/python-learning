# This will create a window with 6 buttons
# These buttons are arranged in a grid, and
# demonstrate different position types.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# define window
class MainWindow(Gtk.Window):

    # set up window contents
    def __init__(self):
        # window title
        Gtk.Window.__init__(self, title="Grid Example")
        # Creat Grid
        grid = Gtk.Grid()
        self.add(grid)

        # Create buttons
        button1 = Gtk.Button(label="button 1")
        button2 = Gtk.Button(label="button 2")
        button3 = Gtk.Button(label="button 3")
        button4 = Gtk.Button(label="button 4")
        button5 = Gtk.Button(label="button 5")
        button6 = Gtk.Button(label="button 6")

        # Add button, default spot
        grid.add(button1)

        # Add button: Ref. to grid
        # item, column, row, width, height
        grid.attach(button2, 1, 0, 2, 1)

        # Add button: Ref. to other button
        # item, ref. item, rel. to ref., width, height
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)

        # Add remaining buttons
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
