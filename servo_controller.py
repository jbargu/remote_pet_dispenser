import time
import RPi.GPIO as GPIO

class ServoController():
    FREQUENCY = 100

    # 2ms pulse => full speed forward
    # 1ms pulse => full speed backward
    COUNTER_CLOCKWISE = (0.002 / (1 / FREQUENCY)) * 100
    CLOCKWISE = (0.001 / (1 / FREQUENCY)) * 100

    def __init__(self, signal_pin=14):
        self.signal_pin = signal_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.signal_pin, GPIO.OUT)

    def dispense(self, amount=10):
        p = GPIO.PWM(self.signal_pin, self.FREQUENCY)

        # Start PWM with 0% duty cycle
        p.start(0)

        # Rotate motor for 0.05 sec clockwise
        p.ChangeDutyCycle(self.CLOCKWISE)
        time.sleep(0.05)

        # Cleanup
        p.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    ServoController().dispense()
