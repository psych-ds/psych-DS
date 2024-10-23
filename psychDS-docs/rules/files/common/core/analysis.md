# [analysis](/en/latest/Schema Reference/objects/files/analysis "A directory to store code or other tools used to analyze the data/ files in order to describe and interpret the dataset. Any intermediate data files created during analysis SHOULD be output to a new file in data/ \(i.e. primary_data/ files SHOULD NOT be modified.\)")

### Definition:

A directory to store code or other tools used to analyze the data/ files in order to describe and interpret the dataset. Any intermediate data files created during analysis SHOULD be output to a new file in data/ \(i.e. primary_data/ files SHOULD NOT be modified.\)

### Properties:

- [**path**](/en/latest/Schema Reference/meta/defs/path "Full path of the current file"): /analysis
- [**directory**](/en/latest/Schema Reference/meta/defs/directory "Indicator for whether a given object is expected to be a directory or a file."): True

**If file/directory not found**:

[**code**](/en/latest/Schema Reference/meta/defs/code): MISSING_ANALYSIS_DIRECTORY

[**level**](/en/latest/Schema Reference/meta/defs/level): warning

[**reason**](/en/latest/Schema Reference/meta/defs/reason): It is recommended to include subdirectory named 'analysis' in the base directory