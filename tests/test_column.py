import pytest

from tests import fm
import datetime
import iteration_utilities
import pandas as pd
import numpy as np

def test_create_column(fm):
    name = "my column"
    type = "text"
    data = ["aaa", "bbb", "ccc"]

    column = fm.Column.create(name, type, data)

    assert column.id is not None
    assert column.id != ""
    assert column.name == name

def test_create_column_numeric(fm):
    name = "my column"
    type = "numeric"
    data = ["aaa", "bbb", "ccc"]

    with pytest.raises(Exception) as e:
        fm.Column.create(name, type, data)
        print(e)
        assert e is ValueError

    name = "my column"
    type = "numeric"
    data = [1, "2", "2.3"]
    column = fm.Column.create(name, type, data)
    assert column.id is not None
    assert column.id != ""
    assert len(column.id) == 24
    assert column.values == [1, 2, 2.3]


def test_create_column_date(fm):
    name = "my column"
    _type = "date"
    data = ["aaa", "bbb", "ccc"]

    with pytest.raises(Exception) as e:
        fm.Column.create(name, _type, data)
        print(e)
        assert e is ValueError

    name = "my column"
    _type = "date"
    now = datetime.datetime.now()
    ts = int(now.timestamp())
    iso = now.isoformat()
    data = [now, ts, iso]
    column = fm.Column.create(name, _type, data)
    assert column.id is not None
    assert column.id != ""
    assert len(column.id) == 24
    now = now.replace(microsecond=0)
    for v in column.values:
        v = v.replace(microsecond=0)
        assert v == now

    id = column.id
    column = fm.Column.get(id)
    assert iteration_utilities.all_isinstance(column.values, (datetime.datetime, type(None)))
    print(column)

def test_type_check(fm):
    _type = "text"
    data = [1,"aaa"]
    data = fm.Column._type_check(_type, data)
    assert data == ["1", "aaa"]

    _type = "numeric"
    data = [1, "2"]
    data = fm.Column._type_check(_type, data)
    assert data == [1.0, 2.0]

    _type = "numeric"
    data = [1, None]
    data = fm.Column._type_check(_type, data)
    assert data == [1.0, None]

    _type = "date"
    now = datetime.datetime.now()
    data = [now, None]
    data = fm.Column._type_check(_type, data)
    assert data == [now.isoformat(), None]

    _type = "numeric"
    data = {1: [1, 2]}
    df = pd.DataFrame.from_dict(data)
    data = df[1]
    data = fm.Column._type_check(_type, data)
    assert data == [1.0, 2.0]

    data = {1: [1, np.nan]}
    df = pd.DataFrame.from_dict(data)
    data = df[1]
    data = fm.Column._type_check(_type, data)
    assert data == [1.0, None]

    _type = "numeric2"
    data = {1: [1, np.nan]}
    df = pd.DataFrame.from_dict(data)
    data = df[1]
    with pytest.raises(Exception) as e:
        data = fm.Column._type_check(_type, data)
        print(e)
        assert e is ValueError


if __name__ == "__main__":
    fm = fm()
    test_create_column_date(fm)