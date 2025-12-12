# Tamteen

This repository hosts a script for Tamteen back-end implenetation and GUI swift implementation.

## Palm Scanner Classification

## Prerequisites

- Python 3.x

## Installation

### Clone the repository

```bash
git clone https://github.com/Norab99/tamteen.git

# Install dependencies
pip install -r requirements.txt
```

### Generate the Trained Model
```bash
py app/palm_vein/palm_vein_model.py
```
## Usage

### Running the script locally

#### `fastapi`

The `app/main.py` script performs palm scanning classification on the uplaod image.

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

# API Endpoint

## Palm Scaaning Classification

The Palm Scanning Classification functionality can be accessed via a FastAPI endpoint:
- **POST** `/classify`: Upload an image file. The response will contain classification result.

### POST /classify

```bash
curl.exe -X POST -F "file=@C:\Users\Nora-Basalamah\Downloads\multimodal pp and pv\DB_Vein\094\094R_VL01.bmp" http://localhost:8000/classify
```
## License

This project is licensed under the terms of the MIT license.

## References
- [Contactless Knuckle-Palm Print and Vein Dataset](https://www.kaggle.com/datasets/michaelgoh/contactless-knuckle-palm-print-and-vein-dataset)
