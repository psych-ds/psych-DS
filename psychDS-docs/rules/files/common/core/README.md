# [README](/en/latest/reference/schema/objects/files/README)

### Definition:

Human-readable file describing the project and dataset in detail. This is an OPTIONAL file, and only one README file should appear in dataset.

### Properties:

| Property | Value | Description |
|----------|--------|-------------|
| [**baseDir**](/en/latest/reference/schema/meta/defs/baseDir) | `/` | Name of the directory under which the file object is expected to appear.
| [**stem**](/en/latest/reference/schema/meta/defs/stem) | `README` | Portion of the filename which excludes the extension.
| [**arbitraryNesting**](/en/latest/reference/schema/meta/defs/arbitraryNesting) | `False` | Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories.
| [**extensions**](/en/latest/reference/schema/meta/defs/extensions) | `['.md', '.txt']` | Extension of current file including initial dot

### If object not found:

| Property | Value |
|----------|--------|
| [**code**](/en/latest/reference/schema/meta/defs/code) | MISSING_README_DOC |
| [**level**](/en/latest/reference/schema/meta/defs/level) | warning |
| [**reason**](/en/latest/reference/schema/meta/defs/reason) | It is recommended to include a 'README.md' or 'README.txt' file in the base directory |