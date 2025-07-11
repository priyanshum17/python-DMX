from DMXEnttecPro import Controller
from EnttecObject import EnttecObject
import logging

MODE_CHUNKS = {
    9: 4,
    10: 6,
    11: 8,
    12: 12,
    13: 16,
    14: 24,
    15: 32,
    16: 48
}

class Infinibar(EnttecObject):
    def __init__(self, address: int, mode: int, controller: Controller, logger: logging.Logger):
        super().__init__(address, controller, logger, min_channel=0, max_channel=7*MODE_CHUNKS[mode])
        self.mode = mode
        self.mode_type = 'CCTRGB' if self.mode < 16 else 'HSI'
        if self.mode >= 9 and self.mode <= 16:
            self._init_chunks(MODE_CHUNKS[self.mode])
        self.logger.debug(self.mode_type)
                
    def _init_chunks(self, chunkCount: int):
        """
        Create pixel chunk indicies for the infinibar. Modes 9-16
        separate the bar into a series of "chunks" that each have equivalent
        channel operations across 7 channels

        :param chunkCount: The number of chunks that needs indexing, should be between 4-48
        :type chunkCount: int
        """
        self.chunks = [7*i for i in range(chunkCount)]
        self.logger.debug(self.chunks)
    
    def OFF(self):
        """
        Metafunction to turn the entire bar off

        Equivalent to set_intensity(chunk, 0) for all chunks
        """
        self.logger.debug("Off")
        for c in range(len(self.chunks)):
            self.set_intensity(c, 0)
    
    def ALMOST_OFF(self, value: int = 56):
        """
        Metafunction to turn the bar _almost_ off, by default 20% brightness

        :param value: 0-225 value to set the brightness to, defaults to 56
        :type value: int
        """
        self.logger.debug("20% on")
        for c in range(len(self.chunks)):
            self.set_intensity(c, value)
    
    def ON(self):
        """
        Meta-function to turn the bar completely on

        Equivalent to set_intensity(chunk, 255) for all chunks
        """
        self.logger.debug("On")
        for c in range(len(self.chunks)):
            self.set_intensity(c, 255)
    
    def set_intensity(self, chunk: int, value: int):
        """
        Sets the intensity/brightness of a given chunk

        Equivalent to adjusting the 1st channel for each chunk

        :param chunk: Index of chunk. *Note:* This is an index, not address value
        :type chunk: int

        :param value: 0-255, sets the intensity of the chunk from 0-100%
        :type value: int
        """
        address = self.chunks[chunk]
        self.set_channel(address, value)
    
    def set_cct_temp(self, chunk: int, value: int):
        """
        Sets the color temperature value of a given chunk

        Equivalent to adjusting the 3rd channel for each chunk

        :param chunk: Index of chunk. *Note:* This is an index, not address value
        :type chunk: int

        :param value: 0-255, sets the color temperature of the chunk from 2000K - 10000K as a percentage
        :type value: int
        """
        address = self.chunks[chunk] + 2
        self.set_channel(address, value)
    
    def set_crossfade(self, chunk: int, value: int):
        """
        Sets the crossfade of a given chunk

        Equivalent to adjusting the 4th channel for each chunk

        :param chunk: Index of chunk. *Note:* This is an index, not address value
        :type chunk: int

        :param value: 0-255, sets the crossfade percentage of the chunk from 0-100%
        :type value: int
        """
        address = self.chunks[chunk] + 3
        self.set_channel(address, value)

    def set_red(self, chunk: int, value: int):
        """
        Sets the red value of a given chunk

        Equivalent to adjusting the 5th channel for each chunk

        :param chunk: Index of chunk. *Note:* This is an index, not address value
        :type chunk: int

        :param value: 0-255, sets the red channel of the chunk from 0-100%
        :type value: int
        """
        address = self.chunks[chunk] + 4
        self.set_channel(address, value)
    
    def set_green(self, chunk: int, value: int):
        """
        Sets the green value of a given chunk

        Equivalent to adjusting the 6th channel for each chunk

        :param chunk: Index of chunk. *Note:* This is an index, not address value
        :type chunk: int

        :param value: 0-255, sets the green channel of the chunk from 0-100%
        :type value: int
        """
        address = self.chunks[chunk] + 5
        self.set_channel(address, value)

    def set_blue(self, chunk: int, value: int):
        """
        Sets the blue value of a given chunk

        Equivalent to adjusting the 7th channel for each chunk

        :param chunk: Index of chunk. *Note:* This is an index, not address value
        :type chunk: int

        :param value: 0-255, sets the blue channel of the chunk from 0-100%
        :type value: int
        """
        address = self.chunks[chunk] + 6
        self.set_channel(address, value)
    