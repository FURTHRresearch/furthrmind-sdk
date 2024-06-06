import os.path

from furthrmind.collection import Experiment, Sample, ResearchItem
from furthrmind import Furthrmind
from typing_extensions import List


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
    return exp


def create_many_experiments():
    data = [
        {"name": "myexperiment111",
         "group_name": "Default group"}
    ]
    Experiment.create_many(data)

def create_sample():
    sample = Sample.create("mysample", group_name="Default group")
    print(sample)


def create_researchitem():
    ri = ResearchItem.create("mysample", group_name="Default group", category_name="test")
    print(ri)


def get_all_experiment():
    exp_list = Experiment.get_all()

    print(1)

def download_file(exps: List[Experiment]):
    exp_name = "myexperiment111"
    for exp in exps:
        if exp.name == exp_name:
            file = exp.files[0]
            path = os.path.abspath(__file__)
            folder = os.path.dirname(path)
            print(folder)
            file.download(folder)
            bytesIO = file.download_bytes()
            file_name = "Hallo"
            with open(file_name, "wb+") as f:
                f.write(bytesIO.getvalue())
            print(1)

def get_all_samples():
    samples = Sample.get_all()
    print(1)


def set_calculation_result(exp_id, field_name):
    exp = fm.Experiment.get(exp_id)
    result = {"key": "value",
              "key2": "value2"}
    exp.set_calculation_result(result, field_name=field_name)

def test_link_exp():
    # exp = Experiment.get(name="myexperiment2")
    # exp.add_linked_experiment(experiment_name="bla")

    # sample = Sample.get(name="s2")
    # sample.add_linked_experiment(experiment_name="bla")

    ri = ResearchItem.get_by_name("test_new", "new")
    ri.add_linked_experiment(experiment_name="bla")

def test_link_sample():
    # exp = Experiment.get(name="myexperiment2")
    # exp.add_linked_sample(sample_name="s2")

    # sample = Sample.get(name="s2")
    # sample.add_linked_sample(sample_name="test_sample")

    ri = ResearchItem.get_by_name("test_new", "new")
    ri.add_linked_sample(sample_name="test_sample")

def test_link_ri():
    # exp = Experiment.get(name="myexperiment2")
    # ri = ResearchItem.get_by_name("test_new", "new")
    # print(ri)
    # exp.add_linked_researchitem(ri.id)

    # sample = Sample.get(name="s2")
    # ri = ResearchItem.get_by_name("test_new", "new")
    # print(ri)
    # sample.add_linked_researchitem(ri.id)

    ri = ResearchItem.get_by_name("test_new", "new")
    ri2 = ResearchItem.get_by_name("n2", "new")

    ri.add_linked_researchitem(ri2.id)

def remove_link_exp():
    # exp = Experiment.get(name="myexperiment2")
    # exp.remove_linked_experiment(experiment_name="bla")

    # s = Sample.get(name="s2")
    # s.remove_linked_experiment(experiment_name="myexperiment2")

    ri = ResearchItem.get_by_name("test_new", "new")
    ri.remove_linked_experiment(experiment_name="myexperiment2")

def remove_link_sample():
    # exp = Experiment.get(name="myexperiment2")
    # exp.remove_linked_sample(sample_name="s2")

    # s = Sample.get(name="test_sample")
    # s.remove_linked_sample(sample_name="s2")

    ri = ResearchItem.get_by_name("test_new", "new")
    ri.remove_linked_sample(sample_name="s2")

def remove_link_ri():
    ri = ResearchItem.get_by_name("test_new", "new")

    # exp = Experiment.get(name="myexperiment2")
    # exp.remove_linked_researchitem(ri.id)

    # s = Sample.get(name="test_sample")
    # s.remove_linked_researchitem(ri.id)

    ri_2 = ResearchItem.get_by_name("n2", "new")
    ri_2.remove_linked_researchitem(ri.id)

def get_groups():
    groups = fm.Group.get_all()
    print(groups)

def get_project_to_dict():
    projects = fm.Project.get_all()
    project = projects[0]
    data = project.to_dict()
    print(1)

def test_create_field_data():
    from furthrmind.collection import FieldData
    data = [{'field_name': 'Date & Time', 'field_type': 'Date', 'value': 1715082365.784481}]
    FieldData.create_many(data)

def test_get_many_groups():
    from furthrmind.collection import Group
    groups = Group.get_many(ids=["664da7ac527fd07f5514837e", "664da7ac527fd07f55148380"])
    for g in groups:
        print(g.id)

def test_get_short_id():
    from furthrmind.collection import Group
    group = Group.get(id="664da7ac527fd07f5514837e")
    print(group)

def test_research_item_name():
    from furthrmind.collection import ResearchItem
    ri = ResearchItem.get(name="test_cat", category_name="cat")
    print(ri)
    print(ri.id, ri.name)

def delete_group(id):
    from furthrmind.collection import Group
    Group.delete(id)

if __name__ == "__main__":
    fm = Furthrmind("http://127.0.0.1:5000", "LW8UDU23IGZ800O6OJYWS8H7IZ0C0T66", project_name="test3")
    # fm = Furthrmind("http://127.0.0.1:5000", "0ZJYO4UJEMQ76P8DCZJV1PAXROYB87PI",
    #                 project_name="ma - sergio")
    # exps = get_all_experiments()
    # exp = exps[0]
    # create_experiment()
    # create_many_experiments()
    # create_sample()
    # create_researchitem()
    #
    # datatable = exp.datatables[0]
    # column = datatable.columns[0]
    # c = column.get()
    # columns = datatable.get_columns()
    # df = datatable.get_pandas_dataframe()
    # download_file(exps)

    # get_all_samples()
    # set_calculation_result(exp_id="exp-grn9fb", field_name="calc5")
    # test_link_exp()
    # test_link_sample()
    # test_link_ri()
    # remove_link_exp()
    # remove_link_sample()
    # remove_link_ri()
    # get_groups()
    # get_project_to_dict()
    # test_create_field_data()
    # test_get_many_groups()
    # test_get_short_id()
    test_research_item_name()
    # group_id = "6650812a4766a76ef5ebc557"
    # delete_group(group_id)
    print(1)

