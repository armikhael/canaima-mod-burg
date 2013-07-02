#!/usr/bin/python
# -*- coding: utf-8 -*-
#@author:  Randy Ortega <ortega571@gmail.com>
#@Maintainer: Carlos Espinoza <carlosarmikhael@gmail.com>

import pygtk
pygtk.require('2.0')
import gtk
import os
import Image
import sys
from subprocess import Popen, PIPE, STDOUT
import webkit
import gobject

#Funcion de barra Progresiva
def barra_progresiva(pbobj):
	new_val = pbobj.barra_progreso.get_fraction() + 0.01
	if new_val > 1.0:
		new_val = 0.0
	pbobj.barra_progreso.set_fraction(new_val)
	return True

##--------------Clase Principal de la aplicación Canaima_mod_burg----------------------##
class CanaimaBurgModificar:
	
	#Rutas - - - - -
    WORKDIR = sys.path[0]
    MONITOR_IMG ='../img/monitor.png'
    RUTA_BUG = '/boot/burg/themes/'
    RUTA_TMP = '/tmp/pre_view.png'
    AYUDA_RUTA_SISTEMA = '/usr/share/gnome/help/canaima-mod-burg/es/canaima-mod-burg.xml'
    
    def __init__(self):
        
        #Vetana - - - - -
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_resizable(False)
        self.window.set_title("Temas del Burg")
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_border_width(0)
        self.window.set_size_request(550, 540)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        #self.window.set_icon_from_file('/usr/share/pixmaps/canaima-burg-icon.png')
        
        #Contenedor - - - - -
        self.fixed = gtk.Fixed()
        
        #Etiqueta Descripción - - - - -
        self.label_description = gtk.Label()
        self.label_description.set_markup(
        "Modifica los temas existentes del burg.")
        self.fixed.put(self.label_description, 130,10)
        self.label_description.show()
		
		#Etiqueta tema - - - - -
        self.label_tema_selec= gtk.Label()
        self.label_tema_selec.set_markup(
        "Seleccione el Thema : ")
        self.fixed.put(self.label_tema_selec, 110, 50)
        self.label_tema_selec.show()
        
        #Pestaña desplegable - - - - -
        ruta_burg = next(os.walk(self.RUTA_BUG))[1]
        ruta_burg.sort(key=lambda x: x.upper())
        self.combox_themas = gtk.combo_box_new_text()
        self.combox_themas.set_size_request(180, 35)
        for datos_ruta in ruta_burg:
			if datos_ruta == "icons" or datos_ruta == "conf.d" or datos_ruta == "burg" or datos_ruta == "radiance":
				False
			else:
				self.combox_themas.append_text(datos_ruta)        
        self.fixed.put(self.combox_themas, 280, 40)
        self.combox_themas.show()
        self.combox_themas.connect('changed', self.emulando_thema_burg)
        
        #Imagen Monitor - - - - -
        self.image_pc = gtk.Image()
        self.image_pc.set_from_file(self.MONITOR_IMG)
        self.fixed.put(self.image_pc, 54, 90)
        self.image_pc.show()
        
        #Boton Aplicar - - - - -
        self.button_aplicar = gtk.Button(stock=gtk.STOCK_APPLY)
        self.button_aplicar.set_size_request(80, 30)
        self.button_aplicar.connect("clicked",self.aplicar_thema_burg)
        self.fixed.put(self.button_aplicar, 460,500)
        self.button_aplicar.show()
        
        #~ #Boton Atras - - - - -
        #~ self.button_atras = gtk.Button(stock=gtk.STOCK_GO_BACK)
        #~ self.button_atras.set_size_request(80, 30)
        #~ self.button_atras.connect("clicked",self.atras_inicio)
        #~ self.fixed.put(self.button_atras, 370,500)
        #~ self.button_atras.show()
        
        #Boton Ayuda - - - - -
        self.button_ayuda = gtk.Button(stock=gtk.STOCK_HELP)
        self.button_ayuda.set_size_request(70, 30)
        self.button_ayuda.connect("clicked",self.ayuda_thema_burg)
        self.fixed.put(self.button_ayuda, 110,500)
        self.button_ayuda.show()
        
        #Boton Cerrar - - - - -
        self.button_cerrar = gtk.Button(stock=gtk.STOCK_QUIT)
        self.button_cerrar.set_size_request(80, 30)
        self.button_cerrar.connect("clicked",self.destroy)
        self.fixed.put(self.button_cerrar, 15,500)
        self.button_cerrar.show()
        
        #WebKit - - - -
        self.view = webkit.WebView()
        
        self.window.add(self.fixed)
        self.window.show_all()
        self.window.show()
	
	#Funcion que emula el tema del burg
    def emulando_thema_burg(self, combox_themas):
        if combox_themas.get_active_text():
            ruta_img_theme = self.RUTA_BUG + combox_themas.get_active_text() + '/background.png'
            imagen_thema = Image.open(ruta_img_theme)
            ancho = 417
            altura = 270
            def_img = imagen_thema.resize((ancho, altura), Image.ANTIALIAS)
            def_img.save(self.RUTA_TMP)
            
            if os.path.exists(self.RUTA_TMP):         
                self.view.open('file:///'+self.WORKDIR+'/html/index.html')
                self.fixed.put(self.view,71, 111)
                self.view.show()
                self.view.reload()
                self.barra_progreso = gtk.ProgressBar()
                self.barra_progreso.set_size_request(250, 12)
                self.fixed.put(self.barra_progreso, 155 , 325)
                self.barra_progreso.show()
                self.timer = gobject.timeout_add (1000, barra_progresiva, self)
                
            else:
                # Tremendo lio Error
                pass 
 
    def delete_event(self, widget, event, data=None):
        return False
 
    def destroy(self, widget, data=None):
        os.system('rm ' + self.RUTA_TMP)
        gtk.main_quit()
    
    #Funcion de Aplicar Tema del Burg
    def aplicar_thema_burg(self, widget):
		self.nombre_thema = self.combox_themas.get_active_text()
		
		#Funcion Barra de Progreso aleatoria
		def barra_aleatoria(self):
			self.barra_progreso.pulse()
			return True
		
		if not self.nombre_thema:
			error_mensaje=gtk.MessageDialog(type=gtk.MESSAGE_ERROR, buttons=gtk.BUTTONS_OK,
			                                message_format="Tiene que seleccionar un tema.\t")
			error_mensaje.set_title('ERROR')
			error_mensaje.run()
			error_mensaje.destroy()
		
		else:
			timer_1 = gobject.timeout_add (100, barra_aleatoria,self)
			os.chdir("/etc/default/")
			Popen(["sed -i 's/GRUB_THEME=.*/GRUB_THEME='"+self.nombre_thema+"'/g' burg"], shell=True, stdout=PIPE)
			Popen(["update-burg"], shell=True, stdout=PIPE)
			self.barra_progreso.set_text("Tema Cambiando ")
			aceptar_mensaje=gtk.MessageDialog(parent=None, flags=0, buttons=gtk.BUTTONS_OK, 
											  message_format='Su tema del Burg ha sido modificado por "'+ 
											  self.nombre_thema + '".\t')
			aceptar_mensaje.set_title('')
			aceptar_mensaje.run()
			aceptar_mensaje.destroy()
			self.combox_themas.set_active(-1)
			timer_2 = gobject.source_remove(timer_1)
			self.barra_progreso.set_text(" ")
	
	#Funcion del Manual de ayuda 
    def ayuda_thema_burg(self, widget):
		x= Popen(['yelp '+self.AYUDA_RUTA_SISTEMA], shell=True, stdout=PIPE)

    #~ def atras_inicio(self, widget):
		#~ canaima_mod_burg_inicio.CanaimaBurgInicio()
		#~ self.window.hide()
		
def main():
    gtk.main()
    return 0
 
if __name__ == "__main__":
    CanaimaBurgModificar()
    main()
