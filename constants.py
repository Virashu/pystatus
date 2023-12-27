"Constants"


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
# brightness_cmd = "light -G | cut -d'.' -f1"
brightness_cmd = "xbacklight -get"
