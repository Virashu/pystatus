"constants"


# volume_cmd = "pactl get-sink-volume 0 | awk '$0~/%/ {print $5}' | tr -d '[%]'"
# mute_cmd = "pactl get-sink-mute 0"
# charge_cmd = "upower -i /org/freedesktop/UPower/devices/battery_BAT1 | grep percentage | grep -o \"[0-9]*\""
# state_cmd = "upower -i /org/freedesktop/UPower/devices/battery_BAT1 | grep state | grep -o \"\\w*$\""
# keymap_cmd = "setxkbmap -query | grep 'layout' | awk '$0~/ / {print $2}'"
# brightness_cmd = "light -G | cut -d'.' -f1"


_battery_charging = ["󰢟", "󰢜", "󰂆", "󰂇", "󰂈", "󰢝", "󰂉", "󰢞", "󰂊", "󰂋", "󰂅"]
_battery_discharging = ["󱃍", "󰁺", "󰁻", "󰁼", "󰁽", "󰁾", "󰁿", "󰂀", "󰂁", "󰂂", "󰁹"]

BATTERY_LEVELS = {
    "charging": _battery_charging,
    "discharging": _battery_discharging,
}


volume_cmd = (
    "pactl get-sink-volume @DEFAULT_SINK@ | grep -Po '[0-9]{1,3}(?=%)' | head -1"
)
mute_cmd = "pactl get-sink-mute @DEFAULT_SINK@ | grep -Po '(?<=Mute: )(yes|no)'"
charge_cmd = "cat /sys/class/power_supply/BAT1/capacity"
state_cmd = "cat /sys/class/power_supply/BAT1/status"
keymap_cmd = (
    "setxkbmap -query | grep 'layout' | awk '$0~/ / {print $2}' | tr ',' '\n' | head -1"
)
brightness_cmd = "xbacklight -get"
