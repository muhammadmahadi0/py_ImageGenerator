import openai
import requests
from PIL import Image

# Set up OpenAI API credentials
openai.api_key = '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'

# Prompt user for input
prompt = input("Enter a prompt for the image: ")

# Generate image using OpenAI's DALL-E API
response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="1024x1024"
)

# Save image to file
filename = input("Enter a filename for the image: ")
url = response['data'][0]['url']
image_data = requests.get(url).content
with open(filename + ".jpg", "wb") as f:
    f.write(image_data)

print(f"Image saved as {filename}.jpg")

