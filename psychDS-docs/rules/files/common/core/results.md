# [results](/en/latest/reference/schema/objects/files/results)

### Definition:

A directory in which to store any results generated using the data in /data.

### Properties:

| Property | Value | Description |
|----------|--------|-------------|
| [**path**](/en/latest/reference/schema/meta/defs/path) | `/results` | Full path of the current file
| [**directory**](/en/latest/reference/schema/meta/defs/directory) | `True` | Indicator for whether a given object is expected to be a directory or a file.

### If object not found:

| Property | Value |
|----------|--------|
| [**code**](/en/latest/reference/schema/meta/defs/code) | MISSING_RESULTS_DIRECTORY |
| [**level**](/en/latest/reference/schema/meta/defs/level) | warning |
| [**reason**](/en/latest/reference/schema/meta/defs/reason) | It is recommended to include subdirectory named 'results' in the base directory |