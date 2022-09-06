import bpy
import random
from math import pi
import os

IMAGE_COUNT = 1000

IMAGE_FOLDER = '//images/'

LABEL_FILE = '//labels.txt'

cam = bpy.data.objects['Camera']
empty = bpy.data.objects['Empty']

os.system(f"rm -rf {bpy.path.abspath(IMAGE_FOLDER)} {bpy.path.abspath(LABEL_FILE)}")

with open(bpy.path.abspath(LABEL_FILE), 'a') as f:

    for i in range(IMAGE_COUNT):
        focal_length = random.randint(10, 120)
        f.write(f"{focal_length}\n")

        cam.data.lens = focal_length
        cam.location.z = 0.1 * focal_length + 1

        # rotate the empty around the cube
        empty.rotation_euler.x = pi / 4#random.uniform(0, 2 * pi)
        empty.rotation_euler.y = 0 #random.uniform(0, 2 * pi)
        empty.rotation_euler.z = pi / 4 #random.uniform(0, 2 * pi)

        # render this iteration
        bpy.context.scene.render.filepath = f'{IMAGE_FOLDER}/{i}.png'
        bpy.ops.render.render( write_still=True )