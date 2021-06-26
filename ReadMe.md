Shopne Arcade - A Frontend for GnGeo NeoGeo emulator written in pure Python

Copyright © 2017-2021 Md Imam Hossain <emamhd@gmail.com> 

This program uses:

Python TkInter for the graphical user interface 
GnGeo for emulating Neo Geo system on Linux PC (gngeo_bin binary file and gngeo_data.zip need to be placed inside the gngeo subfolder of Shopne Arcade folder)

To install TKInter on Ubuntu run the following command into the terminal emulator:

sudo apt-get install python3-tk
    
Shopne Arcade is a front-end application designed to easily play Neo Geo system games on PC. It's interface is compatible for screens with low resolution such as 640x480 pixels. It lets users play Neo Geo system games from one interface where users will be able pick different game play experience settings such as Neo Geo games video resolutions, audio sampling rates, etc. Shopne Arcade is composed of pure Python language without any external dependencies making it portable across various Linux Distributions.

Neo Geo system emulation and front-end features:

- Playing games in fullscreen mode
- Automatically adjusting video frame rates
- Interpolation between frames
- Using GPU memory for performance
- Synchronising video with monitor refresh rate
- Video scaling
- Video effects
- Selecting of rendering engine (Choose YUV for native like graphics and arbitrary window scaling using window handles)
- Emulating audio in different sampling rates
- Full controller configuration for keyboard and gamepads
- Support for different Neo Geo region BIOS
- Save and Load games states (state files are saved in the directory .gngeo inside users home folder)
- Showing games cover arts (double click into the game list)
- Adding multiple game roms files locations
- Saving all settings

![Main window](screenshot/mw.png)
![Graphics settings](screenshot/gr.png)
![Controller settings](screenshot/con.png)
![Sound settings](screenshot/sound.png)
![BIOS settings](screenshot/bi.png)

To be able to play Neo Geo games using Shopne Arcade you need a valid Neo Geo BIOS file where the file should be put in the Neo Geo games rom files.

To launch Shopne Arcade, simply run Shopne.py file.

You can find Shopne Arcade bundled with gngeo binary packages from the following site:

https://shopnearcade.blogspot.com/
