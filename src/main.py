#!/usr/bin/env python3
import random
import sys
import time
import itertools
import os

def clear_terminal():
    os.system('clear')

color_codes = [
    "\033[1;31m",  # Red
    "\033[1;32m",  # Green
    "\033[1;33m",  # Yellow
    "\033[1;34m",  # Blue
    "\033[1;35m",  # Purple
    "\033[1;36m",  # Cyan
]
reset_color = "\033[0m"

def loading_spinner():
    spinner = itertools.cycle(["|", "/", "*", "\\"])
    color_iterator = itertools.cycle(color_codes)
    for _ in range(10):
        color = next(color_iterator)
        sys.stdout.write(f"\r{color}Loading {next(spinner)}{reset_color}")
        sys.stdout.flush()
        time.sleep(0.2)

def main():
    DIR_NAME = sys.argv[1] if len(sys.argv) > 1 else "Final_Dir_Stat"
    selected_color = random.choice(color_codes)
    formatted_message = f"{selected_color}{DIR_NAME}{reset_color}"
    print("Welcome to My Cool App!")
    loading_spinner()
    sys.stdout.write("\r" + " " * 30 + "\r")
    print(f"Your App's Name: {formatted_message}")

if __name__ == '__main__':
    main()

