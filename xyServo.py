# Program to test servo with 0.96 OLED display
# Run sudo pigpiod before executing servo.py
import time
import board
from piservo import Servo
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C, reset=RESET_PIN)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

 
servo1 = Servo(13) # Create a servo object and set PWM to GPIO 13
servo2 = Servo(18) # Create a servo object and set PWM to GPIO 18

# Init at 0°
text = "Init at 0°"
draw.text((0, 30), text, font=font1, fill=255)
# Display image
oled.image(image)
oled.show()

print('Init at 0°')
servo1.write(0)
time.sleep(0.5)
servo2.write(0)
time.sleep(0.5)

while True:
    angle = float(input('0-180: '))
    
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    text = "Go to " + str(angle) + "°"
    draw.text((0, 30), text, font=font1, fill=255)
    # Display image
    oled.image(image)
    oled.show()
    print(text)
        
    servo2.write(angle)
    time.sleep(0.5)
