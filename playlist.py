import urllib.request
import urllib.parse
import re
import webbrowser as wb
import sys
import json

query_string = " ".join(sys.argv[1:]);
html_content = urllib.request.urlopen("https://www.youtube.com/channel/UChQdGwbI1hUWCNpnXaDeJQg/playlists")
ss = html_content.read().decode('gbk','ignore');
m = re.search(r'var ytInitialData = (.*?);\s?</script>',ss); g = json.loads(m.group(1));
req = r'"text"\s*:\s*"'+query_string+r'".+"url"\s*:\s*"(.+?)"\s*,\s*"webPageType"\s*:\s*"WEB_PAGE_TYPE_WATCH"';
kk = json.dumps(g); ppp = re.search(req,kk,flags=re.IGNORECASE);
url = "https://www.youtube.com{}".format(ppp.group(1));
print(url)
wb.open_new(url)