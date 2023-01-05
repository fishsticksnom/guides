<h1 align="center">Orange Pi Zero 2 with Official Image</h1>

<h2>About</h2>

<p>This guide will help you to install the official image for your Orange Pi Zero 2, I guess it can be use for other models.</p>


### Requirements:
- Orange Pi Zero 2.   
- Power Source.  
- SDCard. Class 1(A1) or Class 2(A2)  
- Ethernet Cable.  
- Router Access.  

**Steps:**
1. Download Image from the official Orange Pi website.  
2. Download the Raspberry Pi imager.  
3. Add the Orange Pi image into the SDCard.  
4. Connect to the OrangePi using the ethernet connection and login using SSH.  
5. Change password.  
6. Change sources for downloading packages.  
7. Update and Upgrade..  
8. Activate Wifi.  
9. Delete oranpi user
<h2>Download the image from the website.</h2>

<p>Go to the official <a href="http://www.orangepi.org/html/serviceAndSupport/index.html" target='_blank'></a>Orange Pi website, select your board.</p>

<p>Select a distro, for this guide I will pick Debian, but feel free to select any other.</p>

**All the distros are save in google drive**
<p>Pick a version, at this time I will download Orangepizero2_3.0.6_debian_bullseye_server_linux5.16.17, this version is the headless version. This will not have a desktop enviorment, if you like to use one with it, choose the xfce or the desktop version.</p>

<h2>Download Raspberry Pi Imager</h2>

<p>You can install this software using the terminal or downloading the app from the <a href="https://www.raspberrypi.com/software/">website</a>.</p>

**Terminal:**

```bash
sudo apt install rpi-imager
```

<h2>Format SDCard and Add the Orange Pi image into the SDCard</h2>
**Format SDCard**

<img src="./assets/format.png" alt="format SDCard">

1. Open Raspberry Pi Imager.
2. Plug the SDCard.
3. Choose OS.
4. Select Erase.
5. Choose Storage and select your SDCard.
6. Select Write and Confirm.
7. Close app and open it again.

**Add Image in to the SDCard**
<img src="./assets/write_image.png" alt="write OrangePi image">
1. Select Choose OS.
2. Select Use custom.
3. Select the OrangePi Image.
4. Select Choose storage and select your SDCard.
5. Select Write.
6. Eject the SDCard safely.

**If for some reason you have problems writing the image try to open the app with sudo.**

```bash
sudo rpi-imager
```

<h2>Connect to the OrangePi using the ethernet connection and login using SSH.</h2>
<p>Plug the SDCard into the Orange Pi, the ethernet cable, and for last the power source.</p>
**The first boot takes time so be patient.**

**Find the ip of the Orange Pi.**

<p>You can do this using the terminal.</p>

```bash
sudo apt install arp-scan
sudo arp-scan --localnet
```

<p>Or you can login into your router and look for it.</p>
<p>Login using root and password:</p>
user:root
password: orangepi

```bash
ssh root@paste_the_ip_from_the_opi_here
```

<h2>Change password</h2>

<p>Add a new password.</p>
```bash
passwd
```

<h2>Change sources for downloading packages.</h2>

<p>Change the source of the packages for downlaods, insted of using the repo from China we will use the official repo.</p>

```bash
nano /etc/apt/sources.list
```
**Delete the default repos and add this ones instead**

```bash
deb http://deb.debian.org/debian bullseye main contrib non-free
#deb-src http://deb.debian.org/debian bullseye main contrib non-free

deb http://deb.debian.org/debian bullseye-updates main contrib non-free
#deb-src http://deb.debian.org/debian bullseye-updates main contrib non-free

deb http://deb.debian.org/debian bullseye-backports main contrib non-free
#deb-src http://deb.debian.org/debian bullseye-backports main contrib non-free

deb http://security.debian.org/ bullseye-security main contrib non-free
#deb-src http://security.debian.org/ bullseye-security main contrib non-free
```
<p>Save the file.</p>
<p>Reboot.</p>

```bash
reboot
```
<p>Login using SSH using your new password.</p>

<h2>Update and Upgrade.</h2>

```bash
apt update
apt upgrade
```

<h2>Activate Wifi.</h2>
```bash
orangepi-config
```


<p>To activate the wifi, turn off the bluetooth, make a wifi access point, install IR support</p>

<h2>Delete orange pi user</h2>

<p>By default a orangepi user is created, to delete the this user use:</p>

```bash
deluser --remove-all-files orange pi
```

**Extras:**
<p>Turn system off.</p>

```bash
shutdown now
```
<p>Reboot</p>

```bash
reboot
```
<p>Search for a package.</p>

```bash
apt search neofetch
```

<p>Install packages.</p>

```bash
apt install neofetch
```
<p>Delete packages.</p>

```bash
apt purge neofetch
```
<p>Check process.</p>

```bash
htop
```
<p>Add a new user.</p>

```bash
useradd name_of_the_user_here
```
<p>If you find this guide useful please give it a star and share.</p>
