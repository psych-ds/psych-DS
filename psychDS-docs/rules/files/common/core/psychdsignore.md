# [psychdsignore](/en/latest/reference/schema/objects/files/psychdsignore)

### Definition:

List of files and gitignore expressions describing which files in the directory should be ignored by the Psych-DS validator.

### Properties:

| Property | Value | Description |
|----------|--------|-------------|
| [**path**](/en/latest/reference/schema/meta/defs/path) | `/.psychdsignore` | Full path of the current file

### If object not found:

| Property | Value |
|----------|--------|
| [**code**](/en/latest/reference/schema/meta/defs/code) | MISSING_PSYCHDSIGNORE |
| [**level**](/en/latest/reference/schema/meta/defs/level) | warning |
| [**reason**](/en/latest/reference/schema/meta/defs/reason) | It is recommended to include a file called '.psychdsignore' in the base directory to indicate files/directories that the validator process should ignore. |