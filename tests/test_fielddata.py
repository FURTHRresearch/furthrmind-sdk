import pytest
from tests import fm
from datetime import datetime
from furthrmind import Furthrmind

def test_get_all(fm):
    fielddata = fm.FieldData.get_all()
    assert type(fielddata) == list
    assert all([type(fd) == fm.FieldData for fd in fielddata])
    assert len(fielddata) > 0
    assert hasattr(fielddata[0], "id")
    print(fielddata[0])
    print(len(fielddata))
    
def test_update_fielddata_value_date(fm: Furthrmind):
    fielddata = fm.FieldData.get_all()
    for fd in fielddata:
        if fd.field_type.lower() == "date":
            now = datetime.now()
            fd.update_value(now)
            assert fd.value == now
            break
    else:
        raise ValueError("No date field found")
    
