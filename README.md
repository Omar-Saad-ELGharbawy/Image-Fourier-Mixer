# Image Mixer 

> Image Mixer is a digital signal processing website to mix fourier magnitude and phase of 2 different images in the fourier domain and display the mixed image in the time domain.

## Task info
- Digital signal processing Course
- First Semster
- Date : 3/1/2023

|Team Members|
|----------|
|Mazen Tarek|
|Neven Mohamed|
|Zeyad Amr| 
|Omar Saad|  

## Features
- Upload 2 image
- Display magnitude and phase of each image in fourier domain.
- Select magnitude or phase component of each image and display the mixed image in time domain.
- Crop in magnitude or phase of each image and show the crop effect on the mixed image on real time.

## Tools

1. Frontend :
* HTML 
* CSS 
* Javascript
* React

2. Backend :
* Python
* Flask

## Science
### Fourier Transform 
- Fourier transform of 2d images and calculating **Magnitude** and **Phase** of images.

- **Fourier shift** for visualizing Fourier transform with the zero-frequency component in the middle of the spectrum.

- Mixing magnitude and phase of diffirent image in **fourier domain**.

- **Inverse Fourier Transform** of mixed image to display it in **time domain**.

### Object oriented programming :

1. Image Class contains all image information and methods to :
- Read and resize image.
- Claculate fourier transform of image.
- Crop in image phase and magnitude.

2. Processing class with static functions and static objects of Image Class to store image data in it and to be used in the backend.