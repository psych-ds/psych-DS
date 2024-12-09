# Psych-DS Schema Model

This repository contains the [LinkML](https://linkml.io/) schema model Psych-DS, which serves as the source of ground truth for what constitutes a valid Psych-DS dataset. The schema model is employed by our validator tools as a reference for all rules and objects to check for. The repository also contains python scripts for generating consolidated JSON representations of the schema model as well as generating markdown documents that correspond to the various YAML files that constitute the schema.

For a detailed overview of the LinkML framework and our schema model structure, check out [this page](https://psychds-docs.readthedocs.io/en/latest/reference/schema/schema_overview/) of our docs website.


## Repository Structure

```
schema_model
├── README.md
├── external_schemas
│   └── schemaorg # JSON and YAML versions of schema.org ontology
├── tools
│   ├── convert_to_json.py # script for creating consolidated JSON files of schema model directories
│   └── yaml_to_md.py # script for converting YAML schema model to markdown documentation reference
└── versions # separate directories for each version of the schema model
    ├── jsons # separate directories for each JSON version of the schema model
```

## YAML file example:
```yaml
# rules/files/tabular_data/data.yaml
Datafile: # name of the object to look for, in this case a canonical data file
  requires: data # a "data" directory must be found before the absence of a Datafile is reported
  suffix: "data" # sthe last substring before the extension should be "_data"
  extensions: # the file extension should be ".csv"
    - ".csv"
  baseDir: "data" # the file must be found somewhere under the "/data" subdirectory
  arbitraryNesting: true # the file can be embedded under any number of subdirectories, as long as the first subdirectory is "/data"
  columnsMatchMetadata: true # the column headers found in the file must appear in the "variableMeasured" field of the compiled metadata object
  usesKeywords: true # the filename must use keyword formatting
  nonCanonicalKeywordsAllowed: true # the keywords are not required to come from the official list 
  fileRegex: '([a-z]+-[a-zA-Z0-9]+)(_[a-z]+-[a-zA-Z0-9]+)*_data\.csv' # the filename must conform overall to this regular expression
  code: "MISSING_DATAFILE" # if no valid datafile is found but the "/data" subdirectory is present, then an error with the following parameters will be reported
  level: error
  reason: "No CSV files were found in the data subdirectory (or all of the CSV files found there had a problem - see other error messages.) There must be at least one valid csv datafile under the data/ subdirectory."
```

## Running scripts

To create a JSON file out of a given version of the schema:
```bash
source pyenv/bin/activate
python3 schema_model/tools/convert_to_json.py <version_number>
```

To generate a directory of markdown documents from a given version of the schema:
```bash
source pyenv/bin/activate
python3 schema_model/tools/yaml_to_md.py <version_number>
```

## Learn More
To get started creating high quality datasets, check out [our website](https://psych-ds.github.io/)

For detailed documentation, tutorials, and reference materials, check out our [Readthedocs site](https://psychds-docs.readthedocs.io/en/latest/)

(end of draft README)
---

# Psych-DS

Psych-DS is a community data standard, providing a systematic way of formatting and documenting scientific datasets. It started as a hackathon at [SIPS](https://improvingpsych.org) 2018, and is heavily inspired by the [Brain Image Data Structure (BIDS)](https://bids.neuroimaging.io/) standard for fMRI data.

Psych-DS incorporates a few types of existing recommendations for organizing our work ([well-formatted spreadsheets](https://peerj.com/preprints/3183/), [data dictionaries](https://osf.io/vd4y3/), and [sensible folder structure](https://www.projecttier.org/tier-protocol/specifications/)) into a technical specification - a series of requirements for file structure and format that constitute a standard machine-readable template.

This is an ongoing project, and we are actively looking for contributors! (See [How to contribute](#how-to-contribute)). The current maintainers are Melissa Kline Struhl (Project Lead, @mekline) and Brian Leonard (Software Engineer, @bleonar5). 

*The page you are reading right now shows the advantage of having a technical spec! Across many programming languages and contexts, programmers have agreed to use [a file named README](https://en.wikipedia.org/wiki/README) to describe what a project is about to a person who wants to learn about it.  Because this is a widely adopted and specific convention, a website like GitHub can support new features - when you put a file named README at the top of a repository, GitHub assumes it is the description of the project, and displays it nicely below the repository files. (This is really a raw text document, which you can see by clicking on the link to README.md in the file list above. It uses [Markdown](https://en.wikipedia.org/wiki/Markdown), which is a lightweight way to format text for readable documents.)*

## Some benefits of applying a technical specification to our datasets:

* From the beginning of a project, a researcher can format their data in a way that is likely to make their life easy for data analysis & management, and which will be easy to document and share. We can also avoid the kinds of problems illustrated in [this panda-based cartoon tragedy](https://youtu.be/N2zK3sAtr-4?t=88). Even if you are working on your own, remember that 

* People who make software tools for working with these datasets can write simpler code, and clearly communicate to a user what their data needs to look like to work with the tool. They can also make tools that work well with one another!

* Repositories (and researchers) can extract critical information about datasets to display them and make them discoverable (e.g. indexed by Google Datasets and other search tools.)  

# Ground rules/code of conduct

This project welcomes contributions and contributors of all kinds, and expects you to treat each other with respect. We have adopted a code of conduct based on [Contributor Covenant](https://www.contributor-covenant.org/version/1/4/code-of-conduct), which you can see [here](https://github.com/psych-ds/psych-DS/blob/master/CODE_OF_CONDUCT.md) in full.  Please contact Melissa (mekline@mit.edu) if you have any concerns.

# How to Contribute

This repository serves as the entry point into the Psych-DS project, but many project docs and discussions are elsewhere. As work (led by Brian Leonard, @bleonar5) is gearing up on the validator software, we are beginning to establish more specific ways of working together, but you are always welcome to write a message to the listserv to ask questions! Here is a list of ways to work on the Psych-DS project:

[Psych-DS documentation website](https://psychds-docs.readthedocs.io/en/latest/) - This is the most comprehensive and up-to-date source of information about the Psych-DS standard and its relevant tools. It contains general context, conceptual explanations, various tutorials, links to tools, and schema reference materials. Feel free to make any suggestions for changes/additions to the docs in the form of an [issue on the repository](https://github.com/psych-ds/psychds-docs).

[Psych-DS mailing list](https://groups.google.com/forum/#!forum/psych-data-standards): Discussions about building Psych-DS. You can search the archives to see if a topic has been discussed before, or read previous project updates. [Fill out this form](https://goo.gl/forms/2dd6rouM1efJ3UBh2) to join the mailing list, or just to be notified about Psych-DS when we officially launch the specification.

[Draft Technical Specification](https://docs.google.com/document/d/1u8o5jnWk0Iqp_J06PTu5NjBfVsdoPbBhstht6W0fFp0/edit?usp=sharing) - As of October 2023, this crowdsourced Google Doc is the gold-standard reference of what "counts" as the Psych-DS standard. Up until now, most development of the specification has taken place using comments on this doc, but we are going to be transitioning to issues-based discussion for our main workflow. 

[Issues on this repo](https://github.com/psych-ds/psych-DS/issues) - Issues are the "to do" list of a github repository. Once they are created, anyone can contribute to the project by making comments on it or doing whatever is described in that issue.  Comment on the issue if you would like to work on it or find out what work might already be going on with a particular task! An issue that anyone reading this can help with is [Issue #12](https://github.com/psych-ds/psych-DS/issues/12). 

New issues on this repository should be used for two things: (1) General ideas/questions about how we will get things done with Psych-DS, including proposing tools, ideas about the scope of the specification, or "meta" issues about the project such as ideas for thinking about training and documentation. (2) Ambiguities or decision points on the content of Psych-DS itself. As @bleonar5 is beginning to implement the validator tools, he will be finding places where our human-language descriptions are ambiguous, or where trying to implement a particular rule raises questions about whether we really meant that. Other contributors should feel free to open this type of issue as well! Each individual issue should discuss just one specific aspect of Psych-DS that's under consideration. 

[The Psych-DS Web Validator](https://psych-ds.github.io/validator/) - This is a browser-based tool that any researcher can easily use to input their datasets and check to see if it passes all the rules of the Psych-DS schema. In addition to binary VALID/INVALID feedback, the web validator will proceed through a checklist of all the Psych-DS rules, show you exactly where your dataset fails, and provide actionable feedback on how to resolve the error. Feedback on any aspect of the tool (aesthetics, bugs, feature requests) can be provided in the form of an [issue on the psychds-validator-web repository](https://github.com/psych-ds/psychds-validator-web/issues/new).

[The psychds-validator](https://github.com/psych-ds/psychds-validator/) - This is the source code for all versions of the validator app, and it also functions as a command-line alternative to the web version. It can either be installed directly as a Deno application or [installed via npm as a node package](https://www.npmjs.com/package/psychds-validator). Issues on this repository should be about the implementation of the validator tools, rather than about the content of the specification.  This can include both engineering/architecture questions (how should error messages be factored into the LinkML objects?) and usage questions (Will I be able to do XYZ with the validator? I tried to do ABC with the validator and had a problem, how do I fix it?) 

[Psych-DS example datasets](https://github.com/psych-ds/example-datasets) - In order to make sure the draft specification actually does what it's supposed to, we need to test it out on some *real* datasets. Importantly, these datasets do NOT need to already be in a perfect Psych-DS format, because one of the things we are working on is the process of how to convert datasets. Check out this repository either to browse some examples of what Psych-DS could look like or contribute one of your own. 

Some resources from earlier in Psych-DS development: 

[Psych-DS Hackathon Repositories](https://osf.io/dctue/): - Records from (mostly) annual SIPS Hackathons about Psych-DS.

[OpenCanvas](https://docs.google.com/presentation/d/1GQUpUPL3dHGc-Eb_3dL6WcXnA4hXpUanjAc8jUp16S0/edit?usp=sharing) - a basic definition/roadmap for the project (constructed for the Mozilla Open Leaders workshop and open for comment!)
