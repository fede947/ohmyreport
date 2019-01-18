INSTALL_PATH = /usr/local/sbin/

install: requirements remove
	sudo cp -rfv ../ohmyreport $(INSTALL_PATH)

remove:
	sudo rm -rfv $(INSTALL_PATH)ohmyreport

requirements:
	pip3 install -r requirements.txt
