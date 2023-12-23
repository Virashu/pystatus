from functions import *
import subprocess
import re


delay = .25

# Command      Args
#
# command      command to be executed
# keymap       none
# volume       none
# whitespace   count of whitespace symbols
# datetime     format of date and time

circles = (
    # Tray triangle button #
    (text,          "\x06\x07%s ",                                     []),
   #(command,       "%s ",                                              ["bash ~/scripts/bluetooth.sh"]),
    (command,       " %s ",                                             ["bash /home/virashu/scripts/music.sh"]),
    # Keymap segment #
    (command,        "\x01^b%s^",                                       ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^^d^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
    (keymap,        "%s",                                               []),
   #(command,       " %s ",                                             ["bash /home/virashu/scripts/emoji.sh $(setxkbmap -query | grep \"layout\" | awk '$0~/ / {print $2}' | tr ',' '\\n' | head -1)"]), (command,        "^b%s^",                                           ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
    # Volume segment #
    (command,       "\x02^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]), (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]), (command,       " %s ",                                             ["~/Documents/volume.sh"]),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    # Battery segment #
    (command,       "\x04^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
    (command,       " %s ",                                             ["~/Documents/battery.sh"]),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
    # Time segment #
    (command,       "\x05^d^^c%s^",                                    ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (datetime,      "%s",                                               ["%H:%M"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
)

circles_mono = (
    # Tray triangle button #
    (text,          "\x06\x07%s ",                                     []),
   #(command,       "%s ",                                              ["bash ~/scripts/bluetooth.sh"]),
    (command,       "%s",                                               ["bash /home/virashu/scripts/music.sh"]),
    # Keymap segment #
    (command,        "\x01^b%s^",                                       ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^^d^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (keymap,        "%s",                                               []),
   #(command,       " %s ",                                             ["bash /home/virashu/scripts/emoji.sh $(setxkbmap -query | grep \"layout\" | awk '$0~/ / {print $2}' | tr ',' '\\n' | head -1)"]), (command,        "^b%s^",                                           ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    # Volume segment #
    (command,       "\x02^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (get_vol_icon,  " %s ",                                             []),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    # Battery segment #
    (command,       "\x04^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (get_bat_icon,  " %s ",                                             []),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    # Time segment #
    (command,       "\x05^d^^c%s^",                                    ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (datetime,      "%s",                                               ["%H:%M"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
   #(command,       ";%s",                                              ["bash /home/virashu/scripts/music.sh clean"]),
)

collapsed = (
    (text,          "\x06\x07%s ",                                     []),
   #(command,       "\x06'%s'\x07 ",                                    ["bash /home/virashu/scripts/trayicon.sh get"]),
   #(command,       "%s ",                                              ["bash ~/scripts/bluetooth.sh"]),
    (command,       "\x01^b%s^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^^d^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
    (keymap,        " %s ",                                             []),
   #(command,       " %s ",                                             ["bash /home/virashu/scripts/emoji.sh $(setxkbmap -query | grep \"layout\" | awk '$0~/ / {print $2}' | tr ',' '\\n' | head -1)"]),
    (command,       "\x02^b%s^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^^d^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "  %s  ",                                           ["~/Documents/volume.sh"]),
    (command,       "\x04^b%s^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^^d^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "  %s  ",                                           ["~/Documents/battery.sh"]),
    (command,       "\x05^b%s^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^",                                           ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^c%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (datetime,      " %s ",                                             ["%H:%M"]),
    (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^d^^c%s^^d^ ",                                    ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
)

blocks = circles_mono

