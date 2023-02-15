<div align="center">
<h1>Orange Pi 5 NVMe Instructions For Debian and Ubuntu</h1>
</div>

## About

This instructions will help you to make your opi5 boot from an PCIE NVMe instead of a SDCard.

Requirements.

- SDCard
- PCIE NVMe
- Orange Pi 5
- Power Source
- USB "optional"

For this example I choose the Debian server from the official Orange pi website. 


**Steps**

1. Download Image
1. Burn image in to the SDCard
1. Plug NVMe into the Orange Pi 5
1. Write Linux image to SPI Flash+NVMe SSD
1. Empty NVMe
1. Burn Image into the NVMe


## Download Image

<p>Download image: <a href="http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-pi-5.html">Orange Pi images</a></p>


## Burn image in to the SDCard

So far I been using the raspberry pi imager without issues.

<a href="https://www.raspberrypi.com/software/">Raspberry Pi Imager</a>

```bash
sudo apt install rpi-imager
```

Plug the SDCard

## Plug NVMe

**BEFORE YOU PLUG IN THE NVME BE SURE THAT THE ORANGE PI 5 IS OFF AND WITHOUT THE POWER CORD.**

Plug the NVMe at the bottom, I use 1 nylon screw and 3 nylon nuts to keep it secure.

Once the SDCard and the NVMe are plug, turn on the Orange Pi 5

# Write Linux image to SPI Flash+NVMe SSD

```bash
sudo nand-sata-install
```

**Select number 7 Install/Update the bootlader on SPI Flash**


Wait until you see **Done** on the lower left corner.

## Empty NVMe

```bash
sudo dd bs=1M if=/dev/zero of=/dev/nvme0n1 count=2000 status=progress
sudo sync
```

## Burn Image Into NVMe


Now transfer the image that you donwload on step 1 into the Orange Pi.

<p>

To do this you can use a usb, rsync, or add it using <a href="https://filezilla-project.org/">Filezilla</a>.</p>


I choose to do it using a usb.

1. Transfer the image into the usb
1. Plug the usb into the Orange Pi.
1. Mount the partition.
1. Copy image into the  Orange Pi.

**MOUNT PARTITION**

To locate the USB.

```bash
sudo fdisk -l
```

This will give the path to the partion of the usb.

**CREATE A MOUNT POINT**

```bash
sudo mkdir /mnt/USB
```

**MOUNT THE USB**

```bash
sudo mount /dev/sda1 /mnt/USB
```

**COPY IMAGE INTO THE ORANGE PI**

```bash
cp /dev/sd1/your_image_goes_here.img /home/
```


## Copy image into the NVMe

Locate where the image was copy in the last step and copy the image into the NVMe.


```bash
sudo dd bs=1M if=your_image_goes_here of=/dev/nvme0n1 status=progress
sudo sync
sudo shutdown now
```

Once the device is off remove the SDCard and turn it on once again.

If you find this guide useful please give it a star and share.
