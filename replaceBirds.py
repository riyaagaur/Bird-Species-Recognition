# -*- coding: utf-8 -*-
"""replaceBird.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u0SXCwwn7SJmNMQy8UbqbINiabtWHCLZ
"""

# !pip install diffusers
# !pip install -q git+https://github.com/huggingface/transformers.git
# !pip install accelerate
import PIL
import requests
import torch
from io import BytesIO
# import diffusers
from diffusers import StableDiffusionInpaintPipeline
from PIL import Image

pipeline = StableDiffusionInpaintPipeline.from_pretrained(
    "runwayml/stable-diffusion-inpainting"
)

pipeline = pipeline.to('cpu')

image_dir = [
    # "/content/drive/MyDrive/Colab Notebooks/Applied ML/Assignment 3/Test_Birds/bird_img_1.JPEG",
    # "/content/drive/MyDrive/Colab Notebooks/Applied ML/Assignment 3/Test_Birds/bird_img_2.JPEG",
    # "/content/drive/MyDrive/Colab Notebooks/Applied ML/Assignment 3/Test_Birds/bird_img_3.JPEG",
    # "/content/drive/MyDrive/Colab Notebooks/Applied ML/Assignment 3/Test_Birds/bird_img_4.JPEG",
    "/content/drive/MyDrive/Colab Notebooks/Applied ML/Assignment 3/Test_Birds/bird_img_5.JPEG"
    
]
mask_dir = [
    # "/content/drive/MyDrive/Colab Notebooks/Applied ML/Assignment 3/Masked_Birds/masked_bird_img_1.jpg",
    # "/content/drive/MyDrive/Colab Notebooks/Applied ML/Assignment 3/Masked_Birds/masked_bird_img_2.jpg",
    # "/content/drive/MyDrive/Colab Notebooks/Applied ML/Assignment 3/Masked_Birds/masked_bird_img_3.jpg",
    # "/content/drive/MyDrive/Colab Notebooks/Applied ML/Assignment 3/Masked_Birds/masked_bird_img_4.jpg",
    "/content/drive/MyDrive/Colab Notebooks/Applied ML/Assignment 3/Masked_Birds/masked_bird_img_5.jpg",
    
]

image_path = image_paths[0]
mask_path = mask_paths[0]
init_image = Image.open(image_path).resize((512, 512))
mask_image = Image.open(mask_path).resize((512, 512))
prompt = 'Replace bird with the Asian green bee-eater, high resolution'
image = pipeline(prompt=prompt, image=init_image, mask_image=mask_image).images[0]


image.save('bird_img_6_replaced.jpg')