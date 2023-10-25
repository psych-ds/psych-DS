# psych-DS

Psych-DS is a community attempt to define a standard way of formatting and documenting scientific datasets. It started as a hackathon at [SIPS](https://improvingpsych.org) 2018, and is heavily inspired by the [Brain Image Data Structure (BIDS)](https://bids.neuroimaging.io/) standard for fMRI data. Writing a standard for more general psychological work poses additional and unique challenges due to the more varied nature of psychology research.

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

[Psych-DS mailing list](https://groups.google.com/forum/#!forum/psych-data-standards): Discussions about building Psych-DS. You can search the archives to see if a topic has been discussed before, or read previous project updates. [Fill out this form](https://goo.gl/forms/2dd6rouM1efJ3UBh2) to join the mailing list, or just to be notified about Psych-DS when we officially launch the specification.

[Draft Technical Specification](https://docs.google.com/document/d/1u8o5jnWk0Iqp_J06PTu5NjBfVsdoPbBhstht6W0fFp0/edit?usp=sharing) - As of October 2023, this crowdsourced Google Doc is the gold-standard reference of what "counts" as the Psych-DS standard. Up until now, most development of the specification has taken place using comments on this doc, but we are going to be transitioning to issues-based discussion for our main workflow. 

[Issues on this repo](https://github.com/psych-ds/psych-DS/issues) - Issues are the "to do" list of a github repository. Once they are created, anyone can contribute to the project by making comments on it or doing whatever is described in that issue.  Comment on the issue if you would like to work on it or find out what work might already be going on with a particular task! An issue that anyone reading this can help with is [Issue #12](https://github.com/psych-ds/psych-DS/issues/12). 

New issues on this repository should be used for two things: (1) General ideas/questions about how we will get things done with Psych-DS, including proposing tools, ideas about the scope of the specification, or "meta" issues about the project such as ideas for thinking about training and documentation. (2) Ambiguities or decision points on the content of Psych-DS itself. As @bleonar5 is beginning to implement the validator tools, he will be finding places where our human-language descriptions are ambiguous, or where trying to implement a particular rule raises questions about whether we really meant that. Other contributors should feel free to open this type of issue as well! Each individual issue should discuss just one specific aspect of Psych-DS that's under consideration. 

[The psychds-validator](https://github.com/psych-ds/psychds-validator/) - This is the actual (in-progress) validator which will become the new gold-standard reference for Psych-DS, and which will be used by researchers and tool-builders to check whether an individual dataset follows all the rules of the Psych-DS standard. Issues on this repository should be about the implementation of the validator tools, rather than about the content of the specification.  This can include both engineering/architecture questions (how should error messages be factored into the LinkML objects?) and usage questions (Will I be able to do XYZ with the validator? I tried to do ABC with the validator and had a problem, how do I fix it?) 

[Psych-DS example datasets](https://github.com/psych-ds/example-datasets) - In order to make sure the draft specification actually does what it's supposed to, we need to test it out on some *real* datasets. Importantly, these datasets do NOT need to already be in a perfect Psych-DS format, because one of the things we are working on is the process of how to convert datasets. Check out this repository either to browse some examples of what Psych-DS could look like or contribute one of your own. 

Some resources from earlier in Psych-DS development: 

[Psych-DS Hackathon Repositories](https://osf.io/dctue/): - Records from (mostly) annual SIPS Hackathons about Psych-DS.

[OpenCanvas](https://docs.google.com/presentation/d/1GQUpUPL3dHGc-Eb_3dL6WcXnA4hXpUanjAc8jUp16S0/edit?usp=sharing) - a basic definition/roadmap for the project (constructed for the Mozilla Open Leaders workshop and open for comment!)
