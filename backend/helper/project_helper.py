from pathlib import Path
import os


def get_project_path():
    project_path = os.environ['PYTHONPATH'].split(os.pathsep)[0]
    return project_path


def get_folder_project_root_path():
    CWF = Path(__file__)
    HOME_PROJECT_PATH = str(CWF.parent.parent)
    return HOME_PROJECT_PATH
