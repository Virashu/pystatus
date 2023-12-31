from typing import Any, Callable
from functions import *


StatusLine = tuple[tuple[Callable[..., Any], str, list[Any]], ...]


delay = 0.25

# Command      Args
#
# command      command to be executed
# keymap       none
# volume       none
# whitespace   count of whitespace symbols
# datetime     format of date and time


# fmt: off
circles: StatusLine = (
    # Tray triangle button #
    (text,          "\x06\x07%s ",                                     []),
    (command,       " %s ",                                             ["bash /home/virashu/scripts/music.sh"]),

    # Keymap segment #
    (command,       "\x01^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
    (keymap,        "%s",                                               []),
    (command,        "^b%s^",                                           ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
    
    # Volume segment #
    (command,       "\x02^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (volume_icon,   " %s ",                                             []),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    
    # Battery segment #
    (command,       "\x04^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
    (battery_icon,  " %s ",                                             []),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
    
    # Time segment #
    (command,       "\x05^d^^c%s^",                                    ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (datetime,      "%s",                                               ["%H:%M"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
)

circles_mono: StatusLine = (
    # Tray triangle button #
    (text,          "\x06\x07%s ",                                     []),
    (command,       "%s",                                               ["bash /home/virashu/scripts/music.sh"]),

    # Keymap segment #
    (command,       "\x01^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (keymap,        "%s",                                               []),
    (command,        "^b%s^",                                           ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    
    # Volume segment #
    (command,       "\x02^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (volume_icon,  " %s ",                                              []),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    
    # Battery segment #
    (command,       "\x04^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (battery_icon,  " %s ",                                             []),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    
    # Time segment #
    (command,       "\x05^d^^c%s^",                                    ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (datetime,      "%s",                                               ["%H:%M"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
   #(command,       ";%s",                                              ["bash /home/virashu/scripts/music.sh clean"]),
)

collapsed: StatusLine = (
    (text,          "\x06\x07%s ",                                     []),
    (command,       "%s",                                               ["bash /home/virashu/scripts/music.sh"]),
    (command,       "\x01^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
    (keymap,        " %s ",                                             []),
    (command,       "\x02^b%s^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^^d^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (volume_icon,   "  %s  ",                                           []),
    (command,       "\x04^b%s^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^^d^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
    (battery_icon,  "  %s  ",                                           []),
    (command,       "\x05^b%s^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^",                                           ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (datetime,      " %s ",                                             ["%H:%M"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^d^^c%s^^d^ ",                                    ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
)

blocks: StatusLine = collapsed

# fmt: on
