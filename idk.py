import os
os.system(sudo apt install && sudo apt upgrade)
os.system(sudo apt install wget)
os.system(wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb)
os.system(sudo apt install ./chrome-remote-desktop_current_amd64.deb)
os.system(wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb)
os.system(sudo apt install ./google-chrome-stable_current_amd64.deb)
os.system(sudo DEBIAN_FRONTEND=noninteractive \
    apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver
 
sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session'
 
 
sudo systemctl disable lightdm.service)
