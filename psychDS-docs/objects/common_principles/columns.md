# Columns

Definition: In general, Psych-DS has minimal restraints and conventions regarding column names. 
We RECOMMEND that you use the controlled keywords defined elsewhere in the standard plus "_id"
as column names if referring to the relevant information in a dataset. (That is, if you record trials
with the scope of a given datafile, we RECOMMEND that the name of the column identifying the trial
be "trial_id"). This information can be redundantly stored (i.e., a file named "study-MyExp_trial-1_data.csv"
can also have a column "trial_id" which has rows with the value "1").

In many cases, some combination of columns will uniquely identify every row in the dataset (for instance,
each participant might have several rows, but there might be exactly one row for every combination of 
particupant, condition, and trial.) The column or set of columns provides a unique key for every record/row in
your dataset. We RECOMMEND that you include a description of which columns create a unique key for your dataset
in the README for your project.

If you have a column that uniquely identifies each single row of a dataset explicitly it SHOULD be named
"row_id". A column named "row_id" MUST contain unique values in every row.
