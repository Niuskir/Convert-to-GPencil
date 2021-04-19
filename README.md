# Convert-to-GPencil
A basic Python script for Blender to assist converting a video to Grease Pencil images

This script needs to be run manually

How to use the script:

1) Use Blender to convert your video to seprate images (jpg or png) for each frame. Use XXXX.jpg or XXXX.png name convention. 
2) Download and run the blend file from the repository. 
3) Update line 108 in the Blender Python script to define the source folder where the images reside you created in step 1.  
4) Take one image from step 1 and drop it in the Blender viewport and test converting the image to GPencil (Object->Convert->Convert to Grease Pencil) to determine best GPencil conversion settings.
5) Update line 93 in the Python script with the GPencil settings from step 4.
6) Check if the Blender Camera settings and adjust if necessary.
7) Delete test image and test GPencil from scene
8) Open the system console window (Window->Toggle System Console). The script will show progress processing the frames in the console.
9) Run script manually, for each image in the source folder the script will (1) convert image to Grease Pencil, (2) delete the image, (3)render an image of the GPencel object and (4) deletes the GPencil object    

