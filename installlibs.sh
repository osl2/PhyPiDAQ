#!/bin/bash
#
# script to install libraries PhyPiDAQ depends on
#
# -----------------------------------------------

sudo apt-get install python3-yaml
sudo apt-get install python3-scipy
sudo apt-get install python3-matplotlib
sudo apt-get install python3-pyqt5
sudo apt-get install libatlas-base-dev # needed to build nupmy

sudo pip3 install installlibs/whl/*.whl # python wheels

sudo pip3 install installlibs/tgz/*.tar.gz # python packages 

sudo dpkg -i installlibs/picoscopelibs/*.deb # picoscope 
sudo usermod -a -G tty pi # grant acces to USB for user pi

if ! sudo grep -qF "dtoverlay=w1-gpio" /boot/config.txt;then
	sudo echo "" >> /boot/config.txt
	sudo echo "#PhyPiDAQ:" >> /boot/config.txt
	sudo echo "dtoverlay=w1-gpio" >> /boot/config.txt
fi
