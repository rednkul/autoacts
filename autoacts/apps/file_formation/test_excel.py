import os
from django.conf import settings
from acts.models import Project
from file_formation.excel_processing import create_acts_files as caf

p = Project.objects.get(id=2)

caf(p)