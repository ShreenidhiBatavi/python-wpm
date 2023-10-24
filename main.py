import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr('Hare Krishna')
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)  