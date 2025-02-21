# Django Tutorial

This project is a Django tutorial to help you get started with Django, a high-level Python web framework.

## Getting Started

### Prerequisites

Make sure you have the following installed:
- Python 3.x
- pip
- virtualenv

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/djangotutorial.git
    cd djangotutorial
    ```

2. Install uv: [Refer this link](https://docs.astral.sh/uv/getting-started/installation/)
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Create a virtual environment using `uv`:
    ```bash
    uv venv .venv
    ```

4. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Project

1. Apply migrations:
    ```bash
    python manage.py migrate
    ```

2. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

3. Run the development server:
    ```bash
    python manage.py runserver
    ```

4. Open your web browser and go to `http://127.0.0.1:8000/` to see the project in action.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
