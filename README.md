# Python DMX Lighting Controller for Emotion-Driven Ambiance

This project provides a Python-based solution for controlling DMX lighting fixtures, enabling the creation of dynamic, emotion-driven environments. By analyzing text input, the system identifies the dominant emotion and translates it into a corresponding lighting effect. The project is designed to be easily extensible, allowing for the addition of new emotions, lighting fixtures, and effects.

https://github.com/priyanshum17/python-dmx/assets/67699325/1343335a-8039-4444-8b0a-372181553b5f

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Project Architecture](#project-architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [Running the Emotion Analyzer](#running-the-emotion-analyzer)
  - [Running the Test Script](#running-the-test-script)
- [Adding New Emotions and Fixtures](#adding-new-emotions-and-fixtures)
  - [Adding New Emotions](#adding-new-emotions)
  - [Adding New Lighting Fixtures](#adding-new-lighting-fixtures)
- [API Endpoint](#api-endpoint)
- [Contributing](#contributing)
- [License](#license)

## Features

-   **Emotion-driven lighting:** Analyzes text to determine the dominant emotion and triggers a corresponding lighting effect.
-   **Support for multiple DMX fixtures:** Comes with pre-built support for Aputure Infinibars and Epix Flex 20 LED strips.
-   **Extensible design:** Easily add new emotions, lighting fixtures, and effects.
-   **Command-line interface:** Control the lights and test your setup from the command line.
-   **API endpoint:** A simple Flask-based API endpoint to trigger lighting effects from any application.

## How It Works

The system is comprised of two main components: the emotion analyzer and the DMX lighting controller.

1.  **Emotion Analyzer:** The `emotion_analyzer.py` script takes a string of text as input and uses the Gemini API to determine the dominant emotion. It then maps this emotion to a pre-defined lighting effect.

2.  **DMX Lighting Controller:** The `DMX/emotions.py` script receives the emotion from the analyzer and executes the corresponding lighting effect. It uses the `DMXEnttecPro` library to communicate with an Enttec DMX USB Pro controller, which in turn controls the DMX lighting fixtures.

## Project Architecture

The project is structured as follows:

-   `emotion_analyzer.py`: The main script for analyzing text and triggering lighting effects.
-   `DMX/`: This directory contains all the DMX-related code.
    -   `emotions.py`: Defines the lighting effects for each emotion.
    -   `EnttecObject.py`: A base class for DMX fixtures.
    -   `Aputure.py` and `Epix.py`: Classes for the Aputure Infinibars and Epix Flex 20 strips.
    -   `dmxtest.py`: A script for testing the lighting fixtures.
-   `config.toml`: The configuration file for the project.
-   `docs/`: Contains detailed documentation about the project.
-   `CONTRIBUTING.md`: Guidelines for contributing to the project.

## Getting Started

### Prerequisites

-   Python 3
-   An Enttec DMX USB Pro controller
-   Aputure Infinibars and/or Epix Flex 20 LED strips (or other DMX fixtures)

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

1.  Open the `config.toml` file in a text editor.
2.  Under the `[lights]` section, update the DMX addresses for your lighting fixtures.
3.  The `[colors]` section defines a set of preset colors that can be used in your lighting scripts.

## Usage

### Running the Emotion Analyzer

To analyze a piece of text and trigger the corresponding lighting effect, run the following command:

```bash
python emotion_analyzer.py "Your text here" -c <com_port>
```

Replace `<com_port>` with the COM port of your Enttec controller.

### Running the Test Script

The `dmxtest.py` script provides a simple way to test your lighting setup. To run it, open a terminal, navigate to the `DMX` directory, and run the following command:

```bash
python dmxtest.py -m <mode> -c <com_port>
```

-   `<mode>`: The DMX mode for the Infinibars (9-16).
-   `<com_port>`: The COM port that your Enttec controller is connected to (e.g., `3` for COM3).

## Adding New Emotions and Fixtures

### Adding New Emotions

1.  Add the new emotion to the `EMOTION_SCHEMAS` dictionary in `DMX/emotions.py`.
2.  Define the lighting effect for the new emotion.
3.  Add the new emotion to the `AVAILABLE_EMOTIONS` list in `emotion_analyzer.py`.

### Adding New Lighting Fixtures

1.  Create a new Python class that inherits from `EnttecObject`.
2.  Implement the methods necessary to control the new fixture.
3.  Update the `config.toml` file to include the DMX address of the new fixture.

## API Endpoint

This project includes a simple Flask-based API endpoint to trigger lighting effects from any application. To use it, you'll need to install Flask:

```bash
pip install Flask
```

Then, run the `api.py` script:

```bash
python api.py -c <com_port>
```

This will start a web server on port 5000. You can then send a POST request to the `/trigger-emotion` endpoint with a JSON payload containing the text to be analyzed:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "I am so happy!"}' http://localhost:5000/trigger-emotion
```

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
