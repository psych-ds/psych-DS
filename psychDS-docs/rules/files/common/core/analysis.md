# [analysis](/en/latest/reference/schema/objects/files/analysis)

### Definition:

A directory to store code or other tools used to analyze the data/ files in order to describe and interpret the dataset. Any intermediate data files created during analysis SHOULD be output to a new file in data/ \(i.e. primary_data/ files SHOULD NOT be modified.\)

### Properties:

| Property | Value | Description |
|----------|--------|-------------|
| [**path**](/en/latest/reference/schema/meta/defs/path) | `/analysis` | Full path of the current file
| [**directory**](/en/latest/reference/schema/meta/defs/directory) | `True` | Indicator for whether a given object is expected to be a directory or a file.

### If object not found:

| Property | Value |
|----------|--------|
| [**code**](/en/latest/reference/schema/meta/defs/code) | MISSING_ANALYSIS_DIRECTORY |
| [**level**](/en/latest/reference/schema/meta/defs/level) | warning |
| [**reason**](/en/latest/reference/schema/meta/defs/reason) | It is recommended to include subdirectory named 'analysis' in the base directory |