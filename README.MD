## Auto leveler for DBD Bloodweb

### Overview

This repository contains a simple Python script that acts as an auto clicker to automate the process of leveling up Bloodwebs in Dead by Daylight (DBD). The Bloodweb is a game mechanic where players can spend Bloodpoints to level up their characters and unlock perks, items, and offerings. This script is intended to assist players in automating the repetitive clicking required to progress through the Bloodweb.

### Usage
> WINDOWS
1. Go to [releases](https://github.com/wuku0/bloodweb/releases) and download the current version `.exe`
2. Run the `.exe`
3. In the GUI window, press the "RUN (R)" button to start the auto-leveling process.
5. To stop the automation, press the "STOP (S)" button or close the GUI window.


> LINUX / OSX
1. Install the required libraries by running: `pip install pyautogui keyboard tkinter requests webbrowser`.
2. Run the `main.py` script, or download [latest release `.py`](https://github.com/wuku0/bloodweb/releases). (Root access might be required.)
3. In the GUI window, press the "RUN (R)" button to start the auto-leveling process.
5. To stop the automation, press the "STOP (S)" button or close the GUI window.

## Known Issues
- Make sure your dbd Menu UI scale is set to 100%.
- Windows Defender and some other antivirus applications may report a threat. This is due to a library used to
  compile the application. You should be able to configure your antivirus to ignore this.
  To document that this software contains no malicious content, here are some threads detailing the problem:
     - https://github.com/pyinstaller/pyinstaller/issues/6754
     - https://www.reddit.com/r/learnpython/comments/ng3hmp/pyinstaller_create_onefile_exe_windows/
     - https://stackoverflow.com/questions/43777106/program-made-with-pyinstaller-now-seen-as-a-trojan-horse-by-avg

### Important Note

Although there seems to be no danger in using this script. Use this script responsibly and only for personal use. Automating tasks in games or applications might be against their terms of service, and it can potentially result in penalties or account suspension. Always ensure you have proper permissions to automate any task.

### Contributing

Contributions to this project are welcome! Feel free to create pull requests or report issues if you encounter any problems.

### Disclaimer

This script is provided "as is" and without warranty of any kind. The authors of this script are not responsible for any consequences arising from the use of this software. Use it at your own risk.

### License

This project is licensed under the [MIT License](LICENSE).

For more information about Dead by Daylight, please visit the official [Dead by Daylight website](https://deadbydaylight.com/).
