import urllib.request
import urllib.parse
import re
import webbrowser as wb
import sys

query_string = urllib.parse.urlencode({"search_query" : " ".join(sys.argv[1:])})
html_content = urllib.request.urlopen("https://www.youtube.com/results?search_query="+query_string)
search_results = re.findall(r'\"url\":\"\/watch\?v=(.{11})\"', html_content.read().decode('gbk','ignore'))
print("http://www.youtube.com/watch?v=" + search_results[0])
wb.open_new("http://www.youtube.com/watch?v={}".format(search_results[0]))