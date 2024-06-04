# Ice Breaker

A repository for learning LangChain🦜🔗 by building a generative AI application.

This is a web application that crawls LinkedIn data about a person and customizes an ice breaker with them.

![Logo](https://github.com/emarco177/ice_breaker/blob/main/static/demo.gif)
[![udemy](https://img.shields.io/badge/LangChain%20Udemy%20Course-Coupon%20%2412.99-brightgreen)](https://www.udemy.com/course/langchain/?referralCode=D981B8213164A3EA91AC)

## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:

- `PYTHONPATH=/{YOUR_PATH_TO_PROJECT}/ice_breaker`
- `OPENAI_API_KEY`
- `PROXYCURL_API_KEY`

## Run Locally

Clone the project

```bash
git clone https://github.com/emarco177/ice_breaker.git
```

Go to the project directory

```bash
cd ice_breaker
```

Install dependencies

```bash
pipenv install
```

copy .env.template to .env

```bash
cd .env.template .env
```

Start the Flask server

```bash
pipenv run python app.py
```
Running Tests

To run tests, run the following command

```bash
pipenv run pytest .
```

Installing pipenv on Kubuntu

To install pipenv on Kubuntu, follow these steps:
Update System Packages

Open a terminal and update the package lists and install available updates:

```bash
sudo apt update
sudo apt upgrade
```
Install Python and pip

If you don't have Python installed, install Python and pip with the following commands:

```bash
sudo apt install python3 python3-pip
```
Install pipenv

Once you have pip installed, install pipenv using pip:

```bash
sudo pip3 install pipenv
```

Verify the Installation

To ensure that pipenv has been installed correctly, you can check the installed version with the following command:

```bash
pipenv --version
```

Basic Usage of pipenv

To create a new virtual environment and manage dependencies with pipenv, follow these basic steps:
Create a New Virtual Environment

Navigate to your project directory and run:

```bash
pipenv install
```

Install Packages

To install packages within your virtual environment, use:

```bash
pipenv install <package>
```

Activate the Virtual Environment

To activate the virtual environment and work within it, use:

```bash
pipenv shell
```

Deactivate the Virtual Environment

To exit the virtual environment, simply type:

```bash
exit
```