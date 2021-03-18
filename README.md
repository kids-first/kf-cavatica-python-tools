<p align="center">
  <img src="docs/kids_first_logo.svg" alt="Kids First repository logo" width="660px" />
</p>
<p align="center">
  <a href="https://github.com/kids-first/kf-cavatica-python-tools/blob/master/LICENSE"><img src="https://img.shields.io/github/license/kids-first/kf-cavatica-python-tools.svg?style=for-the-badge"></a>
</p>

# Kids First CAVATICA Python Tools Repository

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
