# Aputure Infinibar

The `Infinibar` class, defined in `Aputure.py`, provides a high-level API for controlling Aputure Infinibars. It allows you to control the intensity, color temperature, and RGB values of the individual chunks of the Infinibar.

## Initialization

To create an `Infinibar` object, you need to provide the DMX address of the bar, the DMX mode, a `Controller` object, and a logger object:

```python
from DMXEnttecPro import Controller
from Aputure import Infinibar
import logging

logger = logging.getLogger()
dmx = Controller('COM3')
bar = Infinibar(1, 9, dmx, logger)
```

## Methods

The `Infinibar` class provides the following methods for controlling the light:

*   `OFF()`: Turns the entire bar off.
*   `ALMOST_OFF(value: int = 56)`: Sets the intensity of the entire bar to a low value (default is 20%).
*   `ON()`: Turns the entire bar on to full intensity.
*   `set_intensity(chunk: int, value: int)`: Sets the intensity of a specific chunk.
*   `set_cct_temp(chunk: int, value: int)`: Sets the color temperature of a specific chunk.
*   `set_crossfade(chunk: int, value: int)`: Sets the crossfade of a specific chunk.
*   `set_red(chunk: int, value: int)`: Sets the red value of a specific chunk.
*   `set_green(chunk: int, value: int)`: Sets the green value of a specific chunk.
*   `set_blue(chunk: int, value: int)`: Sets the blue value of a specific chunk.
