import os 
import glob
import datetime
import json

current_path = os.path.dirname(os.path.realpath(__file__))

gathered_json = {
    "last_updated": str(datetime.datetime.utcnow()),
    "extensions": []
}


for directory in glob.glob(current_path+"/*"):
    if os.path.isdir(directory):
        extension_json_file = os.path.join(directory, "extension.json")
        with open(extension_json_file) as extension_json:
            gathered_json["extensions"].append(json.load(extension_json))

full_json = json.dumps(gathered_json)

extensions_json_path = os.path.join(current_path, "extensions.json")
extensions_js_path = os.path.join(current_path, "extensions.js")

with open(extensions_json_path, "w+") as extensions_json:
    extensions_json.write(full_json)

with open(extensions_js_path, "w+") as extensions_json:
    extensions_json.write("extensions_callback(" + full_json + ")")


