import urllib.request
import re

urls = [
    "https://www.instagram.com/p/DUjJ-5iiOJQ/",
    "https://www.instagram.com/reel/DWJW5lSCGuU/",
    "https://www.instagram.com/p/DQz97X9iPH-/",
    "https://www.instagram.com/p/DTD9YwxiJCX/"
]

req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

for url in urls:
    req = urllib.request.Request(url, headers=req_headers)
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        match = re.search(r'<meta property="og:image" content="(.*?)"', html)
        if match:
            print(f"URL: {url} -> IMG: {match.group(1)}")
        else:
            print(f"URL: {url} -> IMG: NOT FOUND")
    except Exception as e:
        print(f"URL: {url} -> ERROR: {e}")
