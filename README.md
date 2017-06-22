# Extension Repository 

The place where extensions can be registered in order to appear in the docs.

Each extension lives in its own directory in this repo and must contain an _entry.json_ file following the format described in the schema file _entry-schema.json_. 

_entry.json_ must validate against the schema before being included in the registry.

## entry.json

### required fields

* active: a boolean declaring the extension active or inactive status.
* category: part of the docs the extensions appears in.
* core: a boolean declaring the extension core (true) or community (false).
* description: description of the extension, an object mapping language codes to the description of the extension in the language.
* documentationUrl: documentation URL for the extension, an object mapping language codes to an URL with documentation in the language.
* name: name of the extension, an object mapping language codes to the name of the extension in the language
* url: URL of the extension repository, pointing at an _extension.json_ file.

### optional fields

* dependencies; a list of other extensions that this extension depends on.
* slug: it indicates where the extension documentation lives in the standard docs, i.e a slug of location will mean there will be docs at 
_h&#8203;ttp://standard.open-contracting.org/*version*/*lang*/extensions/location_ ── applies to core extensions only.


Here is an example extension.json

```json
{
  "name": {
    "en" : "Example Extension",
    "es" : "Ejemplo de Extensión"
  },
  "description": {
    "en": "Example Extension",
    "es": "Ejemplo de Extensión"
  },
  "url": "http://www.example.com/extension/extension.json",
  "documentationUrl": {
    "en": "http://www.example.com/extension_documentation/en_docs",
    "es": "http://www.example.com/extension_documentation/es_docs"
  },
  "category": "item",
  "core": false,
  "active": true,
  "slug": "example",
  "dependencies": ["path/to/extension1/extension.json","path/to/extension2/extension.json" ]
}
```

## Compile 

In order for the extension to be picked up by the docs the following command needs to be run after a new extension or a change has been made.

`python compile.py`

## Dependencies

_compile.py_ requires [jsonschema](https://pypi.python.org/pypi/jsonschema). You can install jsonschema using pip, ideally within a virtual environment:

```
pip install jsonschema
```
If you prefer not to use a virtual environment, it is recommended to pass the option `--user` to pip so that the package installs for the current user only (avoiding having to use admin privileges and a global install in your system).

```
pip install --user jsonschema
```
