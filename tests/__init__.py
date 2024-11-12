import pytest
from furthrmind import Furthrmind

# host = "https://dev.furthrmind.app"
host = "http://127.0.0.1:5000"
# project_id = "666ada37a9afdf19c9528802"
project_id = "6319f6fb01c844a436e07971"
api_key_path = "/mnt/c/Users/danie/furthrmind_demo_api_key.txt"

@pytest.fixture
def fm():
     fm = Furthrmind(host=host, project_id=project_id, api_key_file=api_key_path)
     return fm
