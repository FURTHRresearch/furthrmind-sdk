import pytest

from tests import fm
from datetime import datetime
import random
import string

def test_get_exp_fielddata_value_date(fm):
    exp_name = "3M - 9501V+_LH326_P_Maskentest"
    exp = fm.Experiment.get(name=exp_name)
    assert exp.name == exp_name
    for fd in exp.fielddata:
        if fd.field_type.lower() == "date":
            assert isinstance(fd.value, (datetime, type(None)))

def test_create_experiment(fm):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    exp = fm.Experiment.create(f"Test Exp {random_string}", group_name="Default group")
    
    assert len(exp.id) == 24
    
    exp = fm.Experiment.get(exp.id)
    assert exp.name == f"Test Exp {random_string}"
    return exp
    
def test_experiment_add_field(fm):
    exp = test_create_experiment(fm)
    exp.add_field("Test Field", "Numeric", value=123)
    
    exp = fm.Experiment.get(exp.id)
    assert exp.fielddata[0].field_name == "Test Field"
    assert exp.fielddata[0].field_type == "Numeric"
    field_id = exp.fielddata[0].field_id
    
    exp.add_field(field_id=field_id, value=456)
    exp = fm.Experiment.get(exp.id)
    assert exp.fielddata[1].value == 456
    
    