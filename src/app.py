import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# get credential values
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
