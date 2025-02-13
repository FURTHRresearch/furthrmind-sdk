import pytest

from tests import fm

def test_get_project(fm):
    project = fm.Project.get(fm.project_id)
    print(project)
    
    name = 'Maskentests_1'
    project = fm.Project.get(name=name)
    
    assert project.name == name
    
    project = fm.Project.get(name=name.lower())
    assert project.name == name
    
    project._fetched = False
    project.get()
    
    assert project.name == name
    assert project._fetched == True
    