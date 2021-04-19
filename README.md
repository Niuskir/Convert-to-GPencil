# Convert-to-GPencil
A basic Python script for Blender to assist converting a video to Grease Pencil images, this is an alternative to the "Sequence" option of the Blender Conversion option, it allows you to manipulate each Grease Pencil object at each frame separately. 

This script needs to be run manually

How to use the script:

1) Use Blender to convert your video to seprate images (jpg or png) for each frame. Use the standard Blender XXXX.jpg or XXXX.png name convention. 
2) Download and run the blend file from the repository. 
3) Update line 108 in the Blender Python script to define the source folder where the images reside you created in step 1.  
4) Take one image from step 1 and drop it in the Blender viewport and test converting the image to GPencil (Object->Convert->Convert to Grease Pencil) to determine best GPencil conversion settings for your video.
5) Update line 93 in the Python script with the GPencil settings from step 4. If different scenes in your video require different conversion settings you can animate the settings.
6) Check the Blender Camera settings and adjust if necessary.
7) Manually delete test image and test GPencil from scene
8) Open the system console window (Window->Toggle System Console). The script will show the progress while processing the frames in the console.
9) Run script manually. 
10) For each image in the source folder the script will (1) convert the image to a Grease Pencil object, (2) delete the source image, (3)render an image of the GPencel object and (4) delete the GPencil object.
11) Use Blender to render a video of the rendered images created in step 10.    

Here an example of a video i converted to Grease Pencil objects and rendered using this script:
https://www.youtube.com/watch?v=RL4CyCvt6aw

Hope this is useful for someone. Let me know.

The script only doas a basic conversion to GPencil, you could for example, change the script to convert to multiple Grease Pencil objects each with different conversion settings, color them separately and combine them in your renders (using png's and transparency). Unfortunately you then need to know at least the basics of Blender Python.  
