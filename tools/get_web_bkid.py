from bs4 import BeautifulSoup, SoupStrainer
import json

def get_web_bkid(page: str | BeautifulSoup) -> str | None:
    if isinstance(page, str):
        soup = BeautifulSoup(page, "html.parser", parse_only=SoupStrainer('script'))
    elif not isinstance(page, BeautifulSoup):
        raise TypeError(  '`page` must be a `str` or `BeautifulSoup` object, '
                         f'not "{type(page)}"' )
    else:
        soup = page

    for script in soup.find_all("script", {"type": "application/json"}):
        if "WebBloksVersioningID" in (string := script.string):
            break
    else:
        return
    
    data = json.loads(string)
    for item in data["require"][0][3][0]["__bbox"]["define"]:
        if isinstance(item, list) and len(item) == 4:
            if item[0] == "WebBloksVersioningID":
                return item[2]["versioningID"]

# with open("page.html", "r") as read:
#     print("bkid:", get_web_bkid(read.read()))