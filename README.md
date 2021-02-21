AutoGit 2.2 by WalleNet
All Rights Reserved

#### Installation Info ####
The .exe file is located in the 'Dist' folder.
If this doesn't work, delete the 'Dist', 'Build', and '.spec' directories and use pyinstaller
to reinstall the application:

In the 'AutoGit' directory, run the following command:

pyinstaller -w --onedir AutoGit.py

You may need to install the following modules via pip (or pip3 if using Linux):
-tkinter
-PIL
-pyautogui

For further comments/concerns email us at rohand.wallenet@gmail.com
