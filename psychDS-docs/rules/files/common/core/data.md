# [data](/en/latest/Schema Reference/objects/files/data "The directory in which to store all datafiles from the dataset.")

### Definition:

The directory in which to store all datafiles from the dataset.

### Properties:

- [**path**](/en/latest/Schema Reference/meta/defs/path "Full path of the current file"): /data
- [**directory**](/en/latest/Schema Reference/meta/defs/directory "Indicator for whether a given object is expected to be a directory or a file."): True
- [**requires**](/en/latest/Schema Reference/meta/defs/requires "Set of schema locations defining the objects that must be present for certain issues to be reported"): dataset_description

**If file/directory not found**:

[**code**](/en/latest/Schema Reference/meta/defs/code): MISSING_DATA_DIRECTORY

[**level**](/en/latest/Schema Reference/meta/defs/level): error

[**reason**](/en/latest/Schema Reference/meta/defs/reason): It is required to include a subdirectory named 'data' in the base directory