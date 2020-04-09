# Accelerometer BIDS Transformation

This repository contains the scripts necessary to transform
the raw accelerometer data into their respective project directories.

The process roughly follows this [evolving diagram](https://drive.google.com/file/d/1wuMSr-RcrVRNRWfBI4J0bQR-8YhSn3kQ/view?usp=sharing).

## Testing the code

I assume you have docker installed and are using linux


```
docker build -t hbclab/accel .
docker run --rm -it -v ${PWD}:/home/coder/project -p 8080:8080 hbclab/accel
```

## Testing the code (manually)
1. Install the conda environment:

    - `conda env create -f environment.yml`

2. install the accel_code locally as an editable package:

    - `pip install -e .`



# Overview of current structure for accelerometer data
The accelBIDSTransform (https://github.com/HBClab/accelBIDSTransform) tool currently uses a subject-specific method of organization for all accelerometer files in accordance with BIDS (https://bids.neuroimaging.io/) standards for data organization. This ensures that all data (accelerometer, imaging, etc.) for each subject is under that specific subject's directory in the study's directory, as per BIDS standards. Accelerometer data files are named such that they contain subject ID, session ID (if applicable for the study), and an `accel.csv` extension.

Currently, all data is contained in the `Projects` folder under the `vosslabhpc` server which is then separated into the different studies. These studies then contain a `/BIDS/` folder which organizes all subject-specific directories under it. However, some studies already have imaging data present in a non-BIDS format and since the tool is only designed to move accelerometer files (since moving imaging data could effect already existing workflows), we decided it would be best to stick to BIDS standards as much as possible and add accelerometer data to already existing subject-specific folders existing under imaging directories for older projects. (These will be outlined below with examples) 

For newer/ongoing projects where BIDS was adhered to from the start, we have added an extra `/beh/` directory under existing subject-specific directories to accomodate accelerometer data. (These are also outlined below)

## Existing non-BIDS formatted studies
- AMBI
- PACR
- BIKE

These project directories were initially set up without adhering to BIDS standards for the imaging data. In order to not modify the current imaging directories, the accelerometer data was added under the subject IDs located in existing `/Imaging/` directories. The accelBIDSTransform tool also takes into account which studies have session IDs, and if applicable, adds a `/ses-X/` directory under the subject specific directory, which then contains a `/beh/` directory for accelerometer data and other behavioral data.

The accelBIDSTransform tool also takes into account cases where the subject ID from redcap doesn't match the subject ID directory name on `vosslabhpc`, as seen in PACR and BIKE studies.

### Example: AMBI
- Given subject ID: `21`
- Given session ID: `N/A`
- BIDS formatted path: `Projects/AMBI/3-Experiment/2-Data/Imaging/BIDS/sub-21/beh/sub-21_accel.csv`

### Example: PACR
- Given subject ID: `51`
- Given session ID: `pre`
- BIDS formatted path: `vosslabhpc/Projects/PACR-AD/Imaging/BIDS/sub-controlSE051/ses-pre/beh/sub-controlSE051_ses-pre_accel.csv`

### Example: BIKE
- Given subject ID: `142`
- Given session ID: `pre`
- BIDS formatted path: `Projects/Bike_ATrain/Imaging/BIDS/sub-SEA142/ses-pre/beh/sub-SEA142_ses-pre_accel.csv`

## BIDS formatted studies
- ALERT
- Normative
- EXTEND
- BETTER

These studies were initially stored in accordance to BIDS format and all data is contained under `/3-Experiment/2-Data/BIDS/` directories located under the study-specific directory. The accelBIDSTransform tool will take into account which subject-specific directories contain session directories and add accelerometer data to the `/beh/` directory located under either the subject or session directories. 

The accelBIDSTransform takes into account the difference in capitalization between studies' directories, but it is recommended to follow a standard capilization scheme in the future. Note: this will not affect how the accelBIDSTransform tool works, and future studies will need to be added to the `accel_code/bids_transform.py` and `accel_code/utils.py` files to ensure that the future project name is included in the path. See the inline comments in `accel_code/bids_transform.py` for more developer-specific information.

The accelBIDSTransform tool also takes into account cases where the subject ID from redcap doesn't match the subject ID directory name on `vosslabhpc`, as seen in the BETTER study.

### Example: ALERT
- Given subject ID: `21`
- Given session ID: `N/A`
- BIDS formatted path: `Projects/ALERT/3-Experiment/2-Data/BIDS/sub-21/beh/sub-21_accel.csv`

### Example: Normative
- Given subject ID: `3795`
- Given session ID: `N/A`
- BIDS formatted path: `Projects/NormativeSample/3-Experiment/2-Data/BIDS/sub-3795/beh/sub-3795_accel.csv`

### Example: EXTEND
- Given subject ID: `2103`
- Given session ID: `3`
- BIDS formatted path: `Projects/BikeExtend/3-Experiment/2-Data/BIDS/sub-2103/ses-accel3/beh/sub-2103_ses-accel3_accel.csv`

### Example: BETTER
- Given subject ID: `120014`
- Given session ID: `pre`
- BIDS formatted path: `Projects/BETTER/3-Experiment/2-data/bids/sub-GE120014/ses-pre/beh/sub-GE120014_ses-pre_accel.csv`