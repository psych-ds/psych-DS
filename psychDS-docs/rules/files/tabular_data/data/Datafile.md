# [Datafile](/en/latest/reference/schema/objects/files/Datafile)

### Definition:

A CSV file under the /data directory in which the official psych-DS compliant data from the dataset is stored. Datafiles must follow Psych-DS file naming conventions, which includes the use of keyword formatting, the '_data' suffix, and the '.csv' extension. An example of a valid datafile might be 'study-123_site-lab4_data.csv'. In the future, more official suffices and extensions may be made available. A controlled list of official keywords is provided, but the use of unofficial keywords is permitted, so long as they are clearly defined and used consistently within a research community.

### Properties:

| Property | Value | Description |
|----------|--------|-------------|
| [**requires**](/en/latest/reference/schema/meta/defs/requires) | `data` | Set of schema locations defining the objects that must be present for certain issues to be reported
| [**suffix**](/en/latest/reference/schema/meta/defs/suffix) | `data` | String following the final '_' in a filename and preceding the '.' of the extension. Used to identify datafiles primarily.
| [**extensions**](/en/latest/reference/schema/meta/defs/extensions) | `['.csv']` | Extension of current file including initial dot
| [**baseDir**](/en/latest/reference/schema/meta/defs/baseDir) | `data` | Name of the directory under which the file object is expected to appear.
| [**arbitraryNesting**](/en/latest/reference/schema/meta/defs/arbitraryNesting) | `True` | Indicator for whether a given file object is allowed to be nested within an arbitrary number of subdirectories.
| [**columnsMatchMetadata**](/en/latest/reference/schema/meta/defs/columnsMatchMetadata) | `True` | Each datafile must only use column headers that appear in the 'variableMeasured' property of the compiled metadata object that corresponds to it.
| [**usesKeywords**](/en/latest/reference/schema/meta/defs/usesKeywords) | `True` | Indicator for whether a given file object requires keyword formatting.
| [**nonCanonicalKeywordsAllowed**](/en/latest/reference/schema/meta/defs/nonCanonicalKeywordsAllowed) | `True` | Indicator for whether a given file object is required to use only official Psych-DS keywords
| [**fileRegex**](/en/latest/reference/schema/meta/defs/fileRegex) | `([a-z]+-[a-zA-Z0-9]+)(_[a-z]+-[a-zA-Z0-9]+)*_data\.csv` | Regular expression defining the legal formatting of a filename.

### If object not found:

| Property | Value |
|----------|--------|
| [**code**](/en/latest/reference/schema/meta/defs/code) | MISSING_DATAFILE |
| [**level**](/en/latest/reference/schema/meta/defs/level) | error |
| [**reason**](/en/latest/reference/schema/meta/defs/reason) | No CSV files were found in the data subdirectory (or all of the CSV files found there had a problem - see other error messages.) There must be at least one valid csv datafile under the data/ subdirectory. |