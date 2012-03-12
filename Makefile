# Makefile

SHELL := sh -e

all: test build

test:
	@echo " Hecho!"

build:
	@echo "Nada para compilar!"


install:

	mkdir -p $(DESTDIR)/usr/share/images/
	mkdir -p $(DESTDIR)/usr/share/canaima-mod-burg/
	mkdir -p $(DESTDIR)/usr/share/applications/
	mkdir -p $(DESTDIR)/usr/bin/
	mkdir -p $(DESTDIR)/usr/share/icons/canaima-iconos/apps/48/
	mkdir -p $(DESTDIR)/usr/share/gnome/help/

	cp imagenes/banner.png $(DESTDIR)/usr/share/images/
	cp imagenes/man-burg-icon.png $(DESTDIR)/usr/share/icons/canaima-iconos/apps/48/
	cp desktop/canaima-mod-burg.desktop $(DESTDIR)/usr/share/applications/
	cp scripts/canaima-mod-burg $(DESTDIR)/usr/bin/
	cp scripts/canaima-mod-burg.py  $(DESTDIR)/usr/share/canaima-mod-burg/
	cp -r canaima-mod-burg $(DESTDIR)/usr/share/gnome/help/

uninstall:

	rm -rf $(DESTDIR)/usr/share/canaima-mod-burg/
	rm -rf $(DESTDIR)/usr/bin/canaima-mod-burg
	rm -rf $(DESTDIR)/usr/share/images/banner.png
	rm -rf $(DESTDIR)/usr/share/icons/canaima-iconos/apps/48/man-burg-icon.png
	rm -rf $(DESTDIR)/usr/share/applications/canaima-mod-burg.desktop
	rm -rf $(DESTDIR)/usr/share/gnome/help/canaima-mod-burg/
	
clean:

distclean:

reinstall: uninstall install
