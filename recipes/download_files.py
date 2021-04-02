"""
script description
"""
import sevenbridges as sbg
import argparse
import pandas as pd
from kf_cavatica.projects import fetch_project

from kf_cavatica.files import list_files_recursively
from pathlib import Path
from tqdm import tqdm
import os

# Arguments
parser = argparse.ArgumentParser(
    prog="Download files from a Cavatica Project",
    description="""Download all the files from a cavatica project.
                   """,
)
parser.add_argument(
    "--project_id",
    metavar="Cavatica project ID",
    type=str,
    help="""'Username/project_name' ID of the project in cavatica where the 
            files come from.""",
)
parser.add_argument(
    "--project_name",
    metavar="Cavatica project name",
    type=str,
    help="""Name of the project in cavatica where the files come from.
            Note that a user may have multiple projects with the same name, so
            best practice is to reference entities by ID.\n
            See `--project_id`.
            """,
)
parser.add_argument(
    "--project_path",
    metavar="Path inside project to look for files to download",
    type=str,
    help="""Specify project path to download files in a certain folder within a
            cavatica project. If no project_path is given, download all files in
            a project.
            """,
)
parser.add_argument(
    "--file_list",
    metavar="File list generated by the cavatica CLI",
    type=str,
    help="""A file list generated by the cavatica CLI:
            `sb files list --project user/project`
            """,
)
parser.add_argument(
    "--download_location",
    metavar="Location to save downloaded files",
    type=str,
    help="""location where files should be downloaded to, e.g.:
            "path/to/files/"
            """,
    default="",
)
parser.add_argument(
    "--sbg_profile",
    metavar="SBG Config Profile",
    type=str,
    help="""Configuration profile to use with the Seven Bridges API.
            Info about setting up the configuration can be found at
            https://docs.sevenbridges.com/docs/store-credentials-to-access-seven-bridges-client-applications-and-libraries
            Default is 'default'
            """,
    default="default",
)


args = parser.parse_args()
print(f"Args: {args.__dict__}")

# Create the download location if it doesn't exist
args.download_location = Path(args.download_location)
args.download_location.mkdir(parents=True, exist_ok=True)


# Connect to the API
config_file = sbg.Config(profile=args.sbg_profile)
api = sbg.Api(
    config=config_file,
    error_handlers=[
        sbg.http.error_handlers.rate_limit_sleeper,
        sbg.http.error_handlers.maintenance_sleeper,
    ],
)

# Generate the project object
project = fetch_project(api, args.project_name, args.project_id)

all_files = list_files_recursively(
    api, api.files.query(project=project), project
)
if args.project_path:
    path_name = Path(args.project_path)
    all_files = [
        f
        for f in all_files
        if not os.path.relpath(
            f.metadata["parent_file_name"], path_name
        ).startswith("..")
    ]
    print(f"{len(all_files)} files found in {path_name}")

# Download the files
for file in tqdm(all_files):
    download_location = (
        args.download_location / file.metadata["parent_file_name"]
    )
    download_location.mkdir(parents=True, exist_ok=True)
    file.download(str(download_location / file.name))
