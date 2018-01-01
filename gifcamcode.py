import picamera
from time import sleep
import time
import RPi.GPIO as GPIO
from os import system
import os
import random, string


# Behaviour Variables

num_frame = 8       # Number of frames in Gif
gif_delay = 15      # Frame delay [ms]
delay = 0.2 #delay time  for mode button in seconds
picoffset = 1.5 # In mode 3: Time between pic 1 and 2


#
# Define GPIO
#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 19 #Button GPIO Pin
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mode = 13 #mode GPIO Pin
GPIO.setup(mode, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#
# Camera
#
camera = picamera.PiCamera()
camera.resolution = (486, 364)
#camera.resolution = (540, 405)
camera.rotation = 180
#camera.brightness = 70
camera.saturation = 0
#camera.color_effects = (128, 128) #to make Black and White

camera.image_effect = 'none'
##GPIO.output(led_2, 1)


def random_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))



def run():
    print "System Ready"

    try:
        state = 1
        print "Mode 1"
        mode1()

    except:
        GPIO.cleanup()


def mode3():
    modeLED3.ChangeDutyCycle(100)
    sleep(delay)
    while True:
        if GPIO.input(button) == False: # BUTTON PRESSED
                # TAKING PICTURES #
                print "Gif Started"

                randomstring = random_generator()
                camera.capture('1.jpg')
                sleep(picoffset)
                camera.capture('2.jpg')

                # PROCESSING GIF #
                print "Processing"
                filename = '/home/pi/gifs/' + randomstring + '-0'

                graphicsmagick = "gm convert -delay " + str(20) + " " + "*.jpg " + filename + ".gif"
                os.system(graphicsmagick)
                os.system("rm ./*.jpg")

                print "Done"
                print "System Ready"

        elif GPIO.input(mode) == False:
            print "load mode 1"
            mode1()

        else :
                sleep(0.05)

def mode2():
    sleep(delay)
    while True:
        if GPIO.input(button) == False: # BUTTON PRESSED
                # TAKING PICTURES #
                print "Gif Started"

                randomstring = random_generator()
                for i in range(num_frame):
                    camera.capture('{0:04d}.jpg'.format(i))

                # PROCESSING GIF #
                for i in range(num_frame - 1):
                    source = str(num_frame - i - 1) + ".jpg"
                    source = source.zfill(8) # pad with zeros
                    dest = str(num_frame + i) + ".jpg"
                    dest = dest.zfill(8) # pad with zeros
                    copyCommand = "cp " + source + " " + dest
                    os.system(copyCommand)

                print "Processing"
                filename = '/home/pi/gifs/' + randomstring + '-0'

                graphicsmagick = "gm convert -delay " + str(gif_delay) + " " + "*.jpg " + filename + ".gif"
                os.system(graphicsmagick)
                os.system("rm ./*.jpg")

                print "Done"
                print "System Ready"

        elif GPIO.input(mode) == False:
            print "load mode 3"
            mode3()

        else :
                sleep(0.05)


def mode1():
    sleep(delay)
    while True:
        if GPIO.input(button) == False: # BUTTON PRESSED
            # TAKING PICTURES #
            print "Gif Started"

            randomstring = random_generator()
            for i in range(num_frame):
                camera.capture('{0:04d}.jpg'.format(i))

            # PROCESSING GIF #
            print "Processing"
            filename = '/home/pi/gifs/' + randomstring + '-0'

            graphicsmagick = "gm convert -delay " + str(gif_delay) + " " + "*.jpg " + filename + ".gif"
            os.system(graphicsmagick)
            os.system("rm ./*.jpg")

            print "Done"
            print "System Ready"

        elif GPIO.input(mode) == False:
            print "load mode 2"
            mode2()

        else :
                sleep(0.05)


run()
