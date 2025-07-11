# Project Overview

This project is a Python-based DMX lighting control system that uses an Enttec DMX USB Pro controller to communicate with lighting fixtures. It provides a high-level API for controlling Aputure Infinibars and Epix Flex 20 LED strips, making it easy to create complex lighting effects.

## Core Components

*   **`DMXEnttecPro` library:** This library provides the low-level communication with the Enttec controller.
*   **`EnttecObject.py`:** This script defines a base class for DMX fixtures, providing a common interface for setting DMX channel values.
*   **`Aputure.py`:** This script implements the `Infinibar` class, which provides a high-level API for controlling Aputure Infinibars.
*   **`Epix.py`:** This script implements the `Flex20` class, which provides a high-level API for controlling Epix Flex 20 LED strips.
*   **`dmxtest.py`:** This script serves as an example of how to use the library and provides a command-line interface for testing the lights.
*   **`config.toml`:** This file contains the configuration for the lighting setup, including the DMX addresses of the fixtures and a set of preset colors.
