__author__= Yossi Ovadia

import sys,requests,re
requests.packages.urllib3.disable_warnings()
username='admin'
password='admin'
if len (sys.argv) != 2 :
   print 'Syntax: ' + sys.argv[0] + ' ipmi_ip'
   sys.exit(0)
ip = sys.argv[1]
r = requests.get( "https://"+ip+"/rpc/WEBSES/create.asp", params={'WEBVAR_USERNAME':username,'WEBVAR_PASSWORD':password} ,verify=False)
cookie = re.search(r"('SESSION_COOKIE' : \')(\w*)",r.text).group(2)
r = requests.get("https://"+ip+"/rpc/getsystemmac.asp",verify=False,cookies={'SessionCookie': cookie})
mac = re.search(r"('MAC_ID' : 1,\'MAC_ADDRESS' : \')(\w.:\w.:\w.:\w.:\w.:\w.)",r.text).group(2)
print ip,mac
