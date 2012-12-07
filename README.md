# spinster

This is the script for my [RFID Record Player](http://thatsaspicymeatball.com/post/3567097734/rfid-record-player) that tells my stereo to play music when an RFID record is placed on the reader. 

The Redbee RFID reader uses XBee to wirelessly send the signal to the USB dongle plugged into my server. I'm running Ubuntu 12.04 LTS which has `ftdi_usb` drivers already built in, so the dongle shows up as `/dev/ttyUSB0`. The script treats that as a serial port. From the manual:

> The RedBee™ RFID reader comes configured to communicate at 9600 baud, No parity, One Stop bit, and No Flow Control.

After it receives the tag, it looks it up against the hash for the corresponding album and then tells mpd to clear the current playlist, search for the album and add it as the current playlist, and play. It also keeps tabs on what the last album played was so it doesn't constantly restart the album (as long as the tag is on the RFID reader, it will continually transmit the tag over and over again). The searchadd command is only available in mpd 0.17 so you may have to compile the newest mpd from source:

	bzip2 -d mpd-0.17.2.tar.bz2 
	cd mpd-0.17.2
	apt-get install libasound2-dev libmad0-dev libid3tag0-dev libflac-dev libflac++-dev
	apt-get install libglib2.0-dev
	./configure
	make
	make install

and then make `/etc/init.d/mpd` point to `/usr/local/bin/mpd` instead of `/usr/bin/mpd`.