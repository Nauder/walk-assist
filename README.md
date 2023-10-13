# Walk Assist

This repository contains the **WIP** code for a project aimed at helping blind individuals navigate specific locations on foot, developed as a university class project. The project involves a Flask-based REST API that utilizes Alchemy for ORM and PostgreSQL for database management. The database migrations are handled with Flask-Migrate

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [License](#license)

## Features

- RESTful API built with Flask for blind navigation assistance.
- Utilizes Alchemy for object-relational mapping.
- PostgreSQL database for storage and retrieval of location and user information.

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL
- pip (Python package manager)

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Nauder/walk-assist
    cd walk-assist
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database by running the `database.sql` script and configure the database settings in the `config/app.conf` file.

5. Run the application:

    ```bash
    python app.py
    ```

## Usage

The API provides endpoints to assist blind individuals in navigating specific locations. Refer to the [API Endpoints](https://app.swaggerhub.com/apis/DEWAVEB140_1/api-de_gerenciamento_de_usuarios_e_rotas/1.0.0#/) on Swagger for detailed information on available endpoints.

## Database Schema

The PostgreSQL database schema includes the following tables:

- `usuario`: Stores application user information including name, password, email and admin status.

## License

This project is licensed under the [MIT License](LICENSE).
