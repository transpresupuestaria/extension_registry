import os
import glob
import datetime
import json

from jsonschema.validators import Draft4Validator as validator

current_path = os.path.dirname(os.path.realpath(__file__))

gathered_json = {
    "last_updated": str(datetime.datetime.utcnow()),
    "extensions": []
}

with open('entry-schema.json') as fp:
    entry_validator = validator(json.load(fp))

exit_status = 0

for directory in glob.glob(current_path + "/*"):
    if os.path.isdir(directory):
        entry_json_file = os.path.join(directory, "entry.json")

        with open(entry_json_file) as fp:
            entry_obj = json.load(fp)
            if entry_validator.is_valid(entry_obj):
                
                ## This loop is temporary only so docs work while transistioning onto new format
                for item in entry_obj:
                    item["documentation_url"] = item["documentationUrl"]["en"]
                    item["url"] = item["url"][:-14]
                ## endloop

                gathered_json["extensions"].append(entry_obj[0])
            else:
                print('ERROR: Skipping extension {}: entry.json is not valid'.format(directory))
                exit_status = 1

full_json = json.dumps(gathered_json)

extensions_json_path = os.path.join(current_path, "extensions.json")
extensions_js_path = os.path.join(current_path, "extensions.js")

with open(extensions_json_path, "w+") as extensions_json:
    extensions_json.write(full_json)

with open(extensions_js_path, "w+") as extensions_json:
    extensions_json.write("extensions_callback(" + full_json + ")")

exit(exit_status)
