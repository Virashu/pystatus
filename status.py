"""Main file"""

import subprocess
from time import sleep

from config import DELAY, STATUS


def set_status(text: str) -> None:
    subprocess.run(["xsetroot", "-name", text], check=False)


DEBUG = False


print("(+) Starting mainloop")

try:
    while True:
        res: str = ""

        for block in STATUS:
            res += block.render()

        set_status(res)
        sleep(DELAY)

except KeyboardInterrupt:
    print("\n(*) Goodbye")
except NameError:
    print("(-) Wrong configuration")
