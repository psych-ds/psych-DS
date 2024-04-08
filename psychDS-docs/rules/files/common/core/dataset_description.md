# [dataset_description](/Schema Reference/objects/files/dataset_description "The metadata file 'dataset_description.json' is a JSON file describing the dataset.")

### Definition:

The metadata file 'dataset_description.json' is a JSON file describing the dataset.

### Properties:

- [**baseDir**](/Schema Reference/meta/defs/baseDir "Name of the directory under which the file object is expected to appear."): /
- [**stem**](/Schema Reference/meta/defs/stem "Portion of the filename which excludes the extension."): dataset_description
- [**arbitraryNesting**](/Schema Reference/meta/defs/arbitraryNesting "Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories."): False
- [**extensions**](/Schema Reference/meta/defs/extensions "Extension of current file including initial dot"): ['.json']

**If file/directory not found**:

[**code**](/Schema Reference/meta/defs/code): MISSING_DATASET_DESCRIPTION

[**level**](/Schema Reference/meta/defs/level): error

[**reason**](/Schema Reference/meta/defs/reason): It is required to include a 'dataset_description.json' in the base directory