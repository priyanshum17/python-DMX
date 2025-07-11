# Epix Flex 20

The `Flex20` class, defined in `Epix.py`, provides a high-level API for controlling Epix Flex 20 LED strips. It allows you to control the foreground and background colors, as well as the built-in programs and effects.

## Initialization

To create a `Flex20` object, you need to provide the DMX address of the strip, a `Controller` object, and a logger object:

```python
from DMXEnttecPro import Controller
from Epix import Flex20
import logging

logger = logging.getLogger()
dmx = Controller('COM3')
strip = Flex20(350, dmx, logger)
```

## Methods

The `Flex20` class provides a wide range of methods for controlling the LED strip, including:

*   `OFF()`: Turns the entire strip off.
*   `main_dim(value: int)`: Sets the main dimmer for the entire strip.
*   `fg_red(value: int)`, `fg_green(value: int)`, `fg_blue(value: int)`: Sets the foreground RGB values.
*   `fg_rgb(value: tuple[int, int, int], brightness: int = 255)`: Sets the foreground RGB values and brightness.
*   `fg_strobe(value: int)`: Sets the foreground strobe effect.
*   `bg_red(value: int)`, `bg_green(value: int)`, `bg_blue(value: int)`: Sets the background RGB values.
*   `bg_rgb(value: tuple[int, int, int])`: Sets the background RGB values.
*   `bg_strobe(value: int)`: Sets the background strobe effect.
*   `fg_program(value: int)`, `fg_speed(value: int)`, `fg_offset(value: int)`: Controls the foreground's built-in programs.
*   `bg_program(value: int)`, `bg_speed(value: int)`, `bg_offset(value: int)`: Controls the background's built-in programs.
