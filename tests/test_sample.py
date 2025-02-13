import pytest

from tests import fm
from datetime import datetime
import random
import string
from furthrmind import Furthrmind

def test_copy_sample(fm: Furthrmind):
    sample_name = "LH333"
    sample = fm.Sample.get(name=sample_name)
    sample_id = sample.id
    
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    new_name = f"Test copy {random_string}"
    
    new_sample = fm.Sample.copy(sample_id, new_name, group_name="Default group", files=True, datatables=True)
    assert new_sample.name == new_name
    assert len(new_sample.fielddata) == len(sample.fielddata)
    import time
    time.sleep(3) # files and datatable are not immediately available
    new_sample = fm.Sample.get(new_sample.id)
    assert len(new_sample.files) == len(sample.files)
    assert len(new_sample.datatables) == len(sample.datatables)