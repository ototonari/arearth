import urllib
import urllib2

 
def send_ref(url,params):
    params = urllib.urlencode(params)

    req = urllib2.urlopen(url + '?' + params)

    body = req.read()
    
