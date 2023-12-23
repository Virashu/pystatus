"""Main file"""

import subprocess
from time import sleep

from config import blocks, delay


# Keymap | Volume | Brightness | Battery | Time
def set_status(text: str) -> None:
    subprocess.run(["xsetroot", "-name", text], check=False)


DEBUG = False


if __name__ == "__main__":
    print("(+) Starting mainloop")
    try:
        while True:
            res = ""
            for block in blocks:
                r = block[0](*block[2])
                l = block[1] % r
                res += l
            set_status(res)
            if DEBUG:
                with open("log.txt", "w", encoding="utf-8") as f:
                    f.write(res)
            sleep(delay)
    except KeyboardInterrupt:
        print("\n(*) Goodbye")
    except NameError:
        print("(-) Wrong configuration")
