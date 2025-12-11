from fastapi import FastAPI, UploadFile, File , Depends
from fastapi.responses import JSONResponse, StreamingResponse

import os
import io
import cv2

from imutils.perspective import four_point_transform
import numpy as np
import pandas as pd
import json
import numpy as np
from PIL import Image

from app.palm_vein.palm_vein_model_api import classify_palm_vein_image

app = FastAPI()


@app.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    # Verify file is an image

    try:
        # Read and preprocess image
        image_bytes = await file.read()
        hh = classify_palm_vein_image(image_bytes)
        
        return hh
    
    except Exception as e:
        return ""
