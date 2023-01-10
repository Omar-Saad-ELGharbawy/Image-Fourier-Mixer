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

### Default Page
![1](https://user-images.githubusercontent.com/84602951/210450461-f5081a7f-32e1-4742-907f-330dff954025.png)

### Upload images
![2](https://user-images.githubusercontent.com/84602951/210450484-e8413e68-5799-4219-b893-034f1d2c4011.png)

### Display magnitude and phase of each image in fourier domain.
![12](https://user-images.githubusercontent.com/84602951/210451605-3d0874b1-0994-4628-9a42-0e0ad7033dc5.png)

### Select magnitude or phase component of one image only to display  uniform magnitude or uniform phase of image in time domain.
![3](https://user-images.githubusercontent.com/84602951/210451764-efcefe52-bc2c-46d9-9607-cc3be85f4c23.png)

### Select magnitude or phase component of each image and display the mixed image in time domain.
![4](https://user-images.githubusercontent.com/84602951/210451810-ffdfbabc-09c1-4a25-b5cb-ddaf572652ad.png)

### Crop in magnitude or phase of each image and show the crop effect on the mixed image on real time.
![6](https://user-images.githubusercontent.com/84602951/210451835-b9d7a34a-8c5c-4faf-8c97-ca0ddf7fbede.png)


## Tools

1. Frontend :
* React Js 
* CSS 

2. Backend :
* Python
* Flask

## Theoretical Technique
### Fourier Transform 
- Fourier transform of 2d images and calculating **Magnitude** and **Phase** of images.

- **Fourier shift** for visualizing Fourier transform with the zero-frequency component in the middle of the spectrum.

- Mixing magnitude and phase of diffirent image in **fourier domain**.

- **Inverse Fourier Transform** of mixed image to display it in **time domain**.


## Project Structure
### Image Class:
- Contains all image information and methods to :
1. Read and resize image.
2. Claculate fourier transform of image.
3. Crop in image phase and magnitude.

### Processing Class:
- Contains static functions and static objects of Image model to store data.
