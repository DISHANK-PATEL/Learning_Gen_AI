# -*- coding: utf-8 -*-
"""temp1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jKMpffuRZeCjTnMH3P-aYz5x_lvWNgEd
"""

!pip install -q -U google-generativeai

import pathlib
import textwrap
import google.generativeai as genai
from google.colab import userdata
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace('.', ' ** ')

    indented_text = textwrap.indent(text, '>', predicate=lambda _: True)
    return Markdown(indented_text)

import os
os.environ['GOOGLE_API_KEY']="AIzaSyDRC0J9w-SknMrM4Hk3xGpeNFkypFE2Rrg"

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model=genai.GenerativeModel('gemini-pro')

response=model.generate_content("Give me info of jaundice ",stream=True)

for chunk in response:
   print(chunk.text)
   print("_"*80)

# !curl -o image.jpg "https://imgs.search.brave.com/pJulsikYgFQBIc5f_QKcaJ9i1rwa1hcO5BYCf3o3-Ls/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/aW5kaWFmb3J1bXMu/Y29tL21lZGlhLzcy/MHgwLzU3LzQ1NTYt/dmlyYXQta29obGkt/YW51c2hrYS1zaGFy/bWEuanBn"
import PIL.Image
img=PIL.Image.open('image.png')
img

model=genai.GenerativeModel('gemini-1.5-flash')

import requests
from PIL import Image
import io
image_url = "https://images.drlogy.com/assets/uploads/lab/image/cbc-absolute-count-test-report-format-example-sample-template-drlogy-lab-report.webp"
response = requests.get(image_url, stream=True)
image = Image.open(io.BytesIO(response.content))
text_prompt = "Tell me about the image wrt to health"
response = model.generate_content([image, text_prompt], stream=True)
for chunk in response:
    print(chunk.text)
    print("_"*80)