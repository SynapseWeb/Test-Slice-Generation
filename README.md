# Test-Slice-Generation
This project contains description and code for generating test slices from known 3D objects. 

## Procedure:

Start with any water-tight outward-normal object in Blender.

Save the file as a new ".blend" file because the script will change the object.

Select the object that you want, set the number of slices (at the top of
the script), and run the script. It will evenly divide the object, but it will
bring in the end slices just a bit so you don't end up with points on the
ends. That's not exactly right, so adjust as needed if you're using it for
important data.

The script will have generated the slices (Plane, Plane.001, Plane.002 ...).
You can now hide the original object and look at the slices.

The trick now is to make images from those slices. I originally did this by
hand, but Tom showed me a "key framing" trick that can help (a little).

Set the number of frames to match your number of slices.
Set the time-line time to the beginning (usually frame 1 or 0).

Select all objects (a), and hide them (h).

Insert a keyframe for the visibility of each "Plane..." object as follows:

        Right click on the "eye" for each plane object (in the outliner).
        From the popup menu select "Insert Keyframe".

That will set the initial state of all objects to be hidden. Now we need
to "unhide" each one at the proper time and then hide it again on the
next frame.

Start by left-clicking the "eye" for the first "Plane" to make it visible.
Then right click the same "eye" and select "Replace Keyframe". Then
you're going to repeat the following steps as you move down all the
"Plane.xxx" objects:

        1. Move to the next time frame (mouse or arrow on Current Frame).
        2. Hide the Plane that's visible (left click the "eye" in outliner).
        3. Right click that same "eye" and select "Insert Keyframe".
        4. Left click the following "eye" to make it visible.
        5. Right click that same (following) "eye" and select "Insert Keyframe".

Repeat steps 1-5 advancing to the next "Plane..." object each time.

The pattern (that you'll repeat many times) will become:

        - Advance Time
        - Left Click Visible Eye (to hide it)
        - Right Click / Insert Keyframe
        - Left Click Next (hidden) Eye (to show it)
        - Right Click / Insert Keyframe

When you're done, you should be able to drag along the time line
and watch each slice appear and disappear (one at a time). Once
you've got that, you're ready to make the pictures. It helps to view
the original object to get the centering and zooming right. You want
to be looking down from the top (View/Top) in "Ortho" mode
(View/ViewPersp/Ortho). Then set the zoom and centering to show
the entire object as you'd like it to appear in the images. You can set
your Render properties for the "X" and "Y" dimensions of your final
images. This is a good time to use the "OpenGL render" button to
see what it will look like (escape to return to normal 3D view).

When you've got the object properly framed, you will want to hide
the original object (otherwise it will obscure your slices).

Now it's time to make the images. Check the "Output" section of
your "Render" panel to see where the images will go. Change as
needed. Then click the "OpenGL render active viewport" button
(below the 3D view), and Blender should make a PNG file for each
frame (named 0001.png, 0002.png ... ). They'll be in the location
that you selected earlier.

Here's what it looks like for a scene made up of a cone, a torus, and an icosphere:

![Animation](docs/Cone_Ico_Torus_Animation.gif?raw=true "Slices through combined objects")

# Other related projects:

        - https://github.com/SynapseWeb/Mystery-Object
        - https://github.com/SynapseWeb/Mystery-Object-2
        - https://github.com/KotaAzul/Mystery-Series
