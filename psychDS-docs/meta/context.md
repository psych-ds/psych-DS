# Schema Context

The context defines the vocabulary of properties that objects and rules within the schema can use.

# Properties:

- schema: (object) The psych-DS schema
- dataset: (object) Properties and contents of the entire dataset
- path: (string) Full path of the current file
- suffix: (string) String following the final '_' in a filename and preceding the '.' of the extension. Used to identify datafiles primarily.
- extensions: (string) Extension of current file including initial dot
- stem: (string) Portion of the filename which excludes the extension.
- level: (string) Property describing the severity of a rule, which determines whether it produces an error, warning, etc.
- code: (string) Unique code identifying a specific error/warning
- reason: (string) Paragraph accompanying an error/warning that provides context for what may cause it.
- directory: (boolean) Indicator for whether a given object is expected to be a directory or a file.
- arbitraryNesting: (boolean) Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories.
- usesKeywords: (boolean) Indicator for whether a given file object requires keyword formatting.
- nonCanonicalKeywordsAllowed: (boolean) Indicator for whether a given file object is required to use only official Psych-DS keywords
- fileRegex: (regular expression) Regular expression defining the legal formatting of a filename.
- baseDir: (string) Name of the directory under which the file object is expected to appear.
- fields: (object) Set of key/value pairs defining the fields that are expected to occur in a given file object, and whether they are required or recommended.
- namespace: (string) URL identifying the required namespace to be used for required fields in the file object. Namespaces are web prefixes that point to ontologies which contain definitions of semantic vocabularies.
- jsonld: (boolean) Indicator for whether the given file object is required to be a valid JSON-LD object.
- containsAllColumns: (boolean) The metadata object, after all inherited sidecars are accounted for, must contain a 'variableMeasured' property listing at least all of the column headers found in the datafile at hand.
- columnsMatchMetadata: (boolean) Each datafile must only use column headers that appear in the 'variableMeasured' property of the compiled metadata object that corresponds to it.
- sidecar: (object) Sidecar metadata constructed via the inheritance principle
- columns: (object) CSV columns, indexed by column header, values are arrays with column contents
- json: (object) Contents of the current JSON file
- keywords: (array) List of key-value pairings associated with the data file, derived from the filename