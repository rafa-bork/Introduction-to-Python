import requests
import sys

try:
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
except IndexError:
    sys.exit('Missing argument')
except requests.RequestException:
    sys.exit('Request failed')
except
    print('Not able to complee request')
else
    print(response.json())
