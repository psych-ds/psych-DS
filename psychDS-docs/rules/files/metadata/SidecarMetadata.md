# [SidecarMetadata](/en/latest/reference/schema/objects/files/SidecarMetadata)

### Definition:

A json file in which to store metadata that applies to a specific datafile within the containing directory. Fields from the file replace the values of the global dataset_description object, and overwrite any fields shared with the directory metadata.

### Properties:

| Property | Value | Description |
|----------|--------|-------------|
| [**baseDir**](/en/latest/reference/schema/meta/defs/baseDir) | `data` | Name of the directory under which the file object is expected to appear.
| [**arbitraryNesting**](/en/latest/reference/schema/meta/defs/arbitraryNesting) | `True` | Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories.
| [**suffix**](/en/latest/reference/schema/meta/defs/suffix) | `data` | String following the final '_' in a filename and preceding the '.' of the extension. Used to identify datafiles primarily.
| [**extensions**](/en/latest/reference/schema/meta/defs/extensions) | `['.json']` | Extension of current file including initial dot

### If object not found:

| Property | Value |
|----------|--------|
| [**code**](/en/latest/reference/schema/meta/defs/code) | MISSING_SIDECAR_METADATA |
| [**level**](/en/latest/reference/schema/meta/defs/level) | warning |
| [**reason**](/en/latest/reference/schema/meta/defs/reason) | Optionally, you can provide an additional 'sidecar' metadata file that has the same name as a data file in the same directory (e.g. 'trial-5_data.csv' and 'trial-5_data.json'). It will override dataset_description.json for that specific csv datafile only. For more information on how this "override" works, visit https://psychds-docs.readthedocs.io/en/latest/Schema%20Reference/objects/common_principles/inheritance/ |