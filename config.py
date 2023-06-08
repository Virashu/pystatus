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

out = subprocess.getoutput("xrdb -query")
sel = re.findall(r"dwm.selbgcolor:\t(#[0-9qbcdef]{6})", out)[0]
# print(sel)


blocks = (
    # command       str         args
    (keymap,        "\x01^b#383838^ %s ",    []),
    (command,       "\x02^b#484848^  %s  ",    ["~/Documents/volume.sh"]),
    (command,       "\x04^b#585858^  %s  ",    ["~/Documents/battery.sh"]),
    (datetime,      f"\x05^b{sel}^^c#282828^  %s  ^b#282828^",    ["%H:%M"]),
    # (whitespace,    "%s",       [20]),
)
