"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        self.start = start
        self.next = start

    def __repr__(self):
        return f"SerialGenerator(start={self.start})"

    def generate(self):
        serial_num = self.next
        self.next += 1
        return serial_num

    def reset(self):
        self.next = self.start


t1 = SerialGenerator(start=100)
