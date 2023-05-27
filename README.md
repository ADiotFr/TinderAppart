# FindAppart

## Introduction

A brief introduction to your project. Describe what your project does and what technologies it uses.

## Requirements

This project requires Python 3.8 (or later) and Django 3.2 (or later). Additional dependencies are listed in the `requirements.txt` file.

## Getting Started

### Installation

1. **Clone the repository**  
   If you have git installed, clone the repository using this command:

    ```shell
    git clone https://github.com/ADiotFr/TinderAppart.git
    ```

2. **Create and activate a virtual environment**  
   It is good practice to create a virtual environment for your project to avoid conflicts between dependencies. You can create a virtual environment using the following commands:
  
    ```shell
    python -m venv env  
    ```
   If a virtual environment is already existing, simply activate it using the following commands:

    ```shell
    source env/bin/activate  # On Unix or MacOS
    env\Scripts\activate     # On Windows
    ```

3. **Install the dependencies**  
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