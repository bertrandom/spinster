#!/usr/bin/env python
import mpd
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)

albums = {
    '128 208 248 247 52'    : ['Vampire Weekend', 'Vampire Weekend'],
    '128 208 4 44 154'      : ['A Tribe Called Quest', 'The Anthology'],
    '128 208 248 94 105'    : ['Broken Bells', 'Broken Bells'],
    '128 208 4 122 228'     : ['XX', 'XX'],
    '128 208 248 213 88'    : ['Beastie Boys', 'Hello Nasty'],
    '148 0 117 188 176'     : ['Cut Copy', 'In Ghost Colours'],
    '148 0 117 148 118'     : ['Lily Allen', 'Alright, Still'],
    '148 0 117 196 148'     : ['Liz Phair', 'Whip Smart'],
    '148 0 117 28 78'       : ['Beatles', 'Let It Be'],
    '148 0 117 220 176'     : ['Modest Mouse', 'Building Nothing'],
    '148 0 117 248 148'     : ['Beastie Boys', 'Ill Communication'],
    '148 0 181 79 106'      : ['Liz Phair', 'Exile in Guyville'],
    '128 208 248 49 231'    : ['Nightmares on Wax', 'Carboot Soul'],
    '36 0 7 145 186'        : ['Jonathan Richman', 'You Must Ask the Heart'],
    '148 0 117 242 157'     : ['Beck', 'Guero'],
    '128 208 4 6 193'       : ['M. Ward', 'Transfiguration of Vincent'],
    '128 208 248 113 113'   : ['Belle and Sebastian', 'Tigermilk'],
    '128 208 248 167 208'   : ['Pixies', 'Bossanova'],
    '128 208 248 97 237'    : ['Pixies', 'Doolittle'],
    '128 208 248 169 225'   : ['Sublime', 'Sublime'],
    '128 208 248 1 153'     : ['Presidents of the United States of America', 'Presidents of the United States of America'],
    '128 208 4 108 0'       : ['She & Him', 'Volume One'],
    '128 208 4 196 115'     : ['Frank Black', 'Teenager of the Year'],
    '128 208 248 129 107'   : ['Ween', 'Chocolate & Cheese'],
    '128 208 4 88 99'       : ['Jurassic 5', 'Power in Numbers'],
    '128 208 4 250 93'      : ['Radiohead', 'Kid A'],
    '128 208 248 23 221'    : ['David Bowie', 'Hunky Dory'],
    '148 0 181 215 155'     : ['Vetiver', 'Vetiver'],
    '128 208 4 248 211'     : ['Cut Copy', 'Bright Like Neon Love'],
    '128 208 248 67 95'     : ['Supreme Beings of Leisure', 'Supreme Beings of Leisure'],
}

last_code = ''

while True:
    line = ser.readline()
    code = line.strip().lstrip('>').replace('T:NACK ', '')
    if code != '' and code != last_code:
        if code in albums:

            print "Playing " + albums[code][0] + ' - ' + albums[code][1]

            client = mpd.MPDClient()
            client.timeout = 10
            client.idletimeout = None
            client.connect("localhost", 6600)
            client.clear()
            client.searchadd("artist", albums[code][0], "album", albums[code][1])
            client.play()
            client.close()
            client.disconnect()

            last_code = code

    time.sleep(0.1)


