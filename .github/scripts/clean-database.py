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


def clean(database, archive):
    """
    Clean the database
    """
    archives = set()
    for path in recursive_find(database, "*metadata.json"):
        meta = read_json(path)

        if meta["url"] is None:
            meta["url"] = meta["data"]["url"]
            save_json(meta, path)

        try:
            res = requests.head(meta.get("html_url") or meta.get("url"))
        except:
            print("Issue with {path}")
            continue

        relpath = os.path.relpath(path, database)
        if res.status_code == 200:
            continue

        elif res.status_code == 404:
            print(f"Found repository no longer present at {relpath}, archiving")
            newpath = os.path.join(archive, relpath)
            newdir = os.path.dirname(newpath)
            shutil.move(os.path.dirname(path), newdir)
            archives.add(os.path.dirname(relpath))

        elif res.status_code in [301, 302]:
            if "gitlab" in res.url:
                import IPython

                IPython.embed()
                sys.exit()
            print(f"Found repository {relpath} with moved location, updating")
            new_location = requests.head(res.headers["Location"])
            meta["html_url"] = new_location.url
            save_json(meta, path)

    # Read in repos.txt and remove archived
    with open("repos.txt", "r") as fd:
        repos = fd.readlines()
    repos = set([x.strip() for x in repos if x.strip()])
    for to_remove in archives:
        repos.remove(to_remove)

    # Save back to file
    with open("repos.txt", "w") as fd:
        fd.write("\n".join(list(repos)))

    import IPython

    IPython.embed()
    sys.exit()


def main():

    # python .github/scripts/clean-database.py $(pwd)
    if len(sys.argv) < 2:
        sys.exit("Please provide a root path with the database and argument")

    root = os.path.abspath(sys.argv[1])
    database = os.path.join(root, "database")
    archive = os.path.join(root, "archive")
    for path in database, archive:
        if not os.path.exists(path):
            sys.exit(f"{path} does not exist.")

    clean(database, archive)


if __name__ == "__main__":
    main()