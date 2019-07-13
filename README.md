# psych-DS

Welcome to the Psych Data Standard project! This is an in-progress community attempt to define a standard way of formatting and documenting scientific datasets. It started as a hackathon at [SIPS](https://improvingpsych.org) 2018, and is heavily inspired by the [Brain Image Data Structure (BIDS)](https://bids.neuroimaging.io/) standard for fMRI data. Writing a standard for more general psychological work poses additional and unique challenges due to the more varied nature of psychology research.

Psych-DS incorporates a few types of existing recommendations for organizing our work ([well-formatted spreadsheets](https://peerj.com/preprints/3183/), [data dictionaries](https://osf.io/vd4y3/), and [sensible folder structure](https://www.projecttier.org/tier-protocol/specifications/)) into a technical specification - a series of requirements for file structure and format that constitute a standard machine-readable template. 

*The page you are reading right now shows the advantage of having a technical spec! Across many programming languages and contexts, programmers have agreed to use [a file named README](https://en.wikipedia.org/wiki/README) to describe what a project is about to a human who wants to learn about it.  Because this is a widely adopted and specific convention, a website like GitHub can support new features - when you put a file named README at the top of a repository, GitHub assumes it is the description of the project, and displays it nicely below the repository files. (This is really a raw text document, which you can see by clicking on the link to README.md. It uses [Markdown](https://en.wikipedia.org/wiki/Markdown), which is a lightweight way to format text for readable documents.)*

## Some advantages of having a technical specification for our datasets:

* From the beginning of a project, a researcher can format their data in a way that is likely to make their life easy for data analysis & management, and which will be easy to document and share.

* People who make software tools for working with these datasets can write simpler code, and clearly communicate to a user what their data needs to look like to work with the tool. They can also make tools that work well with one another!

* Repositories (and researchers) can extract critical information about datasets to display them and make them discoverable (e.g. indexed by Google Datasets and other search tools.)  

This is an ongoing project, and we are actively looking for contributors! (See [How to get involved](#how-to-get-involved))

# Ground rules/code of conduct

This project welcomes contributions and contributors of all kinds, and expects you to treat each other with respect. We have adopted a code of conduct based on [Contributor Covenant](https://www.contributor-covenant.org/version/1/4/code-of-conduct), which you can see [here](https://github.com/psych-ds/psych-DS/blob/master/CODE_OF_CONDUCT.md) in full.  Please contact Melissa (mekline@mit.edu) if you have any concerns.

# Project Documents

This repository serves as the root/entry point for the Psych-DS project, but most project docs and discussions are elsewhere. 

[Draft Technical Specification](https://docs.google.com/document/d/1u8o5jnWk0Iqp_J06PTu5NjBfVsdoPbBhstht6W0fFp0/edit?usp=sharing) - This is the main document we are working on.

[OpenCanvas](https://docs.google.com/presentation/d/1GQUpUPL3dHGc-Eb_3dL6WcXnA4hXpUanjAc8jUp16S0/edit?usp=sharing) - a basic definition/roadmap for the project (constructed for the Mozilla Open Leaders workshop and open for comment!)

[Psych-DS mailing list](https://groups.google.com/forum/#!forum/psych-data-standards) - Discussion on building the specification starts here! If we identify a discrete task/topic, it moves to the:

[Projects Page](https://github.com/mekline/psych-DS/projects) - The Projects page of the repository organizes the open issues we're working on into some categories. If you'd like to jump right in to contributing, this is the place to look.

# Roadmap

We are starting to track project goals and milestones (aka ways to [get involved!](#how-to-get-involved)) in the [Issues](https://github.com/mekline/psych-DS/issues) section of this repository. Right now, we need help building some example datasets: 

[#11](https://github.com/mekline/psych-DS/issues/11) - In order to make sure the draft specification actually does what it's supposed to, we need to test it out on some *real* datasets. To try this on your or one of the other examples already open, check out the [example-datasets repo](https://github.com/psych-ds/example-datasets). 

# How to Get Involved

* Right now, discussions about this project take place via comments/edits to the [technical specification draft](https://docs.google.com/document/d/1u8o5jnWk0Iqp_J06PTu5NjBfVsdoPbBhstht6W0fFp0/edit?usp=sharing), on the [mailing list](https://groups.google.com/forum/#!forum/psych-data-standards), and (as plans solidify a bit more) in [Issues](https://github.com/mekline/psych-DS/issues) on this repository. Each issue has (or should have!) some instructions on how you can contribute to building a piece of Psych-DS. [Issue 12](https://github.com/mekline/psych-DS/issues/12) is a great place to start for new contributors.
* A good place to start **even if you have no coding experience** is to read the [technical specification draft](https://docs.google.com/document/d/1u8o5jnWk0Iqp_J06PTu5NjBfVsdoPbBhstht6W0fFp0/edit?usp=sharing) and simply leave a comment on anything you find to be unclear.
* If you would like to join the mailing list, OR just want to hear about Psych-DS when we officially launch the specification, fill out [this form](https://goo.gl/forms/2dd6rouM1efJ3UBh2).
* To propose edits to this README document, please submit a pull request or comment below!

Please also feel free to contact me (Melissa Kline, melissa.e.kline@gmail.com) if you have further questions.
