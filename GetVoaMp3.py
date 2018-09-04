import re
import urllib.request as req
res=req.urlopen("http://www.51voa.com")
data=res.read().decode()
res.close()
mp3url = re.findall( 'a href="/lrc/(.*?).lrc',data)
if mp3url:
    mp3url='http://downdb.51voa.com/'+mp3url[0]+'.mp3'
    req.urlretrieve(mp3url,'voa.mp3')