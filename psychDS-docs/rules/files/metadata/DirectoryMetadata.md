# [DirectoryMetadata](/Schema Reference/objects/files/DirectoryMetadata "A json file in which to store metadata that applies to all datafiles within the containing directory or within any nested subdirectories. Fields from the file replace the values of the global dataset_description object.")

### Definition:

A json file in which to store metadata that applies to all datafiles within the containing directory or within any nested subdirectories. Fields from the file replace the values of the global dataset_description object.

### Properties:

- [**stem**](/Schema Reference/meta/defs/stem "Portion of the filename which excludes the extension."): file_metadata
- [**extensions**](/Schema Reference/meta/defs/extensions "Extension of current file including initial dot"): ['.json']
- [**baseDir**](/Schema Reference/meta/defs/baseDir "Name of the directory under which the file object is expected to appear."): data
- [**arbitraryNesting**](/Schema Reference/meta/defs/arbitraryNesting "Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories."): True

**If file/directory not found**:

[**code**](/Schema Reference/meta/defs/code): MISSING_DIRECTORY_METADATA

[**level**](/Schema Reference/meta/defs/level): warning

[**reason**](/Schema Reference/meta/defs/reason): It is optional to include a json metadata file within a data subdirectory that applies to all files within the current directory and its subdirectories