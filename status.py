from config import blocks, delay, xrdb
from functions import *
from time import sleep
from common import xresources


# Keymap | Volume | Brightness | Battery | Time
def set_status(text: str) -> None:
    subprocess.run(["xsetroot", "-name", text])


def mainloop():
    print("(+) Starting mainloop")
    try:
        while True:
            res = ""
            for block in blocks:
                # print(*block[2])
                res += block[1] % (block[0](*block[2]))
            set_status(res)
            # print(f"\"{res}\"")
            sleep(delay)
    except KeyboardInterrupt:
        print("\n(*) Goodbye")
    except NameError:
        print("(-) Wrong configuration")


mainloop()
