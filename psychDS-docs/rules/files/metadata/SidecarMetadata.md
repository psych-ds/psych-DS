# [SidecarMetadata](/en/latest/Schema Reference/objects/files/SidecarMetadata "A json file in which to store metadata that applies to a specific datafile within the containing directory. Fields from the file replace the values of the global dataset_description object, and overwrite any fields shared with the directory metadata.")

### Definition:

A json file in which to store metadata that applies to a specific datafile within the containing directory. Fields from the file replace the values of the global dataset_description object, and overwrite any fields shared with the directory metadata.

### Properties:

- [**baseDir**](/en/latest/Schema Reference/meta/defs/baseDir "Name of the directory under which the file object is expected to appear."): data
- [**arbitraryNesting**](/en/latest/Schema Reference/meta/defs/arbitraryNesting "Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories."): True
- [**suffix**](/en/latest/Schema Reference/meta/defs/suffix "String following the final '_' in a filename and preceding the '.' of the extension. Used to identify datafiles primarily."): data
- [**extensions**](/en/latest/Schema Reference/meta/defs/extensions "Extension of current file including initial dot"): ['.json']

**If file/directory not found**:

[**code**](/en/latest/Schema Reference/meta/defs/code): MISSING_SIDECAR_METADATA

[**level**](/en/latest/Schema Reference/meta/defs/level): warning

[**reason**](/en/latest/Schema Reference/meta/defs/reason): It is optional to include a json metadata file within a data subdirectory that applies to a specific csv datafile within the current directory