import os
from dotenv import load_dotenv

load_dotenv() # loads the variables from the .env file

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"