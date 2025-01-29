from pathlib import Path

parent = Path(__file__).parent

with open(parent / "com.bloks.www.ig.about_this_account.graphql_www.json", "r") as read:
    com__bloks__www__ig__about_this_account__graphql_www = read.read()
with open(parent / "com.bloks.www.ig.about_this_account.ios.json", "r") as read:
    com__bloks__www__ig__about_this_account__ios = read.read()
with open(parent / "com.bloks.www.ig.about_this_account.web.js", "r") as read:
    com__bloks__www__ig__about_this_account__web = read.read()