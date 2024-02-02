import sys
from Xlib import X, display as xdisplay, Xutil

display = xdisplay.Display("host.docker.internal:0")
screen = display.screen()
window = screen.root.create_window(
    50, 50, 300, 200, 2,
    screen.root_depth,
    X.InputOutput,
    X.CopyFromParent,

    # special attribute values
    background_pixel=screen.white_pixel,
    event_mask=(X.ExposureMask |
                X.StructureNotifyMask |
                X.ButtonPressMask |
                X.ButtonReleaseMask |
                X.Button1MotionMask),
    colormap=X.CopyFromParent,
)

WM_DELETE_WINDOW = display.intern_atom('WM_DELETE_WINDOW')
WM_PROTOCOLS = display.intern_atom('WM_PROTOCOLS')

window.map()

while 1:
    event = display.next_event()
    
    if event.type == X.DestroyNotify:
        sys.exit(0)

    if event.type == X.ClientMessage:
        if event.client_type == WM_PROTOCOLS:
            fmt, data = event.data
            if fmt == 32 and data[0] == WM_DELETE_WINDOW:
                sys.exit(0)
