#!/usr/bin/env python3

import json
import os
import fnmatch
import requests
import shutil
import sys
import time


def recursive_find(base, pattern="*.json"):
    """recursive find will yield python files in all directory levels
    below a base path.

    Arguments:
      - base (str) : the base directory to search
      - pattern: a pattern to match, defaults to *.py
    """
    for root, _, filenames in os.walk(base):
        for filename in fnmatch.filter(filenames, pattern):
            yield os.path.join(root, filename)


def read_json(path):
    """
    Read json into dict!
    """
    with open(path, "r") as fd:
        content = json.loads(fd.read())
    return content


def save_json(meta, path):
    with open(path, "w") as fd:
        fd.write(json.dumps(meta, indent=4))


def clean(repos_file, database, archive):
    """
    Clean the database
    """
    # Read in repos.txt and remove archived
    with open(repos_file, "r") as fd:
        subset = fd.readlines()

    with open("repos.txt", "r") as fd:
        repos = fd.readlines()

    repos = set([x.strip() for x in repos if x.strip()])
    subset = set([x.strip() for x in subset if x.strip()])

    for path in recursive_find(database, "*metadata.json"):
        meta = read_json(path)
        relpath = os.path.relpath(path, database)

        # Ensure UID is correct
        uid = meta['url'].rsplit('/', 3)
        uid = "/".join(uid[1:]).replace('.com', '')

        # Only look at subset
        if uid not in subset:
            continue

        # Spurious bug with empty url
        if meta["url"] is None:
            meta["url"] = meta["data"]["url"]
            save_json(meta, path)

        try:
            res = requests.head(meta.get("html_url") or meta.get("url"))
        except:
            print("Issue with {path}")
            continue

        if res.status_code == 200:
            continue

        elif res.status_code == 404:
            print(f"Found repository no longer present at {relpath}, archiving")
            newpath = os.path.join(archive, relpath)
            newdir = os.path.dirname(newpath)
            shutil.move(os.path.dirname(path), newdir)
            uid = os.path.dirname(relpath)
            if uid in repos:
                repos.remove(uid)

        elif res.status_code in [301, 302]:
            print(f"Found repository {relpath} with moved location, updating")
            new_location = requests.head(res.headers["Location"])
            meta["url"] = new_location.url                  
            save_json(meta, path)

        if uid not in relpath:
           old_uid = os.path.dirname(relpath)
           shutil.move(os.path.dirname(path), os.path.join(database, uid))
           print(f"{relpath} should be {uid}")
           if old_uid in repos:
               repos.remove(old_uid)
           repos.add(uid)

    # Save back to file
    with open("repos.txt", "w") as fd:
        fd.write("\n".join(list(repos)))

def main():

    # python .github/scripts/clean-database.py $(pwd)
    if len(sys.argv) < 3:
        sys.exit("Please provide a root path (with the database and argument) and a text file of repos.")

    root = os.path.abspath(sys.argv[1])
    repos_file = os.path.abspath(sys.argv[2])
    database = os.path.join(root, "database")
    archive = os.path.join(root, "archive")
    for path in database, archive:
        if not os.path.exists(path):
            sys.exit(f"{path} does not exist.")

    clean(repos_file, database, archive)


if __name__ == "__main__":
    main()
