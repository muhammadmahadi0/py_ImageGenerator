# py_ImageGenerator
# Image Generator using OpenAI DALL-E API
This Python code uses OpenAI's DALL-E API to generate images based on a given prompt.

## Requirements
* OpenAI [API key](https://platform.openai.com/account/api-keys)
* Python 3.x
* requests and openai library (can be installed using pip)
## Setup
1. Install Python 3.x on your system.
2. Install the `requests` and `openai` library by running `pip install requests openai` in the terminal.
3. Set up your OpenAI API credentials by replacing `YOUR_API_KEY` in the code below with your actual API key:
```python
openai.api_key = 'YOUR_API_KEY'

```
## Usage
1. Run the Python script using the following command:
```bash
python image_generator.py
```
2. Enter a prompt for the image when prompted by the script.
3. The generated image will be saved to the current working directory with the name `generated_image.jpg`.

# Disclaimer
This code is provided for educational purposes only. The use of OpenAI's DALL-E API is subject to their [terms of use](https://beta.openai.com/terms/).

# License
This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.
