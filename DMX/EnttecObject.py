from DMXEnttecPro import Controller
import logging

class EnttecObject(object):
    def __init__(self, address: int, controller: Controller, logger: logging.Logger, min_channel=0, max_channel=511):
        self.address = address
        self.controller = controller
        self.logger = logger
        self.min_address = self.address + min_channel
        self.max_address = self.address + max_channel
    
    def set_channel(self, channel: int, value: int):
        """
        Set's the DMX value of the channel to a specified value

        :param channel: The DMX channel to set
        :type channel: int

        :param value: The value, between 0 and 255 to set
        :type value: int
        """
        # Guard against improper values (outside of 0-255)
        if value > 255:
            self.logger.debug("Value of %d is too high, resetting to 255" % value)
            value = 255
        elif value < 0:
            self.logger.debug("Value of %d is too low, resetting to 0" % value)
        
        # Guard against out of bounds channels
        address = self.address + channel
        if address < self.min_address:
            raise(ValueError("Channel too low: Channel %d maps to address %d which is out of bounds for this object." % (channel, address)))
        elif address > self.max_address:
            raise(ValueError("Channel too high: Channel %d maps to address %d which is out of bounds for this object." % (channel, address)))
        
        # Send to the DMX controller
        self.controller.set_channel(address, value)

    def submit(self):
        """
        Wrapper to submit values if auto_submit is not True
        """
        self.controller.submit()
        