# This demonstrates the various ways to style
# text in GTK3 applications.  It doesn't do
# anything else :)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

# define window
class MainWindow(Gtk.Window):

    # set up window contents
    def __init__(self):
        Gtk.Window.__init__(self, title="Notebook Example")
        self.set_border_width(20)
        self.set_default_size(500, 400)

        # Boxes

        # Outer horizontal box
        hbox = Gtk.Box(spacing = 20)
        hbox.set_homogeneous(False)
        # Inner vertical box, left
        vbox_left = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
        vbox_left.set_homogeneous(False)
        # Inner vertical box, right
        vbox_right = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
        vbox_right.set_homogeneous(False)

        # Pack the two columns
        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        # Normal Label
        label = Gtk.Label("This is a label")
        vbox_left.pack_start(label, True, True, 0)

        # Left aligned label
        label = Gtk.Label()
        label.set_text("This text is left-aligned. \n  Wow! Multiple lines!")
        label.set_justify(Gtk.Justification.LEFT)
        vbox_left.pack_start(label, True, True, 0)

        # Right aligned label
        label = Gtk.Label("This text is right-aligned")
        label.set_justify(Gtk.Justification.RIGHT)
        vbox_left.pack_start(label, True, True, 0)

        # Line Wrap
        label = Gtk.Label("Hi I'm Isaac, I am learning python.")
        label.set_line_wrap(True)
        vbox_right.pack_start(label, True, True, 0)

        # Fill (newspaper style)
        label = Gtk.Label("Hi, I'm writing a fake column for a fake newspaper to fill up some very real space so that it demonstrates a point the YouTube guy is trying to show me.")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        vbox_right.pack_start(label, True, True, 0)

        # Markup
        label = Gtk.Label()
        label.set_markup("<small>small text</small> \n"
                         "<b>bold text</b>\n"
                         "<a href=\"https://duckduckgo.com\" title=\"Search with ducks\">This is a link</a>"
                         )
        vbox_right.pack_start(label, True, True, 0)

        self.add(hbox)

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
