import requests
import dotenv
import os
import streamlit as st
import pandas as pd

dotenv.load_dotenv()

CENT_API_KEY = os.getenv("CENT_API_KEY")

# building the prompt
PROMPT_TEMPLATE = ''''''

input_text = 'Gasoline prices are $5.99 per gallon in Canada.'
prompt = PROMPT_TEMPLATE.replace("{input_text}", input_text)

# set up the api request


# call the api


# parse the response