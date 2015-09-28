import os

from .company import Company
from .person import Person

key = os.getenv('FULLCONTACT_KEY', None)
VERSION = '1.0.0'
