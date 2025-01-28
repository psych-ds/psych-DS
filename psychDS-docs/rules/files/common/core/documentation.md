# [documentation](/en/latest/reference/schema/objects/files/documentation)

### Definition:

A directory in which to store any project-related documentation that is used for conducting the study \(e.g. consent forms\)

### Properties:

| Property | Value | Description |
|----------|--------|-------------|
| [**path**](/en/latest/reference/schema/meta/defs/path) | `/documentation` | Full path of the current file
| [**directory**](/en/latest/reference/schema/meta/defs/directory) | `True` | Indicator for whether a given object is expected to be a directory or a file.

### If object not found:

| Property | Value |
|----------|--------|
| [**code**](/en/latest/reference/schema/meta/defs/code) | MISSING_DOCUMENTATION_DIRECTORY |
| [**level**](/en/latest/reference/schema/meta/defs/level) | warning |
| [**reason**](/en/latest/reference/schema/meta/defs/reason) | It is recommended to include subdirectory named 'documentation' in the base directory |