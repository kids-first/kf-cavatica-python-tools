import sevenbridges as sbg


def fetch_project(api, project_name=None, project_id=None):
    """
    fetch a project from the sb api.
    :param api: API object generated by sevenbridges.Api()
    :type api: Sevenbridges API Object
    :param project_name: name of a project to return e.g. 'forsure'
    :type project_name: string
    :param project_id: username/project name pair - e.g. 'doesnotexist/forsure'
    :type project_id: string
    :return: Project object from the sevenbridges api
    :rtype: sevenbridges.models.project.Project
    """
    if project_id:
        project = api.projects.get(id=project_id)
        if not project.id:
            print(
                f"""Project {project_id} not found. Check spelling
             (especially trailing spaces)"""
            )
            raise KeyboardInterrupt
        else:
            return project
    elif project_name:
        project_list = api.projects.query(name=project_name)
        if not project_list:
            print(
                f"""Project {project_name} not found. Check spelling
             (especially trailing spaces)"""
            )
            raise KeyboardInterrupt
        else:
            return project_list[0]
    else:
        print("No project passed.")
        raise KeyboardInterrupt
