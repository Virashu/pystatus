import datetime
import subprocess
from time import sleep, localtime, strftime


# volume_cmd = "pactl get-sink-volume 0 | awk '$0~/%/ {print $5}' | tr -d '[%]'"
# mute_cmd = "pactl get-sink-mute 0"
# charge_cmd = "upower -i /org/freedesktop/UPower/devices/battery_BAT1 | grep percentage | grep -o \"[0-9]*\""
# state_cmd = "upower -i /org/freedesktop/UPower/devices/battery_BAT1 | grep state | grep -o \"\\w*$\""
# keymap_cmd = "setxkbmap -query | grep 'layout' | awk '$0~/ / {print $2}'"
# brightness_cmd = "light -G | cut -d'.' -f1"

volume_cmd = "pactl get-sink-volume @DEFAULT_SINK@ | grep -Po '[0-9]{1,3}(?=%)' | head -1"
mute_cmd = "pactl get-sink-mute @DEFAULT_SINK@ | greap -Po '(?<=Mute: )(yes|no)'"
charge_cmd = "cat /sys/class/power_supply/{}/capacity"
state_cmd = "cat /sys/class/power_supply/{}/status"
keymap_cmd = "setxkbmap -query | grep 'layout' | awk '$0~/ / {print $2}' | tr ',' '\n' | head -1"
brightness_cmd = "xbacklight -get"


def command(cmd: str) -> str:
    return get(cmd)


def get(cmd) -> str:
    out = subprocess.getoutput(cmd).rstrip('\n ').strip('\n ')
    return out


def get_bat_icon() -> str:
    charge = int(get(charge_cmd))
    state = get(state_cmd)
    levels = {"charging": ['󰢟', '󰢜', '󰂆', '󰂇', '󰂈', '󰢝', '󰂉', '󰢞', '󰂊', '󰂋', '󰂅'],
              "discharging": ['󱃍', '󰁺', '󰁻', '󰁼', '󰁽', '󰁾', '󰁿', '󰂀', '󰂁', '󰂂', '󰁹']}
    return levels[state][charge // 10]


def get_vol_icon():
    vol = int(get(volume_cmd))
    mute = get(mute_cmd)
    if mute == "Mute: yes":
        if vol == 0:
            return "󰸈"
        return "󰖁"
    if vol > 67:
        return "󰕾"
    if vol > 33:
        return "󰖀"
    if vol > 0:
        return "󰕿"
    return "󰝟"


# Shortcuts


def datetime(frm: str) -> str:
    return strftime(frm, localtime())


def keymap() -> str:
    return get(keymap_cmd)


def volume() -> str:
    return get(volume_cmd)


def mute() -> str:
    return get(mute_cmd)


def whitespace(count: int) -> str:
    return ' ' * count