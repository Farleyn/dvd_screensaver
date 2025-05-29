import os
import sys
import time
import signal

# Settings
FRAME_RATE       = 29.97
FRAME_DURATION   = 1.0 / FRAME_RATE
TEXT             = "DVD"
COLOR_CODES      = [
    "\033[31m",  # red
    "\033[32m",  # green
    "\033[33m",  # yellow
    "\033[34m",  # blue
    "\033[35m",  # magenta
    "\033[36m",  # cyan
    "\033[37m",  # white
]

# ANSI escape codes
ENTER_ALT_BUFFER = "\033[?1049h"
EXIT_ALT_BUFFER  = "\033[?1049l"
CLEAR_SCREEN     = "\033[2J"
CURSOR_HOME      = "\033[H"
RESET_COLOR      = "\033[0m"

def get_terminal_size():
    try:
        sz = os.get_terminal_size()
        return max(sz.columns, len(TEXT) + 2), max(sz.lines, 3)
    except OSError:
        return len(TEXT) + 2, 3

def cleanup_and_exit(signum=None, frame=None):
    sys.stdout.write(EXIT_ALT_BUFFER + RESET_COLOR)
    sys.stdout.flush()
    sys.exit(0)

def draw_frame(x, y, width, height, color):
    sys.stdout.write(CLEAR_SCREEN + CURSOR_HOME)
    for row in range(height):
        if row == y:
            line = " " * x + color + TEXT + RESET_COLOR
            line += " " * (width - x - len(TEXT))
            sys.stdout.write(line + "\n")
        else:
            sys.stdout.write(" " * width + "\n")
    sys.stdout.flush()

def main():
    signal.signal(signal.SIGINT, cleanup_and_exit)
    sys.stdout.write(ENTER_ALT_BUFFER)
    sys.stdout.flush()

    width, height = get_terminal_size()
    x, y = 0, 0
    dx, dy = 1, 1
    color_index = 0

    last_time = time.perf_counter()

    while True:
        now = time.perf_counter()
        if now - last_time >= FRAME_DURATION:
            last_time += FRAME_DURATION

            draw_frame(x, y, width, height, COLOR_CODES[color_index])

            x += dx
            y += dy
            bounced = False

            if x + len(TEXT) >= width:
                x = width - len(TEXT); dx = -dx; bounced = True
            elif x <= 0:
                x = 0; dx = -dx; bounced = True

            if y >= height - 1:
                y = height - 1; dy = -dy; bounced = True
            elif y <= 0:
                y = 0; dy = -dy; bounced = True

            if bounced:
                color_index = (color_index + 1) % len(COLOR_CODES)
        else:
            time.sleep(0.001)

if __name__ == "__main__":
    main()
