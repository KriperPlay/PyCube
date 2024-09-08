
# ▒█▀▀█ ▒█░░▒█ ▒█▀▀█ ▒█░▒█ ▒█▀▀█ ▒█▀▀▀ 　 ▒█▀▀█ ▒█░░▒█ 　 ▄▀▀▄ ▒█▀▀▀█ ▒█▀▀▀ ▒█▀▀▀ 
# ▒█▄▄█ ▒█▄▄▄█ ▒█░░░ ▒█░▒█ ▒█▀▀▄ ▒█▀▀▀ 　 ▒█▀▀▄ ▒█▄▄▄█ 　 ▀▄▄█ ▒█░░▒█ ▒█▀▀▀ ▒█▀▀▀ 
# ▒█░░░ ░░▒█░░ ▒█▄▄█ ░▀▄▄▀ ▒█▄▄█ ▒█▄▄▄ 　 ▒█▄▄█ ░░▒█░░ 　 ░▄▄▀ ▒█▄▄▄█ ▒█░░░ ▒█░░░

from ursina import *
import sys
from ursina.prefabs.first_person_controller import FirstPersonController 
import json

try:
    file1 = open(sys.argv[2], 'r')
except FileNotFoundError:
    print("File not found")

with open("settings.json", 'r') as f:
    settings = json.load(f)

Mode_player = sys.argv[1]
current_block = "grass"
fly = False

if ".pycube" not in sys.argv[2]:
    print("File must be .pycube")
    exit(0)
else:
    pass

def minus_plus(a,b):
    if int(a) > 0:
        return b
    else:
        return -1 * b

class Voxel(Button):
   def __init__(self, texture,position=(0, 0, 0)):
       super().__init__(parent=scene, model='cube', 
           scale=1, texture=texture, position=position,
           color = color.color(0,0,random.uniform(0.9,1))
           )
   
   def input(self, key):
       global current_block
       if key == "1":
           current_block = settings["slot1"]
       elif key == "2":
           current_block = settings["slot2"]
       elif key == "3":
           current_block = settings["slot3"]
       elif key == "4":
           current_block = settings["slot4"]
       elif key == "5":
           current_block = settings["slot5"]
       elif key == "6":
           current_block = settings["slot6"]
       elif key == "7":
           current_block = settings["slot7"]

       if self.hovered:
           if key == 'right mouse down':
               Voxel(position=self.position + mouse.normal, texture=current_block)

           if key == 'left mouse down':
               destroy(self)


def input(key):
  if key == 'escape':
    quit()

def create_platform(line):
    x1 = 16
    z1 = 16
    s_open = line.strip().find('{')
    s_close = line.strip().find('}')
    separator = line[s_open:s_close].strip().find('x')
    y0 = line[s_open:s_close].find('y')
    x1 = line[s_open+1:separator+s_open]
    z1 = line[separator+s_open+1:s_open+y0]
    y = int(line[s_open+y0+1:s_close])
    texture1 = line[0:s_open-1].strip()

    for x in range(abs(int(x1))): 
        for z in range(abs(int(z1))):
            if Mode_player == "camera-mode":
                Entity(model='cube', texture=texture1, scale=1, collider='box',
                        position=Vec3((minus_plus(x1,x),y,minus_plus(z1,z)))
                )
            elif Mode_player == "player-mode":
                Voxel(texture1, position=(minus_plus(x1,x),y,minus_plus(z1,z)))


def create_block(line):
    s_open = line.find('[')
    s_close = line.find(']')
    x0 =  line[s_open:s_close].find('x')
    y0 = line[s_open:s_close].find('y')
    z0 = line[s_open:s_close].find('z')
    x = int(line[s_open+x0+1:s_open+y0])
    y = int(line[s_open+y0+1:s_open+z0])
    z = int(line[s_open+z0+1:s_close])

    texture1 = line[0:s_open-1].strip()

    if Mode_player == "camera-mode":
        Entity(model='cube', texture=texture1, scale=1, collider='box',
                position=Vec3(x,y,z)
        )
    elif Mode_player == "player-mode":
        Voxel(texture1, position=(x,y,z))

if __name__ == "__main__":
    app = Ursina(asset_folder="textures/", title="PyCube")

    # Sky(texture="sky_default")
    skybox = Sky(model = "sphere", double_sided = True, texture = "sky", rotation = (0, 90, 0))

    for line in file1:
        if line.find('[') != -1 and line.strip().find('{') == -1:
            create_block(line)
        else:
            create_platform(line)

    if Mode_player == "camera-mode":
        EditorCamera() 
        camera.fov = settings["camera-mode_fov"]
    elif Mode_player == "player-mode":
        player = FirstPersonController()
        player.scale = 0.9
        camera.fov = settings["player-mode_fov"]

        def input(key):
            global fly

            if key == "f":
                player.gravity = 0
                fly = True
            if key == "g":
                player.gravity = 1
                fly = False
            if key == "q":
                if fly:
                    player.y -= 1
            if key == "e":
                if fly:
                    player.y += 1
            if key == 'escape':
                quit()

    app.run()
