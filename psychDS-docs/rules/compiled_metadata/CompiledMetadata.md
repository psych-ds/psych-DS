# [CompiledMetadata](/en/latest/Schema Reference/objects/files/CompiledMetadata "The metadata object that results from the combination of global metadata and directory- and file-level metadata files according to the rules of inheritance.")

### Definition:

The metadata object that results from the combination of global metadata and directory- and file-level metadata files according to the rules of inheritance.

### Properties:

- [**fields**](/en/latest/Schema Reference/meta/defs/fields "Set of key/value pairs defining the fields that are expected to occur in a given file object, and whether they are required or recommended."): {'name': 'required', 'description': 'required', 'variableMeasured': 'required', 'author': 'recommended', 'citation': 'recommended', 'license': 'recommended', 'funder': 'recommended', 'url': 'recommended', 'identifier': 'recommended', 'privacyPolicy': 'recommended', 'keywords': 'recommended'}
- [**namespace**](/en/latest/Schema Reference/meta/defs/namespace "URL identifying the required namespace to be used for required fields in the file object. Namespaces are web prefixes that point to ontologies which contain definitions of semantic vocabularies."): http://schema.org/
- [**jsonld**](/en/latest/Schema Reference/meta/defs/jsonld "Indicator for whether the given file object is required to be a valid JSON-LD object."): True
- [**containsAllColumns**](/en/latest/Schema Reference/meta/defs/containsAllColumns "The metadata object, after all inherited sidecars are accounted for, must contain a 'variableMeasured' property listing at least all of the column headers found in the datafile at hand."): True