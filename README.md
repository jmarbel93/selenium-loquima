# Selenium Loquima

## Requirements
- Python 
- Git 
- pip
- Virtual environment module (Venv)

## Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/jmarbel93/selenium-loquima.git
    cd selenium-loquima
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Verify the installation:
    ```bash
    pip list
    ```
    (Check that "pytest" and "selenium" appear in the list of installed packages)

## Running Tests
To execute the test suite, use the following command:
   ```bash
   pytest tests/
   ```

For more detailed output, run:
   ```bash
   pytest -v
   ```

To run a specific test file:
   ```bash
   pytest tests/test_amazon_music.py
   ```

To stop execution on the first failure:
   ```bash
   pytest -x
   ```