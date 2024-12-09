# [README](/en/latest/Schema Reference/objects/files/README "Human-readable file describing the project and dataset in detail. This is an OPTIONAL file, and only one README file should appear in dataset.")

### Definition:

Human-readable file describing the project and dataset in detail. This is an OPTIONAL file, and only one README file should appear in dataset.

### Properties:

- [**baseDir**](/en/latest/Schema Reference/meta/defs/baseDir "Name of the directory under which the file object is expected to appear."): /
- [**stem**](/en/latest/Schema Reference/meta/defs/stem "Portion of the filename which excludes the extension."): README
- [**arbitraryNesting**](/en/latest/Schema Reference/meta/defs/arbitraryNesting "Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories."): False
- [**extensions**](/en/latest/Schema Reference/meta/defs/extensions "Extension of current file including initial dot"): ['.md', '.txt']

**If file/directory not found**:

[**code**](/en/latest/Schema Reference/meta/defs/code): MISSING_README_DOC

[**level**](/en/latest/Schema Reference/meta/defs/level): warning

[**reason**](/en/latest/Schema Reference/meta/defs/reason): It is recommended to include a 'README.md' or 'README.txt' file in the base directory