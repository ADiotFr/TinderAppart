# FindAppart

## Introduction

FindAppart is a web platform built using Django framework that facilitates the matching process between property owners and potential tenants. The platform allows property owners to list their properties and tenants to create profiles and specify their preferences. The goal is to match tenants with suitable properties based on their preferences and property owners' listings.
## Requirements

This project requires Python 3.8 (or later) and Django 3.2 (or later). Additional dependencies are listed in the `requirements.txt` file.

## Getting Started

### Installation

1. **Create and activate a virtual environment**  
   It is good practice to create a virtual environment for your project to avoid conflicts between dependencies. You can create a virtual environment using the following commands:
  
    ```shell
    python -m venv env  
    ```
   If a virtual environment is already existing, simply activate it using the following commands:

    ```shell
    source env/bin/activate  # On Unix or MacOS
    env\Scripts\activate     # On Windows
    ```

2. **Install the dependencies**  
   Install the project dependencies with pip:

    ```shell
    pip install -r requirements.txt
    ```

### Running the project

To start the Django server, navigate to the project directory (where `manage.py` is located) and use the following command:

```shell
python manage.py runserver
```

This will start the server at http://127.0.0.1:8000/. Navigate to this address in your web browser to view your project.