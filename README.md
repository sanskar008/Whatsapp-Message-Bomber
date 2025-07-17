# Whatsapp-Message-Bomber

[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![GitHub Stars](https://img.shields.io/github/stars/sanskar008/Whatsapp-Message-Bomber?style=social)](https://github.com/sanskar008/Whatsapp-Message-Bomber/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/sanskar008/Whatsapp-Message-Bomber?style=social)](https://github.com/sanskar008/Whatsapp-Message-Bomber/network/members)
[![License: Unspecified](https://img.shields.io/badge/License-Unspecified-lightgrey.svg)](#license)

## ⚠️ Disclaimer

This tool is provided for educational and experimental purposes only. **Misuse of this tool, including spamming, harassment, or any activity that violates WhatsApp's Terms of Service or local laws, is strictly prohibited.** The developer is not responsible for any misuse or damage caused by this software. Use it responsibly and ethically.

## Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Using `selenium_code.py` (Web Automation)](#using-selenium_code.py-web-automation)
  - [Using `text_code.py` (Plain Text Bombing)](#using-text_code.py-plain-text-bombing)
  - [Using `text+emoji_code.py` (Text & Emoji Bombing)](#using-textemoji_code.py-text--emoji-bombing)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About The Project

`Whatsapp-Message-Bomber` is a collection of Python scripts designed to automate the sending of multiple WhatsApp messages. The project demonstrates different approaches to achieving this, ranging from web automation using Selenium to simpler text generation techniques.

This tool can be used for testing, personal automation, or educational purposes to understand web automation and messaging APIs.

## Features

*   **`selenium_code.py`**: Automates WhatsApp Web using Selenium to send a specified number of messages to a target contact. Requires browser setup and QR code scanning.
*   **`text_code.py`**: A simpler script focused on generating and potentially sending a large number of plain text messages.
*   **`text+emoji_code.py`**: Extends `text_code.py` by allowing the inclusion of emojis in the repetitive messages.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.x**:
    ```bash
    python --version
    ```
    If not installed, download from [python.org](https://www.python.org/downloads/).
*   **pip** (Python package installer): Usually comes with Python.
    ```bash
    pip --version
    ```
*   **Google Chrome** (for `selenium_code.py`): The Selenium script is configured to use Chrome. Ensure you have the latest version installed.
*   **ChromeDriver**: Selenium requires a WebDriver to interact with the browser. `webdriver_manager` will automatically handle downloading the correct ChromeDriver, but a stable internet connection is required for the first run.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/sanskar008/Whatsapp-Message-Bomber.git
    cd Whatsapp-Message-Bomber
    ```

2.  **Install Python dependencies:**
    The `selenium_code.py` script requires the `selenium` and `webdriver-manager` libraries.
    ```bash
    pip install selenium webdriver-manager
    ```
    The other scripts (`text_code.py`, `text+emoji_code.py`) generally do not require external libraries beyond standard Python.

## Usage

Each script in this repository serves a slightly different purpose and has its own usage method.

### Using `selenium_code.py` (Web Automation)

This script automates sending messages via WhatsApp Web.

1.  **Run the script:**
    ```bash
    python selenium_code.py
    ```

2.  **Follow the prompts:**
    *   The script will open a Chrome browser window and navigate to WhatsApp Web.
    *   You will be prompted to scan the QR code with your phone to log in.
    *   Once logged in, the script will ask for the target contact's name (as it appears in your WhatsApp contacts), the message you want to send, and the number of times to send it.

    ```
    Please scan the QR code to log in to WhatsApp Web.
    Press Enter after scanning QR code...
    Enter target contact name: John Doe
    Enter message to send: Hello from the bomber!
    Enter number of messages: 100
    ```

    The script will then navigate to the chat, type, and send the messages.

### Using `text_code.py` (Plain Text Bombing)

This script focuses on generating and potentially sending a large volume of plain text messages. The exact sending mechanism may vary, or it might output text for manual pasting.

1.  **Run the script:**
    ```bash
    python text_code.py
    ```

2.  **Follow the prompts:**
    *   The script will ask for the message you want to repeat and the number of repetitions.

    ```
    Enter message to repeat: Spam this!
    Enter number of repetitions: 50
    ```

    *   The script will then generate or attempt to send the specified number of messages.

### Using `text+emoji_code.py` (Text & Emoji Bombing)

Similar to `text_code.py`, but allows you to specify an emoji to include with each message.

1.  **Run the script:**
    ```bash
    python text+emoji_code.py
    ```

2.  **Follow the prompts:**
    *   The script will ask for the message, the emoji to include, and the number of repetitions.

    ```
    Enter message to repeat: Bombarding you!
    Enter emoji to include (e.g., 😂): 🚀
    Enter number of repetitions: 75
    ```

    *   The script will then generate or attempt to send the messages with the specified text and emoji.

## How It Works

*   **`selenium_code.py`**: Leverages the [Selenium WebDriver](https://www.selenium.dev/) to automate browser interactions. It simulates user actions like opening WhatsApp Web, scanning the QR code, finding contacts, typing messages, and clicking the send button. `webdriver_manager` simplifies the setup by automatically downloading the correct ChromeDriver for your browser version.
*   **`text_code.py` and `text+emoji_code.py`**: These scripts are designed for simpler message generation. Depending on their internal implementation, they might either:
    *   Print the generated repetitive text to the console, allowing you to manually copy
