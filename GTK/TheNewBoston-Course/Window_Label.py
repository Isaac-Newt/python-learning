# my first python program with pygobject
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()

#create widget
label = Gtk.Label() 
#set properties
label.set_label("Python and GTK3 Rock!")
label.set_angle(25)
label.set_halign(Gtk.Align.END)
#add to window
window.add(label) 

#get angle property
print(label.get_properties("angle"))

window.connect("delete-event", Gtk.main_quit)
window.show_all()

Gtk.main()
