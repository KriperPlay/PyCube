# PyCube

![logo](https://github.com/user-attachments/assets/84f75835-c0b9-419c-9aa1-70ed93e52619)

# LICENSE
Check LICENSE file

# About
PyCube - voxel game and world editor
(not minecraft copy)

# Need to install
* python3 and pip
* ursina engine

# How to use
'esc' - exit of game

HOW TO RUN
* ```bash
    git clone https://github.com/KriperPlay/PyCube/
    cd PyCube
    python3 main.py [mode] [file.pycube]
    ```
  
MODES
* player-mode
* * ```python3 main.py player-mode file.pycube```
  * a like minecraft creative-mode
  * 'wasd' - defolt control
  * 'space' - jump
  * 'f' - onn fly-mode
  * 'g' - off fly-mode
  * 'q' - down (fly-mode)
  * 'e' - up (fly-mode)
  * 'right click' - place block
  * 'left click' - destroy block
  * '`1-7' - choose a block for placed (configure blocks locations can in 'setting.json')
* camera-mode
* * ```python3 main.py camera-mode file.pycube```
  * you can look around the world.

HOW TO CREATE WORLD IN FILES
(the block name is the texture name without extension, check paragraph 'BLOCKS LIST')
* place platform
* * block_name{0x0y}
  * 0 and 0 - size a platform
  * y - platform location in y
* place a block
* * block_name[x0y0z0]
  * here you indicate the coordinates of the block

BLOCKS LIST
* all blocks in dir 'textures'
* once you add a texture to this folder, it will be immediately ready to use

CONFIG
* config - 'setting.json'
* in config you can configure a blocks locations for '1-7' for placed their in player-mode and configure FOV for player-mode and camera-mode
* ```json
  {
    "camera-mode_fov": 60,
    "player-mode_fov": 90,
    "slot1": "grass",
    "slot2": "brick",
    "slot3": "wood",
    "slot4": "glass",
    "slot5": "water",
    "slot6": "lava",
    "slot7": "stone"
  }
  ```

# SCREENSHOTS
* # player-mode
* * ![изображение](https://github.com/user-attachments/assets/36fd2f68-957e-4968-be4f-2a5e64dff075)
* # camera-mode
* * ![изображение](https://github.com/user-attachments/assets/38f34372-f64d-409d-80a6-b2cdeff7e33c)
  * ![изображение](https://github.com/user-attachments/assets/9ca1c714-0315-4fcc-97ca-93a4f2da4d5d)

