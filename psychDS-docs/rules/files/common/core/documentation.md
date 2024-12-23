# [documentation](/en/latest/Schema Reference/objects/files/documentation "A directory in which to store any project-related documentation that is used for conducting the study \(e.g. consent forms\)")

### Definition:

A directory in which to store any project-related documentation that is used for conducting the study \(e.g. consent forms\)

### Properties:

- [**path**](/en/latest/Schema Reference/meta/defs/path "Full path of the current file"): /documentation
- [**directory**](/en/latest/Schema Reference/meta/defs/directory "Indicator for whether a given object is expected to be a directory or a file."): True

**If file/directory not found**:

[**code**](/en/latest/Schema Reference/meta/defs/code): MISSING_DOCUMENTATION_DIRECTORY

[**level**](/en/latest/Schema Reference/meta/defs/level): warning

[**reason**](/en/latest/Schema Reference/meta/defs/reason): It is recommended to include subdirectory named 'documentation' in the base directory