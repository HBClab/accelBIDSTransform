# Accelerometer BIDS Transformation

This repository contains the scripts necessary to transform
the raw accelerometer data into their respective project directories.

The process roughly follows this [evolving diagram](https://drive.google.com/file/d/1wuMSr-RcrVRNRWfBI4J0bQR-8YhSn3kQ/view?usp=sharing).

## Testing the code

I assume you have docker installed and are using linux


```
docker build -t hbclab/accel-dev .
docker run -it --rm -v ${PWD}:/home/coder/projects -p 127.0.0.1:8080:8080 hbclab/accel-dev
```

then visit 0.0.0.0:8080 in your browser

## Testing the code (manually)

1. Install the conda environment:

    - `conda env create -f environment.yml`

2. install the accel_code locally as an editable package:

    - `pip install -e .`

