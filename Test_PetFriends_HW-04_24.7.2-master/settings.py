import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')

no_valid_email = os.getenv('no_valid_email')
no_valid_password = os.getenv('no_valid_password')