<h1 align='center'>Manage multiple ssh keys</h1>

<div align='center'>
    <img src="./assets/terminal-logo.png" alt="teminal logo" width="200"/>
</div>

<p align="center">SSH (Secure Shell) keys are an access credential that is used in the SSH protocol and they 
are foundational to modern Infrastructure-as-a-Service platforms such as AWS, Google Cloud, and Azure.</p>


**Steps:**

1. Create ssh key using encryption ed25519.
2. Save key inside the .ssh directory.
3. Add a passphrase aka password.
4. Copy key into your server.

## Create ssh key using encryption ed25519

**For this example I will create a ssh key for a Raspberry Pi.**

```bash
ssh-keygen -t ed25519 -C "Raspberry Pi"
```

**Flags:**

**-t**: Specifies the type of encryption.

**-C**: Provides a comment for our ssh key this comment, will be add it at the end of our key.

## Save key inside the .ssh directory

You will be asked where you want to save the key, the path will be **/home/my_user_name/.ssh/raspberrypi_key**, I choose the name **raspberrypi_key** because is easy to identify.

```bash
/home/my_user_name_here/.ssh/raspberrypi_key
```

## Add a passphrase aka password

Secure your key with a passphrase.

You will be ask for this passphrase every time you use the key.

## Copy ssh key into server

```bash
ssh-copy-id -i ~/.ssh/server_key.pub pi@ip_of_the_server
```

## Config File

**Steps:**
1. Create a config file.
2. Add config info.
4. Login using the key.

## Create a config file


```bash
cd .ssh/
touch config
nano config
```

## Add the configuration of your sever

In this file we will add the information neccessary for login to our server.

```bash
Host raspberrypi
    HostName ip_of_the_server
    User pi
    Port 22
    IdentityFile ~/.ssh/raspberrypi_key
```


**Save file.**


**Explanation:**

**Host:** this will be the name you will use to login.  
**HostName:** ip of the server. "In this case the ip of my Raspberry Pi"  
**User:** username on the server.  
**Port:** Port for connection.  
**IdentityFile:** path to the raspberrypi_key.  


You can create multiple keys and manage them using the config file.

## Login using the key

Now is possible to login into the Raspberry pi using the raspberrypi_key.

```bash
ssh raspberrypi
```
## Extras:

**For security reasons is recommended access the server only using ssh keys insted of passwords.**

For this we will modify the **sshd_config** file.

Inside of your server modify the file /etc/ssh/sshd_config

```bash
sudo nano /etc/ssh/sshd_config
```

This file is for the sshd daemon (the program that listens to any incoming connection request to the SSH port) on the host machine.

Change these lines.

```bash
PermitRootLogin yes  
PasswordAuthentication yes
#PubkeyAuthentication yes
#ChallengeResponseAuthentication no
X11Forwarding yes 
AllowTcpForwarding yes
```

For:

```bash
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
ChallengeResponseAuthentication no
X11Forwarding no 
AllowTcpForwarding no 
```

To make this changes work you will need to restart the ssh server or you can simple reboot.

**Restart SSH server**

```bash
sudo service sshd restart
```

**Reboot**

```bash
sudo reboot
```

This is a basic secure configuration, other things you can look for are: change the default ssh port, disable unnecessary services, lock the root user, install packages like fail2ban, and ufw.

<p>If you find this guide useful please give it a star and share!</p>
