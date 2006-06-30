#	Makefile de Xtrasgu Temperatura
#	¡Los espacios son tabuladores!

# Edited for Debian GNU/Linux.
DESTDIR =

install:
	mkdir -m 755 -p $(DESTDIR)/usr/lib/xatar
	cp XATAR_Factory.server $(DESTDIR)/usr/lib/bonobo/servers
	cp xatar.py $(DESTDIR)/usr/lib/xatar
	cp xatar.xml $(DESTDIR)/usr/lib/xatar
	cp xatar.png $(DESTDIR)/usr/share/pixmaps
	chmod 644 $(DESTDIR)/usr/lib/bonobo/servers/XATAR_Factory.server
	chmod 755 $(DESTDIR)/usr/lib/xatar/xatar.py
	chmod 644 $(DESTDIR)/usr/lib/xatar/xatar.xml
	chmod 644 $(DESTDIR)/usr/share/pixmaps/xatar.png

uninstall:
	rm $(DESTDIR)/usr/lib/bonobo/servers/XATAR_Factory.server
	rm $(DESTDIR)/usr/lib/xatar/xatar.py
	rm $(DESTDIR)/usr/lib/xatar/xatar.xml
	rm $(DESTDIR)/usr/share/pixmaps/xatar.png
	rmdir $(DESTDIR)/usr/lib/xatar

clean:
	rm *~
