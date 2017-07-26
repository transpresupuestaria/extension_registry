"""
A convenience script for creating entries here from their extension.json files
"""

import requests
import optparse
import json
import os


def main():
    usage = 'Usage: %prog name, url'
    parser = optparse.OptionParser(usage=usage)

    (options, args) = parser.parse_args()

    if args[1]:
        r = requests.get(args[1].replace("github.com", "raw.githubusercontent.com") + "/master/extension.json")
        ext = r.json()
        if os.path.isdir(args[0]):
            print("Extension already exists. Exiting.")
        else:
            os.mkdir(args[0])
            reg = {
                "name": {"en": ext['name']},
                "description": {"en": ext['description']},
                "url": args[1].replace("github.com", "raw.githubusercontent.com") + "/master/",
                "documentation_url": args[1] + "/blob/master/README.md",
                "active": True,
                "core": False,
                "category": "",
                "slug": args[0]
            }
            with open(args[0] + "/extension.json", "w") as file:
                file.write(json.dumps(reg, indent=4))

            print("Extension created - check details before committing.")

    else:
        print("Provide URL on the command line")


if __name__ == '__main__':
    main()
