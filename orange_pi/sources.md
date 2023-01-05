<h1 align="center">Change repositories from China</h1>

<p align="center">This is only required if you use the iso from the OrangePi website</p>

```bash
nano etc/apt/sources.list
```

Remove all the repositories from China and add the officials insted.

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
