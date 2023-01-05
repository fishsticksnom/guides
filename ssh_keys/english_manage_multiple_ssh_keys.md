<div align='ceter'>
    <img src="./assets/terminal-logo.png" alt="teminal logo" />
</div>

<p>SSH (Secure Shell) keys are an access credential that is used in the SSH protocol and they 
are foundational to modern Infrastructure-as-a-Service platforms such as AWS, Google Cloud, and Azure.</p>

<h2 align='center'>Manage multiple ssh keys.</h2>

<p>**Steps:**</p>

1. Create ssh key using encryption ed25519.
2. Save key inside the .ssh directory.
3. Add a passphrase aka password.
4. Copy key into your server.

<h2>Create ssh key using encryption ed25519</h2>

<p>For this example I will create a ssh key for a Raspberry Pi.</p>

```bash
ssh-keygen -t ed25519 -C "Raspberry Pi"
```
<p>**Flags:**</p>

<p>**-t**: Specifies the type of encryption.</p>
<p>**-C**: Provides a new comment.</p>

<h2>Save key inside the .ssh directory.</h2>

<p>You will be asked where you want to save the key, the path will be **/home/my_user_name/.ssh/raspberrypi_key**, I choose the name raspberrypi_key because is easy to identify.</p>

```bash
/home/my_user_name_here/.ssh/raspberrypi_key
```

<h2>Add a passphrase aka password.</h2>

<p>Add passphrase</p>

<p>You will be ask for this passphrase every time you use the key.</p>

<h2>Copy ssh key into server</h2>

```bash
ssh-copy-id -i ~/.ssh/server_key.pub pi@ip_of_the_server
```

<h2>Config file</h2>

<h2>**Steps:**</h2>
1. Create a config file.
2. Add config info.
3. Use the key
4. Login

<h2>Create a config file.</h2>

```bash
cd .ssh/
touch config
nano config
```

<h2>Add config info </h2>

<p>In this file we will add the information neccessary for login to our Host</p>

```bash
Host raspberrypi
    HostName ip_of_the_server
    User pi
    Port 22
    IdentityFile ~/.ssh/raspberrypi_key
```
<p>Save file.</p>

**Explanation:**

<p>**Host:** this will be the name you will use to login.</p>
<p>**HostName:** ip of the server.</p>
<p>**User:** username on the server.</p>
<p>**Port:** Port for connection.</p>
<p>**IdentityFile:** raspberrypi_key path.</p>

<h2>Login</h2>

<p>Now is possible to login into the Raspberry pi using the raspberrypi_key.</p>

```bash
ssh raspberrypi
```

<p>raspberrypi is the Host save on the config file.</p>

<p>You can create multiple keys and manage them using the config file.</p>

<h2>Extras:</h2>

<p>For security reasons is recommended access the server only using ssh keys insted of passwords.</p>

<p>Inside of your serve modify the file /etc/ssh/sshd_config</p>

```bash
nano /etc/ssh/ssh_config
```

<p>Change this line.</p>

```bash
#PasswordAuthentication yes
```
<p>For:</p>

```bash
#PasswordAuthentication no
```

<p>If you find this guide useful please give it a star and share.</p>
