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

Make sure to set the endpoint to the cavatica api endpoint `https://cavatica-api.sbgenomics.com/v2`in the config file.

## Recipes

### Download files from a Cavatica Project

In the `recipes` directory in this repo is a script to download files. Pass that script the name of the project you want to download all the files from and the location you want to save the files. 

#### Download All the Files in a Cavatica Project

To run the script from your shell:

```sh
python recipes/download_files.py --project project_name  --download_location path/to/files
```

#### Download Files from a Directory in a Cavatic Project

To only download files in a specific directory in a project, specify the path to those files within the project

To run the script from your shell:

```sh
python recipes/download_files.py --project project_name  --download_location path/to/files --project_path path/to/stuff
```

#### Notes

If a file can't be downloaded, a warning is sent to the console. Archived files
 can not be downloaded from the API. To Download archived files, they first need
 to be restored in Cavatica.