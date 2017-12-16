# This doesn't seem to work, but the parts taken
# from this and added to python-gtk-textedit.py
# work as expected. ¯\_(ツ)_/¯

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

# define window
class MainWindow(Gtk.Window):
    def __init__(self):
        # Set window size
        self.set_border_width(10)
        self.set_default_size(500, 400)

        button = Gtk.Button("About")
        button.connect("clicked", self.button_clicked)
        self.add(button)

    def button_clicked(self, widget):
        Dialog = Popup(self)
        response = Dialog.run()

        if response == Gtk.ResponseType.OK:
            print("You clicked ok")
        elif response == Gtk.ResponseType.CANCEL:
            print("You clicked cancel")

        Dialog.destroy()

class Popup(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Popup Title", parent, Gtk.DialogFlags.MODAL,
            ("Custom Cancel Text", Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_border_width(10)
        self.set_default_size(200, 250)

        area = self.get_content_area()
        area.add(Gtk.Label("This is descriptive text for the about Dialog"))
        self.show_all()

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
