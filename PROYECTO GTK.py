import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

#             _____________________________________
#____________/ Ventana del menu

win = Gtk.Window()
win = Gtk.Window(title= "PLAY 2048 PLUS")
win.set_default_size(700,700)
win.set_resizable(False)


#_______________________
Menu_C = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
win.add(Menu_C)

MainBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
MainBox.set_halign(Gtk.Align.CENTER)
Menu_C.pack_end(MainBox,False,False,15)

#             ___________________
#____________/ Grid

Grid = Gtk.Grid()
Grid.set_halign(Gtk.Align.CENTER)
Menu_C.pack_end(Grid,False,False,15)

#             ______________________
#____________/ Entry 

NombreJugador = Gtk.Entry ()
Nom








win.connect("destroy",Gtk.main_quit)
win.show_all()
Gtk.main()
