# [CHANGES](/en/latest/Schema Reference/objects/files/CHANGES "Version history of the dataset \(describing changes, updates and corrections\) MAY be provided in the form of a 'CHANGES' text file. \(.txt or .md\).")

### Definition:

Version history of the dataset \(describing changes, updates and corrections\) MAY be provided in the form of a 'CHANGES' text file. \(.txt or .md\).

### Properties:

- [**baseDir**](/en/latest/Schema Reference/meta/defs/baseDir "Name of the directory under which the file object is expected to appear."): /
- [**stem**](/en/latest/Schema Reference/meta/defs/stem "Portion of the filename which excludes the extension."): CHANGES
- [**arbitraryNesting**](/en/latest/Schema Reference/meta/defs/arbitraryNesting "Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories."): False
- [**extensions**](/en/latest/Schema Reference/meta/defs/extensions "Extension of current file including initial dot"): ['.md', '.txt']

**If file/directory not found**:

[**code**](/en/latest/Schema Reference/meta/defs/code): MISSING_CHANGES_DOC

[**level**](/en/latest/Schema Reference/meta/defs/level): warning

[**reason**](/en/latest/Schema Reference/meta/defs/reason): It is recommended to include a 'CHANGES.md' or 'CHANGES.txt' file in the base directory