# Psych-DS Schema Model

This repository contains the [LinkML](https://linkml.io/) schema model Psych-DS, which serves as the source of ground truth for what constitutes a valid Psych-DS dataset. The schema model is employed by our validator tools as a reference for all rules and objects to check for. The repository also contains python scripts for generating consolidated JSON representations of the schema model as well as generating markdown documents that correspond to the various YAML files that constitute the schema.

For a detailed overview of the LinkML framework and our schema model structure, check out [this page](https://psychds-docs.readthedocs.io/en/latest/reference/schema/schema_overview/) of our docs website.


## Repository Structure

```
schema_model
├── README.md
├── external_schemas
│   └── schemaorg # JSON and YAML versions of schema.org ontology
├── tools
│   ├── convert_to_json.py # script for creating consolidated JSON files of schema model directories
│   └── yaml_to_md.py # script for converting YAML schema model to markdown documentation reference
└── versions # separate directories for each version of the schema model
    ├── jsons # separate directories for each JSON version of the schema model
```

## YAML file example:
```yaml
# rules/files/tabular_data/data.yaml
Datafile: # name of the object to look for, in this case a canonical data file
  requires: data # a "data" directory must be found before the absence of a Datafile is reported
  suffix: "data" # sthe last substring before the extension should be "_data"
  extensions: # the file extension should be ".csv"
    - ".csv"
  baseDir: "data" # the file must be found somewhere under the "/data" subdirectory
  arbitraryNesting: true # the file can be embedded under any number of subdirectories, as long as the first subdirectory is "/data"
  columnsMatchMetadata: true # the column headers found in the file must appear in the "variableMeasured" field of the compiled metadata object
  usesKeywords: true # the filename must use keyword formatting
  nonCanonicalKeywordsAllowed: true # the keywords are not required to come from the official list 
  fileRegex: '([a-z]+-[a-zA-Z0-9]+)(_[a-z]+-[a-zA-Z0-9]+)*_data\.csv' # the filename must conform overall to this regular expression
  code: "MISSING_DATAFILE" # if no valid datafile is found but the "/data" subdirectory is present, then an error with the following parameters will be reported
  level: error
  reason: "No CSV files were found in the data subdirectory (or all of the CSV files found there had a problem - see other error messages.) There must be at least one valid csv datafile under the data/ subdirectory."
```

## Running scripts

To create a JSON file out of a given version of the schema:
```bash
source pyenv/bin/activate
python3 schema_model/tools/convert_to_json.py <version_number>
```

To generate a directory of markdown documents from a given version of the schema:
```bash
source pyenv/bin/activate
python3 schema_model/tools/yaml_to_md.py <version_number>
```

## Learn More
To get started creating high quality datasets, check out [our website](https://psych-ds.github.io/)

For detailed documentation, tutorials, and reference materials, check out our [Readthedocs site](https://psychds-docs.readthedocs.io/en/latest/)
