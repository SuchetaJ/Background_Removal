from carvekit.ml.files.models_loc import download_all
download_all();


import torch
from IPython import display
from carvekit.web.schemas.config import MLConfig
from carvekit.web.utils.init_utils import init_interface

SHOW_FULLSIZE = False
PREPROCESSING_METHOD = "none"
SEGMENTATION_NETWORK = "tracer_b7"
POSTPROCESSING_METHOD = "fba"
SEGMENTATION_MASK_SIZE = 640
TRIMAP_DILATION = 30
TRIMAP_EROSION = 5
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


config = MLConfig(segmentation_network=SEGMENTATION_NETWORK,
                  preprocessing_method=PREPROCESSING_METHOD,
                  postprocessing_method=POSTPROCESSING_METHOD,
                  seg_mask_size=SEGMENTATION_MASK_SIZE,
                  trimap_dilation=TRIMAP_DILATION,
                  trimap_erosion=TRIMAP_EROSION,
                  device=DEVICE)


interface = init_interface(config)


def background_removal(img):
  images = interface(img)
  for im in enumerate(images):
    if not SHOW_FULLSIZE:
      im[1].thumbnail((768, 768), resample=3)
    no_bg = im[1].convert('RGB')
    print(im)
    return no_bg

import gradio as gr
from PIL import Image
import cv2

# Define the input and output interfaces using Gradio
input_image = gr.inputs.Image()


def background_removal2(image):
  # create an image from the numpy array
  img = Image.fromarray(image.astype('uint8'))
  if len(image.shape) == 3:
    h, w, k = image.shape
  else:
    h, w = image.shape
  if h>=w :
    new_size = (700, (700*h)//w)
  else:
    new_size = ((700*w)//h,700)
  img = img.resize(new_size)
  # save the image to a file
  img.save('1.jpg')
  no_bg = interface(['1.jpg'])[0]
  no_bg = no_bg.resize(new_size)
  return no_bg

# Create the Gradio interface
interface2 = gr.Interface(fn=background_removal2,  inputs=input_image, outputs='image', title="Background Removal").launch(server_name ='0.0.0.0',share=True)
