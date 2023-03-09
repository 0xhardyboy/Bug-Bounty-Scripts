# Fix-URLs
Useful for fixing a list of URLs for processing.
Simply checks a URL or a list of URLs for the scheme `http://` or `https://`, adds the `http://` scheme to the URL if it missing.

# Usage and Inputs Options:
```
python script.py --url example.com
python script.py --url-list url_list.txt
cat url_list.txt | python script.py
python script.py < url_list.txt
```

## Input List Example:
```
http://google.com
facebook.com
https://www.tesla.com
yahoo.com
```

## Output Example:
```
http://google.com
http://facebook.com
https://www.tesla.com
http://yahoo.com
```
