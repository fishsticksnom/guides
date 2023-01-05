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

**-C**: Provides a new comment.

## Save key inside the .ssh directory

You will be asked where you want to save the key, the path will be **/home/my_user_name/.ssh/raspberrypi_key**, I choose the name raspberrypi_key because is easy to identify.

```bash
/home/my_user_name_here/.ssh/raspberrypi_key
```

## Add a passphrase aka password

Add a passphrase.

You will be ask for this passphrase every time you use the key.

## Copy ssh key into server

```bash
ssh-copy-id -i ~/.ssh/server_key.pub pi@ip_of_the_server
```

## Config file

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

## Add config info

In this file we will add the information neccessary for login to our Host.

```bash
Host raspberrypi
    HostName ip_of_the_server
    User pi
    Port 22
    IdentityFile ~/.ssh/raspberrypi_key
```
Save file.

**Explanation:**

**Host:** this will be the name you will use to login.  
**HostName:** ip of the server.  
**User:** username on the server.  
**Port:** Port for connection.  
**IdentityFile:** raspberrypi_key path.  

## Login uisng the key

Now is possible to login into the Raspberry pi using the raspberrypi_key.

```bash
ssh raspberrypi
```

raspberrypi is the Host save on the config file.

You can create multiple keys and manage them using the config file.

## Extras:

For security reasons is recommended access the server only using ssh keys insted of passwords.

Inside of your server modify the file /etc/ssh/sshd_config

```bash
nano /etc/ssh/sshd_config
```
This file is for the sshd daemon (the program that listens to any incoming connection request to the SSH port) on the host machine.

Change this line.

```bash
#PasswordAuthentication yes
```
For:

```bash
PasswordAuthentication no
```
Reboot and login again.

<p>If you find this guide useful please give it a star and share.</p>
