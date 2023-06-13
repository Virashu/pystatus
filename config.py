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

# out = subprocess.getoutput("xrdb -query")
# sel = re.findall(r"dwm.selbgcolor:\t(#[0-9qbcdef]{6})", out)[0]
# print(sel)

#󰂯󰂱
blocks = (
    # command       str                              args
    # (keymap,        "\x01^b#383838^ %s ",            []),
    # (command,       "\x02^b#484848^  %s  ",          ["~/Documents/volume.sh"]),
    # (command,       "\x04^b#585858^  %s  ",          ["~/Documents/battery.sh"]),
    # # (datetime,      f"\x05^b{sel}^^c#282828^  %s  ^b#282828^",    ["%H:%M"]),
    # (command,       "\x05^b%s",                      ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    # (datetime,      "^^c#282828^  %s  ^b#282828^",   ["%H:%M"]),
    # # (whitespace,    "%s",       [20]),
    (text,          "\x06\x07%s ",                                        []),
    #(command,       "%s ",                                             ["bash ~/scripts/bluetooth.sh"]),
    #(text,          "%s",                                             []),
    (keymap,        "\x01^b%s^^c#3c3836^^d^^b#3c3836^ %s ",       []),
    (command,       "\x02^b#3c3836^^c#504945^^d^^b#504945^  %s  ",     ["~/Documents/volume.sh"]),
    (command,       "\x04^b#504945^^c#665c54^^d^^b#665c54^  %s  ",     ["~/Documents/battery.sh"]),
    (command,       "\x05^b#665c54^^c%s^",                              ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (command,       "^b%s^",                                           ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
    (datetime,      "^c#282828^  %s  ^b#282828^",                       ["%H:%M"]),
    (command,       "^d^^c%s^^d^ ",                                    ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
)
