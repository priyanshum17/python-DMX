from DMXEnttecPro import Controller
from EnttecObject import EnttecObject
import logging, typing

class Flex20(EnttecObject):
    def __init__(self, address: int, controller: Controller, logger: logging.Logger):
        super().__init__(address, controller, logger, min_channel=0, max_channel=15)

    def OFF(self):
        """
        Meta function to turn everything off
        """
        self.main_dim(0)

    def main_dim(self, value: int):
        """
        Set the main dimmer value

        Equivalent to channel 1 of the LED strip

        :param value: 0-255, sets brightness from 0-100%
        :type value: int
        """
        addr = 0
        self.set_channel(addr, value)
    
    def fg_red(self, value: int):
        """
        Set the Foreground Red value

        Equivalent to channel 2 of the LED strip
        
        :param value: 0-255, sets red channel from 0-100%
        :type value: int
        """
        addr = 1
        self.set_channel(addr, value)
    
    def fg_green(self, value: int):
        """
        Set the Foreground Green value

        Equivalent to channel 3 of the LED strip
        
        :param value: 0-255, sets green channel from 0-100%
        :type value: int
        """
        addr = 2
        self.set_channel(addr, value)
    
    def fg_blue(self, value: int):
        """
        Set the Foreground Blue value

        Equivalent to channel 4 of the LED strip
        
        :param value: 0-255, sets blue channel from 0-100%
        :type value: int
        """
        addr = 3
        self.set_channel(addr, value)
    
    def fg_rgb(self, value: typing.Tuple[int,int,int], brightness: int=255):
        """
        Set the foreground RGB channels all at once

        :param value: RGB values
        :type value: Tuple[int,int,int]
        """
        r,g,b = value
        self.main_dim(brightness)
        self.fg_red(r)
        self.fg_green(g)
        self.fg_blue(b)
    
    def fg_strobe(self, value: int):
        """
        Set the foreground strobe value

        0-10: no function
        11-50: Strobe, slow to fast
        51-90: Random strobe, slow to fast
        91-140: Synchronized random strobe, slow to fast
        141-255: Reserved for future use

        Equivalent to channel 5 of the LED strip

        :param value: 0-255, sets strobe function/speed
        :type value: int
        """
        if value > 140:
            self.logger.debug("Value too high, %d is reserved for future use" % value)
            value = 0
        addr = 4
        self.set_channel(addr, value)

    def bg_red(self, value: int):
        """
        Set the Background Red value

        Equivalent to channel 6 of the LED strip

        :param value: 0-255, sets red channel from 0-100%
        :type value: int
        """
        addr = 5
        self.set_channel(addr, value)
    
    def bg_green(self, value: int):
        """
        Set the Background Green value

        Equivalent to channel 7 of the LED strip

        :param value: 0-255, sets green channel from 0-100%
        :type value: int
        """
        addr = 6
        self.set_channel(addr, value)
    
    def bg_blue(self, value: int):
        """
        Set the Background Blue value

        Equivalent to channel 8 of the LED strip

        :param value: 0-255, sets blue channel from 0-100%
        :type value: int
        """
        addr = 7
        self.set_channel(addr, value)
    
    def bg_rgb(self, value: typing.Tuple[int,int,int]):
        """
        Set the background RGB channels all at once

        :param value: RGB values
        :type value: Tuple[int,int,int]
        """
        r,g,b = value
        self.bg_red(r)
        self.bg_green(g)
        self.bg_blue(b)
    
    def bg_strobe(self, value: int):
        """
        Set the Background strobe value

        0-10: no function
        11-50: Strobe, slow to fast
        51-90: Random strobe, slow to fast
        91-140: Synchronized random strobe, slow to fast
        141-255: Reserved for future use

        Equivalent to channel 9 of the LED strip

        :param value: 0-255, sets strobe function/speed
        :type value: int
        """
        if value > 140:
            self.logger.warning("Value %d is too high for this function, resetting to 0" % value)
            value = 0
        addr = 8
        self.set_channel(addr, value)
    
    def fg_program(self, value: int):
        """
        Set the foreground program

        000: No function
        1-20: Auto 0
        21-40: Auto 1
        41-60: Auto 2
        61-65: Auto 3
        66-80: Multicolor
        81-100: Color fade 1
        101-120: Color fade 2
        121-140: Color fade 3
        141-255: Reserved for future use

        Equivalent to channel 10 of the LED strip

        :param value: 0-255, sets program operation
        :type value: int
        """
        if value > 140:
            self.logger.debug("Value too high, %d is reserved for future use" % value)
            value = 0
        addr = 9
        self.set_channel(addr, value)
    
    def fg_speed(self, value: int):
        """
        Set the foreground program speed, slow to fast

        Equivalent to channel 11 of the LED strip

        :param value: 0-255, sets program speed from 0-100%
        :type value: int
        """
        addr = 10
        self.set_channel(addr, value)
    
    def fg_offset(self, value: int):
        """
        Set the foreground program offset delay, short to long

        Equivalent to channel 12 of the LED strip

        :param value: 0-255, sets program offset delay from 0-100%
        :type value: int
        """
        addr = 11
        self.set_channel(addr, value)
    
    def bg_program(self, value: int):
        """
        Set the background program

        000: No function
        1-20: Auto 0
        21-40: Auto 1
        41-60: Auto 2
        61-65: Auto 3
        66-80: Multicolor
        81-100: Color fade 1
        101-120: Color fade 2
        121-140: Color fade 3
        141-255: Reserved for future use

        Equivalent to channel 13 of the LED strip

        :param value: 0-255, sets program operation
        :type value: int
        """
        if value > 140:
            self.logger.debug("Value too high, %d is reserved for future use" % value)
            value = 0
        addr = 12
        self.set_channel(addr, value)
    
    def bg_speed(self, value: int):
        """
        Set the background program speed, slow to fast

        Equivalent to channel 14 of the LED strip

        :param value: 0-255, sets program speed from 0-100%
        :type value: int
        """
        addr = 13
        self.set_channel(addr, value)
    
    def bg_offset(self, value: int):
        """
        Set the background program offset delay, short to long

        Equivalent to channel 15 of the LED strip

        :param value: 0-255, sets program offset delay from 0-100%
        :type value: int
        """
        addr = 14
        self.set_channel(addr, value)
