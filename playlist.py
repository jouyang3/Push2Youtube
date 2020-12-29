import urllib.request
import urllib.parse
import re
import webbrowser as wb
import sys
import json

# Change this string to your YouTube channel URL
channel = "https://www.youtube.com/channel/UChQdGwbI1hUWCNpnXaDeJQg";

html_content = urllib.request.urlopen(channel+"/playlists");
query_string = " ".join(sys.argv[1:]);
ss = html_content.read().decode('gbk','ignore');
m = re.search(r'var ytInitialData = (.*?);\s?</script>',ss); g = json.loads(m.group(1));
req = r'"text"\s*:\s*"'+query_string+r'".+"url"\s*:\s*"(.+?)"\s*,\s*"webPageType"\s*:\s*"WEB_PAGE_TYPE_WATCH"';
kk = json.dumps(g); ppp = re.search(req,kk,flags=re.IGNORECASE);
url = "https://www.youtube.com{}".format(ppp.group(1));
print(url)
wb.open_new(url)