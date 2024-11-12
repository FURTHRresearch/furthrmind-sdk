import pytest

from tests import fm
from datetime import datetime

def test_get_exp_fielddata_value_date(fm):
    exp_name = "3M - 9501V+_LH326_P_Maskentest"
    exp = fm.Experiment.get(name=exp_name)
    assert exp.name == exp_name
    for fd in exp.fielddata:
        if fd.field_type.lower() == "date":
            assert isinstance(fd.value, (datetime, type(None)))
