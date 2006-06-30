#!/usr/bin/env python
# coding: utf-8
# Sensor de Temperatura para un iBook

# Importo las bibliotecas que necesito:
import os, gtk, gnome.applet, gnome.ui


def actualizar(label):

   # Tratacamos la temperatura de la cpu
   try:
      fich = open('/sys/devices/temperatures/sensor1_temperature','r')
      cpu_temperature = fich.read(2)
      fich.close()
   except IOError:
      # linux<=2.6.11
      try:
         fich = open('/sys/devices/temperatures/cpu_temperature','r')
         cpu_temperature = fich.read(2)
         fich.close()
      except IOError:
         cpu_temperatura = '??'
                  

   # Y la velocidad del ventilador
   try:
      fich = open('/sys/devices/temperatures/sensor1_fan_speed','r')
      aux = fich.read().split('(')
      cpu_fan_speed = aux[1][:-2]
      fich.close()
   except IOError:
      # linux<=2.6.11
      try:
         fich = open('/sys/devices/temperatures/cpu_fan_speed','r')
         aux = fich.read().split('(')
         cpu_fan_speed = aux[1][:-2]
         fich.close()
      except IOError:
         cpu_fan_speed = '?? rpm'


   # etiqueta para el applet
   label.set_text(cpu_temperature + "\302\260C - " + cpu_fan_speed)

   # Este TRUE es fundamental
   return gtk.TRUE

def about(uicomponent, verb):
   gnome.ui.About("xatar",
                  "v0.0.1",
                  "Copyright 2005 Pablo Lopez Cienfuegos",
                  ("Xtrasgu Applet for Temperature And Revolutions"),
                  ["Pablo Lopez Cienfuegos <xtrasgu@asturlinux.org> \nSergio Fdez Lopez <wikier@asturlinux.org>"],
                  ["Programa sin documentar (los comentarios son tus amigos)"],
                  "Programa sin traducir",
                  gtk.gdk.pixbuf_new_from_file("/usr/share/pixmaps/xatar.png")).show()


def xatar_applet(applet, iid):
   # Definimos el Applet
   label = gtk.Label("xatar")
   applet.add(label)
   applet.show_all()

   # Creamos el temporizador
   gtk.timeout_add(500, actualizar, label)   # Milisegundos, Funcion, Parametro

   # Entrada About del menu... ¿quién coño documenta esto?
   applet.setup_menu_from_file(None, "/usr/lib/xatar/xatar.xml", None, [("About", about)])

   # Salimos como chicos buenos
   return gtk.TRUE


gnome.applet.bonobo_factory("OAFIID:XATAR_Factory",
                            gnome.applet.Applet.__gtype__, 
                            "hello", "0", xatar_applet)


# Código para depurar el Applet:
#import sys
#if len(sys.argv) == 2:
#   main_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
#   main_window.set_title("Python Applet")
#   main_window.connect("destroy", gtk.main_quit)
#   app = gnome.applet.Applet()
#   xtrasgu_applet(app, None)
#   app.reparent(main_window)
#   main_window.show_all()
#   gtk.main()
#   sys.exit()
