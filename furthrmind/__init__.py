import requests
from furthrmind.collection.project import Project
import os
from furthrmind import collection


class Furthrmind:
    Experiment = collection.Experiment
    File = collection.File
    FieldData = collection.FieldData
    ResearchItem = collection.ResearchItem
    Sample = collection.Sample
    Unit = collection.Unit
    ComboBoxEntry = collection.ComboBoxEntry
    Field = collection.Field
    DataTable = collection.DataTable
    Group = collection.Group
    Column = collection.Column
    Project = collection.Project
    Category = collection.Category

    def __init__(self, host, api_key=None, api_key_file=None, project_id=None, project_name=None):

        if not host.startswith("http"):
            host = f"https://{host}"
        self.host = host
        self.base_url = f"{host}/api2"
        self.session = requests.session()
        self.project_url = None

        assert api_key is not None or api_key_file is not None, "Either api_key or api_key_file must be specified"

        if api_key_file:
            assert os.path.isfile(api_key_file), "Api key file is not a valid file"
            with open(api_key_file, "r") as f:
                api_key = f.read()

        self.session.headers.update({"X-API-KEY": api_key})

        self.api_key = api_key
        self.project_id = project_id
        self._write_fm_to_base_class()

        self.set_project(project_id, project_name)


    def set_project(self, id=None, name=None):
        if not id and not name:
            return
        if id:
            self.project_id = id
            self.project_url = f"{self.base_url}/projects/{self.project_id}"
            return
        if name:
            projects = Project.get_all()
            for project in projects:
                if project.name == name.lower():
                    self.project_id = project.id
                    self.project_url = f"{self.base_url}/projects/{self.project_id}"
                    return
            raise ValueError("Project not found")

    def get_project_url(self, project_id=None):
        if project_id is None:
            if self.project_url is None:
                raise ValueError("Project URL not set")
            return self.project_url
        else:
            project_url = f"{self.base_url}/projects/{project_id}"
            return project_url

    def _write_fm_to_base_class(self):
        from furthrmind.collection.baseclass import BaseClass
        BaseClass.fm = self

    def send_email(self, mail_to: str, mail_subject: str, mail_body: str):
        url = f"{self.base_url}/send-email"
        data = {
            "mail_to": mail_to,
            "mail_subject": mail_subject,
            "mail_body": mail_body,
        }
        self.session.post(url, json=data)



