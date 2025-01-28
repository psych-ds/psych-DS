# [data](/en/latest/reference/schema/objects/files/data)

### Definition:

The directory in which to store all datafiles from the dataset.

### Properties:

| Property | Value | Description |
|----------|--------|-------------|
| [**path**](/en/latest/reference/schema/meta/defs/path) | `/data` | Full path of the current file
| [**directory**](/en/latest/reference/schema/meta/defs/directory) | `True` | Indicator for whether a given object is expected to be a directory or a file.
| [**requires**](/en/latest/reference/schema/meta/defs/requires) | `dataset_description` | Set of schema locations defining the objects that must be present for certain issues to be reported

### If object not found:

| Property | Value |
|----------|--------|
| [**code**](/en/latest/reference/schema/meta/defs/code) | MISSING_DATA_DIRECTORY |
| [**level**](/en/latest/reference/schema/meta/defs/level) | error |
| [**reason**](/en/latest/reference/schema/meta/defs/reason) | It is required to include a subdirectory named 'data' in the base directory |