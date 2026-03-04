import os
from dotenv import load_dotenv
import pytest

# load environment variables from .env file if present
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

@pytest.fixture(scope="session")
def base_url():
    # you can define BASE_URL in your .env file and use it in tests
    return os.getenv('BASE_URL', 'http://localhost:3000')

# additional fixtures (e.g., for authentication) can go here
