# Makefile

SHELL := sh -e

all: test build

test:
	@echo " Hecho!"

build:	gen-img
	@echo "Nada para compilar!"

gen-img: clean-img

	@printf "Generando imágenes desde las fuentes [SVG > PNG,JPG] ["
	@for IMAGE in $(IMAGES); do \
		$(CONVERT) -background None img/$${IMAGE}.svg img/$${IMAGE}.png; \
		printf "."; \
	done;
	@printf "]\n"

clean-img:

	@printf "Cleaning generated images [JPG,PNG] ["
	@for IMAGE in $(IMAGES); do \
		rm -rf img/$${IMAGE}.png; \
		printf "."; \
	done
	@printf "]\n"

clean-pyc:

	@printf "Cleaning precompilated python files ["
	@for PYC in $(PYCS); do \
		rm -rf $${PYC}; \
		printf "."; \
	done
	@printf "]\n"

install:
	mkdir -p $(DESTDIR)/usr/share/canaima-mod-burg/
	mkdir -p $(DESTDIR)/usr/share/canaima-mod-burg/img/
	mkdir -p $(DESTDIR)/usr/share/applications/
	mkdir -p $(DESTDIR)/usr/bin/
	mkdir -p $(DESTDIR)/usr/share/pixmaps/
	mkdir -p $(DESTDIR)/usr/share/gnome/help/
	
	cp -r img/monitor.png $(DESTDIR)/usr/share/canaima-mod-burg/img/
	cp -r img/canaima-burg-icon.png $(DESTDIR)/usr/share/pixmaps/	
	cp -r desktop/canaima-mod-burg.desktop $(DESTDIR)/usr/share/applications/
	cp -r scripts  $(DESTDIR)/usr/share/canaima-mod-burg/
	chmod +x $(DESTDIR)/usr/share/canaima-mod-burg/scripts/canaima-mod-burg.py
	cp -r ayuda/canaima-mod-burg $(DESTDIR)/usr/share/gnome/help/
	ln -s /usr/share/canaima-mod-burg/scripts/canaima-mod-burg.py $(DESTDIR)/usr/bin/canaima-mod-burg

uninstall:
	rm -rf $(DESTDIR)/usr/share/canaima-mod-burg/
	rm -rf $(DESTDIR)/usr/share/pixmaps/canaima-burg-icon.png
	rm -rf $(DESTDIR)/usr/share/applications/canaima-mod-burg.desktop
	rm -rf $(DESTDIR)/usr/share/gnome/help/canaima-mod-burg/
	
clean:

distclean:

reinstall: uninstall install
