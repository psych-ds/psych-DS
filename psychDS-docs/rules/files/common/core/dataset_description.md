# [dataset_description](/en/latest/reference/schema/objects/files/dataset_description)

### Definition:

The metadata file 'dataset_description.json' is a JSON file describing the dataset.

### Properties:

| Property | Value | Description |
|----------|--------|-------------|
| [**baseDir**](/en/latest/reference/schema/meta/defs/baseDir) | `/` | Name of the directory under which the file object is expected to appear.
| [**stem**](/en/latest/reference/schema/meta/defs/stem) | `dataset_description` | Portion of the filename which excludes the extension.
| [**arbitraryNesting**](/en/latest/reference/schema/meta/defs/arbitraryNesting) | `False` | Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories.
| [**extensions**](/en/latest/reference/schema/meta/defs/extensions) | `['.json']` | Extension of current file including initial dot

### If object not found:

| Property | Value |
|----------|--------|
| [**code**](/en/latest/reference/schema/meta/defs/code) | MISSING_DATASET_DESCRIPTION |
| [**level**](/en/latest/reference/schema/meta/defs/level) | error |
| [**reason**](/en/latest/reference/schema/meta/defs/reason) | It is required to include a 'dataset_description.json' in the base directory |