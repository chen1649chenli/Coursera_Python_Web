import json
import urllib

while True:
    location = raw_input('Enter location:')
    if len(location) <1: break
    data = urllib.urlopen(location).read()
    data = json.loads(data)
    total = 0
    comments = data["comments"]
    for comment in comments:
        total = total + int(comment["count"])
    print total
