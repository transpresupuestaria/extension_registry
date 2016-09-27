# Extension Repository 

The place where extensions can be registered in order to appear in the docs.

Each extension lives in its own directory in this repo and must contain an extension.json file

## extension.json

The extension.json must contain a name, description, docucumentation_url and a url field. 

The name and description fields must language objects with the key being the langage code i.e en and the value being the string in that language.

The url field is the home your extension normally a link to the github repo.

A category field says which part of the docs the extension appears in.

The core field says if it is part of the core standard and has documentation written in the main docs.

The slug field is only useful for core extensions, it says where the extension docs live in the main docs. i.e a slug of location will mean there will be docs at 
http://standard.open-contracting.org/*version*/*lang*/extensions/location.

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
  "url": "http://www.example.com/extension_url",
  "documentaion_url": "http://www.example.com/extension_documentation_url",
  "category": "item",
  "core": false,
  "slug": "example"
}
```

## Compile 

In order for the extension to be picked up by the docs the following command needs to be run after a new extension or a change has been made.

`python compile.py`

