# [DirectoryMetadata](/en/latest/Schema Reference/objects/files/DirectoryMetadata "A json file in which to store metadata that applies to all datafiles within the containing directory or within any nested subdirectories. Fields from the file replace the values of the global dataset_description object.")

### Definition:

A json file in which to store metadata that applies to all datafiles within the containing directory or within any nested subdirectories. Fields from the file replace the values of the global dataset_description object.

### Properties:

- [**stem**](/en/latest/Schema Reference/meta/defs/stem "Portion of the filename which excludes the extension."): file_metadata
- [**extensions**](/en/latest/Schema Reference/meta/defs/extensions "Extension of current file including initial dot"): ['.json']
- [**baseDir**](/en/latest/Schema Reference/meta/defs/baseDir "Name of the directory under which the file object is expected to appear."): data
- [**arbitraryNesting**](/en/latest/Schema Reference/meta/defs/arbitraryNesting "Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories."): True

**If file/directory not found**:

[**code**](/en/latest/Schema Reference/meta/defs/code): MISSING_DIRECTORY_METADATA

[**level**](/en/latest/Schema Reference/meta/defs/level): warning

[**reason**](/en/latest/Schema Reference/meta/defs/reason): Optionally, you can provide an additional metadata file that is named file_metadata.json and overrides dataset_description.json for an entire directory. It will apply to all files within that directory and its subdirectories. For more information on how this "override" works, visit https://psychds-docs.readthedocs.io/en/latest/Schema%20Reference/objects/common_principles/inheritance/