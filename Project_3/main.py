# import the wifi interface
from wireless import wifi
# the wifi module needs a networking driver to be loaded
# in order to control the board hardware.
# THIS EXAMPLE IS SET TO WORK WITH SPWF01SA WIFI DRIVER
from stm.spwf01sa import spwf01sa as wifi_driver
# Import the Zerynth APP library
from zerynthapp import zerynthapp

# import MAX7219 library to handle 8x8 led matrix
from maxim.max7219 import max7219
# import fonts file where matrix numbers are defined
import fonts

import streams
# Create a serial console
streams.serial()

# Setup Led Matrix (8x8 Click on slot A of a Flip n Click device)
display = max7219.MAX7219(SPI0, D17)

# counter variable
num = 0

# Function to shutdown the display attached
display.shutdown(False)

# Sets the intensity of the LEDs output (values 0 to 15)
intensity = 9
display.set_intensity(intensity)

sleep(1000)
print("STARTING...")

try:
   # Wifi 4 Click on slot B (specify which serial port will be used and which RST pin)
    wifi_driver.init(SERIAL2,D24, baud=9600) 
except Exception as e:
    print(e)
    
for i in range(0,5):
    try:
        # connect to the wifi network (Set your SSID and password below)
        wifi.link("SSID",wifi.WIFI_WPA2,"PASSWORD")
        break
    except Exception as e:
        print("Can't link",e)
else:
    print("Impossible to link!")
    while True:
        sleep(1000)

try:
    # Device UID and TOKEN can be created in the ADM panel
    zapp = zerynthapp.ZerynthApp("DEVICE UID", "DEVICE TOKEN", log=True)
except Exception as e:
    print(e)

# Start the Zerynth app instance!
# Remember to create a template with the files under the "template" folder you just cloned
# upload it to the ADM and associate it with the connected device
zapp.run()


def set_led(num):
    print("Display Number:", num)
    # print the maxi number on led matrix
    for row in range(8):
        for col in range(8):
            if fonts.numbers[num][row][col]:
                display.set_led(row, col, 1)  # Allows the control of a single LED(row (values 0 to 7), column (values 0 to 7),1 for Led ON and 0 for Led OFF)
            else:
                display.set_led(row, col, 0)
    
# link "set_led" to the function set_led
zapp.on("set_led", set_led)    



while True:
    print("......")
    sleep(2000)
        