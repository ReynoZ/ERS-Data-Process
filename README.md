# ERS Data Process

## Assignment 1

Main target of the assignment 1 has been achieved.

### This program is now able to:

- go through all the sample data in the USGS database, calculate the Euclidean distance between each sample data and my measurement to find a most similar one as a match.
- Plot both the USGS and my measurements in one figure. Seen as below.

![sample4](/fig_sample_4.png)
![sample5](/fig_sample_5.png)

### Improvements needed:

- Output format needed to be improved(using Regex Expression maybe).
- Use Mahalanobis Distance to improve the matching.
- Use cosine similarity to take figure shape into consideration when matching.
- Better-looking plots.
- Process bar.

## Assignment 2

**TASK DESCRIPTION:** Download Landsat surface reflectance images, and use the spectral profile tool to extract typical spectral reflectance profiles for vegetation, water, urban area, clouds, etc.

I downloaded the Landsat 8 surface relectance images from the USGS website and pre-processed the images with ENVI 5.3.

The exported spectral profiles data contains values stored in signed 16bit format. So I used Python for radiometric calibration, converted the original value to reflectance by mutiplying the data by the scale factor 0.0001.

Four typical points(vegetation, water, urban area and clouds) are selected. The output figure is as below,

![spectral](/Landsat8_Spectral_Profiles.png)

Repository Address: https://github.com/ReynoZ/ERS-Data-Process
