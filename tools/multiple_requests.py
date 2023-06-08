from argparse import ArgumentParser
from urllib.parse import unquote
import requests
import json

WANTED_BKID = []

def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", required=True)
    parser.add_argument("-i", "--bkids", nargs="*")
    args = vars(parser.parse_args())

    wanted_bkid = arg_bkids if (arg_bkids := args["bkids"]) else WANTED_BKID
    if not any(wanted_bkid):
        exit("no bkid wanted !")

    with open(args["file"], "r") as read:
        data = json.load(read)['log']['entries'][0]['request']

    headers = data['headers']
    for header in headers:
        if header['name'] == "X-Bloks-Version-Id":
            bkid = header["value"]
            break
    else:
        exit("bkid not found !")

    client = requests.Session()
    client.headers = {h['name']: h['value'] for h in headers}

    for new_bkid in wanted_bkid + [bkid]:
        post_data = {"signed_body": unquote(data['postData']['params'][0]['value']).replace(bkid, new_bkid)}
        url = data['url']
        response = client.post(url, data=post_data)
        app_id = url.split("/")[-2]
        with open(f"{app_id} | {new_bkid}.json", "w") as write:
            json.dump(response.json(), write, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()