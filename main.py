import pyautogui
import time
import keyboard
import tkinter as tk
import requests
import webbrowser

coordinates = [
    (677, 124),
    (683, 222),
    (500, 273),
    (857, 276),
    (741, 347),
    (620, 348),
    (500, 406),
    (374, 409),
    (287, 354),
    (860, 406),
    (998, 405),
    (676, 458),
    (441, 523),
    (574, 519),
    (782, 510),
    (894, 522),
    (1036, 584),
    (921, 638),
    (788, 646),
    (573, 645),
    (440, 642),
    (319, 580),
    (677, 581),
    (677, 707),
    (494, 754),
    (499, 888),
    (369, 758),
    (619, 797),
    (673, 932),
    (871, 902),
    (735, 798),
    (845, 736),
    (899, 521),
    (1004, 721),
    (961, 794),
    (876, 870),
    (740, 798),
    (619, 797),
    (835, 742),
    (903, 520),
    (1043, 106)
]

stop_clicking = False
def perform_click(x, y):
    pyautogui.click(x, y)
    time.sleep(0.5)
def start_clicking():
    global stop_clicking
    stop_clicking = False
    run_button.config(state=tk.DISABLED)
    print("Press 'S' to stop clicking.")
    try:
        while not keyboard.is_pressed('s'):
            for x, y in coordinates:
                if stop_clicking:
                    break
                perform_click(x, y)
            if stop_clicking:
                break
        print("Clicking stopped.")
    except KeyboardInterrupt:
        print("Clicking interrupted by user.")
    run_button.config(state=tk.NORMAL)
def stop_clicking_process():
    global stop_clicking
    stop_clicking = True
def check_version():
    url = "https://raw.githubusercontent.com/wuku0/bloodweb/main/version.cc"
    try:
        response = requests.get(url)
        web_version = int(response.text.strip().split('=')[1])
        if web_version > 1:
            update_text.set("Update available!")
            update_link_label.bind("<Button-1>", lambda event: webbrowser.open("https://github.com/wuku0/bloodweb/releases"))
        else:
            update_text.set("Up-to-date")
    except requests.RequestException:
        update_text.set("Error checking update")
root = tk.Tk()
root.title("bloodweb-clicker")
root.geometry("300x150")
version_label = tk.Label(root, text="Version 1", anchor="e")
version_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")
run_button = tk.Button(root, text="RUN (R)", command=start_clicking)
run_button.grid(row=1, column=0, padx=10, pady=10)
stop_button = tk.Button(root, text="STOP (S)", command=stop_clicking_process)
stop_button.grid(row=1, column=1, padx=10, pady=10)
footer_link_label = tk.Label(root, text="roko.cc", fg="blue", cursor="hand2")
footer_link_label.grid(row=2, columnspan=3, padx=10, pady=10)
footer_link_label.bind("<Button-1>", lambda event: webbrowser.open("https://wuku0.github.io"))
update_text = tk.StringVar()
update_link_label = tk.Label(root, textvariable=update_text, cursor="hand2")
update_link_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
check_version()
root.mainloop()
