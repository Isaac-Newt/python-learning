# my first python program with pygobject
from gi.repository import Gtk

window = Gtk.Window()
window.connect("delete-event", Gtk_main.close)
wondow.show_all()

Gtk.main()
