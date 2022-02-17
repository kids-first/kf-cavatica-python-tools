"""
Script to query a cavatica project by participant id and then download the
resulting list of files.

Adapted from:
https://github.com/sbg/okAPI/blob/master/Recipes/SBPLAT/files_listByMetadataRecursive.ipynb
and
https://github.com/d3b-center/d3b-cavatica-python-tools/blob/master/scripts/import_files_from_volume.py
"""

import pandas as pd
import sevenbridges as sbg

# [USER INPUT] specify credentials file profile {cgc, sbg, default}
# this looks for a config file at ~/.sevenbridges/credentials.
# See instructions for setting up api environment here:
# https://github.com/sbg/okAPI/blob/master/Recipes/SBPLAT/Setup_API_environment.ipynb
prof = "kids-first-drc"

config_file = sbg.Config(profile=prof)
api = sbg.Api(
    config=config_file,
    error_handlers=[
        sbg.http.error_handlers.rate_limit_sleeper,
        sbg.http.error_handlers.maintenance_sleeper,
    ],
)
source_project = "cavatica/pbta-cbttc"
source_dataset = "cavatica/sd-bhjxbdqk"
source_pnoc_dataset = "cavatica/sd-m3dbxd12"
# SET THIS TO BE THE TARGET PROJECT NAME
target_project = "CBTN-DIPG-Germline Delivery"
# SET THIS TO BE WHERE YOUR PARTICIPANT LIST IS
file_path = "/home/ubuntu/mount/copy_2021-02-22-dipg-dmg-germline-IDs.txt"
participant_id_list = pd.read_csv(file_path)[
    "Kids_First_Participant_ID"
].to_list()


def find_files_by_metadata(
    metadata_to_match,
    parent=None,
    dataset_id=None,
    project_id=None,
):
    """
    If parent is set, it is a folder id to search in.
    """
    if not parent:
        # Query by metadata in the root
        matched_files = list(
            api.files.query(
                project=project_id,
                limit=100,
                metadata=metadata_to_match,
                dataset=dataset_id,
            ).all()
        )
        for item in api.files.query(
            limit=100,
            project=project_id,
            dataset=dataset_id,
        ).all():
            if item.is_folder():
                matched_files.extend(
                    find_files_by_metadata(
                        metadata_to_match,
                        item.id,
                        dataset_id,
                        project_id,
                    )
                )
    else:
        # Query by metadata in the folder
        matched_files = list(
            api.files.query(
                parent=parent,
                limit=100,
                metadata=metadata_to_match,
            ).all()
        )
        for item in api.files.query(limit=100, parent=parent).all():
            if item.is_folder():
                matched_files.extend(
                    find_files_by_metadata(
                        metadata_to_match,
                        item.id,
                        dataset_id,
                        project_id,
                    )
                )
    return matched_files


# Double-check that your project exists
my_project = api.projects.query(name=target_project)
if not my_project:
    print(f"Your project ({target_project}) not found, check spelling")
    raise KeyboardInterrupt
else:
    my_project = my_project[0]

# this step queries for files that are in your list of participant ids
query = {"Kids First Participant ID": participant_id_list}
print(f"searching project {source_project} files for in your participant list")
matched_project_files = find_files_by_metadata(
    query, project_id=source_project
)
print(
    f"Count of files that are in your participant list: {len(matched_project_files)}"
)

print(f"searching dataset {source_dataset} files for in your participant list")
matched_dataset_files = find_files_by_metadata(
    query, dataset_id=source_dataset
)
print(
    f"Count of files that are in your participant list: {len(matched_dataset_files)}"
)
print(
    f"searching dataset {source_pnoc_dataset} files for in your participant list"
)
matched_pnoc_dataset_files = find_files_by_metadata(
    query, dataset_id=source_pnoc_dataset
)
print(
    f"Count of files that are in your participant list: {len(matched_pnoc_dataset_files)}"
)
breakpoint()
matched_project_files.extend(matched_dataset_files).extend(
    matched_pnoc_dataset_files
)

print(
    "building unique list of files"
    + "(some files may be in both project and dataset)"
)
all_files = []
[
    all_files.append(f)
    for f in matched_project_files
    if f.name not in [x.name for x in all_files]
]

# LIST all file names in your project
# Note that listing files in a project does not list subfolders
my_file_names = [
    f.name for f in api.files.query(limit=100, project=my_project).all()
]


breakpoint()
# Copy files if they don't already exist in my_project
for f in all_files:
    if f.name in my_file_names:
        print(f"File {f.name} already exists in target project, skipping")
    else:
        print(
            f"File {f.name} does not exist in {my_project.name}; copying now"
        )
        new_file = f.copy(project=my_project, name=f.name)
        # re-list files in target project to verify the copy worked
        my_files = [
            f.name
            for f in api.files.query(limit=100, project=my_project).all()
        ]
        if f.name in my_files:
            print("Sucessfully copied one file!")
        else:
            print("Something went wrong...")

print("all done!")
