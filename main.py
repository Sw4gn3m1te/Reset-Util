import requests
import re
import sys
from threading import Thread
import warnings
warnings.filterwarnings("ignore")


#voicecom
url_teamspeak = "https://files.teamspeak-services.com/releases/client/{0}/TeamSpeak3-Client-win64-{0}.exe".format(
    sorted(re.findall("3\.[0-9]\.[0-9]", requests.get("https://files.teamspeak-services.com/releases/client/").text))[-1])

url_discord = "https://discord.com/api/download?platform=win"

#browsers
url_firefox = "https://download.mozilla.org/?product=firefox-stub&os=win"
url_opera = "https://www.opera.com/de/computer/thanks?ni=stable&os=windows"

#games
url_steam = "https://steamcdn-a.akamaihd.net/client/installer/SteamSetup.exe"
url_uplay = "https://ubistatic3-a.akamaihd.net/orbit/launcher_installer/UbisoftConnectInstaller.exe"
url_wot = "https://redirect.wargaming.net/WGC/Wargaming_Game_Center_Install_WoT_EU.exe"
url_epic = "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi" #msi
url_osu = "https://m1.ppy.sh/r/osu!install.exe"
url_origin = "https://www.dm.origin.com/download"

#utility
url_winrar = "https://www.netzmechanik.de/dl/4/winrar-x64-{}.exe".format(
    sorted(re.findall("[0-9]\.[0-9]{2}", requests.get("https://www.winrar.de/downld.php").text))[-1].replace(".", ""))

url_java = "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=243737_61ae65e088624f5aaa0b1d2d801acb16"

url_wireshark = "https://1.eu.dl.wireshark.org/win64/Wireshark-win64-{}.exe".format(
    sorted(re.findall("3\.[0-9]\.[0-9]", requests.get("https://www.wireshark.org/#download").text))[-1])


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
                sys.stdout.write("\rDownloading form: {} ({}{})".format(url ,"="*progress, " "*(50-progress)))
                sys.stdout.flush()



selected_urls = []
counter = 0
for url in selected_urls:
    counter += 1
    t = Thread(target=download, args=(url, counter))
    t.start()