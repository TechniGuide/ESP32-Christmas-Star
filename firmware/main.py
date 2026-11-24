from machine import Pin, deepsleep
from time import sleep_ms

LED_PIN = 10

# Initialize GPIO and release any previous pin hold
led = Pin(LED_PIN, Pin.OUT, value=0, hold=False)

# Blink the LED for 3 seconds
for _ in range(3):
    led.on()
    sleep_ms(500)

    led.off()
    sleep_ms(500)

# Ensure the LED is turned off
led.off()

# Retain the LOW state during Deep Sleep
led.init(Pin.OUT, value=0, hold=True)

# Enter Deep Sleep for 3 seconds
deepsleep(3000)
