### Definition:

In addition to the mandatory "dataset_description.json" file at the root of the dataset,
Psych-DS allows for the inclusion of additional metadata files, whose fields apply to 
specific subsets of the data. There are two types of inherited metadata:

1. Sidecar files, which contain metadata that pertains to one specific datafile. These sidecars
must have the exact same name as their corresponding datafile, with the ".json" extension instead 
of the ".csv" extension. Sidecars must occupy the same directory as their datafile.
2. Directory metadata, which always takes the form "file_metadata.json". The metadata contained in
such files apply to all datafiles within its directory and all subdirectories thereof.

Metadata key/value pairs found in higher-level JSON files are inherited by all lower levels unless they are explicitly 
overridden by a file at the lower level.

For example, suppose we have the following project structure:

data/
  file_metadata.json
  subject-1/
    file_metadata.json
    subject-1_condition-A_data.csv
    subject-1_condition-B_data.json
    subject-1_condition-B_data.csv
  subject-2/
    subject-2_condition-A_data.json
    subject-2_condition-A_data.csv
    subject-2_condition-B_data.csv

There are 4 datafiles within the data/ hierarchy; let's consider which metadata files apply to each one, and in what order 
the metadata files should be processed/inherited:
 - data/subject-1/subject-1_condition-A_data.csv: There is no JSON sidecar for this file. 
   However, there is a file_metadata.json file in the same directory as the data file, 
   as well as in one above it. The consolidated metadata object would start with the 
   contents of the higher-level file (data/file_metadata.json), and then update it with 
   the contents of the lower-level file (data/subject-1/file_metadata.json).
 - data/subject-1/subject-1_condition-B_data.csv: The same process unfolds as for the previous 
   file; however, the consolidated object is now further updated with the contents of the target 
   data file’s JSON sidecar (i.e., subject-1_condition-B_data.json).
 - data/subject-2/subject-2_condition-A_data.csv: The contents of data/file_metadata.json 
   are read, and then updated with the contents of data/subject-2/subject-2_condition-A_data.json.
 - data/subject-2/subject-2_condition-B_data.csv: There is only a single applicable metadata 
   file (data/file_metadata.json), from which all metadata is read.

Note that any inherited key/value pair from a metadata file replaces the value for the key wholesale,
and there is no merging processed involved. For instance, if the root metadata file contains a "variableMeasured"
property with 10 elements, and a lower level metadata file contains a "variableMeasured" property with
5 elements, the resulting inherited object will only contain the 5 "variableMeasured" elements
from the inherited metadata. The lists are not combined in any way, but replaced.

| Property | Value |
|----------|--------|
