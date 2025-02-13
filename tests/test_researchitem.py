import pytest

from tests import fm
from datetime import datetime
import random
import string
from furthrmind import Furthrmind

def test_create_researchitem(fm: Furthrmind):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    ri = fm.ResearchItem.create(f"Test Research Item {random_string}", group_name="Default group", category_name="Default category")
    
    assert len(ri.id) == 24
    
    ri = fm.ResearchItem.get(ri.id)
    assert ri.name == f"Test Research Item {random_string}"
    return ri

def test_copy_researchitem(fm: Furthrmind):
    ri = test_create_researchitem(fm)
    ri_id = ri.id

    ri.add_field("Test Field", "Numeric", value=123)
    
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    new_name = f"Test copy {random_string}"
    
    new_ri = fm.ResearchItem.copy(ri_id, new_name, group_name="Default group", files=True, datatable=True)
    assert new_ri.name == new_name
    assert len(new_ri.fielddata) == len(ri.fielddata)
    import time
    time.sleep(3) # files and datatable are not immediately available
    new_ri = fm.ResearchItem.get(new_ri.id)
    assert len(new_ri.files) == len(ri.files)
    assert len(new_ri.datatables) == len(ri.datatables)