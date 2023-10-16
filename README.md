# Tapsshop.pl Automation Tests

This repository contains a Python Selenium unittest project for automating tests on the [tapsshop.pl](https://tapsshop.pl/) sample e-commerce website. The project covers various test scenarios and page objects, allowing you to validate the functionality of the website.

## Project Structure

The project is organized into different directories to help manage your tests and resources:

- **Browsers**: This directory is where you should place the browsers to be used for testing.

- **Config**: Contains test data and configurations. You can modify the settings in the `Test_settings.py` file.

- **Drivers**: Place the ChromeDriver executable here, which is required for Selenium to work with Chrome.

- **Pages_objects**: Contains page object classes that represent different pages of the website. Each page object class encapsulates the elements and actions specific to that page.

- **Tests**: This directory holds the individual test scripts, one for each aspect of the website you want to test.

- **Utilities**: Includes utility functions and classes that help with common testing tasks.

## Getting Started

Before running the tests, you need to:

1. Download and place a Chrome browser in the `Browsers/Chrome` directory.
2. Download the ChromeDriver executable and place it in the `Drivers` directory.
3. Install the required Python packages by running `pip install -r requirements.txt` in a virtual environment.
