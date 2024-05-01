# [Datafile](/en/latest/Schema Reference/objects/files/Datafile "A CSV file under the /data directory in which the official psych-DS compliant data from the dataset is stored. Datafiles must follow Psych-DS file naming conventions, which includes the use of keyword formatting, the '_data' suffix, and the '.csv' extension. An example of a valid datafile might be 'study-123_site-lab4_data.csv'. In the future, more official suffices and extensions may be made available. A controlled list of official keywords is provided, but the use of unofficial keywords is permitted, so long as they are clearly defined and used consistently within a research community.")

### Definition:

A CSV file under the /data directory in which the official psych-DS compliant data from the dataset is stored. Datafiles must follow Psych-DS file naming conventions, which includes the use of keyword formatting, the '_data' suffix, and the '.csv' extension. An example of a valid datafile might be 'study-123_site-lab4_data.csv'. In the future, more official suffices and extensions may be made available. A controlled list of official keywords is provided, but the use of unofficial keywords is permitted, so long as they are clearly defined and used consistently within a research community.

### Properties:

- [**requires**](/en/latest/Schema Reference/meta/defs/requires "Set of schema locations defining the objects that must be present for certain issues to be reported"): data
- [**suffix**](/en/latest/Schema Reference/meta/defs/suffix "String following the final '_' in a filename and preceding the '.' of the extension. Used to identify datafiles primarily."): data
- [**extensions**](/en/latest/Schema Reference/meta/defs/extensions "Extension of current file including initial dot"): ['.csv']
- [**baseDir**](/en/latest/Schema Reference/meta/defs/baseDir "Name of the directory under which the file object is expected to appear."): data
- [**arbitraryNesting**](/en/latest/Schema Reference/meta/defs/arbitraryNesting "Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories."): True
- [**columnsMatchMetadata**](/en/latest/Schema Reference/meta/defs/columnsMatchMetadata "Each datafile must only use column headers that appear in the 'variableMeasured' property of the compiled metadata object that corresponds to it."): True
- [**usesKeywords**](/en/latest/Schema Reference/meta/defs/usesKeywords "Indicator for whether a given file object requires keyword formatting."): True
- [**nonCanonicalKeywordsAllowed**](/en/latest/Schema Reference/meta/defs/nonCanonicalKeywordsAllowed "Indicator for whether a given file object is required to use only official Psych-DS keywords"): True
- [**fileRegex**](/en/latest/Schema Reference/meta/defs/fileRegex "Regular expression defining the legal formatting of a filename."): ([a-z]+-[a-zA-Z0-9]+)(_[a-z]+-[a-zA-Z0-9]+)*_data\.csv

**If file/directory not found**:

[**code**](/en/latest/Schema Reference/meta/defs/code): MISSING_DATAFILE

[**level**](/en/latest/Schema Reference/meta/defs/level): error

[**reason**](/en/latest/Schema Reference/meta/defs/reason): It is required to include at least one valid csv datafile under the data subdirectory