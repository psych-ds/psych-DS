# [results](/en/latest/Schema Reference/objects/files/results "A directory in which to store any results generated using the data in /data.")

### Definition:

A directory in which to store any results generated using the data in /data.

### Properties:

- [**path**](/en/latest/Schema Reference/meta/defs/path "Full path of the current file"): /results
- [**directory**](/en/latest/Schema Reference/meta/defs/directory "Indicator for whether a given object is expected to be a directory or a file."): True

**If file/directory not found**:

[**code**](/en/latest/Schema Reference/meta/defs/code): MISSING_RESULTS_DIRECTORY

[**level**](/en/latest/Schema Reference/meta/defs/level): warning

[**reason**](/en/latest/Schema Reference/meta/defs/reason): It is recommended to include subdirectory named 'results' in the base directory