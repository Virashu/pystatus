import subprocess
from time import localtime, strftime

from constants import *


def get(cmd: str) -> str:
    out = subprocess.getoutput(cmd).rstrip("\n").strip("\n")
    return out


def command(cmd: str) -> str:
    return get(cmd)


def text() -> str:
    return ""


def battery_icon() -> str:
    charge = get_charge_level()
    state = get_charge_state_raw()
    return BATTERY_LEVELS[state][charge // 10]


def volume_icon():
    res = volume()
    if res == "":
        return ""

    vol = int(res)
    mute = get_mute()

    if mute:
        return "󰖁" if vol > 0 else "󰸈"

    if vol > 67:
        return "󰕾"
    if vol > 33:
        return "󰖀"
    if vol > 0:
        return "󰕿"
    return "󰝟"


# Shortcuts


def datetime(format_: str) -> str:
    return strftime(format_, localtime())


def keymap() -> str:
    return get(keymap_cmd)


def volume() -> str:
    res = get(volume_cmd)
    if "Failed" in res:
        return ""
    return res


def get_mute_raw() -> str:
    return get(mute_cmd)


def get_mute() -> bool:
    return get_mute_raw() == "Mute: yes"


def get_charge_level() -> int:
    return int(get(charge_cmd))


def get_charge_state_raw() -> str:
    return get(state_cmd).lower()


def whitespace(count: int) -> str:
    return " " * count


# ?
def load_xresources(resources: dict[str, str]) -> None:
    r = get("xrdb -query")
    for i in r.splitlines():
        k, v = i.split()
        resources[k] = v


def xres(name: str) -> str:
    return get("xrdb -query")
