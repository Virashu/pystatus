from config import blocks, delay
from functions import *
from time import sleep


# Keymap | Volume | Brightness | Battery | Time
def set_status(text: str) -> None:
    subprocess.run(["xsetroot", "-name", text])

debug = False
def mainloop():
    print("(+) Starting mainloop")
    try:
        while True:
            res = ""
            for block in blocks:
                r = (block[0](*block[2]))
                l = block[1] % r
                res += l
            set_status(res)
            if debug:
                print("bruh")
                with open("log.txt", "w") as f:
                    f.write(res)
            sleep(delay)
    except KeyboardInterrupt:
        print("\n(*) Goodbye")
    except NameError:
        print("(-) Wrong configuration")


mainloop()
