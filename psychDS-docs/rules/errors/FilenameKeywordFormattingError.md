| Property | Value |
|----------|--------|
| [**code**](/en/latest/reference/schema/meta/defs/code) | FILENAME_KEYWORD_FORMATTING_ERROR |
| [**level**](/en/latest/reference/schema/meta/defs/level) | error |
| [**reason**](/en/latest/reference/schema/meta/defs/reason) | All datafiles must use psych-DS keyword formatting. That is, datafile names must consist of a series of keyword-value pairs, separated by underscores, with keywords using only lowercase alphabetic characters and values using any alphanumeric characters of either case. A keyword-value pair would look something like this: "subject-123a", where "subject" is the keyword and "123a" is the value. The file must end with '_data.csv'. An example file might look like this: "subject-123a_session-2_data.csv". This filename has two keyword-value pairs, separated by an underscore, the "_data" suffix, and the ".csv" extension. In other words, files must follow this regex: /([a-z]+-[a-zA-Z0-9]+)(_[a-z]+-[a-zA-Z0-9]+)*_data\.csv/
 |