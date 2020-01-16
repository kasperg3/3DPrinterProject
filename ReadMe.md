
__Setup PlatformIO and build marlin__
In platformio.ini from marlin, edit the board type to you specific type(Ender3 uses sanguino_atmega1284p)

__Using platform specific marlin code__
Copy the examples into the root folder of marlin to get the right build type.

__Using an UsbAsp to flash firmware__
```
sudo avrdude -p atmega1284p -C /etc/avrdude.conf  -c usbasp –v -U flash:w:firmware.hex:i
```


__Resources used for this process:__
https://johnwyles.github.io/posts/flashing-the-creality-ender-3-with-a-raspberry-pi/
https://www.fission3d.com/guides/flash-bootloader-and-install-firmware-with-raspberry-pi
