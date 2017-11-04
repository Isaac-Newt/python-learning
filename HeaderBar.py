# https://www.youtube.com/watch?v=A2EmtjDe0kA

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
# Gio = icons, themes

# define window
class MainWindow(Gtk.Window):

    # set up window contents
    def __init__(self):
        Gtk.Window.__init__(self, title="HeaderBar Example")
        self.set_border_width(10)
        # Set window size
        self.set_default_size(500, 400)

        # Create HeaderBar
        headerbar = Gtk.HeaderBar()
        # Show close button
        headerbar.set_show_close_button(True)
        # Show, define title
        headerbar.props.title = "Fake Music Player"
        # Set titlebar to use headerbar
        self.set_titlebar(headerbar)

        # Add icons to HeaderBar

        # Audio button on right
        audio_button_right = Gtk.Button()
        # Take icon from Gio
        cd_icon = Gio.ThemedIcon(name="gnome-dev-cdrom-audio")
        # Convert icon to image; param = icon, size
        image = Gtk.Image.new_from_gicon(cd_icon, Gtk.IconSize.BUTTON)
        # Cleanup
        audio_button_right.add(image)
        headerbar.pack_end(audio_button_right)

        # Create box for linked items
        box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        # Left Arrow
        left_arrow = Gtk.Button()
        left_arrow.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(left_arrow)

        # right Arrow
        right_arrow = Gtk.Button()
        right_arrow.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        box.add(right_arrow)

        # Add box to HeaderBar
        headerbar.pack_start(box)

        # Add text typing area
        self.add(Gtk.TextView())

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
