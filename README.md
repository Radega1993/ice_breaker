
# ice_breaker

A repository for learning LangChain🦜🔗  by building a generative ai application.

This is a web application crawling Linkedin & Twitter data about a person and customizes an ice breaker with them.


![Logo](https://github.com/emarco177/ice_breaker/blob/main/static/demo.gif)
[![udemy](https://img.shields.io/badge/LangChain%20Udemy%20Course-Coupon%20%2412.99-brightgreen)](https://www.udemy.com/course/langchain/?referralCode=D981B8213164A3EA91AC)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PYTHONPATH=/{YOUR_PATH_TO_PROJECT}/ice_breaker`

`OPENAI_API_KEY`

`PROXYCURL_API_KEY`

`TAVILY_API_KEY`

`TWITTER_API_KEY`

`TWITTER_API_SECRET`

`TWITTER_ACCESS_TOKEN`

`TWITTER_ACCESS_SECRET`
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

Start the flask server

```bash
  pipenv run app.py
```


## Running Tests

To run tests, run the following command

```bash
  pipenv run pytest .
```


Para instalar pipenv en Kubuntu, puedes seguir estos pasos detallados:

    Actualizar los paquetes del sistema:
    Abre una terminal y actualiza la lista de paquetes e instala las actualizaciones disponibles:

    bash

sudo apt update
sudo apt upgrade

Instalar Python y pip:
Si no tienes Python instalado, puedes instalar Python y pip con los siguientes comandos:

bash

sudo apt install python3 python3-pip

Instalar pipenv:
Una vez que tienes pip instalado, puedes instalar pipenv utilizando pip:

bash

sudo pip3 install pipenv

Verificar la instalación:
Para asegurarte de que pipenv se ha instalado correctamente, puedes verificar la versión instalada con el siguiente comando:

bash

    pipenv --version

Uso básico de pipenv

Para crear un nuevo entorno virtual y gestionar dependencias con pipenv, puedes seguir estos pasos básicos:

    Crear un nuevo entorno virtual:
    Navega al directorio de tu proyecto y ejecuta:

    bash

pipenv install

Instalar paquetes:
Para instalar paquetes dentro de tu entorno virtual, usa:

bash

pipenv install <paquete>

Activar el entorno virtual:
Para activar el entorno virtual y trabajar dentro de él, usa:

bash

pipenv shell

Salir del entorno virtual:
Para salir del entorno virtual, simplemente escribe:

bash

exit
