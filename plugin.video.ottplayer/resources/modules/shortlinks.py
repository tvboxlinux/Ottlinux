import xbmc,xbmcgui,requests
from resources.modules import control,tools


username     = control.setting('Username')
password     = control.setting('Password')
host         = control.setting('host')
port         = control.setting('port')
def Get():
	xbmc.executebuiltin("ActivateWindow(busydialog)")
	m3u  = 'http:///get.php?username='+username+'&password='+password+'&type=m3u_plus&output=ts'
	epg  = 'http:///xmltv.php?username='+username+'&password='+password
	auth = 'http:///enigma2.php?username='+username+'&password='+password+'&type=get_vod_categories'
	auth = tools.OPEN_URL(auth)
	if not auth=="":
		request  = 'https://tinyurl.com/create.php?source=indexpage&url='+m3u+'&submit=Make+TinyURL%21&alias='
		xbmc.log(str(request))
		request2 = 'https://tinyurl.com/create.php?source=indexpage&url='+epg+'&submit=Make+TinyURL%21&alias='
		m3u = tools.OPEN_URL(request)
		epg = tools.OPEN_URL(request2)
		xbmc.log(str(epg))
		shortm3u = tools.regex_from_to(m3u,'<div class="indent"><b>','</b>')
		shortepg = tools.regex_from_to(epg,'<div class="indent"><b>','</b>')
		xbmc.executebuiltin("Dialog.Close(busydialog)")
		xbmcgui.Dialog().ok('Global Entertainment','[COLOR lime]M3U URL: [/COLOR]%s'%shortm3u,'','[COLOR lime]EPG URL: [/COLOR]%s'%shortepg)
	else:
		return
