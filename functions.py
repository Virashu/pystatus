import subprocess
from constants import *


def get(cmd: str) -> str:
    """Get command output"""
    try:
        out: str = (
            subprocess.check_output(cmd, shell=True, text=True, encoding="utf-8")
            .rstrip("\n")
            .strip("\n")
        )
    except UnicodeDecodeError:
        out = ""
    except UnicodeError:
        out = ""

    return out


def get_command(command: str) -> str:
    """Get command output"""
    return get(command)


def get_keymap() -> str:
    """Keyboard layout"""
    return get(keymap_cmd)


def get_volume() -> str:
    """Volume level"""
    res = get(volume_cmd)
    if "Failed" in res:
        return ""
    return res


def get_mute() -> bool:
    """Mute state"""
    return "yes" in get(mute_cmd)


def get_charge_level() -> int:
    """Charge level"""
    raw = get(charge_cmd)
    if raw == "":
        return 0
    return int(raw)


def get_charge_state() -> str:
    """Charge state

    ('charging', 'discharging', 'full')
    """
    return get(state_cmd).lower()


def get_volume_icon() -> str:
    """Volume icon"""
    res = get_volume()
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


def get_battery_icon() -> str:
    """Battery icon"""
    charge = get_charge_level()
    state = get_charge_state()
    return BATTERY_LEVELS[state][charge // 10]
