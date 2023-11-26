import gi
import random

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class mojProzor(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Projekat")

        grid = Gtk.Grid()
        self.add(grid)

        self.set_border_width(10)
        self.set_size_request(200, 100)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.add(vbox)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        self.add(vbox)

        self.objasnjenje = Gtk.Label()
        self.objasnjenje.set_label("Napiši ispod šta želiš da piše na dugmadima")
        vbox.pack_start(self.objasnjenje, True, True, 0)

        #Ulaz
        self.ulaz1 = Gtk.Entry()
        vbox.pack_start(self.ulaz1, True, True, 0)
        
        self.ulaz2 = Gtk.Entry()
        vbox.pack_start(self.ulaz2, True, True, 0)

        self.stavi = Gtk.Button()
        self.stavi.set_label("Stavi")
        self.stavi.connect("clicked", self.jej)
        vbox.pack_start(self.stavi, True, True, 0)

        self.dugme1 = Gtk.Button()
        self.dugme1.connect("clicked", self.odgovor)
        hbox.pack_start(self.dugme1, True, True, 0)

        
        self.dugme2 = Gtk.Button()
        self.dugme2.connect("clicked", self.odgovor)
        hbox.pack_start(self.dugme2, True, True, 0)

        grid.add(vbox)
        grid.attach(hbox, 0, 1, 1, 1)

    def jej(self, wiget):
        self.dugme1.set_label(self.ulaz1.get_text())
        self.dugme2.set_label(self.ulaz2.get_text())
        
    def odgovor(self, wiget):
        class oProzor(Gtk.Window):
            def __init__(self):
                Gtk.Window.__init__(self, title="Odgovor")
                self.set_size_request(200, 100)

                broj = random.randint(0,9)

                if broj % 2 == 0:
                    self.lepo = Gtk.Label("Lepo")
                    self.add(self.lepo)
                else:
                    self.zanimljivo = Gtk.Label("Zanimljivo")
                    self.add(self.zanimljivo)
        op = oProzor()
        op.connect("destroy", Gtk.main_quit)
        op.show_all()
        Gtk.main()

prozor = mojProzor()
prozor.connect("destroy", Gtk.main_quit)
prozor.show_all()
Gtk.main()
