# [data](/Schema Reference/objects/files/data "The directory in which to store all datafiles from the dataset.")

### Definition:

The directory in which to store all datafiles from the dataset.

### Properties:

- [**path**](/Schema Reference/meta/defs/path "Full path of the current file"): /data
- [**directory**](/Schema Reference/meta/defs/directory "Indicator for whether a given object is expected to be a directory or a file."): True

**If file/directory not found**:

[**code**](/Schema Reference/meta/defs/code): MISSING_DATA_DIRECTORY

[**level**](/Schema Reference/meta/defs/level): error

[**reason**](/Schema Reference/meta/defs/reason): It is required to include a subdirectory named 'data' in the base directory