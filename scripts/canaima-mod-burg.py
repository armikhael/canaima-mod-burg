#!/usr/bin/python

#Modificador de temas Burg-Canaima
import pygtk
import gtk
import os
import Image

# -------------- Variable global ------------------------------
text = next(os.walk("/boot/burg/themes"))[1]
combobox=gtk.combo_box_new_text()

for t in text:
	if t == "icons" or t == "conf.d" or t == "burg" or t == "radiance":
		print "No es tema"
	else:	
		combobox.append_text(t)
     
#---------------- Clase Principal -----------------------------
class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()
  
        # Defino la ventana
        self.set_title("Modificador de temas del BURG")
        self.set_size_request(300, 200)
        self.set_resizable(0)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_icon_from_file('/usr/share/icons/canaima-iconos/apps/48/man-burg-icon.png')

        self.fixed = gtk.Fixed()

		# Defino el banner        
        self.image = gtk.Image()
        self.image.set_from_file('/usr/share/images/banner.png')
        self.fixed.put(self.image, 0, 0)
        self.image.show()

		# Defino la etiqueta del titulo        
        self.label = gtk.Label()
        self.label.set_markup("<b>MODIFICADOR DE TEMAS DEL BURG</b>")
        self.fixed.put(self.label, 21, 60)
        
        # Defino la linea separadora
        self.linea = gtk.HSeparator() 
        self.linea.set_size_request(300, 1)
        self.fixed.put(self.linea, 0, 85)
        self.linea.show()

		# Defino la etiqueta de tema
        self.label = gtk.Label("TEMA:")
        self.fixed.put(self.label, 60, 110)
        
              
        self.button = gtk.Button("Guardar")
        self.fixed.put(self.button, 35,150)
        self.button.connect("clicked",self.modificar)
        
        self.button = gtk.Button("Ayuda")
        self.fixed.put(self.button, 123,150)
        self.button.connect("clicked",self.ayudar)
        
        # Defino el boton
        self.button = gtk.Button("Cancelar")
        self.button.connect("clicked",gtk.main_quit)
        self.fixed.put(self.button, 200,150)
        
		
        self.fixed.put(combobox, 100,105)
        

        self.connect("destroy", gtk.main_quit)
        self.add(self.fixed)
        self.show_all()
        
    def ayudar(self, widget=None):
        os.system('yelp /usr/share/gnome/help/canaima-mod-burg/es/canaima-mod-burg.xml')
        
    def modificar(self, event):
		tema = combobox.get_active_text()
		
		if not tema: 
			error=gtk.MessageDialog(type=gtk.MESSAGE_ERROR, buttons=gtk.BUTTONS_OK, message_format="Tiene que seleccionar un tema")
			error.run()
			error.destroy()
		else:
			os.chdir("/etc/default/")
			os.system("sed -i 's/GRUB_THEME=.*/GRUB_THEME='"+tema+"'/g' burg")
			os.system("update-burg")
			os.system("xterm -e burg-emu")	
			fin=gtk.MessageDialog(type=gtk.MESSAGE_WARNING, buttons=gtk.BUTTONS_OK, message_format="Su tema ha sido modificado")
			fin.run()
			fin.destroy()
			combobox.set_active(-1)
PyApp()
gtk.main()
