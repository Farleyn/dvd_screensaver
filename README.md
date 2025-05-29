# DVD Screensaver Simulator

A console-based recreation of the classic DVD Screensaver. The "DVD" logo moves around the terminal window at 29.97 FPS, bouncing off edges and changing color with every bounce.

## Features

- Runs in a standard terminal (xterm, Windows Terminal, iTerm2, etc.).
- Utilizes the Alternate Screen Buffer so there is no scrollback history.
- High-precision frame timing based on `time.perf_counter()`.
- Original DVD screensaver colors: red, green, yellow, blue, magenta, cyan, white.
- Exits cleanly on Ctrl+C, returning you to the main terminal buffer.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Farleyn/dvd-screensaver.git
   cd dvd-screensaver
   ```
2. Ensure you have Python 3.6 or later installed.

## Usage

```bash
python dvd_screensaver.py
```

Press `Ctrl+C` to exit and return to your main terminal buffer.
