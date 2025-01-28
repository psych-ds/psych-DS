# [materials](/en/latest/reference/schema/objects/files/materials)

### Definition:

A directory in which to store any materials used to conduct the study.

### Properties:

| Property | Value | Description |
|----------|--------|-------------|
| [**path**](/en/latest/reference/schema/meta/defs/path) | `/materials` | Full path of the current file
| [**directory**](/en/latest/reference/schema/meta/defs/directory) | `True` | Indicator for whether a given object is expected to be a directory or a file.

### If object not found:

| Property | Value |
|----------|--------|
| [**code**](/en/latest/reference/schema/meta/defs/code) | MISSING_MATERIALS_DIRECTORY |
| [**level**](/en/latest/reference/schema/meta/defs/level) | warning |
| [**reason**](/en/latest/reference/schema/meta/defs/reason) | It is recommended to include subdirectory named 'materials' in the base directory |