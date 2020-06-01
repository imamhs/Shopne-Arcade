# Copyright (c) 2017, Md Imam Hossain (emamhd at gmail dot com)
# see LICENSE.txt for details

from os import popen

GNGEO_AUDIO_SAMPLE_RATES = ['default', '8000', '11025', '16000', '22050', '24000', '44100']
GNGEO_VIDEO_EFFECTS = ['default', 'hq2x', 'hq3x', 'lq2x', 'lq3x', 'scanline', 'scanline50', 'disabled']
GNGEO_BLITTERS = ['default', 'soft', 'yuv']
GNGEO_GAME_COUNTRIES = {'Default':'default', 'Japan':'japan', 'Asia':'asia', 'USA':'usa', 'Europe':'europe'}
GNGEO_VIDEO_SCALINGS = ['default', '1', '2', '3']
GNGEO_KEYBOARD_KEYCODES = {'A': 'K97', 'B': 'K98', 'C': 'K99', 'D': 'K100', 'E': 'K101', 'F': 'K102', 'G': 'K103', 'H': 'K104', 'I': 'K105', 'J': 'K106', 'K': 'K107', 'L': 'K108', 'M': 'K109', 'N': 'K110', 'O': 'K111', 'P': 'K112', 'Q': 'K113', 'R': 'K114', 'S': 'K115', 'T': 'K116', 'U': 'K117', 'V': 'K118', 'W': 'K119', 'X': 'K120', 'Y': 'K121', 'Z': 'K122', '0': 'K256', 'Numeric keypad 1': 'K257', 'Numeric keypad 2': 'K258', 'Numeric keypad 3': 'K259', 'Numeric keypad 4': 'K260', 'Numeric keypad 5': 'K261', 'Numeric keypad 6': 'K262', 'Numeric keypad 7': 'K263', 'Numeric keypad 8': 'K264', 'Numeric keypad 9': 'K265', 'Numeric keypad PERIOD': 'K266', 'Numeric keypad DIVIDE': 'K267', 'Numeric keypad MULTIPLY': 'K268', 'Numeric keypad MINUS': 'K269', 'Numeric keypad PLUS': 'K270', 'Numeric keypad ENTER': 'K271', 'Numeric keypad EQUALS': 'K272', 'UP': 'K273', 'DOWN': 'K274', 'RIGHT': 'K275', 'LEFT': 'K276', 'Insert': 'K277', 'Home': 'K278', 'End': 'K279', 'Page up': 'K280', 'Page down': 'K281', 'Left bracket': 'K91', 'Backslash': 'K92', 'Right bracket': 'K93', 'Caret': 'K94', 'Underscore': 'K95', 'Backquote': 'K96', 'Exclamation': 'K33', 'QUOTEDBL': 'K34', 'Hash': 'K35', 'Dollar': 'K36', 'Ampersand': 'K38', 'Quote': 'K39', 'Left parenthesis': 'K40', 'Right parenthesis': 'K41', 'Asterish': 'K42', 'Plus': 'K43', 'Comma': 'K44', 'Minus': 'K45', 'Period': 'K46', 'Slash': 'K47', '0': 'K48', '1': 'K49', '2': 'K50', '3': 'K51', '4': 'K52', '5': 'K53', '6': 'K54', '7': 'K55', '8': 'K56', '9': 'K57', 'Colon': 'K58', 'Semicolon': 'K59', 'Less than': 'K60', 'Equals': 'K61', 'Greater than': 'K62', 'Question mark': 'K63', 'AT': 'K64'}
GNGEO_GAMEPAD1_KEYCODES = {'1': 'J0B0', '2': 'J0B1', '3': 'J0B2', '4': 'J0B3', '5': 'J0B4', '6': 'J0B5', '7': 'J0B6', '8': 'J0B7', '9': 'J0B8', 'Select': 'J0B9', 'Start': 'J0B10', 'Up': 'J0a1', 'Down': 'J0a1', 'Left': 'J0A0', 'Right': 'J0A0'}
GNGEO_GAMEPAD2_KEYCODES = {'1': 'J1B0', '2': 'J1B1', '3': 'J1B2', '4': 'J1B3', '5': 'J1B4', '6': 'J1B5', '7': 'J1B6', '8': 'J1B7', '9': 'J1B8', 'Select': 'J1B9', 'Start': 'J1B10', 'Up': 'J1a1', 'Down': 'J1a1', 'Left': 'J1A0', 'Right': 'J1A0'}
GNGEO_CONTROLLERS = ['Keyboard', 'Gamepad 1', 'Gamepad 2']
GNGEO_ROMS_LIST = {'nam1975': 'NAM-1975', 'bstars': 'Baseball Stars Professional', 'tpgolf': 'Top Player\'s Golf', 'mahretsu': 'Mahjong Kyoretsuden', 'maglord': 'Magician Lord (set 1)', 'maglordh': 'Magician Lord (set 2)', 'ridhero': 'Riding Hero (set 1)', 'ridheroh': 'Riding Hero (set 2)', 'alpham2': 'Alpha Mission II / ASO II - Last Guardian', 'ncombat': 'Ninja Combat', 'cyberlip': 'Cyber-Lip', 'superspy': 'The Super Spy', 'mutnat': 'Mutation Nation', 'kotm': 'King of the Monsters', 'sengoku': 'Sengoku / Sengoku Denshou (set 1)', 'sengokh': 'Sengoku / Sengoku Denshou (set 2)', 'burningf': 'Burning Fight (set 1)', 'burningh': 'Burning Fight (set 2)', 'lbowling': 'League Bowling', 'gpilots': 'Ghost Pilots', 'joyjoy': 'Puzzled / Joy Joy Kid', 'bjourney': 'Blue\'s Journey / Raguy', 'quizdais': 'Quiz Daisousa Sen - The Last Count Down', 'lresort': 'Last Resort', 'eightman': 'Eight Man', 'minasan': 'Minnasanno Okagesamadesu', 'legendos': 'Legend of Success Joe / Ashitano Joe Densetsu', '2020bb': '2020 Super Baseball (set 1)', '2020bbh': '2020 Super Baseball (set 2)', 'socbrawl': 'Soccer Brawl', 'roboarmy': 'Robo Army', 'fatfury1': 'Fatal Fury - King of Fighters / Garou Densetsu - shukumei no tatakai', 'fbfrenzy': 'Football Frenzy', 'bakatono': 'Bakatonosama Mahjong Manyuki', 'crsword': 'Crossed Swords', 'trally': 'Thrash Rally', 'kotm2': 'King of the Monsters 2 - The Next Thing', 'sengoku2': 'Sengoku 2 / Sengoku Denshou 2', 'bstars2': 'Baseball Stars 2', 'quizdai2': 'Quiz Meintantei Neo Geo - Quiz Daisousa Sen Part 2', '3countb': '3 Count Bout / Fire Suplex', 'aof': 'Art of Fighting / Ryuuko no Ken', 'samsho': 'Samurai Shodown / Samurai Spirits', 'tophuntr': 'Top Hunter - Roddy & Cathy', 'fatfury2': 'Fatal Fury 2 / Garou Densetsu 2 - arata-naru tatakai', 'janshin': 'Jyanshin Densetsu - Quest of Jongmaster', 'androdun': 'Andro Dunos', 'ncommand': 'Ninja Commando', 'viewpoin': 'Viewpoint', 'ssideki': 'Super Sidekicks / Tokuten Ou', 'wh1': 'World Heroes', 'kof94': 'The King of Fighters \'94', 'aof2': 'Art of Fighting 2 / Ryuuko no Ken 2', 'wh2': 'World Heroes 2', 'fatfursp': 'Fatal Fury Special / Garou Densetsu Special', 'savagere': 'Savage Reign / Fu\'un Mokushiroku - kakutou sousei', 'fightfev': 'Fight Fever / Crystal Legacy', 'ssideki2': 'Super Sidekicks 2 - The World Championship / Tokuten Ou 2 - real fight football', 'spinmast': 'Spinmaster / Miracle Adventure', 'samsho2': 'Samurai Shodown II / Shin Samurai Spirits - Haohmaru jigokuhen', 'wh2j': 'World Heroes 2 Jet', 'wjammers': 'Windjammers / Flying Power Disc', 'karnovr': 'Karnov\'s Revenge / Fighter\'s History Dynamite', 'gururin': 'Gururin', 'pspikes2': 'Power Spikes II', 'fatfury3': 'Fatal Fury 3 - Road to the Final Victory / Garou Densetsu 3 - haruka-naru tatakai', 'panicbom': 'Panic Bomber', 'aodk': 'Aggressors of Dark Kombat / Tsuukai GANGAN Koushinkyoku', 'sonicwi2': 'Aero Fighters 2 / Sonic Wings 2', 'zedblade': 'Zed Blade / Operation Ragnarok', 'galaxyfg': 'Galaxy Fight - Universal Warriors', 'strhoop': 'Street Hoop / Street Slam / Dunk Dream', 'quizkof': 'Quiz King of Fighters', 'ssideki3': 'Super Sidekicks 3 - The Next Glory / Tokuten Ou 3 - eikoue no michi', 'doubledr': 'Double Dragon (Neo-Geo)', 'pbobblen': 'Puzzle Bobble / Bust-A-Move (Neo-Geo)', 'kof95': 'The King of Fighters \'95', 'tws96': 'Tecmo World Soccer \'96', 'samsho3': 'Samurai Shodown III / Samurai Spirits - Zankurou Musouken', 'stakwin': 'Stakes Winner / Stakes Winner - GI kinzen seihae no michi', 'pulstar': 'Pulstar', 'whp': 'World Heroes Perfect', 'kabukikl': 'Kabuki Klash - Far East of Eden / Tengai Makyou Shinden - Far East of Eden', 'neobombe': 'Neo Bomberman', 'gowcaizr': 'Voltage Fighter - Gowcaizer / Choujin Gakuen Gowcaizer', 'rbff1': 'Real Bout Fatal Fury / Real Bout Garou Densetsu', 'aof3': 'Art of Fighting 3 - The Path of the Warrior / Art of Fighting - Ryuuko no Ken Gaiden', 'sonicwi3': 'Aero Fighters 3 / Sonic Wings 3', 'turfmast': 'Neo Turf Masters / Big Tournament Golf', 'mslug': 'Metal Slug - Super Vehicle-001', 'puzzledp': 'Puzzle De Pon', 'mosyougi': 'Syougi No Tatsujin - Master of Syougi', 'marukodq': 'Chibi Marukochan Deluxe Quiz', 'neomrdo': 'Neo Mr. Do!', 'sdodgeb': 'Super Dodge Ball / Kunio no Nekketsu Toukyuu Densetsu', 'goalx3': 'Goal! Goal! Goal!', 'overtop': 'Over Top', 'neodrift': 'Neo Drift Out - New Technology', 'kof96': 'The King of Fighters \'96', 'ssideki4': 'The Ultimate 11 / Tokuten Ou - Honoo no Libero', 'kizuna': 'Kizuna Encounter - Super Tag Battle / Fu\'un Super Tag Battle', 'ninjamas': 'Ninja Master\'s - haoh-ninpo-cho', 'ragnagrd': 'Operation Ragnagard / Shin-Oh-Ken', 'pgoal': 'Pleasure Goal / Futsal - 5 on 5 Mini Soccer', 'magdrop2': 'Magical Drop II', 'samsho4': 'Samurai Shodown IV - Amakusa\'s Revenge / Samurai Spirits - Amakusa Kourin', 'rbffspec': 'Real Bout Fatal Fury Special / Real Bout Garou Densetsu Special', 'twinspri': 'Twinkle Star Sprites', 'wakuwak7': 'Waku Waku 7', 'stakwin2': 'Stakes Winner 2', 'breakers': 'Breakers', 'miexchng': 'Money Puzzle Exchanger / Money Idol Exchanger', 'kof97': 'The King of Fighters \'97', 'magdrop3': 'Magical Drop III', 'lastblad': 'The Last Blade / Bakumatsu Roman - Gekkano Kenshi', 'puzzldpr': 'Puzzle De Pon R', 'popbounc': 'Pop \'n Bounce / Gapporin', 'shocktro': 'Shock Troopers', 'shocktrj': 'Shock Troopers (Japan)', 'blazstar': 'Blazing Star', 'rbff2': 'Real Bout Fatal Fury 2 - The Newcomers / Real Bout Garou Densetsu 2 - the newcomers', 'mslug2': 'Metal Slug 2 - Super Vehicle-001/II', 'kof98': 'The King of Fighters \'98 - The Slugfest / King of Fighters \'98 - dream match never ends', 'lastbld2': 'The Last Blade 2 / Bakumatsu Roman - Dai Ni Maku Gekkano Kenshi', 'neocup98': 'Neo-Geo Cup \'98 - The Road to the Victory', 'breakrev': 'Breakers Revenge', 'shocktr2': 'Shock Troopers - 2nd Squad', 'flipshot': 'Battle Flip Shot', 'pbobbl2n': 'Puzzle Bobble 2 / Bust-A-Move Again (Neo-Geo)', 'ctomaday': 'Captain Tomaday', 'mslugx': 'Metal Slug X - Super Vehicle-001', 'kof99p': 'The King of Fighters \'99 - Millennium Battle (prototype)', 'garoup': 'Garou - Mark of the Wolves (prototype)', 'pbobble': 'game pbobble MVS ', 'kof99': 'The King of Fighters \'99 - Millennium Battle', 'garou': 'Garou - Mark of the Wolves (set 1)', 'kof2000n': 'The King of Fighters 2000 (Encrypted GFX)', 'mslug3n': 'Metal Slug 3 (Encrypted GFX)', 'kof2001n': 'The King ofFighter 2001 (non encrypted)', 'kof2003a': 'KoF 2003a', 'kof2003b': 'KoF 2003', 'kof2k2': 'The King of Fighter 2002', 'kof2003': 'KoF 2003', 'kof2002': 'KoF 2002', 'rodd': 'Rage of the dragons (decrypted)', 'pim': 'Power Instinct - Matrimelee', 'svcplus': 'SNK vs Capcom - SVC Chaos', 'ncombata': 'ncombata', 'kotmh': 'kotmh', '2020bba': '2020bba', 'roboarma': 'roboarma', 'tophunta': 'tophunta', 'wh1h': 'wh1h', 'aof2a': 'aof2a', 'fatfursa': 'fatfursa', 'fightfva': 'fightfva', 'pbobblna': 'pbobblna', 'kof95a': 'kof95a', 'samsho3a': 'samsho3a', 'zintrckb': 'zintrckb', 'kof96h': 'kof96h', 'ghostlop': 'ghostlop', 'kof97a': 'kof97a', 'kof97pls': 'kof97pls', 'lastblda': 'lastblda', 'shocktra': 'shocktra', 'rbff2a': 'rbff2a', 'kof98k': 'kof98k', 'kof98n': 'kof98n', 'mslug5': 'Metal Slug 5', 'samsho5sp': 'Samurai Shodown 5 Special', 'kof2k1rp': 'The King of Fighters 2001 plus', 'cthd2003': 'Crouching Tiger Hidden Dragon ', 'kof2k2pls': 'The King of Fighter 2002 plus', 'kof2k4es': 'The King of Fighters 2004 hack', 'ssvsp': 'ssvsp', 'nitd': 'Nightmare in the Dark', 'sengoku3': 'sengoku3', 'preisle2': 'Prehistoric Island 2', 'bangbead': 'Bang Bead', 'jockeygp': 'Jockey Grandprix', 'mslug3': 'Metal Slug 3', 'mslug4': 'Metal Slug 4(non encrypted)', 'neopong': 'Neopong 1.1', 'pochi': 'Pochi and Nyaa', 'samsho5': 'Samurai Shodown 5', 's1945p': 'Striker 1945 Plus', 'kof10thu': 'The King of Fighters 10th Unique hack', 'kog': 'The King of Gladiator', 'zupapa': 'Zupapa', 'cthd2003sp': 'Crouching Tiger Hidden Dragon Plus'}

class GnGeo():

    def __init__(self):

        self.version = 0.0
        self.copyright = ''
        self.exe = ''
        self.exe_dir = ''
        self.datafile = ''
        self.scale = 'default'
        self.autoframeskip = True
        self.interpolation = True
        self.blitter = 'default'
        self.effect = 'default'
        self.hwsurface = True
        self.vsync = False
        self.country = 'default'
        self.fullscreen = False
        self.joystick = True
        self.samplerate = 'default'
        self.sound = True
        self.p1control = ''
        self.p2control = ''

    def set_exe(self, _exe_path, _data_path, _exe_dir):

        command_buffer = 'LD_LIBRARY_PATH=\"$LD_LIBRARY_PATH\":' + '\"' + _exe_dir + '\" ' + '\"' + _exe_path + '\"' + ' --version'
        command = popen(command_buffer)
        command_output = command.read()

        if command.close() == None:

            for command_output_line in command_output.split('\n'):

                if command_output_line.split(' ')[0] == 'Gngeo':

                    self.version = command_output_line.split(' ')[1]

                elif command_output_line.split(' ')[0] == 'Copyright':

                    self.copyright = command_output_line

            self.exe = _exe_path
            self.datafile = _data_path
            self.exe_dir = _exe_dir

            return 0

        else:

            return 1

    def run_game(self, _rom, _rom_path):

        command_buffer = ""
        command_arguments = ""

        if (self.scale != '1' and self.scale != 'default' and self.scale != 'disabled'):

            command_arguments += ' --scale=' + self.scale

        if (self.autoframeskip == True):

            command_arguments += ' --autoframeskip'

        else:

            command_arguments += ' --no-autoframeskip'

        if (self.interpolation == True):

            command_arguments += ' --interpolation'

        else:

            command_arguments += ' --no-interpolation'

        if (self.blitter == 'default'):

            command_arguments += ' --blitter=soft'

        else:

            command_arguments += ' --blitter=' + self.blitter

        if (self.effect == 'default'):

            command_arguments += ' --effect=hq2x'

        else:

            command_arguments += ' --effect=' + self.effect

        if (self.hwsurface == True):

            command_arguments +=  ' --hwsurface'

        else:

            command_arguments += ' --no-hwsurface'

        if (self.vsync == True):

            command_arguments += ' --vsync'

        else:

            command_arguments += ' --no-vsync'

        if (self.country != 'default'):

            command_arguments += ' --country=' + self.country

        if (self.fullscreen == True):

            command_arguments += ' --fullscreen'

        else:

            command_arguments += ' --no-fullscreen'

        if (self.joystick == True):

            command_arguments += ' --joystick'

        else:

            command_arguments += ' --no-joystick'

        if (self.samplerate != 'default' and self.sound == True):

            command_arguments += ' --samplerate=' + self.samplerate

        if (self.sound == True):

            command_arguments += ' --sound'

        else:

            command_arguments += ' --no-sound'

        if (self.p1control != ''):

            command_arguments += ' --p1control=' + self.p1control

        if (self.p2control != ''):

            command_arguments += ' --p2control=' + self.p2control

        command_buffer = 'LD_LIBRARY_PATH=\"$LD_LIBRARY_PATH\":' + '\"' + self.exe_dir + '\" ' + '\"' + self.exe + '\"' + ' --datafile=' + '\"' + self.datafile + '\"' + ' --rompath=' + '\"' + _rom_path + '\"' + command_arguments + ' ' + _rom

        print('Shopne Arcade: loading game ...\n', command_buffer, '\n')

        command = popen(command_buffer)
        command_output = command.read()

        print('Shopne Arcade: GnGeo output\n', command_output, '\n')

        if command.close() == None:
            return 0
        return 1
