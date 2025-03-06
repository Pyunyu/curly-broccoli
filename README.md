# Full Metal Squelita

Full Metal Squelita is a Flask-based API for managing users and their addresses. It uses SQLAlchemy for database interactions and provides endpoints for retrieving and creating users and addresses.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SamuelCarmona83/full-metal-squelita.git
cd full-metal-squelita
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:

```bash
python main.py
```

2. The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

### Users

- `GET /users`: Retrieve all users.
- `POST /users`: Create a new user.

### Addresses

- `GET /addresses`: Retrieve all addresses.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.