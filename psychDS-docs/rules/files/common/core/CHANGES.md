# [CHANGES](/en/latest/reference/schema/objects/files/CHANGES)

### Definition:

Version history of the dataset \(describing changes, updates and corrections\) MAY be provided in the form of a 'CHANGES' text file. \(.txt or .md\).

### Properties:

| Property | Value | Description |
|----------|--------|-------------|
| [**baseDir**](/en/latest/reference/schema/meta/defs/baseDir) | `/` | Name of the directory under which the file object is expected to appear.
| [**stem**](/en/latest/reference/schema/meta/defs/stem) | `CHANGES` | Portion of the filename which excludes the extension.
| [**arbitraryNesting**](/en/latest/reference/schema/meta/defs/arbitraryNesting) | `False` | Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories.
| [**extensions**](/en/latest/reference/schema/meta/defs/extensions) | `['.md', '.txt']` | Extension of current file including initial dot

### If object not found:

| Property | Value |
|----------|--------|
| [**code**](/en/latest/reference/schema/meta/defs/code) | MISSING_CHANGES_DOC |
| [**level**](/en/latest/reference/schema/meta/defs/level) | warning |
| [**reason**](/en/latest/reference/schema/meta/defs/reason) | It is recommended to include a 'CHANGES.md' or 'CHANGES.txt' file in the base directory |