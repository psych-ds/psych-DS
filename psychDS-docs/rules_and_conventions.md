# Psych-DS Rules and Conventions

The full technical reference for the Psych-DS rules and conventions is the [schema model](link), whose markdown conversion lives [here](link). For ease of access and reference, this page enumerates the most crucial elements of the schema in bulleted form, and it can be used as a checklist for thinking about Pysch-DS compliance.

## Rules
**(Failure to satisfy these rules results in an error)**
- Datasets must contain a [global metadata file](link) named "dataset_description.json" in the root directory.

    - The file must use valid [JSON formatting](link) and must be a valid [JSON-LD](link) linked data file.
    - The file must contain the following fields:

        - [name](link)
        - [description](link)
        - [variableMeasured](link)

    - These required fields must use the schema.org [namespace](link), either by including a "@context" field with the value "https://schema.org", or by prepending the namespace directly in the field, as in "https://schema.org/description".
    - The file must have a field called "@type" or "type" with the value "Dataset" or "https://schema.org/Dataset"
    - The following is an example of a valid global metadata file:

        ```
            {
                "name": "Example dataset",
                "description": "This dataset is just an example",
                "variableMeasured": ['var1','var2','var3'],
                "@type": "Dataset",
                "@context": "https://schema.org"
            }
        ```

- Datasets must contain a [subdirectory called "data"](link), located within the root directory.
- Datasets must include at least one valid [data file](link) within the "data" subdirectory.

    - Data files can be located anywhere under the "data" subdirectory, under any number of [nested subdirectories](link). For instance, they can be located directly within "data", or they could be found within nested subdirectories, like "data/primary_data".
    - Data files must use the ".csv" [extension](link) and be formatted as [valid CSV files](link).
    - Names for data files must end with the [suffix](link) "_data".
    - Names for data files must use [keyword formatting](link), described below:

        - [keywords](link) are pairs of keys and values in the format "<key>-<value>"
            - keys can be any sequence of lowercase alphabetic characters ("a-z")
            - values can be any sequence of upper- and lowercase alphanumeric characters ("a-zA-Z0-9")
        - Multiple keywords can be combined together using underscores ("_")

    - An example of a valid data file: "data/primary_data/study-123a_subject-aaa1_session-3_data.csv"

        - In this example, "study-123a_subject-aaa1_session-3" are the "keywords", "_data" is the suffix, and ".csv" is the extension.
        

## Conventions
**(Failure to follow these recommendations results in a warning)**


