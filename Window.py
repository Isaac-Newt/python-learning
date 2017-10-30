# my first python program with pygobject
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()
window.connect("delete-event", Gtk.main_quit)
window.show_all()

Gtk.main()
