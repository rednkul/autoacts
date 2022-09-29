import sys, os
import openpyxl
from openpyxl.styles import PatternFill, Border, Side, Alignment, Font

import datetime

def create_acts_files(project):
    acts = project.acts.all()
    template = project.template
    make_dir(project)
    for act in acts:
        act_from_template(act, template)

def make_dir(project):
    os.chdir("media/files/projects/excel")
    project_dir_name = f'{project.name}_{project.id}'
    if not os.path.isdir("folder"):
        os.mkdir(project_dir_name)
    os.chdir(project_dir_name)


def act_from_template(act, template):
    ...



