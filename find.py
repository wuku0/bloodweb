from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        print(f"Mouse Position - X: {x}, Y: {y}")

def start_mouse_listener():
    with mouse.Listener(on_click=on_click) as listener:
        print("Found. Running Finder.")
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nMouse position finder stopped.")
start_mouse_listener()
