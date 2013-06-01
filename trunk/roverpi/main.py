import rover as r
import curses

x = r.Rover()
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Using Up, Left and Right arrow to control the rover. Hit 'q' to quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP: 
        stdscr.addstr(2, 20, "Up")
        x.forward()
    elif key == curses.KEY_DOWN: 
        stdscr.addstr(3, 20, "Down")
        # not implemented
    elif key == curses.KEY_LEFT:
        stdscr.addstr(3, 15, "Left")
        x.left(0.53)
    elif key == curses.KEY_RIGHT:
        stdscr.addstr(3, 25, "Right")
        x.right(0.53)
curses.endwin()
