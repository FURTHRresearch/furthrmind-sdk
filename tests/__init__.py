from furthrmind_sdk.collection import Experiment, Sample, ResearchItem
from furthrmind_sdk.furthrmind import FURTHRmind

def get_all_experiments():
    exps = Experiment.get_all()
    return exps

def get_exp_and_add_one_fielddata(item):
    item.add_field(field_name="Num", field_type="Numeric",
                  value=5, unit="cm")

def remove_field(item):
    item.remove_field(fieldname="Num")

def add_file(item):
    item.add_file("README.md")

def update_field_value_unit(item):
    item.update_field_value(10, "Num")
    item.update_field_unit("m", "Num")

def add_fiels(item):
    fielddata_list = [
        {"field_name": "Num", "field_type": "Numeric", "value": 5, "unit": "cm"},
        {"field_name": "Num", "field_type": "Numeric", "value": 10, "unit": "cm"},
        {"field_name": "Num", "field_type": "Numeric", "value": 20, "unit": "m"},
    ]
    item.add_many_fields(fielddata_list)

def create_experiment():
    exp = Experiment.create("myexperiment2", group_name="Default group")
    print(exp)

def create_sample():
    sample = Sample.create("mysample", group_name="Default group")
    print(sample)

def create_researchitem():
    ri = ResearchItem.create("mysample", group_name="Default group", category_name="test")
    print(ri)

def get_all_experiment():

    exp_list = Experiment.get_all()

    print(1)

if __name__ == "__main__":
    # fm = FURTHRmind("http://127.0.0.1:5000", "LW8UDU23IGZ800O6OJYWS8H7IZ0C0T66", project_name="test")
    fm = FURTHRmind("http://127.0.0.1:5000", "4R25HIKQ0FXE7MFD4KSY3JJYO54E61J3", project_id="6319f6fb01c844a436e07971")
    exps = get_all_experiments()
    exp = exps[0]
    # create_experiment()
    # create_sample()
    # create_researchitem()

    datatable = exp.datatables[0]
    column = datatable.columns[0]
    column.get()

    print(1)