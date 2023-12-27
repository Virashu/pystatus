from blocks import Text, Command, Keymap, VolumeIcon, BatteryIcon, StatusLine, DateTime


DELAY = 0.25

color_command = "xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"
alt_color_command = "xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"

circles_mono: StatusLine = (
    # Tray triangle button #
    Text("\x06\x07"),
    Command("bash /home/virashu/scripts/music.sh", "{}"),
    # Keymap segment #
    Command(color_command, "\x01^d^^c{}^^d^"),
    Command(color_command, "^b{}^"),
    Keymap(),
    Command(color_command, "^d^^c{}^^d^\x07 "),
    # Volume segment #
    Command(color_command, "\x02^d^^c{}^^d^"),
    Command(color_command, "^b{}^"),
    VolumeIcon(),
    Command(color_command, "^d^^c{}^^d^\x07 "),
    # Battery segment #
    Command(color_command, "\x04^d^^c{}^^d^"),
    Command(color_command, "^b{}^"),
    BatteryIcon(),
    Command(color_command, "^d^^c{}^^d^\x07 "),
    # Time segment #
    Command(alt_color_command, "\x05^d^^c{}^"),
    Command(alt_color_command, "^b{}^"),
    Command("xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'", "^c{}^"),
    DateTime("%H:%M"),
    Command(alt_color_command, "^d^^c{}^^d^\x07 "),
    # Command("bash /home/virashu/scripts/music.sh clean", ";{}"),
)

STATUS: StatusLine = circles_mono

# circles: StatusLine = (
#     # Tray triangle button #
#     (text,          "\x06\x07%s ",                                     []),
#     (command,       " %s ",                                             ["bash /home/virashu/scripts/music.sh"]),

#     # Keymap segment #
#     (command,       "\x01^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
#     (keymap,        "%s",                                               []),
#     (command,        "^b%s^",                                           ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),

#     # Volume segment #
#     (command,       "\x02^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
#     (volume_icon,   " %s ",                                             []),
#     (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),

#     # Battery segment #
#     (command,       "\x04^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
#     (battery_icon,  " %s ",                                             []),
#     (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),

#     # Time segment #
#     (command,       "\x05^d^^c%s^",                                    ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^c%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
#     (datetime,      "%s",                                               ["%H:%M"]),
#     (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^d^^c%s^^d^\x07 ",                                ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
# )

# collapsed: StatusLine = (
#     (text,          "\x06\x07%s ",                                     []),
#     (command,       "%s",                                               ["bash /home/virashu/scripts/music.sh"]),
#     (command,       "\x01^d^^c%s^^d^",                                 ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
#     (keymap,        " %s ",                                             []),
#     (command,       "\x02^b%s^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg1:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^c%s^^d^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
#     (volume_icon,   "  %s  ",                                           []),
#     (command,       "\x04^b%s^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg2:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^c%s^^d^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
#     (battery_icon,  "  %s  ",                                           []),
#     (command,       "\x05^b%s^",                                        ["xrdb -query | grep -Po '(?<=\\*.bg3:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^c%s^",                                           ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^c%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
#     (datetime,      " %s ",                                             ["%H:%M"]),
#     (command,       "^b%s^",                                            ["xrdb -query | grep -Po '(?<=\\*.bg0:\\t)(#[0-9abcdef]{6})'"]),
#     (command,       "^d^^c%s^^d^ ",                                    ["xrdb -query | grep -Po '(?<=dwm.selbgcolor:\\t)(#[0-9abcdef]{6})'"]),
# )

# blocks: StatusLine = collapsed
