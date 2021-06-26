# Copyright (c) 2017-2021, Md Imam Hossain (emamhd at gmail dot com)
# see LICENSE.txt for details

from functools import partial
import os
import json
import tkinter
from roms import Roms
from roms_directory_selection_dialog import FoldersSelectionWindow
from engine import GnGeo
from engine import GNGEO_ROMS_LIST
from engine import GNGEO_VIDEO_SCALINGS
from engine import GNGEO_VIDEO_EFFECTS
from engine import GNGEO_BLITTERS
from engine import GNGEO_AUDIO_SAMPLE_RATES
from engine import GNGEO_CONTROLLERS
from engine import GNGEO_KEYBOARD_KEYCODES
from engine import GNGEO_GAMEPAD1_KEYCODES
from engine import GNGEO_GAMEPAD2_KEYCODES
from engine import GNGEO_GAME_COUNTRIES

class ShopneVariables():

    def __init__(self):

        self.game_country_selection = None
        self.fullscreen_ckeck_button_state = None
        self.autoframeskip_ckeck_button_state = None
        self.interpolation_ckeck_button_state = None
        self.hwsurface_ckeck_button_state = None
        self.vsync_ckeck_button_state = None
        self.video_scaling_combobox_selection = None
        self.video_effects_combobox_selection = None
        self.video_renderer_combobox_selection = None
        self.sound_ckeck_button_state = None
        self.audio_sampling_combobox_selection = None
        self.button_names = None
        self.player1_controller_selection = None
        self.player1_controller_selection_current = None
        self.player1_button_selections = None
        self.player1_keyboard_buttons = None
        self.player1_gamepad1_buttons = None
        self.player1_gamepad2_buttons = None
        self.player2_controller_selection = None
        self.player2_controller_selection_current = None
        self.player2_button_selections = None
        self.player2_keyboard_buttons = None
        self.player2_gamepad1_buttons = None
        self.player2_gamepad2_buttons = None
        self.main_window_status_label = None
        self.currrent_roms_directory_location = None
        self.shopne_arcade_version = None
        self.shopne_arcade_description = None
        self.shopne_arcade_copyright = None
        self.shopne_arcade_home_pade = None
        self.shopne_arcade_email = None
        self.shopne_arcade_licence = None

    def initialise(self):

        self.game_country_selection = tkinter.StringVar()
        self.fullscreen_ckeck_button_state = tkinter.IntVar()
        self.autoframeskip_ckeck_button_state = tkinter.IntVar()
        self.interpolation_ckeck_button_state = tkinter.IntVar()
        self.hwsurface_ckeck_button_state = tkinter.IntVar()
        self.vsync_ckeck_button_state = tkinter.IntVar()
        self.video_scaling_combobox_selection = tkinter.StringVar()
        self.video_effects_combobox_selection = tkinter.StringVar()
        self.video_renderer_combobox_selection = tkinter.StringVar()
        self.sound_ckeck_button_state = tkinter.IntVar()
        self.audio_sampling_combobox_selection = tkinter.StringVar()
        self.button_names = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'LEFT', 5: 'RIGHT', 6: 'UP', 7: 'DOWN', 8: 'START', 9: 'COIN'}
        self.player1_controller_selection = tkinter.StringVar()
        self.player1_controller_selection_current = tkinter.StringVar()
        self.player1_keyboard_buttons = {}
        self.player1_gamepad1_buttons = {}
        self.player1_gamepad2_buttons = {}
        self.player1_button_selections = []
        for i in range(len(self.button_names)):
            self.player1_button_selections.append(tkinter.StringVar())
        self.player2_controller_selection = tkinter.StringVar()
        self.player2_controller_selection_current = tkinter.StringVar()
        self.player2_keyboard_buttons = {}
        self.player2_gamepad1_buttons = {}
        self.player2_gamepad2_buttons = {}
        self.player2_button_selections = []
        for i in range(len(self.button_names)):
            self.player2_button_selections.append(tkinter.StringVar())
        self.main_window_status_label = tkinter.StringVar()
        self.currrent_roms_directory_location = tkinter.StringVar()
        self.shopne_arcade_version = 1.9
        self.shopne_arcade_description = 'A frontend for GnGeo emulator written purely in Python'
        self.shopne_arcade_email = 'emamhd@gmail.com'
        self.shopne_arcade_copyright = 'Md Imam Hossain ' + '<' + self.shopne_arcade_email + '>'
        self.shopne_arcade_licence = 'This program comes with absolutely no warranty.'

class GngeoEngineData():

    def __init__(self):

        self.audio_configuration = {}
        self.graphics_configuration = {}
        self.controller_configuration = {}
        self.roms_directories = {}
        self.game_options = {}

def roms_directory_open_button_callback(window, dir_list_widget, folder_selection):

    global roms, shopne_variables

    directory_path = folder_selection.listing_directory.location

    if not len(directory_path) == 0:
        roms.add_directory(directory_path)
        shopne_variables.currrent_roms_directory_location.set(directory_path)

    dir_list_widget.delete(0, tkinter.END)

    for directory in roms.directories:
        dir_list_widget.insert(tkinter.END, directory)

    window.destroy()

def add_directory_button_callback(window, dir_list_widget):

    global shopne_variables

    window_background_color = '#171718'
    window_foreground_color = '#FFFFFF'
    window_button_background_color = '#B17513'
    window_button_focus_background_color = '#B18C50'
    window_button_foreground_color = '#171718'

    rom_directories_selection_dialog_window = tkinter.Toplevel(window)
    rom_directories_selection_dialog_window.title("Select games location")
    rom_directories_selection_dialog_window.geometry('%dx%d+%d+%d' % (460, 420, window.winfo_x() + ((window.winfo_width() / 2) - (460 / 2)), window.winfo_y() + ((window.winfo_height() / 2) - (420 / 2))))

    rom_directories_selection_dialog_frame = tkinter.Frame(rom_directories_selection_dialog_window, padx=10, pady=5, background=window_background_color)
    rom_directories_selection_dialog_frame.pack_propagate(False)
    rom_directories_selection_dialog_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE)

    folder_selection = FoldersSelectionWindow(rom_directories_selection_dialog_frame, shopne_variables.currrent_roms_directory_location.get(), './data/folder_icon.gif', window_background_color=window_background_color, window_foreground_color=window_foreground_color, window_button_background_color=window_button_background_color, window_button_focus_background_color=window_button_focus_background_color, window_button_foreground_color=window_button_foreground_color)

    folder_selection.folders_selection_window_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, side=tkinter.TOP)

    open_button = tkinter.Button(rom_directories_selection_dialog_frame, font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color, text="Add current folder location", command=lambda: roms_directory_open_button_callback(rom_directories_selection_dialog_window, dir_list_widget, folder_selection))
    open_button.pack(fill=tkinter.X, side=tkinter.TOP)

    rom_directories_selection_dialog_window.grab_set()
    window.wait_window(rom_directories_selection_dialog_window)

def remove_directory_button_callback(dir_list_widget):

    global roms

    selection = dir_list_widget.curselection()

    if not len(selection) == 0:
        roms.remove_directory(dir_list_widget.get(selection[0]))
        dir_list_widget.delete(selection[0])

def rom_directories_selection_button_callback(window, game_list_widget):

    global roms, shopne_variables

    window_background_color = '#171718'
    window_foreground_color = '#FFFFFF'
    window_button_background_color = '#B17513'
    window_button_focus_background_color = '#B18C50'
    window_button_foreground_color = '#171718'

    rom_directories_selection_window = tkinter.Toplevel(window)
    rom_directories_selection_window.title("Games locations")
    rom_directories_selection_window.geometry('%dx%d+%d+%d' % (400, 420, window.winfo_x() + ((window.winfo_width() / 2) - (400 / 2)), window.winfo_y() + ((window.winfo_height() / 2) - (420 / 2))))

    rom_directories_selection_frame = tkinter.Frame(rom_directories_selection_window, padx=10, pady=10, background=window_background_color)
    rom_directories_selection_frame.pack_propagate(False)
    rom_directories_selection_frame.pack(fill=tkinter.BOTH, expand=1)

    rom_directories_window = tkinter.LabelFrame(rom_directories_selection_frame, foreground=window_foreground_color, background=window_background_color, text="Game rom files locations", font=(None, 12), relief=tkinter.FLAT)
    rom_directories_window.pack(fill=tkinter.BOTH, expand=1, side=tkinter.TOP)

    directories_list = tkinter.Listbox(rom_directories_window, relief=tkinter.FLAT, highlightcolor='#DFDFDF', highlightthickness=2, font=(None, 12))
    directories_list.focus()
    for directory in roms.directories:
        directories_list.insert(tkinter.END, directory)
    directories_list.pack(fill=tkinter.BOTH, expand=1, padx=5, pady=10)

    add_directory_button = tkinter.Button(rom_directories_selection_frame, font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color, text="Add games location", command=lambda: add_directory_button_callback(rom_directories_selection_window, directories_list))
    add_directory_button.pack(fill=tkinter.X, side=tkinter.TOP)

    remove_directory_button = tkinter.Button(rom_directories_selection_frame, font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color, text="Remove selected location", command=lambda: remove_directory_button_callback(directories_list))
    remove_directory_button.pack(fill=tkinter.X, side=tkinter.TOP)

    rom_directories_selection_window.grab_set()
    window.wait_window(rom_directories_selection_window)

    roms.update_roms()

    game_list_widget.delete(0, tkinter.END)

    for rom in roms.roms:
        game_list_widget.insert(tkinter.END, GNGEO_ROMS_LIST[rom])

    number_of_roms = game_list_widget.size()

    if number_of_roms == 0:
        shopne_variables.main_window_status_label.set('No games in the library')
        window.after(5000, lambda: shopne_variables.main_window_status_label.set('Click Game files locations to add games to library'))
    elif number_of_roms == 1:
        shopne_variables.main_window_status_label.set(str(game_list_widget.size()) + ' game in the library')
        window.after(10000, lambda: shopne_variables.main_window_status_label.set('Select the game from Games and click Load game'+"\nDouble click on the game to see the cover art"))
    else:
        shopne_variables.main_window_status_label.set(str(game_list_widget.size()) +' games in the library')
        window.after(10000, lambda: shopne_variables.main_window_status_label.set('Select a game from Games and click Load game'+"\nDouble click on the game to see the cover art"))

def graphics_default_settings_callback():

    global shopne_variables

    shopne_variables.fullscreen_ckeck_button_state.set(0)
    shopne_variables.autoframeskip_ckeck_button_state.set(1)
    shopne_variables.interpolation_ckeck_button_state.set(1)
    shopne_variables.hwsurface_ckeck_button_state.set(1)
    shopne_variables.vsync_ckeck_button_state.set(1)
    shopne_variables.video_scaling_combobox_selection.set(GNGEO_VIDEO_SCALINGS[0])
    shopne_variables.video_effects_combobox_selection.set(GNGEO_VIDEO_EFFECTS[1])
    shopne_variables.video_renderer_combobox_selection.set(GNGEO_BLITTERS[1])

def video_renderer_combobox_selection_callback (video_effects_combobox_widget, *args):

    global shopne_variables

    if shopne_variables.video_renderer_combobox_selection.get() == GNGEO_BLITTERS[2]:
        video_effects_combobox_widget.config(state=tkinter.DISABLED)
        shopne_variables.video_effects_combobox_selection.set(GNGEO_VIDEO_EFFECTS[9])
    else:
        video_effects_combobox_widget.config(state=tkinter.NORMAL)

def video_effects_combobox_selection_callback (video_scaling_combobox_widget, *args):

    global shopne_variables

    if shopne_variables.video_effects_combobox_selection.get() == GNGEO_VIDEO_EFFECTS[9]:
        video_scaling_combobox_widget.config(state=tkinter.NORMAL)
    else:
        shopne_variables.video_scaling_combobox_selection.set(GNGEO_VIDEO_SCALINGS[0])
        video_scaling_combobox_widget.config(state=tkinter.DISABLED)

def graphics_options_button_callback(window):

    global gngeo_engine, shopne_variables

    window_background_color = '#171718'
    window_foreground_color = '#FFFFFF'
    window_button_background_color = '#B17513'
    window_button_focus_background_color = '#B18C50'
    window_button_foreground_color = '#171718'

    graphics_options_window = tkinter.Toplevel(window)
    graphics_options_window.title("Graphics options")
    graphics_options_window.geometry('%dx%d+%d+%d' % (400, 300, window.winfo_x() + ((window.winfo_width() / 2) - (400 / 2)), window.winfo_y() + ((window.winfo_height() / 2) - (300 / 2))))

    graphics_options_frame = tkinter.Frame(graphics_options_window, padx=10, pady=5, background=window_background_color)
    graphics_options_frame.pack_propagate(False)
    graphics_options_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, anchor=tkinter.NW)

    fullscreen_ckeck_button = tkinter.Checkbutton(graphics_options_frame, font=(None, 10), selectcolor=window_background_color, foreground=window_foreground_color, activeforeground=window_foreground_color, background=window_background_color, highlightbackground=window_background_color, activebackground=window_background_color,text="  Run game in fullscreen mode", variable=shopne_variables.fullscreen_ckeck_button_state)
    fullscreen_ckeck_button.pack(fill=tkinter.Y, expand=tkinter.TRUE, anchor=tkinter.NW)

    autoframeskip_ckeck_button = tkinter.Checkbutton(graphics_options_frame, font=(None, 10), selectcolor=window_background_color, foreground=window_foreground_color, activeforeground=window_foreground_color, background=window_background_color, highlightbackground=window_background_color, activebackground=window_background_color, text="  Automatically adjust graphics performance", variable=shopne_variables.autoframeskip_ckeck_button_state)
    autoframeskip_ckeck_button.pack(fill=tkinter.Y, expand=tkinter.TRUE, anchor=tkinter.NW)

    interpolation_ckeck_button = tkinter.Checkbutton(graphics_options_frame, font=(None, 10), selectcolor=window_background_color, foreground=window_foreground_color, activeforeground=window_foreground_color, background=window_background_color, highlightbackground=window_background_color, activebackground=window_background_color, text="  Improve graphics animations", variable=shopne_variables.interpolation_ckeck_button_state)
    interpolation_ckeck_button.pack(fill=tkinter.Y, expand=tkinter.TRUE, anchor=tkinter.NW)

    hwsurface_ckeck_button = tkinter.Checkbutton(graphics_options_frame, font=(None, 10), selectcolor=window_background_color, foreground=window_foreground_color, activeforeground=window_foreground_color, background=window_background_color, highlightbackground=window_background_color, activebackground=window_background_color, text="  Use graphics card memory", variable=shopne_variables.hwsurface_ckeck_button_state)
    hwsurface_ckeck_button.pack(fill=tkinter.Y, expand=tkinter.TRUE, anchor=tkinter.NW)

    vsync_ckeck_button = tkinter.Checkbutton(graphics_options_frame, font=(None, 10), selectcolor=window_background_color, foreground=window_foreground_color, activeforeground=window_foreground_color, background=window_background_color, highlightbackground=window_background_color, activebackground=window_background_color, text="  Synchronise video with the screen", variable=shopne_variables.vsync_ckeck_button_state)
    vsync_ckeck_button.pack(fill=tkinter.Y, expand=tkinter.TRUE, anchor=tkinter.NW)

    video_scaling_frame = tkinter.Frame(graphics_options_frame, background=window_background_color)
    video_scaling_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, anchor=tkinter.NW)

    video_scaling_label = tkinter.Label(video_scaling_frame, font=(None, 10), background=window_background_color, foreground=window_foreground_color, text="Video scaling")
    video_scaling_label.pack(side=tkinter.LEFT, padx=20, pady=10)

    video_scaling_combobox = tkinter.OptionMenu(video_scaling_frame, shopne_variables.video_scaling_combobox_selection, *GNGEO_VIDEO_SCALINGS)
    video_scaling_combobox.config(font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color)
    video_scaling_combobox["menu"].config(background=window_background_color, foreground=window_foreground_color)
    video_scaling_combobox.pack(side=tkinter.RIGHT)

    video_effects_frame = tkinter.Frame(graphics_options_frame, background=window_background_color)
    video_effects_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, anchor=tkinter.NW)

    video_effects_label = tkinter.Label(video_effects_frame, font=(None, 10), background=window_background_color, foreground=window_foreground_color, text="Video effect")
    video_effects_label.pack(side=tkinter.LEFT, padx=20, pady=10)

    video_effects_combobox_selection_callback_id = None

    video_effects_combobox = tkinter.OptionMenu(video_effects_frame, shopne_variables.video_effects_combobox_selection, *GNGEO_VIDEO_EFFECTS)
    video_effects_combobox.config(font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color)
    video_effects_combobox["menu"].config(background=window_background_color, foreground=window_foreground_color)
    video_effects_combobox.pack(side=tkinter.RIGHT)

    video_effects_combobox_selection_callback_id = shopne_variables.video_effects_combobox_selection.trace('w', lambda a, b, c, d=video_scaling_combobox: video_effects_combobox_selection_callback(d, a, b, c))
    video_effects_combobox_selection_callback(video_scaling_combobox, None, None, None)

    video_renderer_frame = tkinter.Frame(graphics_options_frame, background=window_background_color)
    video_renderer_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, anchor=tkinter.NW)

    video_renderer_label = tkinter.Label(video_renderer_frame, font=(None, 10), background=window_background_color, foreground=window_foreground_color, text="Video engine")
    video_renderer_label.pack(side=tkinter.LEFT, padx=20, pady=10)

    video_renderer_combobox_callback_id = None

    video_renderer_combobox = tkinter.OptionMenu(video_renderer_frame, shopne_variables.video_renderer_combobox_selection, *GNGEO_BLITTERS)
    video_renderer_combobox.config(font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color)
    video_renderer_combobox["menu"].config(background=window_background_color, foreground=window_foreground_color)
    video_renderer_combobox.pack(side=tkinter.RIGHT)

    video_renderer_combobox_callback_id = shopne_variables.video_renderer_combobox_selection.trace('w', lambda a, b, c, d=video_effects_combobox: video_renderer_combobox_selection_callback(d, a, b, c))
    video_renderer_combobox_selection_callback(video_effects_combobox, None, None, None)

    default_button = tkinter.Button(graphics_options_frame, font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color, text="Restore to default settings", command=graphics_default_settings_callback)
    default_button.pack(fill=tkinter.X, expand=tkinter.TRUE, side=tkinter.BOTTOM)

    graphics_options_window.grab_set()
    window.wait_window(graphics_options_window)

    if not video_renderer_combobox_callback_id == None:
        shopne_variables.video_renderer_combobox_selection.trace_vdelete('w', video_renderer_combobox_callback_id)

    if not video_effects_combobox_selection_callback_id == None:
        shopne_variables.video_effects_combobox_selection.trace_vdelete('w', video_effects_combobox_selection_callback_id)

    if shopne_variables.fullscreen_ckeck_button_state.get() == 0:
        gngeo_engine.fullscreen = False
    else:
        gngeo_engine.fullscreen = True

    if shopne_variables.autoframeskip_ckeck_button_state.get() == 0:
        gngeo_engine.autoframeskip = False
    else:
        gngeo_engine.autoframeskip = True

    if shopne_variables.interpolation_ckeck_button_state.get() == 0:
        gngeo_engine.interpolation = False
    else:
        gngeo_engine.interpolation = True

    if shopne_variables.hwsurface_ckeck_button_state.get() == 0:
        gngeo_engine.hwsurface = False
    else:
        gngeo_engine.hwsurface = True

    if shopne_variables.vsync_ckeck_button_state.get() == 0:
        gngeo_engine.vsync = False
    else:
        gngeo_engine.vsync = True

    gngeo_engine.scale = shopne_variables.video_scaling_combobox_selection.get()
    gngeo_engine.effect = shopne_variables.video_effects_combobox_selection.get()
    gngeo_engine.blitter = shopne_variables.video_renderer_combobox_selection.get()

def sound_options_button_callback(window):

    global gngeo_engine, shopne_variables

    window_background_color = '#171718'
    window_foreground_color = '#FFFFFF'
    window_button_background_color = '#B17513'
    window_button_focus_background_color = '#B18C50'
    window_button_foreground_color = '#171718'

    sound_options_window = tkinter.Toplevel(window)
    sound_options_window.title("Sound options")
    sound_options_window.geometry('%dx%d+%d+%d' % (400, 100, window.winfo_x() + ((window.winfo_width() / 2) - (400 / 2)), window.winfo_y() + ((window.winfo_height() / 2) - (100 / 2))))

    sound_options_frame = tkinter.Frame(sound_options_window, padx=10, pady=5, background=window_background_color)
    sound_options_frame.pack_propagate(False)
    sound_options_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, anchor=tkinter.NW)

    audio_sampling_frame = tkinter.Frame(sound_options_frame, background=window_background_color)
    audio_sampling_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, anchor=tkinter.NW)

    audio_sampling_label = tkinter.Label(audio_sampling_frame, font=(None, 10), background=window_background_color, foreground=window_foreground_color, text="Eumlation audio sampling rate in Hz")
    audio_sampling_label.pack(side=tkinter.LEFT, padx=20, pady=10)

    audio_sampling_combobox = tkinter.OptionMenu(audio_sampling_frame, shopne_variables.audio_sampling_combobox_selection, *GNGEO_AUDIO_SAMPLE_RATES)
    audio_sampling_combobox.config(font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color)
    audio_sampling_combobox["menu"].config(background=window_background_color, foreground=window_foreground_color)
    audio_sampling_combobox.pack(side=tkinter.RIGHT)

    sound_ckeck_button = tkinter.Checkbutton(sound_options_frame, font=(None, 10), selectcolor=window_background_color, foreground=window_foreground_color, activeforeground=window_foreground_color, background=window_background_color, highlightbackground=window_background_color, activebackground=window_background_color, text="  Emulate audio", variable=shopne_variables.sound_ckeck_button_state)
    sound_ckeck_button.pack(fill=tkinter.Y, expand=tkinter.TRUE, anchor=tkinter.NW)

    sound_options_window.grab_set()
    window.wait_window(sound_options_window)

    if shopne_variables.sound_ckeck_button_state.get() == 0:
        gngeo_engine.sound = False
    else:
        gngeo_engine.sound = True

    gngeo_engine.samplerate = shopne_variables.audio_sampling_combobox_selection.get()

def buttons_list_callback(event, window, selection_button):

    index = int(event.widget.curselection()[0])
    value = event.widget.get(index)
    selection_button.set(value)
    window.after(250, lambda: window.destroy())

def button_selection_button_callback(window, player, selection_button):

    global shopne_variables

    button_selection_window = tkinter.Toplevel(window)
    button_selection_window.title("Select key")
    button_selection_window.geometry('%dx%d+%d+%d' % (260, 80, window.winfo_pointerx(), window.winfo_pointery()))
    button_selection_window.overrideredirect(True)

    buttons_list_list = tkinter.Listbox(button_selection_window, relief=tkinter.FLAT, highlightcolor='#E81742', highlightthickness=4, font=(None, 14))
    buttons_list_scrollbar = tkinter.Scrollbar(button_selection_window, orient=tkinter.VERTICAL)
    buttons_list_scrollbar.config(command=buttons_list_list.yview)
    buttons_list_scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    buttons_list_list.config(yscrollcommand=buttons_list_scrollbar.set)

    buttons_list_list.bind('<<ListboxSelect>>', lambda event: buttons_list_callback(event, button_selection_window, selection_button))

    if player == 1:

        if shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[0]:
            for key in keyboard_keys:
                buttons_list_list.insert(tkinter.END, key)
        elif shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[1]:
            for gamepad_button in gamepad1_buttons:
                buttons_list_list.insert(tkinter.END, gamepad_button)
        elif shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[2]:
            for gamepad_button in gamepad2_buttons:
                buttons_list_list.insert(tkinter.END, gamepad_button)

    elif player == 2:

        if shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[0]:
            for key in keyboard_keys:
                buttons_list_list.insert(tkinter.END, key)
        elif shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[1]:
            for gamepad_button in gamepad1_buttons:
                buttons_list_list.insert(tkinter.END, gamepad_button)
        elif shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[2]:
            for gamepad_button in gamepad2_buttons:
                buttons_list_list.insert(tkinter.END, gamepad_button)

    buttons_list_list.pack(fill=tkinter.BOTH, expand=tkinter.TRUE)

def controllers_options_window_click_callback(event, window):

    child_windows = window.winfo_children()
    button_popup_window = None

    for window in child_windows:
        if window.winfo_class() == 'Toplevel':
            button_popup_window = window

    if button_popup_window != None:
        button_popup_window.destroy()

def player_default_selection_button_callback(player):

    global shopne_variables

    if player == 1:

        if shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[0]:

            shopne_variables.player1_button_selections[0].set(keyboard_keys[86])
            shopne_variables.player1_button_selections[1].set(keyboard_keys[80])
            shopne_variables.player1_button_selections[2].set(keyboard_keys[34])
            shopne_variables.player1_button_selections[3].set(keyboard_keys[31])
            shopne_variables.player1_button_selections[4].set(keyboard_keys[10])
            shopne_variables.player1_button_selections[5].set(keyboard_keys[21])
            shopne_variables.player1_button_selections[6].set(keyboard_keys[84])
            shopne_variables.player1_button_selections[7].set(keyboard_keys[76])
            shopne_variables.player1_button_selections[8].set(keyboard_keys[1])
            shopne_variables.player1_button_selections[9].set(keyboard_keys[3])

        elif shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[1]:

            shopne_variables.player1_button_selections[0].set(gamepad1_buttons[0])
            shopne_variables.player1_button_selections[1].set(gamepad1_buttons[1])
            shopne_variables.player1_button_selections[2].set(gamepad1_buttons[2])
            shopne_variables.player1_button_selections[3].set(gamepad1_buttons[3])
            shopne_variables.player1_button_selections[4].set(gamepad1_buttons[14])
            shopne_variables.player1_button_selections[5].set(gamepad1_buttons[15])
            shopne_variables.player1_button_selections[6].set(gamepad1_buttons[12])
            shopne_variables.player1_button_selections[7].set(gamepad1_buttons[13])
            shopne_variables.player1_button_selections[8].set(gamepad1_buttons[4])
            shopne_variables.player1_button_selections[9].set(gamepad1_buttons[5])

        elif shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[2]:

            shopne_variables.player1_button_selections[0].set(gamepad2_buttons[0])
            shopne_variables.player1_button_selections[1].set(gamepad2_buttons[1])
            shopne_variables.player1_button_selections[2].set(gamepad2_buttons[2])
            shopne_variables.player1_button_selections[3].set(gamepad2_buttons[3])
            shopne_variables.player1_button_selections[4].set(gamepad2_buttons[14])
            shopne_variables.player1_button_selections[5].set(gamepad2_buttons[15])
            shopne_variables.player1_button_selections[6].set(gamepad2_buttons[12])
            shopne_variables.player1_button_selections[7].set(gamepad2_buttons[13])
            shopne_variables.player1_button_selections[8].set(gamepad2_buttons[4])
            shopne_variables.player1_button_selections[9].set(gamepad2_buttons[5])

    elif player == 2:

        if shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[0]:

            shopne_variables.player2_button_selections[0].set(keyboard_keys[86])
            shopne_variables.player2_button_selections[1].set(keyboard_keys[80])
            shopne_variables.player2_button_selections[2].set(keyboard_keys[34])
            shopne_variables.player2_button_selections[3].set(keyboard_keys[31])
            shopne_variables.player2_button_selections[4].set(keyboard_keys[10])
            shopne_variables.player2_button_selections[5].set(keyboard_keys[21])
            shopne_variables.player2_button_selections[6].set(keyboard_keys[84])
            shopne_variables.player2_button_selections[7].set(keyboard_keys[76])
            shopne_variables.player2_button_selections[8].set(keyboard_keys[1])
            shopne_variables.player2_button_selections[9].set(keyboard_keys[3])

        elif shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[1]:

            shopne_variables.player2_button_selections[0].set(gamepad1_buttons[0])
            shopne_variables.player2_button_selections[1].set(gamepad1_buttons[1])
            shopne_variables.player2_button_selections[2].set(gamepad1_buttons[2])
            shopne_variables.player2_button_selections[3].set(gamepad1_buttons[3])
            shopne_variables.player2_button_selections[4].set(gamepad1_buttons[14])
            shopne_variables.player2_button_selections[5].set(gamepad1_buttons[15])
            shopne_variables.player2_button_selections[6].set(gamepad1_buttons[12])
            shopne_variables.player2_button_selections[7].set(gamepad1_buttons[13])
            shopne_variables.player2_button_selections[8].set(gamepad1_buttons[4])
            shopne_variables.player2_button_selections[9].set(gamepad1_buttons[5])

        elif shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[2]:

            shopne_variables.player2_button_selections[0].set(gamepad2_buttons[0])
            shopne_variables.player2_button_selections[1].set(gamepad2_buttons[1])
            shopne_variables.player2_button_selections[2].set(gamepad2_buttons[2])
            shopne_variables.player2_button_selections[3].set(gamepad2_buttons[3])
            shopne_variables.player2_button_selections[4].set(gamepad2_buttons[14])
            shopne_variables.player2_button_selections[5].set(gamepad2_buttons[15])
            shopne_variables.player2_button_selections[6].set(gamepad2_buttons[12])
            shopne_variables.player2_button_selections[7].set(gamepad2_buttons[13])
            shopne_variables.player2_button_selections[8].set(gamepad2_buttons[4])
            shopne_variables.player2_button_selections[9].set(gamepad2_buttons[5])

def player_controller_combobox_selection_callback (player, *args):

    global shopne_variables

    if player == 1:

        if shopne_variables.player1_controller_selection_current.get() == GNGEO_CONTROLLERS[0]:

            shopne_variables.player1_keyboard_buttons.clear()

            for i in range(len(shopne_variables.button_names)):

                shopne_variables.player1_keyboard_buttons[shopne_variables.button_names[i]] = shopne_variables.player1_button_selections[i].get()

        elif shopne_variables.player1_controller_selection_current.get() == GNGEO_CONTROLLERS[1]:

            shopne_variables.player1_gamepad1_buttons.clear()

            for i in range(len(shopne_variables.button_names)):

                shopne_variables.player1_gamepad1_buttons[shopne_variables.button_names[i]] = shopne_variables.player1_button_selections[i].get()

        elif shopne_variables.player1_controller_selection_current.get() == GNGEO_CONTROLLERS[2]:

            shopne_variables.player1_gamepad2_buttons.clear()

            for i in range(len(shopne_variables.button_names)):

                shopne_variables.player1_gamepad2_buttons[shopne_variables.button_names[i]] = shopne_variables.player1_button_selections[i].get()

        if shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[0]:

            if (len(shopne_variables.player1_keyboard_buttons) == 10):

                for i in range(len(shopne_variables.button_names)):

                    shopne_variables.player1_button_selections[i].set(shopne_variables.player1_keyboard_buttons[shopne_variables.button_names[i]])
            else:

                shopne_variables.player1_button_selections[0].set(keyboard_keys[86])
                shopne_variables.player1_button_selections[1].set(keyboard_keys[80])
                shopne_variables.player1_button_selections[2].set(keyboard_keys[34])
                shopne_variables.player1_button_selections[3].set(keyboard_keys[31])
                shopne_variables.player1_button_selections[4].set(keyboard_keys[10])
                shopne_variables.player1_button_selections[5].set(keyboard_keys[21])
                shopne_variables.player1_button_selections[6].set(keyboard_keys[84])
                shopne_variables.player1_button_selections[7].set(keyboard_keys[76])
                shopne_variables.player1_button_selections[8].set(keyboard_keys[1])
                shopne_variables.player1_button_selections[9].set(keyboard_keys[3])

        elif shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[1]:

            if len(shopne_variables.player1_gamepad1_buttons) == 10:

                for i in range(len(shopne_variables.button_names)):

                    shopne_variables.player1_button_selections[i].set(shopne_variables.player1_gamepad1_buttons[shopne_variables.button_names[i]])

            else:

                shopne_variables.player1_button_selections[0].set(gamepad1_buttons[0])
                shopne_variables.player1_button_selections[1].set(gamepad1_buttons[1])
                shopne_variables.player1_button_selections[2].set(gamepad1_buttons[2])
                shopne_variables.player1_button_selections[3].set(gamepad1_buttons[3])
                shopne_variables.player1_button_selections[4].set(gamepad1_buttons[14])
                shopne_variables.player1_button_selections[5].set(gamepad1_buttons[15])
                shopne_variables.player1_button_selections[6].set(gamepad1_buttons[12])
                shopne_variables.player1_button_selections[7].set(gamepad1_buttons[13])
                shopne_variables.player1_button_selections[8].set(gamepad1_buttons[4])
                shopne_variables.player1_button_selections[9].set(gamepad1_buttons[5])

        elif shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[2]:

            if len(shopne_variables.player1_gamepad2_buttons) == 10:

                for i in range(len(shopne_variables.button_names)):

                    shopne_variables.player1_button_selections[i].set(shopne_variables.player1_gamepad2_buttons[shopne_variables.button_names[i]])

            else:

                shopne_variables.player1_button_selections[0].set(gamepad2_buttons[0])
                shopne_variables.player1_button_selections[1].set(gamepad2_buttons[1])
                shopne_variables.player1_button_selections[2].set(gamepad2_buttons[2])
                shopne_variables.player1_button_selections[3].set(gamepad2_buttons[3])
                shopne_variables.player1_button_selections[4].set(gamepad2_buttons[14])
                shopne_variables.player1_button_selections[5].set(gamepad2_buttons[15])
                shopne_variables.player1_button_selections[6].set(gamepad2_buttons[12])
                shopne_variables.player1_button_selections[7].set(gamepad2_buttons[13])
                shopne_variables.player1_button_selections[8].set(gamepad2_buttons[4])
                shopne_variables.player1_button_selections[9].set(gamepad2_buttons[5])

        shopne_variables.player1_controller_selection_current.set(shopne_variables.player1_controller_selection.get())

    elif player == 2:

        if shopne_variables.player2_controller_selection_current.get() == GNGEO_CONTROLLERS[0]:

            shopne_variables.player2_keyboard_buttons.clear()

            for i in range(len(shopne_variables.button_names)):
                shopne_variables.player2_keyboard_buttons[shopne_variables.button_names[i]] = shopne_variables.player2_button_selections[i].get()

        elif shopne_variables.player2_controller_selection_current.get() == GNGEO_CONTROLLERS[1]:

            shopne_variables.player2_gamepad1_buttons.clear()

            for i in range(len(shopne_variables.button_names)):
                shopne_variables.player2_gamepad1_buttons[shopne_variables.button_names[i]] = shopne_variables.player2_button_selections[i].get()

        elif shopne_variables.player2_controller_selection_current.get() == GNGEO_CONTROLLERS[2]:

            shopne_variables.player2_gamepad2_buttons.clear()

            for i in range(len(shopne_variables.button_names)):
                shopne_variables.player2_gamepad2_buttons[shopne_variables.button_names[i]] = shopne_variables.player2_button_selections[i].get()

        if shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[0]:

            if (len(shopne_variables.player2_keyboard_buttons) == 10):

                for i in range(len(shopne_variables.button_names)):
                    shopne_variables.player2_button_selections[i].set(shopne_variables.player2_keyboard_buttons[shopne_variables.button_names[i]])
            else:

                shopne_variables.player2_button_selections[0].set(keyboard_keys[86])
                shopne_variables.player2_button_selections[1].set(keyboard_keys[80])
                shopne_variables.player2_button_selections[2].set(keyboard_keys[34])
                shopne_variables.player2_button_selections[3].set(keyboard_keys[31])
                shopne_variables.player2_button_selections[4].set(keyboard_keys[10])
                shopne_variables.player2_button_selections[5].set(keyboard_keys[21])
                shopne_variables.player2_button_selections[6].set(keyboard_keys[84])
                shopne_variables.player2_button_selections[7].set(keyboard_keys[76])
                shopne_variables.player2_button_selections[8].set(keyboard_keys[1])
                shopne_variables.player2_button_selections[9].set(keyboard_keys[3])

        elif shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[1]:

            if len(shopne_variables.player2_gamepad1_buttons) == 10:

                for i in range(len(shopne_variables.button_names)):
                    shopne_variables.player2_button_selections[i].set(shopne_variables.player2_gamepad1_buttons[shopne_variables.button_names[i]])

            else:

                shopne_variables.player2_button_selections[0].set(gamepad1_buttons[0])
                shopne_variables.player2_button_selections[1].set(gamepad1_buttons[1])
                shopne_variables.player2_button_selections[2].set(gamepad1_buttons[2])
                shopne_variables.player2_button_selections[3].set(gamepad1_buttons[3])
                shopne_variables.player2_button_selections[4].set(gamepad1_buttons[14])
                shopne_variables.player2_button_selections[5].set(gamepad1_buttons[15])
                shopne_variables.player2_button_selections[6].set(gamepad1_buttons[12])
                shopne_variables.player2_button_selections[7].set(gamepad1_buttons[13])
                shopne_variables.player2_button_selections[8].set(gamepad1_buttons[4])
                shopne_variables.player2_button_selections[9].set(gamepad1_buttons[5])

        elif shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[2]:

            if len(shopne_variables.player2_gamepad2_buttons) == 10:

                for i in range(len(shopne_variables.button_names)):
                    shopne_variables.player2_button_selections[i].set(shopne_variables.player2_gamepad2_buttons[shopne_variables.button_names[i]])

            else:

                shopne_variables.player2_button_selections[0].set(gamepad2_buttons[0])
                shopne_variables.player2_button_selections[1].set(gamepad2_buttons[1])
                shopne_variables.player2_button_selections[2].set(gamepad2_buttons[2])
                shopne_variables.player2_button_selections[3].set(gamepad2_buttons[3])
                shopne_variables.player2_button_selections[4].set(gamepad2_buttons[14])
                shopne_variables.player2_button_selections[5].set(gamepad2_buttons[15])
                shopne_variables.player2_button_selections[6].set(gamepad2_buttons[12])
                shopne_variables.player2_button_selections[7].set(gamepad2_buttons[13])
                shopne_variables.player2_button_selections[8].set(gamepad2_buttons[4])
                shopne_variables.player2_button_selections[9].set(gamepad2_buttons[5])

        shopne_variables.player2_controller_selection_current.set(shopne_variables.player2_controller_selection.get())

def controllers_options_button_callback(window):

    global gngeo_engine, shopne_variables

    window_background_color = '#171718'
    window_foreground_color = '#FFFFFF'
    window_button_background_color = '#B17513'
    window_button_focus_background_color = '#B18C50'
    window_button_foreground_color = '#171718'

    controllers_options_window = tkinter.Toplevel(window)
    controllers_options_window.title("Controller options")
    controllers_options_window.geometry('%dx%d+%d+%d' % (600, 480, window.winfo_x() + ((window.winfo_width() / 2) - (600 / 2)), window.winfo_y() + ((window.winfo_height() / 2) - (480 / 2))))
    controllers_options_window.bind("<Button-1>", lambda event: controllers_options_window_click_callback(event, controllers_options_window))

    controllers_options_frame = tkinter.Frame(controllers_options_window, padx=10, pady=5, background=window_background_color)
    controllers_options_frame.pack_propagate(False)
    controllers_options_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, anchor=tkinter.NW)

    player1_options_frame = tkinter.Frame(controllers_options_frame, background=window_background_color)
    player1_options_frame.pack(fill=tkinter.Y, expand=tkinter.TRUE, side=tkinter.LEFT)

    player1_label = tkinter.Label(player1_options_frame, font=(None, 12, 'bold'), background=window_background_color, foreground=window_foreground_color, text="Player 1")
    player1_label.pack(fill=tkinter.Y, expand=tkinter.TRUE, anchor=tkinter.CENTER, pady=10)

    player1_controller_frame = tkinter.Frame(player1_options_frame, background=window_background_color)
    player1_controller_frame.pack(fill=tkinter.Y, expand=tkinter.TRUE, anchor=tkinter.NW)

    player1_controller_label = tkinter.Label(player1_controller_frame, font=(None, 10), background=window_background_color, foreground=window_foreground_color, text="Controller")
    player1_controller_label.pack(side=tkinter.LEFT, padx=20, pady=10)

    player1_controller_combobox_selection_callback_id = None

    player1_controller_combobox = tkinter.OptionMenu(player1_controller_frame, shopne_variables.player1_controller_selection, *GNGEO_CONTROLLERS)
    player1_controller_combobox.config(font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color)
    player1_controller_combobox["menu"].config(background=window_background_color, foreground=window_foreground_color)
    player1_controller_combobox.pack(side=tkinter.RIGHT)

    player1_controller_combobox_selection_callback_id = shopne_variables.player1_controller_selection.trace('w', lambda a, b, c, d=1: player_controller_combobox_selection_callback(d, a, b, c))

    for i in range(len(shopne_variables.button_names)):

        player1_button_frame = tkinter.Frame(player1_options_frame, background=window_background_color)
        player1_button_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, anchor=tkinter.NW)

        player1_button_label = tkinter.Label(player1_button_frame, font=(None, 10), background=window_background_color, foreground=window_foreground_color,text="Button " + shopne_variables.button_names[i])
        player1_button_label.pack(side=tkinter.LEFT, padx=20)

        player1_button_selection_button = tkinter.Button(player1_button_frame, font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color, textvariable=shopne_variables.player1_button_selections[i], command=partial(button_selection_button_callback, controllers_options_window, 1, shopne_variables.player1_button_selections[i]))
        player1_button_selection_button.pack(side=tkinter.RIGHT)

    player1_default_selection_button = tkinter.Button(player1_options_frame, font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color, text="Use defaults", command=lambda: player_default_selection_button_callback(1))
    player1_default_selection_button.pack(fill=tkinter.X, side=tkinter.TOP, anchor=tkinter.NW, pady=10)

    player2_options_frame = tkinter.Frame(controllers_options_frame, background=window_background_color)
    player2_options_frame.pack(fill=tkinter.Y, expand=tkinter.TRUE, side=tkinter.RIGHT)

    player2_label = tkinter.Label(player2_options_frame, font=(None, 12, 'bold'), background=window_background_color, foreground=window_foreground_color, text="Player 2")
    player2_label.pack(fill=tkinter.Y, expand=tkinter.TRUE, anchor=tkinter.CENTER, pady=10)

    player2_controller_frame = tkinter.Frame(player2_options_frame, background=window_background_color)
    player2_controller_frame.pack(fill=tkinter.Y, expand=tkinter.TRUE, anchor=tkinter.NW)

    player2_controller_label = tkinter.Label(player2_controller_frame, font=(None, 10), background=window_background_color, foreground=window_foreground_color, text="Controller")
    player2_controller_label.pack(side=tkinter.LEFT, padx=20, pady=10)

    player2_controller_combobox_selection_callback_id = None

    player2_controller_combobox = tkinter.OptionMenu(player2_controller_frame, shopne_variables.player2_controller_selection, *GNGEO_CONTROLLERS)
    player2_controller_combobox.config(font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color)
    player2_controller_combobox["menu"].config(background=window_background_color, foreground=window_foreground_color)
    player2_controller_combobox.pack(side=tkinter.RIGHT)

    player2_controller_combobox_selection_callback_id = shopne_variables.player2_controller_selection.trace('w', lambda a, b, c, d=2: player_controller_combobox_selection_callback(d, a, b, c))

    for i in range(len(shopne_variables.button_names)):

        player2_button_frame = tkinter.Frame(player2_options_frame, background=window_background_color)
        player2_button_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, anchor=tkinter.NW)

        player2_button_label = tkinter.Label(player2_button_frame, font=(None, 10), background=window_background_color, foreground=window_foreground_color,text="Button " + shopne_variables.button_names[i])
        player2_button_label.pack(side=tkinter.LEFT, padx=20)

        player2_button_selection_button = tkinter.Button(player2_button_frame, font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color, textvariable=shopne_variables.player2_button_selections[i], command=partial(button_selection_button_callback, controllers_options_window, 2, shopne_variables.player2_button_selections[i]))
        player2_button_selection_button.pack(side=tkinter.RIGHT)

    player2_default_selection_button = tkinter.Button(player2_options_frame, font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color, text="Use defaults", command=lambda: player_default_selection_button_callback(2))
    player2_default_selection_button.pack(fill=tkinter.X, side=tkinter.TOP, anchor=tkinter.NW, pady=10)

    controllers_options_window.grab_set()
    window.wait_window(controllers_options_window)

    if not player1_controller_combobox_selection_callback_id == None:

        shopne_variables.player1_controller_selection.trace_vdelete('w', player1_controller_combobox_selection_callback_id)

    if not player2_controller_combobox_selection_callback_id == None:

        shopne_variables.player2_controller_selection.trace_vdelete('w', player2_controller_combobox_selection_callback_id)

    if shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[0]:

        shopne_variables.player1_controller_selection_current.set(GNGEO_CONTROLLERS[0])

        shopne_variables.player1_keyboard_buttons.clear()

        for i in range(len(shopne_variables.button_names)):

            shopne_variables.player1_keyboard_buttons[shopne_variables.button_names[i]] = shopne_variables.player1_button_selections[i].get()

        gngeo_engine.p1control = 'A=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[0].get()] + ',B=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[1].get()] + ',C=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[2].get()] + ',D=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[3].get()] + ',LEFT=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[4].get()] + ',RIGHT=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[5].get()] + ',UP=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[6].get()] + ',DOWN=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[7].get()] + ',START=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[8].get()] + ',COIN=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[9].get()]

    elif shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[1]:

        shopne_variables.player1_controller_selection_current.set(GNGEO_CONTROLLERS[1])

        shopne_variables.player1_gamepad1_buttons.clear()

        for i in range(len(shopne_variables.button_names)):

            shopne_variables.player1_gamepad1_buttons[shopne_variables.button_names[i]] = shopne_variables.player1_button_selections[i].get()

        gngeo_engine.p1control = 'A=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[0].get()] + ',B=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[1].get()] + ',C=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[2].get()] + ',D=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[3].get()] + ',LEFT=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[4].get()] + ',RIGHT=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[5].get()] + ',UP=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[6].get()] + ',DOWN=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[7].get()] + ',START=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[8].get()] + ',COIN=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[9].get()]

    elif shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[2]:

        shopne_variables.player1_controller_selection_current.set(GNGEO_CONTROLLERS[2])

        shopne_variables.player1_gamepad2_buttons.clear()

        for i in range(len(shopne_variables.button_names)):

            shopne_variables.player1_gamepad2_buttons[shopne_variables.button_names[i]] = shopne_variables.player1_button_selections[i].get()

        gngeo_engine.p1control = 'A=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[0].get()] + ',B=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[1].get()] + ',C=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[2].get()] + ',D=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[3].get()] + ',LEFT=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[4].get()] + ',RIGHT=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[5].get()] + ',UP=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[6].get()] + ',DOWN=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[7].get()] + ',START=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[8].get()] + ',COIN=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[9].get()]

    if shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[0]:

        shopne_variables.player2_controller_selection_current.set(GNGEO_CONTROLLERS[0])

        shopne_variables.player2_keyboard_buttons.clear()

        for i in range(len(shopne_variables.button_names)):

            shopne_variables.player2_keyboard_buttons[shopne_variables.button_names[i]] = shopne_variables.player2_button_selections[i].get()

        gngeo_engine.p2control = 'A=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[0].get()] + ',B=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[1].get()] + ',C=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[2].get()] + ',D=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[3].get()] + ',LEFT=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[4].get()] + ',RIGHT=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[5].get()] + ',UP=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[6].get()] + ',DOWN=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[7].get()] + ',START=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[8].get()] + ',COIN=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[9].get()]

    elif shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[1]:

        shopne_variables.player2_controller_selection_current.set(GNGEO_CONTROLLERS[1])

        shopne_variables.player2_gamepad1_buttons.clear()

        for i in range(len(shopne_variables.button_names)):

            shopne_variables.player2_gamepad1_buttons[shopne_variables.button_names[i]] = shopne_variables.player2_button_selections[i].get()

        gngeo_engine.p2control = 'A=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[0].get()] + ',B=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[1].get()] + ',C=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[2].get()] + ',D=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[3].get()] + ',LEFT=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[4].get()] + ',RIGHT=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[5].get()] + ',UP=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[6].get()] + ',DOWN=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[7].get()] + ',START=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[8].get()] + ',COIN=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[9].get()]

    elif shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[2]:

        shopne_variables.player2_controller_selection_current.set(GNGEO_CONTROLLERS[2])

        shopne_variables.player2_gamepad2_buttons.clear()

        for i in range(len(shopne_variables.button_names)):

            shopne_variables.player2_gamepad2_buttons[shopne_variables.button_names[i]] = shopne_variables.player2_button_selections[i].get()

        gngeo_engine.p2control = 'A=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[0].get()] + ',B=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[1].get()] + ',C=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[2].get()] + ',D=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[3].get()] + ',LEFT=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[4].get()] + ',RIGHT=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[5].get()] + ',UP=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[6].get()] + ',DOWN=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[7].get()] + ',START=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[8].get()] + ',COIN=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[9].get()]

def game_options_button_callback(window):

    global gngeo_engine, shopne_variables

    window_background_color = '#171718'
    window_foreground_color = '#FFFFFF'
    window_button_background_color = '#B17513'
    window_button_focus_background_color = '#B18C50'
    window_button_foreground_color = '#171718'

    game_options_window = tkinter.Toplevel(window)
    game_options_window.title("Game options")
    game_options_window.geometry('%dx%d+%d+%d' % (400, 100, window.winfo_x() + ((window.winfo_width() / 2) - (400 / 2)), window.winfo_y() + ((window.winfo_height() / 2) - (100 / 2))))

    game_options_frame = tkinter.Frame(game_options_window, padx=10, pady=5, background=window_background_color)
    game_options_frame.pack_propagate(False)
    game_options_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, anchor=tkinter.NW)

    game_country_frame = tkinter.Frame(game_options_frame, background=window_background_color)
    game_country_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, anchor=tkinter.NW)

    game_country_label = tkinter.Label(game_country_frame, font=(None, 10), background=window_background_color, foreground=window_foreground_color, text="System BIOS country")
    game_country_label.pack(side=tkinter.LEFT, padx=20, pady=10)

    game_country_combobox = tkinter.OptionMenu(game_country_frame, shopne_variables.game_country_selection, *game_countries)
    game_country_combobox.config(font=(None, 10), activeforeground=window_button_foreground_color, activebackground=window_button_focus_background_color, highlightbackground=window_background_color, background=window_button_background_color, foreground=window_button_foreground_color)
    game_country_combobox["menu"].config(background=window_background_color, foreground=window_foreground_color)
    game_country_combobox.pack(side=tkinter.RIGHT)

    game_options_window.grab_set()
    window.wait_window(game_options_window)

    gngeo_engine.country = GNGEO_GAME_COUNTRIES[shopne_variables.game_country_selection.get()]

def about_button_callback(window):

    global shopne_variables

    window_background_color = '#171718'
    window_foreground_color = '#FFFFFF'
    window_button_background_color = '#B17513'
    window_button_focus_background_color = '#B18C50'
    window_button_foreground_color = '#171718'

    about_window = tkinter.Toplevel(window)
    about_window.title("About Shopne Arcade")
    about_window.geometry('%dx%d+%d+%d' % (600, 480, window.winfo_x() + ((window.winfo_width() / 2) - (600 / 2)), window.winfo_y() + ((window.winfo_height() / 2) - (480 / 2))))

    about_window_frame = tkinter.Frame(about_window, padx=10, pady=5, background=window_background_color)
    about_window_frame.pack_propagate(False)
    about_window_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, side=tkinter.TOP)

    shopne_arcade_logo_image = tkinter.PhotoImage(file='./data/logo.png')

    shopne_arcade_logo = tkinter.Label(about_window_frame, image=shopne_arcade_logo_image, background=window_background_color, foreground=window_foreground_color)
    shopne_arcade_logo.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, side=tkinter.TOP, padx=20, pady=10)

    shopne_arcade_label = tkinter.Label(about_window_frame, background=window_background_color, foreground=window_foreground_color, text='Shopne Arcade ' + str(shopne_variables.shopne_arcade_version) + " " + shopne_variables.shopne_arcade_description)
    shopne_arcade_label.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, side=tkinter.TOP, padx=20, pady=4)

    shopne_arcade_description_label = tkinter.Label(about_window_frame, background=window_background_color, foreground=window_foreground_color, text= ' using GnGeo version ' + str(gngeo_engine.version))
    shopne_arcade_description_label.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, side=tkinter.TOP, padx=20, pady=4)

    shopne_arcade_copyright_label = tkinter.Label(about_window_frame, background=window_background_color, foreground=window_foreground_color, text='Copyright © 2017-2021 ' + shopne_variables.shopne_arcade_copyright)
    shopne_arcade_copyright_label.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, side=tkinter.TOP, padx=20)

    shopne_arcade_licence_label = tkinter.Label(about_window_frame, background=window_background_color, foreground=window_foreground_color, text=shopne_variables.shopne_arcade_licence)
    shopne_arcade_licence_label.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, side=tkinter.TOP, padx=20, pady=4)
    
    shopne_arcade_other_label = tkinter.Label(about_window_frame, background=window_background_color, foreground=window_foreground_color, text="All game cover arts are the property of their respective copyright holders.")
    shopne_arcade_other_label.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, side=tkinter.TOP, padx=20, pady=4)

    about_window.grab_set()
    window.wait_window(about_window)

def cover_callback(event, window, game_list_widget):

    window_background_color = '#171718'
    window_foreground_color = '#FFFFFF'
    window_button_background_color = '#B17513'
    window_button_focus_background_color = '#B18C50'
    window_button_foreground_color = '#171718'

    selection = game_list_widget.get(game_list_widget.curselection()[0])

    cover_window = tkinter.Toplevel(window)
    cover_window.title("Game cover: "+ selection)
    cover_window.geometry('%dx%d+%d+%d' % (273, 365, window.winfo_x() + ((window.winfo_width() / 2) - (273 / 2)), window.winfo_y() + ((window.winfo_height() / 2) - (365 / 2))))

    cover_window_frame = tkinter.Frame(cover_window, padx=5, pady=5, background=window_background_color)
    cover_window_frame.pack_propagate(False)
    cover_window_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, side=tkinter.TOP)

    rom_selection = None

    for rom in GNGEO_ROMS_LIST:
        if (GNGEO_ROMS_LIST[rom] == selection):
            rom_selection = rom
            break

    cover_arcade_logo_image = tkinter.PhotoImage(file='./data/covers/' + rom_selection + '.png')

    cover_arcade_logo = tkinter.Label(cover_window_frame, image=cover_arcade_logo_image, background=window_background_color, foreground=window_foreground_color)
    cover_arcade_logo.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, side=tkinter.TOP, padx=5, pady=5)

    #cover_window.grab_set()
    window.wait_window(cover_window)

def load_rom_callback(window, game_list_widget):

    global gngeo_engine, roms, shopne_variables

    if game_list_widget.size() < 1:
        shopne_variables.main_window_status_label.set('No games in the library')
        window.after(3000, lambda: shopne_variables.main_window_status_label.set('Click Game rom files locations to add games to the library'))
        return

    if len(game_list_widget.curselection()) < 1:
        shopne_variables.main_window_status_label.set('Select a game from Games')
        return

    selection = game_list_widget.get(game_list_widget.curselection()[0])

    rom_selection = None

    for rom in GNGEO_ROMS_LIST:
        if (GNGEO_ROMS_LIST[rom] == selection):
            rom_selection = rom
            break

    if not gngeo_engine.run_game(rom_selection, roms.roms[rom_selection]) == 0:
        shopne_variables.main_window_status_label.set('Launching the game failed')
        window.after(2000, lambda: shopne_variables.main_window_status_label.set('Select a different game from Games'))

# load settings from files
def load_settings():

    global shopne_variables, gngeo_engine_data, roms

    shopne_variables.initialise()

    shopne_variables.currrent_roms_directory_location.set(os.path.expanduser('~'))

    if os.path.isfile('./settings/game_options.json'):
        game_options_conf_file = open("./settings/game_options.json", "r")
        gngeo_engine_data.game_options.clear()
        try:
            gngeo_engine_data.game_options = json.load(game_options_conf_file)
        except ValueError:
            print('Shopne Arcade:', 'could not load game options')
        else:
            pass
        game_options_conf_file.close()

    if len(gngeo_engine_data.game_options) > 0:
        shopne_variables.game_country_selection.set(gngeo_engine_data.game_options['country'])
    else:
        shopne_variables.game_country_selection.set('Default')

    gngeo_engine.country = GNGEO_GAME_COUNTRIES[shopne_variables.game_country_selection.get()]

    if os.path.isfile('./settings/sound.json'):
        sound_conf_file = open("./settings/sound.json", "r")
        gngeo_engine_data.audio_configuration.clear()
        try:
            gngeo_engine_data.audio_configuration = json.load(sound_conf_file)
        except ValueError:
            print('Shopne Arcade:', 'could not load audio configurations')
        else:
            pass
        sound_conf_file.close()

    if len(gngeo_engine_data.audio_configuration) > 0:
        shopne_variables.sound_ckeck_button_state.set(gngeo_engine_data.audio_configuration['emulate audio'])
        shopne_variables.audio_sampling_combobox_selection.set(gngeo_engine_data.audio_configuration['sampling rate'])
    else:
        shopne_variables.sound_ckeck_button_state.set(1)
        shopne_variables.audio_sampling_combobox_selection.set(GNGEO_VIDEO_SCALINGS[0])

    if shopne_variables.sound_ckeck_button_state.get() == 0:
        gngeo_engine.sound = False
    else:
        gngeo_engine.sound = True

    gngeo_engine.samplerate = shopne_variables.audio_sampling_combobox_selection.get()

    if os.path.isfile('./settings/graphics.json'):
        graphics_conf_file = open("./settings/graphics.json", "r")
        gngeo_engine_data.graphics_configuration.clear()
        try:
            gngeo_engine_data.graphics_configuration = json.load(graphics_conf_file)
        except ValueError:
            print('Shopne Arcade:', 'could not load graphics configurations')
        else:
            pass
        graphics_conf_file.close()

    if len(gngeo_engine_data.graphics_configuration) > 0:

        shopne_variables.fullscreen_ckeck_button_state.set(gngeo_engine_data.graphics_configuration['fullscreen'])
        shopne_variables.autoframeskip_ckeck_button_state.set(gngeo_engine_data.graphics_configuration['adjust'])
        shopne_variables.interpolation_ckeck_button_state.set(gngeo_engine_data.graphics_configuration['interpolation'])
        shopne_variables.hwsurface_ckeck_button_state.set(gngeo_engine_data.graphics_configuration['gpu'])
        shopne_variables.vsync_ckeck_button_state.set(gngeo_engine_data.graphics_configuration['sync'])
        shopne_variables.video_scaling_combobox_selection.set(gngeo_engine_data.graphics_configuration['scaling'])
        shopne_variables.video_effects_combobox_selection.set(gngeo_engine_data.graphics_configuration['effect'])
        shopne_variables.video_renderer_combobox_selection.set(gngeo_engine_data.graphics_configuration['renderer'])

    else:

        shopne_variables.fullscreen_ckeck_button_state.set(0)
        shopne_variables.autoframeskip_ckeck_button_state.set(1)
        shopne_variables.interpolation_ckeck_button_state.set(1)
        shopne_variables.hwsurface_ckeck_button_state.set(1)
        shopne_variables.vsync_ckeck_button_state.set(1)
        shopne_variables.video_scaling_combobox_selection.set(GNGEO_VIDEO_SCALINGS[0])
        shopne_variables.video_effects_combobox_selection.set(GNGEO_VIDEO_EFFECTS[1])
        shopne_variables.video_renderer_combobox_selection.set(GNGEO_BLITTERS[1])

    if shopne_variables.fullscreen_ckeck_button_state.get() == 0:
        gngeo_engine.fullscreen = False
    else:
        gngeo_engine.fullscreen = True

    if shopne_variables.autoframeskip_ckeck_button_state.get() == 0:
        gngeo_engine.autoframeskip = False
    else:
        gngeo_engine.autoframeskip = True

    if shopne_variables.interpolation_ckeck_button_state.get() == 0:
        gngeo_engine.interpolation = False
    else:
        gngeo_engine.interpolation = True

    if shopne_variables.hwsurface_ckeck_button_state.get() == 0:
        gngeo_engine.hwsurface = False
    else:
        gngeo_engine.hwsurface = True

    if shopne_variables.vsync_ckeck_button_state.get() == 0:
        gngeo_engine.vsync = False
    else:
        gngeo_engine.vsync = True

    gngeo_engine.scale = shopne_variables.video_scaling_combobox_selection.get()
    gngeo_engine.effect = shopne_variables.video_effects_combobox_selection.get()
    gngeo_engine.blitter = shopne_variables.video_renderer_combobox_selection.get()

    if os.path.isfile('./settings/control1.json'):
        controller_conf_file = open("./settings/control1.json", "r")
        gngeo_engine_data.controller_configuration.clear()
        try:
            gngeo_engine_data.controller_configuration = json.load(controller_conf_file)
        except ValueError:
            print('Shopne Arcade:', 'could not load controller 1 configurations')
        else:
            pass
        controller_conf_file.close()

    if len(gngeo_engine_data.controller_configuration) > 0:

        shopne_variables.player1_controller_selection.set(gngeo_engine_data.controller_configuration['controller'])
        shopne_variables.player1_button_selections[0].set(gngeo_engine_data.controller_configuration['A'])
        shopne_variables.player1_button_selections[1].set(gngeo_engine_data.controller_configuration['B'])
        shopne_variables.player1_button_selections[2].set(gngeo_engine_data.controller_configuration['C'])
        shopne_variables.player1_button_selections[3].set(gngeo_engine_data.controller_configuration['D'])
        shopne_variables.player1_button_selections[4].set(gngeo_engine_data.controller_configuration['LEFT'])
        shopne_variables.player1_button_selections[5].set(gngeo_engine_data.controller_configuration['RIGHT'])
        shopne_variables.player1_button_selections[6].set(gngeo_engine_data.controller_configuration['UP'])
        shopne_variables.player1_button_selections[7].set(gngeo_engine_data.controller_configuration['DOWN'])
        shopne_variables.player1_button_selections[8].set(gngeo_engine_data.controller_configuration['START'])
        shopne_variables.player1_button_selections[9].set(gngeo_engine_data.controller_configuration['COIN'])

    else:

        shopne_variables.player1_controller_selection.set(GNGEO_CONTROLLERS[0])
        shopne_variables.player1_button_selections[0].set(keyboard_keys[86])
        shopne_variables.player1_button_selections[1].set(keyboard_keys[80])
        shopne_variables.player1_button_selections[2].set(keyboard_keys[34])
        shopne_variables.player1_button_selections[3].set(keyboard_keys[31])
        shopne_variables.player1_button_selections[4].set(keyboard_keys[10])
        shopne_variables.player1_button_selections[5].set(keyboard_keys[21])
        shopne_variables.player1_button_selections[6].set(keyboard_keys[84])
        shopne_variables.player1_button_selections[7].set(keyboard_keys[76])
        shopne_variables.player1_button_selections[8].set(keyboard_keys[1])
        shopne_variables.player1_button_selections[9].set(keyboard_keys[3])


    if os.path.isfile('./settings/control2.json'):
        controller_conf_file = open("./settings/control2.json", "r")
        gngeo_engine_data.controller_configuration.clear()
        try:
            gngeo_engine_data.controller_configuration = json.load(controller_conf_file)
        except ValueError:
            print('Shopne Arcade:', 'could not load controller 2 configurations')
        else:
            pass
        controller_conf_file.close()

    if len(gngeo_engine_data.controller_configuration) > 0:

        shopne_variables.player2_controller_selection.set(gngeo_engine_data.controller_configuration['controller'])
        shopne_variables.player2_button_selections[0].set(gngeo_engine_data.controller_configuration['A'])
        shopne_variables.player2_button_selections[1].set(gngeo_engine_data.controller_configuration['B'])
        shopne_variables.player2_button_selections[2].set(gngeo_engine_data.controller_configuration['C'])
        shopne_variables.player2_button_selections[3].set(gngeo_engine_data.controller_configuration['D'])
        shopne_variables.player2_button_selections[4].set(gngeo_engine_data.controller_configuration['LEFT'])
        shopne_variables.player2_button_selections[5].set(gngeo_engine_data.controller_configuration['RIGHT'])
        shopne_variables.player2_button_selections[6].set(gngeo_engine_data.controller_configuration['UP'])
        shopne_variables.player2_button_selections[7].set(gngeo_engine_data.controller_configuration['DOWN'])
        shopne_variables.player2_button_selections[8].set(gngeo_engine_data.controller_configuration['START'])
        shopne_variables.player2_button_selections[9].set(gngeo_engine_data.controller_configuration['COIN'])

    else:

        shopne_variables.player2_controller_selection.set(GNGEO_CONTROLLERS[1])
        shopne_variables.player2_button_selections[0].set(gamepad1_buttons[0])
        shopne_variables.player2_button_selections[1].set(gamepad1_buttons[1])
        shopne_variables.player2_button_selections[2].set(gamepad1_buttons[2])
        shopne_variables.player2_button_selections[3].set(gamepad1_buttons[3])
        shopne_variables.player2_button_selections[4].set(gamepad1_buttons[14])
        shopne_variables.player2_button_selections[5].set(gamepad1_buttons[15])
        shopne_variables.player2_button_selections[6].set(gamepad1_buttons[12])
        shopne_variables.player2_button_selections[7].set(gamepad1_buttons[13])
        shopne_variables.player2_button_selections[8].set(gamepad1_buttons[4])
        shopne_variables.player2_button_selections[9].set(gamepad1_buttons[5])

    if shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[0]:

        gngeo_engine.p1control = 'A=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[0].get()] + ',B=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[1].get()] + ',C=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[2].get()] + ',D=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[3].get()] + ',LEFT=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[4].get()] + ',RIGHT=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[5].get()] + ',UP=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[6].get()] + ',DOWN=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[7].get()] + ',START=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[8].get()] + ',COIN=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player1_button_selections[9].get()]

    elif shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[1]:

        gngeo_engine.p1control = 'A=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[0].get()] + ',B=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[1].get()] + ',C=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[2].get()] + ',D=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[3].get()] + ',LEFT=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[4].get()] + ',RIGHT=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[5].get()] + ',UP=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[6].get()] + ',DOWN=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[7].get()] + ',START=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[8].get()] + ',COIN=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player1_button_selections[9].get()]

    elif shopne_variables.player1_controller_selection.get() == GNGEO_CONTROLLERS[2]:

        gngeo_engine.p1control = 'A=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[0].get()] + ',B=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[1].get()] + ',C=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[2].get()] + ',D=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[3].get()] + ',LEFT=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[4].get()] + ',RIGHT=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[5].get()] + ',UP=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[6].get()] + ',DOWN=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[7].get()] + ',START=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[8].get()] + ',COIN=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player1_button_selections[9].get()]

    if shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[0]:

        gngeo_engine.p2control = 'A=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[0].get()] + ',B=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[1].get()] + ',C=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[2].get()] + ',D=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[3].get()] + ',LEFT=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[4].get()] + ',RIGHT=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[5].get()] + ',UP=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[6].get()] + ',DOWN=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[7].get()] + ',START=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[8].get()] + ',COIN=' + GNGEO_KEYBOARD_KEYCODES[shopne_variables.player2_button_selections[9].get()]

    elif shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[1]:

        gngeo_engine.p2control = 'A=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[0].get()] + ',B=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[1].get()] + ',C=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[2].get()] + ',D=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[3].get()] + ',LEFT=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[4].get()] + ',RIGHT=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[5].get()] + ',UP=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[6].get()] + ',DOWN=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[7].get()] + ',START=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[8].get()] + ',COIN=' + GNGEO_GAMEPAD1_KEYCODES[shopne_variables.player2_button_selections[9].get()]

    elif shopne_variables.player2_controller_selection.get() == GNGEO_CONTROLLERS[2]:

        gngeo_engine.p2control = 'A=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[0].get()] + ',B=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[1].get()] + ',C=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[2].get()] + ',D=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[3].get()] + ',LEFT=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[4].get()] + ',RIGHT=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[5].get()] + ',UP=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[6].get()] + ',DOWN=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[7].get()] + ',START=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[8].get()] + ',COIN=' + GNGEO_GAMEPAD2_KEYCODES[shopne_variables.player2_button_selections[9].get()]

    if os.path.isfile('./settings/roms_locations.json'):
        roms_locations_conf_file = open("./settings/roms_locations.json", "r")
        gngeo_engine_data.roms_directories.clear()
        try:
            gngeo_engine_data.roms_directories = json.load(roms_locations_conf_file)
        except ValueError:
            print('Shopne Arcade:', 'could not load roms directory locations')
        else:
            pass
        roms_locations_conf_file.close()

    if len(gngeo_engine_data.roms_directories) > 0:

        for i in range(len(gngeo_engine_data.roms_directories)):

            if not len(gngeo_engine_data.roms_directories[str(i)]) == 0:
                roms.add_directory(gngeo_engine_data.roms_directories[str(i)])

# save settings to files
def save_settings():

    global shopne_variables, gngeo_engine_data, roms

    gngeo_engine_data.game_options.clear()
    gngeo_engine_data.game_options['country'] = shopne_variables.game_country_selection.get()

    game_options_conf_file = open("./settings/game_options.json", "w")
    json.dump(gngeo_engine_data.game_options, game_options_conf_file)
    game_options_conf_file.close()

    gngeo_engine_data.audio_configuration.clear()
    gngeo_engine_data.audio_configuration['sampling rate'] = shopne_variables.audio_sampling_combobox_selection.get()
    gngeo_engine_data.audio_configuration['emulate audio'] = shopne_variables.sound_ckeck_button_state.get()

    sound_conf_file = open("./settings/sound.json", "w")
    json.dump(gngeo_engine_data.audio_configuration, sound_conf_file)
    sound_conf_file.close()

    gngeo_engine_data.graphics_configuration.clear()
    gngeo_engine_data.graphics_configuration['fullscreen'] = shopne_variables.fullscreen_ckeck_button_state.get()
    gngeo_engine_data.graphics_configuration['adjust'] = shopne_variables.autoframeskip_ckeck_button_state.get()
    gngeo_engine_data.graphics_configuration['interpolation'] = shopne_variables.interpolation_ckeck_button_state.get()
    gngeo_engine_data.graphics_configuration['gpu'] = shopne_variables.hwsurface_ckeck_button_state.get()
    gngeo_engine_data.graphics_configuration['sync'] = shopne_variables.vsync_ckeck_button_state.get()
    gngeo_engine_data.graphics_configuration['scaling'] = shopne_variables.video_scaling_combobox_selection.get()
    gngeo_engine_data.graphics_configuration['effect'] = shopne_variables.video_effects_combobox_selection.get()
    gngeo_engine_data.graphics_configuration['renderer'] = shopne_variables.video_renderer_combobox_selection.get()

    graphics_conf_file = open("./settings/graphics.json", "w")
    json.dump(gngeo_engine_data.graphics_configuration, graphics_conf_file)
    graphics_conf_file.close()

    gngeo_engine_data.controller_configuration.clear()
    gngeo_engine_data.controller_configuration['controller'] = shopne_variables.player1_controller_selection.get()
    gngeo_engine_data.controller_configuration['A'] = shopne_variables.player1_button_selections[0].get()
    gngeo_engine_data.controller_configuration['B'] = shopne_variables.player1_button_selections[1].get()
    gngeo_engine_data.controller_configuration['C'] = shopne_variables.player1_button_selections[2].get()
    gngeo_engine_data.controller_configuration['D'] = shopne_variables.player1_button_selections[3].get()
    gngeo_engine_data.controller_configuration['LEFT'] = shopne_variables.player1_button_selections[4].get()
    gngeo_engine_data.controller_configuration['RIGHT'] = shopne_variables.player1_button_selections[5].get()
    gngeo_engine_data.controller_configuration['UP'] = shopne_variables.player1_button_selections[6].get()
    gngeo_engine_data.controller_configuration['DOWN'] = shopne_variables.player1_button_selections[7].get()
    gngeo_engine_data.controller_configuration['START'] = shopne_variables.player1_button_selections[8].get()
    gngeo_engine_data.controller_configuration['COIN'] = shopne_variables.player1_button_selections[9].get()

    controller_conf_file = open("./settings/control1.json", "w")
    json.dump(gngeo_engine_data.controller_configuration, controller_conf_file)
    controller_conf_file.close()

    gngeo_engine_data.controller_configuration.clear()
    gngeo_engine_data.controller_configuration['controller'] = shopne_variables.player2_controller_selection.get()
    gngeo_engine_data.controller_configuration['A'] = shopne_variables.player2_button_selections[0].get()
    gngeo_engine_data.controller_configuration['B'] = shopne_variables.player2_button_selections[1].get()
    gngeo_engine_data.controller_configuration['C'] = shopne_variables.player2_button_selections[2].get()
    gngeo_engine_data.controller_configuration['D'] = shopne_variables.player2_button_selections[3].get()
    gngeo_engine_data.controller_configuration['LEFT'] = shopne_variables.player2_button_selections[4].get()
    gngeo_engine_data.controller_configuration['RIGHT'] = shopne_variables.player2_button_selections[5].get()
    gngeo_engine_data.controller_configuration['UP'] = shopne_variables.player2_button_selections[6].get()
    gngeo_engine_data.controller_configuration['DOWN'] = shopne_variables.player2_button_selections[7].get()
    gngeo_engine_data.controller_configuration['START'] = shopne_variables.player2_button_selections[8].get()
    gngeo_engine_data.controller_configuration['COIN'] = shopne_variables.player2_button_selections[9].get()

    controller_conf_file = open("./settings/control2.json", "w")
    json.dump(gngeo_engine_data.controller_configuration, controller_conf_file)
    controller_conf_file.close()

    gngeo_engine_data.roms_directories.clear()

    for i in range(len(roms.directories)):

        gngeo_engine_data.roms_directories[str(i)] = roms.directories[i]

    roms_locations_conf_file = open("./settings/roms_locations.json", "w")
    json.dump(gngeo_engine_data.roms_directories, roms_locations_conf_file)
    roms_locations_conf_file.close()

def main(gngeo_status):

    global shopne_variables, roms

    application_background_color = '#F7F7F7'
    button_background_color = '#4285F4'
    button_background_focus_color = '#75A5F4'
    button_foreground_color = '#FFFFFF'

    main_window = tkinter.Tk()
    icon = tkinter.PhotoImage(file='./data/icon.png')
    main_window.title("Shopne Arcade")
    main_window.geometry('%dx%d+%d+%d' % (640, 480, (main_window.winfo_screenwidth()/2)-(640/2), (main_window.winfo_screenheight()/2)-(480/2)))
    main_window.tk.call('wm', 'iconphoto', main_window._w, '-default', icon)

    load_settings()

    main_window_frame = tkinter.Frame(main_window, padx=10, pady=20, background=application_background_color)
    main_window_frame.pack_propagate(False)
    main_window_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE)

    rom_list_frame = tkinter.Frame(main_window_frame, width=400, height=250, background=application_background_color)
    rom_list_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, side=tkinter.LEFT)

    rom_list_label = tkinter.Label(rom_list_frame, text="Games", font=(None, 14, 'bold'), background=application_background_color)
    rom_list_label.pack(side=tkinter.TOP, anchor=tkinter.NW)

    game_list = tkinter.Listbox(rom_list_frame, selectmode=tkinter.SINGLE, relief=tkinter.FLAT, highlightthickness=2, font=(None, 14), activestyle='underline', cursor='hand1')
    game_list.pack(fill=tkinter.BOTH, expand=tkinter.TRUE, side=tkinter.TOP)
    game_list.focus()
    game_list.bind('<Double-Button-1>', lambda event: cover_callback(event, main_window, game_list))

    if(gngeo_status == 0):

        roms.update_roms()

        for rom in roms.roms:
            game_list.insert(tkinter.END, GNGEO_ROMS_LIST[rom])
            game_list.itemconfig(tkinter.END, bg = 'gray95' if game_list.size() % 2 == 0 else 'gray98')

        number_of_roms = game_list.size()

        if number_of_roms == 0:
            shopne_variables.main_window_status_label.set('No games in the library')
            main_window.after(5000, lambda: shopne_variables.main_window_status_label.set('Click Game files locations to add games to library'))
        elif number_of_roms == 1:
            shopne_variables.main_window_status_label.set(str(game_list.size()) + ' game in the library')
            main_window.after(10000, lambda: shopne_variables.main_window_status_label.set('Select the game from Games and click Load game'+"\nDouble click on the game to see the cover art"))
        else:
            shopne_variables.main_window_status_label.set(str(game_list.size()) + ' games in the library')
            main_window.after(10000, lambda: shopne_variables.main_window_status_label.set('Select a game from Games and click Load game'+"\nDouble click on the game to see the cover art"))

    load_rom_button = tkinter.Button(rom_list_frame, text="Load game", font=(None, 12), foreground=button_foreground_color, activeforeground=button_foreground_color, activebackground=button_background_focus_color, background=button_background_color, highlightbackground=application_background_color, command=lambda: load_rom_callback(main_window, game_list))
    if (gngeo_status == 1):
        load_rom_button.config(state=tkinter.DISABLED)
    load_rom_button.pack(fill=tkinter.X, side=tkinter.TOP)

    settings_frame = tkinter.Frame(main_window_frame, width=190, height=280, background=application_background_color)
    settings_frame.pack(side=tkinter.RIGHT)

    rom_directories_button = tkinter.Button(settings_frame, text ="Game files locations", font=(None, 10), foreground=button_foreground_color, activeforeground=button_foreground_color, activebackground=button_background_focus_color, background=button_background_color, highlightbackground=application_background_color, command=lambda: rom_directories_selection_button_callback(main_window, game_list))
    if (gngeo_status == 1):
        rom_directories_button.config(state=tkinter.DISABLED)
    rom_directories_button.pack(fill=tkinter.X)

    graphics_options_button = tkinter.Button(settings_frame, text="Graphics options", font=(None, 10), foreground=button_foreground_color, activeforeground=button_foreground_color, activebackground=button_background_focus_color, background=button_background_color, highlightbackground=application_background_color, command=lambda: graphics_options_button_callback(main_window))
    if (gngeo_status == 1):
        graphics_options_button.config(state=tkinter.DISABLED)
    graphics_options_button.pack(fill=tkinter.X)

    sound_options_button = tkinter.Button(settings_frame, text="Sound options", font=(None, 10), foreground=button_foreground_color, activeforeground=button_foreground_color, activebackground=button_background_focus_color, background=button_background_color, highlightbackground=application_background_color, command=lambda: sound_options_button_callback(main_window))
    if (gngeo_status == 1):
        sound_options_button.config(state=tkinter.DISABLED)
    sound_options_button.pack(fill=tkinter.X)

    controller_options_button = tkinter.Button(settings_frame, text="Controller options", font=(None, 10), foreground=button_foreground_color, activeforeground=button_foreground_color, activebackground=button_background_focus_color, background=button_background_color, highlightbackground=application_background_color, command=lambda: controllers_options_button_callback(main_window))
    if (gngeo_status == 1):
        controller_options_button.config(state=tkinter.DISABLED)
    controller_options_button.pack(fill=tkinter.X)

    game_options_button = tkinter.Button(settings_frame, text="Game options",font=(None, 10), foreground=button_foreground_color, activeforeground=button_foreground_color, activebackground=button_background_focus_color, background=button_background_color, highlightbackground=application_background_color, command=lambda: game_options_button_callback(main_window))
    if (gngeo_status == 1):
        game_options_button.config(state=tkinter.DISABLED)
    game_options_button.pack(fill=tkinter.X)

    status_label = tkinter.Label(settings_frame, textvariable=shopne_variables.main_window_status_label, background=application_background_color)
    if (gngeo_status == 1):
        shopne_variables.main_window_status_label.set('Please check you have all the system libraries\ninstalled for running Shopne Arcade')
    status_label.pack(fill=tkinter.X, pady=10)

    about_button = tkinter.Button(settings_frame, text="About", font=(None, 10), foreground=button_foreground_color, activeforeground=button_foreground_color, activebackground=button_background_focus_color, background=button_background_color, highlightbackground=application_background_color, command=lambda: about_button_callback(main_window))
    about_button.pack(fill=tkinter.X)

    main_window.mainloop()

    save_settings()

# Constants
keyboard_keys = list(GNGEO_KEYBOARD_KEYCODES.keys())
keyboard_keys.sort()

gamepad1_buttons = list(GNGEO_GAMEPAD1_KEYCODES.keys())

gamepad2_buttons = list(GNGEO_GAMEPAD2_KEYCODES.keys())

game_countries = list(GNGEO_GAME_COUNTRIES.keys())
game_countries.sort()

# Variables
roms = Roms()
gngeo_engine = GnGeo()
shopne_variables = ShopneVariables()
gngeo_engine_data = GngeoEngineData()

if __name__ == '__main__':

    gngeo_path = os.path.join(os.path.abspath(os.getcwd()), 'gngeo')
    gngeo_exe = os.path.join(gngeo_path, 'gngeo_bin')
    gngeo_data = os.path.join(gngeo_path, 'gngeo_data.zip')

    gngeo_status = gngeo_engine.set_exe(gngeo_exe, gngeo_data, gngeo_path)

    if gngeo_status == 0:

        print('Shopne Arcade: using GnGeo version', gngeo_engine.version)

    else:

        print('Shopne Arcade: could not load GnGeo')

    main(gngeo_status)
