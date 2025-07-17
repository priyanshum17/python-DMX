# Contributing to the Python DMX Lighting Controller

First off, thank you for considering contributing to this project! Your help is greatly appreciated.

This document provides guidelines for contributing to the project. Please read it carefully to ensure a smooth and effective contribution process.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Style Guides](#style-guides)
  - [Git Commit Messages](#git-commit-messages)
  - [Python Style Guide](#python-style-guide)
- [Project Architecture](#project-architecture)
  - [Core Components](#core-components)
  - [Adding New Lighting Fixtures](#adding-new-lighting-fixtures)
  - [Adding New Emotions](#adding-new-emotions)
- [Setting Up Your Development Environment](#setting-up-your-development-environment)
- [Running Tests](#running-tests)

## Code of Conduct

This project and everyone participating in it is governed by the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

If you find a bug, please open an issue on GitHub. When you report a bug, please include the following:

-   A clear and descriptive title.
-   A detailed description of the problem, including steps to reproduce it.
-   The expected behavior and what actually happened.
-   Your operating system, Python version, and any other relevant information about your environment.
-   If possible, include a traceback or error message.

### Suggesting Enhancements

If you have an idea for an enhancement, please open an issue on GitHub. When you suggest an enhancement, please include the following:

-   A clear and descriptive title.
-   A detailed description of the proposed enhancement and why it would be beneficial.
-   Any alternative solutions or features you've considered.

### Pull Requests

We welcome pull requests! If you'd like to contribute code, please follow these steps:

1.  Fork the repository and create your branch from `main`.
2.  Make your changes, ensuring you adhere to the style guides.
3.  Add or update tests for your changes.
4.  Ensure all tests pass.
5.  Update the documentation if your changes require it.
6.  Open a pull request with a clear and descriptive title and a detailed description of your changes.

## Style Guides

### Git Commit Messages

-   Use the present tense ("Add feature" not "Added feature").
-   Use the imperative mood ("Move file to..." not "Moves file to...").
--   Limit the first line to 72 characters or less.
-   Reference issues and pull requests liberally after the first line.

### Python Style Guide

-   Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
-   Use a linter like `flake8` or `pylint` to check your code for style issues.

## Project Architecture

The project is designed to be modular and extensible. Here's a brief overview of the architecture:

### Core Components

-   `DMX/EnttecObject.py`: This is the base class for all DMX fixtures. It handles the low-level communication with the Enttec DMX USB Pro controller.
-   `DMX/Aputure.py` and `DMX/Epix.py`: These files contain the classes for the Aputure Infinibars and Epix Flex 20 strips, respectively. They inherit from `EnttecObject` and provide a high-level API for controlling the lights.
-   `DMX/emotions.py`: This script defines the lighting effects for different emotions. It uses the `Aputure` and `Epix` classes to control the lights.
-   `emotion_analyzer.py`: This script uses the Gemini API to analyze text and determine the dominant emotion. It then calls the `DMX/emotions.py` script to trigger the corresponding lighting effect.
-   `config.toml`: This file contains the configuration for the project, including the DMX addresses of the lighting fixtures and a set of preset colors.

### Adding New Lighting Fixtures

To add support for a new lighting fixture, you'll need to create a new Python class that inherits from `EnttecObject`. This class should implement the methods necessary to control the new fixture. You'll also need to update the `config.toml` file to include the DMX address of the new fixture.

### Adding New Emotions

To add a new emotion, you'll need to do the following:

1.  Add the new emotion to the `EMOTION_SCHEMAS` dictionary in `DMX/emotions.py`. This dictionary maps emotions to lighting effects.
2.  Define the lighting effect for the new emotion. This can be a new effect or an existing one.
3.  Add the new emotion to the `AVAILABLE_EMOTIONS` list in `emotion_analyzer.py`.

## Setting Up Your Development Environment

1.  Clone the repository:
    ```bash
    git clone https://github.com/priyanshum17/python-dmx.git
    ```
2.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3.  Activate the virtual environment:
    -   On Windows:
        ```bash
        venv\Scripts\activate
        ```
    -   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
4.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

To run the tests, you'll need to have a DMX controller and lights connected. Then, you can run the `dmxtest.py` script:

```bash
python DMX/dmxtest.py -m <mode> -c <com_port>
```

Replace `<mode>` with the DMX mode for your lights and `<com_port>` with the COM port of your DMX controller.
