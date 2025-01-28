from tests import fm
from datetime import datetime
import random
import string
from tests.test_experiment import test_create_experiment
from furthrmind.collection import Experiment, DataTable

def test_create_datatable(fm):
    exp: Experiment = test_create_experiment(fm)
    
    columns = [
        {
            "name": "my column",
            "type": "Text",
            "data": ["aaa", "bbb", "ccc"]
        },
        {
            "name": "my column 2",
            "type": "Text",
            "data": ["aaa", "bbb", "ccc"]
        },
    ]
    
    datatable = exp.add_datatable(name="test_datatable", columns=columns)
    assert datatable.name == "test_datatable"
    assert isinstance(datatable, DataTable)
    
    return datatable

def test_add_column(fm):
    datatable: DataTable = test_create_datatable(fm)
    
    
    datatable.add_column(name="col3", type="text", data=["aaa", "bbb", "ccc"])
    
    new_datatable = fm.DataTable.get(datatable.id)
    
    for col in new_datatable.columns:
        if col.name == "col3":
            assert col.values == ["aaa", "bbb", "ccc"]
            
            
    
    return datatable

def test_get_pandas_dataframe(fm):
    datatable: DataTable = test_create_datatable(fm)
    
    df = datatable.get_pandas_dataframe()
    
    return datatable