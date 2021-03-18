<p align="center">
  <img src="docs/kids_first_logo.svg" alt="Kids First repository logo" width="660px" />
</p>
<p align="center">
  <a href="https://github.com/kids-first/kf-cavatica-python-tools/blob/master/LICENSE"><img src="https://img.shields.io/github/license/kids-first/kf-cavatica-python-tools.svg?style=for-the-badge"></a>
</p>

# Kids First Repository Template

Use this template to bootstrap a new Kids First repository.

### Badges

Update the LICENSE badge to point to the new repo location on GitHub.
Note that the LICENSE badge will fail to render correctly unless the repo has
been set to **public**.

Add additional badges for CI, docs, and other integrations as needed within the
`<p>` tag next to the LICENSE.

### Repo Description

Update the repositories description with a short summary of the repository's
intent.
Include an appropriate emoji at the start of the summary.

Add a handful of tags that summarize topics relating to the repository.
If the repo has a documentation site or webpage, add it next to the repository
description.

## Requires

Python >= 3.6

## Installation

```sh
pip install git+https://github.com/kids-first/kf-cavatica-python-tools.git
```

## Setup

To authenticate with sevenbridges, this package looks for a sevenbridges credential profile. For instructions to set up a credential file, see instructions on Sevenbridges' website, [here](https://docs.sevenbridges.com/docs/store-credentials-to-access-seven-bridges-client-applications-and-libraries#section-unified-configuration-file).

## Recipes

### Download All the Files in a Cavatica Project

In the `recipes` directory in this repo is a script to download files. Pass that script the name of the project you want to download all the files from and the location you want to save the files. 

To run the script from your shell:

```sh
python recipes/download_files.py --project project_name  --download_location path/to/files
```
