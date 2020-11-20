import requests
import re
import sys
from threading import Thread
import json
import warnings
warnings.filterwarnings("ignore")


#voicecom
url_teamspeak = "https://files.teamspeak-services.com/releases/client/{0}/TeamSpeak3-Client-win64-{0}.exe".format(
    sorted(re.findall("3\.[0-9]\.[0-9]", requests.get("https://files.teamspeak-services.com/releases/client/").text))[-1])

url_discord = "https://discord.com/api/download?platform=win"

#browsers
url_firefox = "https://download.mozilla.org/?product=firefox-stub&os=win"
url_opera = "https://www.opera.com/de/computer/thanks?ni=stable&os=windows"
url_chrome = "https://dl.google.com/tag/s/appguid/update2/installers/ChromeSetup.exe"

#games
url_steam = "https://steamcdn-a.akamaihd.net/client/installer/SteamSetup.exe"
url_uplay = "https://ubistatic3-a.akamaihd.net/orbit/launcher_installer/UbisoftConnectInstaller.exe"
url_wot = "https://redirect.wargaming.net/WGC/Wargaming_Game_Center_Install_WoT_EU.exe"
url_epic = "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi" #msi
url_osu = "https://m1.ppy.sh/r/osu!install.exe"
url_origin = "https://www.dm.origin.com/download"
url_rockstar = "https://gamedownloads.rockstargames.com/public/installer/Rockstar-Games-Launcher.exe"

#utility
url_winrar = "https://www.netzmechanik.de/dl/4/winrar-x64-{}.exe".format(
    sorted(re.findall("[0-9]\.[0-9]{2}", requests.get("https://www.winrar.de/downld.php").text))[-1].replace(".", ""))

url_java = "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=243737_61ae65e088624f5aaa0b1d2d801acb16"

url_wireshark = "https://1.eu.dl.wireshark.org/win64/Wireshark-win64-{}.exe".format(
    sorted(re.findall("3\.[0-9]\.[0-9]", requests.get("https://www.wireshark.org/#download").text))[-1])

url_corsair_icue = "https://downloads.corsair.com/Files/CUE/iCUESetup_{}_release.msi".format(
    sorted(re.findall("3\.[0-9]{2}\.[0-9]{3}", requests.get("https://www.corsair.com/de/de/downloads#download_form_1").text))[-1])

url_filezilla = "https://download.filezilla-project.org/client/FileZilla_{}_win64_sponsored-setup.exe".format(
    sorted(re.findall("3\.[0-9]{2}\.[0-9]", requests.get("https://filezilla-project.org/download.php?type=client").text))[-1])

url_cygwin = "https://cygwin.com/setup-x86_64.exe"

url_dashlane = json.loads(requests.get("https://ws1.dashlane.com/5/binaries/query?platform=website&target=launcher_win&os=WIN_10_0_0").
                          content.decode())["content"]["location"]

#editors
url_vs_code = "https://aka.ms/win32-x64-user-stable"

url_miktex = "https://miktex.org/download/ctan/systems/win32/miktex/setup/windows-x64/{}".format(
    sorted(re.findall("basic-miktex.{1,}x64.exe", requests.get("https://miktex.org/download").text))[-1])

url_notepad_pp = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v{0}/npp.{0}.Installer.x64.exe".format(
    sorted(re.findall("[0-9]\.[0-9]\.[0-9]", requests.get("https://notepad-plus-plus.org/downloads/").text))[-1])

url_pycharm = "https://download.jetbrains.com/python/pycharm-professional-{}.exe".format(
    sorted(re.findall("20[0-9]{2}\.[0-9].[0-9]",requests.get("https://www.jetbrains.com/de-de/pycharm/download/").text))[-1])

url_intellij = "https://download.jetbrains.com/idea/ideaIU-{}.exe".format(
    sorted(re.findall("20[0-9]{2}\.[0-9].[0-9]",requests.get("https://www.jetbrains.com/de-de/pycharm/download/").text))[-1])

url_adobe_acrobat_reader = "https://admdownload.adobe.com/bin/livebeta/readerdc_de_ha_crd_install.exe"

def download(url, name):
    with open("installer_{}.exe".format(name), "wb") as f:
        resp = requests.get(url, stream=True, verify=False)
        fsize = resp.headers.get("content-length")

        if fsize is None:
            f.write(resp.content)
        else:
            downloaded_bytes = 0
            fsize = int(fsize)
            for data in resp.iter_content(chunk_size=4096):
                downloaded_bytes += len(data)
                f.write(data)
                progress = int(50 * downloaded_bytes / fsize)
                sys.stdout.write("\rDownloading form: {} ({}{})".format(url, "="*progress, " "*(50-progress)))
                sys.stdout.flush()



selected_urls = [url_dashlane]
counter = 0
for url in selected_urls:
    print(url)
    counter += 1
    t = Thread(target=download, args=(url, counter))
    t.start()



