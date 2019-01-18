INSTALL_PATH = /usr/local/sbin/

install: requirements remove
	mkdir $(INSTALL_PATH)ohmyreportLib
	cp -rf * $(INSTALL_PATH)ohmyreportLib
	touch $(INSTALL_PATH)ohmyreport
	echo 'python3 $(INSTALL_PATH)ohmyreportLib/ohmyreport $\$$@' > $(INSTALL_PATH)ohmyreport
	chmod +x $(INSTALL_PATH)/ohmyreportLib/ohmyreport
	chmod +x $(INSTALL_PATH)ohmyreport

remove:
	sudo rm -fv $(INSTALL_PATH)ohmyreport
	sudo rm -rf $(INSTALL_PATH)ohmyreportLib

requirements:
	pip3 install -r requirements.txt
