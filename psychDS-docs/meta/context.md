# Schema Context

The context defines the vocabulary of properties that objects and rules within the schema can use.

### Properties:

| Property | Type | Description |
|----------|------|-------------|
| [schema](/en/latest/reference/schema/meta/defs/schema)| `object` | The psych-DS schema |
| [dataset](/en/latest/reference/schema/meta/defs/dataset)| `object` | Properties and contents of the entire dataset |
| [path](/en/latest/reference/schema/meta/defs/path)| `string` | Full path of the current file |
| [suffix](/en/latest/reference/schema/meta/defs/suffix)| `string` | String following the final '_' in a filename and preceding the '.' of the extension. Used to identify datafiles primarily. |
| [extensions](/en/latest/reference/schema/meta/defs/extensions)| `string` | Extension of current file including initial dot |
| [stem](/en/latest/reference/schema/meta/defs/stem)| `string` | Portion of the filename which excludes the extension. |
| [level](/en/latest/reference/schema/meta/defs/level)| `string` | Property describing the severity of a rule, which determines whether it produces an error, warning, etc. |
| [code](/en/latest/reference/schema/meta/defs/code)| `string` | Unique code identifying a specific error/warning |
| [reason](/en/latest/reference/schema/meta/defs/reason)| `string` | Paragraph accompanying an error/warning that provides context for what may cause it. |
| [directory](/en/latest/reference/schema/meta/defs/directory)| `boolean` | Indicator for whether a given object is expected to be a directory or a file. |
| [arbitraryNesting](/en/latest/reference/schema/meta/defs/arbitraryNesting)| `boolean` | Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories. |
| [usesKeywords](/en/latest/reference/schema/meta/defs/usesKeywords)| `boolean` | Indicator for whether a given file object requires keyword formatting. |
| [nonCanonicalKeywordsAllowed](/en/latest/reference/schema/meta/defs/nonCanonicalKeywordsAllowed)| `boolean` | Indicator for whether a given file object is required to use only official Psych-DS keywords |
| [fileRegex](/en/latest/reference/schema/meta/defs/fileRegex)| `regular expression` | Regular expression defining the legal formatting of a filename. |
| [baseDir](/en/latest/reference/schema/meta/defs/baseDir)| `string` | Name of the directory under which the file object is expected to appear. |
| [fields](/en/latest/reference/schema/meta/defs/fields)| `object` | Set of key/value pairs defining the fields that are expected to occur in a given file object, and whether they are required or recommended. |
| [namespace](/en/latest/reference/schema/meta/defs/namespace)| `string` | URL identifying the required namespace to be used for required fields in the file object. Namespaces are web prefixes that point to ontologies which contain definitions of semantic vocabularies. |
| [jsonld](/en/latest/reference/schema/meta/defs/jsonld)| `boolean` | Indicator for whether the given file object is required to be a valid JSON-LD object. |
| [containsAllColumns](/en/latest/reference/schema/meta/defs/containsAllColumns)| `boolean` | The metadata object, after all inherited sidecars are accounted for, must contain a 'variableMeasured' property listing at least all of the column headers found in the datafile at hand. |
| [columnsMatchMetadata](/en/latest/reference/schema/meta/defs/columnsMatchMetadata)| `boolean` | Each datafile must only use column headers that appear in the 'variableMeasured' property of the compiled metadata object that corresponds to it. |
| [sidecar](/en/latest/reference/schema/meta/defs/sidecar)| `object` | Sidecar metadata constructed via the inheritance principle |
| [columns](/en/latest/reference/schema/meta/defs/columns)| `object` | CSV columns, indexed by column header, values are arrays with column contents |
| [json](/en/latest/reference/schema/meta/defs/json)| `object` | Contents of the current JSON file |
| [requires](/en/latest/reference/schema/meta/defs/requires)| `array` | Set of schema locations defining the objects that must be present for certain issues to be reported |
| [keywords](/en/latest/reference/schema/meta/defs/keywords)| `array` | List of key-value pairings associated with the data file, derived from the filename |