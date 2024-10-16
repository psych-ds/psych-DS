# [materials](/en/latest/Schema Reference/objects/files/materials "A directory in which to store any materials used to conduct the study.")

### Definition:

A directory in which to store any materials used to conduct the study.

### Properties:

- [**path**](/en/latest/Schema Reference/meta/defs/path "Full path of the current file"): /materials
- [**directory**](/en/latest/Schema Reference/meta/defs/directory "Indicator for whether a given object is expected to be a directory or a file."): True

**If file/directory not found**:

[**code**](/en/latest/Schema Reference/meta/defs/code): MISSING_MATERIALS_DIRECTORY

[**level**](/en/latest/Schema Reference/meta/defs/level): ignore

[**reason**](/en/latest/Schema Reference/meta/defs/reason): It is recommended to include subdirectory named 'materials' in the base directory