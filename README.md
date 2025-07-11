# Python DMX Lighting Controller

This project provides a Python-based solution for controlling DMX lighting fixtures, specifically tested with Aputure Infinibars and Epix Flex 20 LED strips, using an Enttec DMX USB Pro controller.

## How It Works

The system is built around the `DMXEnttecPro` library, which provides the low-level communication with the Enttec controller. The `EnttecObject.py` script defines a base class for DMX fixtures, and `Aputure.py` and `Epix.py` implement specific classes for the Infinibars and Flex 20 strips, respectively. These classes provide a high-level API for controlling the lights, abstracting away the underlying DMX channel manipulation.

The `dmxtest.py` script serves as an example of how to use the library and provides a command-line interface for testing the lights. It reads a `config.toml` file to determine the DMX addresses of the lighting fixtures.

## Getting Started

### Prerequisites

*   Python 3
*   An Enttec DMX USB Pro controller
*   Aputure Infinibars and/or Epix Flex 20 LED strips (or other DMX fixtures, with some code modification)

### Installation

1.  Clone this repository:
    ```bash
    git clone https://github.com/priyanshum17/python-dmx.git
    ```
2.  Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```
3.  Connect your Enttec DMX USB Pro controller to your computer.
4.  Connect your DMX lighting fixtures to the controller.

### Configuration

1.  Open the `DMX/config.toml` file in a text editor.
2.  Under the `[lights]` section, update the DMX addresses for your lighting fixtures. The `BARS` array should contain the starting DMX addresses for your Infinibars, and the `STRIPS` array should contain the starting DMX addresses for your Flex 20 strips.
3.  The `[colors]` section defines a set of preset colors that can be used in your lighting scripts. You can add or modify these as needed.

### Running the Test Script

The `dmxtest.py` script provides a simple way to test your lighting setup. To run it, open a terminal, navigate to the `DMX` directory, and run the following command:

```bash
python dmxtest.py -m <mode> -c <com_port>
```

*   `<mode>`: The DMX mode for the Infinibars (9-16).
*   `<com_port>`: The COM port that your Enttec controller is connected to (e.g., `3` for COM3).

For more detailed information about the available command-line arguments, run:

```bash
python dmxtest.py -h
```

## Documentation

For more detailed documentation on the project, including the API for the `Infinibar` and `Flex20` classes, please see the documents in the `docs` directory.