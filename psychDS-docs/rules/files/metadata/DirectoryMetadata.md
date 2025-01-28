# [DirectoryMetadata](/en/latest/reference/schema/objects/files/DirectoryMetadata)

### Definition:

A json file in which to store metadata that applies to all datafiles within the containing directory or within any nested subdirectories. Fields from the file replace the values of the global dataset_description object.

### Properties:

| Property | Value | Description |
|----------|--------|-------------|
| [**stem**](/en/latest/reference/schema/meta/defs/stem) | `file_metadata` | Portion of the filename which excludes the extension.
| [**extensions**](/en/latest/reference/schema/meta/defs/extensions) | `['.json']` | Extension of current file including initial dot
| [**baseDir**](/en/latest/reference/schema/meta/defs/baseDir) | `data` | Name of the directory under which the file object is expected to appear.
| [**arbitraryNesting**](/en/latest/reference/schema/meta/defs/arbitraryNesting) | `True` | Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories.

### If object not found:

| Property | Value |
|----------|--------|
| [**code**](/en/latest/reference/schema/meta/defs/code) | MISSING_DIRECTORY_METADATA |
| [**level**](/en/latest/reference/schema/meta/defs/level) | warning |
| [**reason**](/en/latest/reference/schema/meta/defs/reason) | Optionally, you can provide an additional metadata file that is named file_metadata.json and overrides dataset_description.json for an entire directory. It will apply to all files within that directory and its subdirectories. For more information on how this "override" works, visit https://psychds-docs.readthedocs.io/en/latest/Schema%20Reference/objects/common_principles/inheritance/
 |