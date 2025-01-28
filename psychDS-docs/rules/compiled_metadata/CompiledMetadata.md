# [CompiledMetadata](/en/latest/reference/schema/objects/files/CompiledMetadata)

### Definition:

The metadata object that results from the combination of global metadata and directory- and file-level metadata files according to the rules of inheritance.

### Properties:

| Property | Value | Description |
|----------|--------|-------------|
| [**fields**](/en/latest/reference/schema/meta/defs/fields) | `{'name': 'required', 'description': 'required', 'variableMeasured': 'required', 'author': 'recommended', 'citation': 'recommended', 'license': 'recommended', 'funder': 'recommended', 'url': 'recommended', 'identifier': 'recommended', 'privacyPolicy': 'recommended', 'keywords': 'recommended'}` | Set of key/value pairs defining the fields that are expected to occur in a given file object, and whether they are required or recommended.
| [**namespace**](/en/latest/reference/schema/meta/defs/namespace) | `http://schema.org/` | URL identifying the required namespace to be used for required fields in the file object. Namespaces are web prefixes that point to ontologies which contain definitions of semantic vocabularies.
| [**jsonld**](/en/latest/reference/schema/meta/defs/jsonld) | `True` | Indicator for whether the given file object is required to be a valid JSON-LD object.
| [**containsAllColumns**](/en/latest/reference/schema/meta/defs/containsAllColumns) | `True` | The metadata object, after all inherited sidecars are accounted for, must contain a 'variableMeasured' property listing at least all of the column headers found in the datafile at hand.