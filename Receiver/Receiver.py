#Imports
import base64
import requests # type: ignore
from github import Github # type: ignore

#Github
g = Github("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")
repo = g.get_repo("anigamer101/Arkens")
contents = repo.get_contents("")

#Print
for content in contents:
    print(content.name)