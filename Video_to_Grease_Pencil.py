import bpy
import os

"""Process images"""
def imageLoad(imgpath, fp):
    files = os.listdir(imgpath)
    scene = bpy.context.scene
    # get existing output path
    #Get the names of the files in the provided folder
    for x in range(len(files)):
        bpy.ops.object.select_all(action='DESELECT')
        imagename = files[x][0:4]
        print (imagename)
        if files[x].endswith('.jpg') or files[x].endswith('.png'):
            print(files[x])
            empty = bpy.data.objects.new('image.' + imagename, None)
            scene.collection.objects.link(empty)
            empty.location = (0,0,0)
            empty.empty_display_type = 'IMAGE'
            img = bpy.data.images.load(imgpath + files[x])
            empty.data = img
            # Link light object to the active collection of current view layer so that it'll appear in the current scene.

            #trace image to grease pencil
            trace_image(imagename, empty)
            #rename GPencil
            rename_GPencil(imagename)
            
            #for debugging purposes
#            if imagename == '0002':
#                return
            
            #delete empty object
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects['image.' + imagename].select_set(True)
            bpy.ops.object.delete()
                    
            #render image
            render_single_frame(imagename, fp)
            
            #delete grease pencil object
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects['gpencil.' + imagename].select_set(True)
            bpy.ops.object.delete()
            
            #for debugging purposes            
#            if imagename == '0002':
#                return

            

"""Delete empty objects"""
def delete_empties():    
    bpy.ops.object.select_all(action='DESELECT')
    # select all grease pencil objects 
    for ob in bpy.context.scene.objects:              
        if ob.type == 'EMPTY' and ob.name.startswith("image."):
            #Select the object
            ob.select_set(state=True)     
    #Delete all objects selected above 
    bpy.ops.object.delete()
    
"""Delete grease pencil objects"""
def delete_gpencils():    
    bpy.ops.object.select_all(action='DESELECT')
    # select all grease pencil objects 
    for ob in bpy.context.scene.objects:              
        if ob.type == 'GPENCIL' and ob.name.startswith("gpencil."):
            #Select the object
            ob.select_set(state=True)     
    #Delete all objects selected above 
    bpy.ops.object.delete()

"""render frame"""
def render_single_frame(frame, fp):
    scene = bpy.context.scene
    # set current frame
    scene.frame_set(int(frame))
    # set output path so render won't get overwritten
    scene.render.filepath = fp + frame    
    #render the frame
    bpy.ops.render.render(write_still=True) # render still
    #reset filepath
    scene.render.filepath = fp

"""trace selected image to grease pencil"""
def trace_image(frame, empty):
    print("trace." + frame)
    #make empty active and select
    bpy.context.view_layer.objects.active = empty
    empty.select_set(state=True)
    
    bpy.ops.gpencil.trace_image(target='NEW', thickness=1, resolution=5, scale=0.97, sample=0.0, threshold=0.502, turnpolicy='MINORITY', mode='SINGLE')

"""rename grease pencel object"""
def rename_GPencil(frame):    
    bpy.context.view_layer.objects.active = bpy.data.objects['GPencil']
    bpy.data.objects["image." + frame].select_set(False)
    bpy.data.objects["GPencil"].select_set(True)
    bpy.context.view_layer.objects.active
    bpy.context.object.name = ('gpencil.' + frame)

# check for empty & grease pencil objects added in previous run of this script and delete them
delete_empties()
delete_gpencils()

# set path where source images reside 
imgpathfull = "C:/tmp/"    

#Get path where rendered images will be written
scene = bpy.context.scene
fp = scene.render.filepath

#load images, create empties, convert to GP and render each image 
imageLoad(imgpathfull, fp)