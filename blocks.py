"""Contains the blocks used in the status bar"""
import abc
import time
from typing import Iterable

from functions import *


class Block(abc.ABC):
    """A block in the status bar"""

    @abc.abstractmethod
    def render(self) -> str:
        """
        Render the block
        """


class Text(Block):
    """Plain text"""

    def __init__(self, text: str):
        self.text = text

    def render(self) -> str:
        return self.text


class Space(Block):
    """Spacing"""

    def __init__(self, size: int = 1):
        self.size = size

    def render(self) -> str:
        return " " * self.size


class Command(Block):
    def __init__(self, command: str, format_: str = ""):
        super().__init__()
        self.command = command
        self.format = format_

    def render(self) -> str:
        return get_command(self.command).format(self.format)


class Keymap(Block):
    """Keyboard layout"""

    def render(self) -> str:
        return get_keymap()


class VolumeIcon(Block):
    """Volume icon"""

    def render(self) -> str:
        return get_volume_icon()


class BatteryIcon(Block):
    """Battery icon"""

    def render(self) -> str:
        return get_battery_icon()


class DateTime(Block):
    """Date and time"""

    def __init__(self, format_: str):
        self.format = format_

    def render(self) -> str:
        return time.strftime(self.format, time.localtime())


StatusLine = Iterable[Block]
