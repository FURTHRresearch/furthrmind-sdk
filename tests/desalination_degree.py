from furthrmind_sdk.furthrmind import FURTHRmind
from furthrmind_sdk.collection import Experiment, ResearchItem

def calc(config):
    host = config["callbackUrl"]
    api_key = config["apiKey"]
    project_id = config["projectId"]
    
    fm = FURTHRmind(host=host, api_key=api_key, project_id=project_id)
    result_item_id = config.get("researchItemId")
    
    result_item = get_result_item(result_item_id)
    exp = get_exp(result_item)
    
    if not exp:
        set_result({"error": "exp not found"})
        
    sample_aw = get_sample_aw(exp)
    sample_dil_out = get_sample_dil_out(exp)
    print(1)


def get_result_item(research_item_id):
    result_item = ResearchItem.get(research_item_id)
    return result_item

def get_exp(result_item):
    if result_item.linked_experiments:
        exp = result_item.linked_experiments[0]
        exp = exp.get()
        return exp

def get_sample_aw(exp: Experiment):
    cat_dict = exp.linked_researchitems
    sample_aw = cat_dict["Samples_AW"][0]
    sample_aw = sample_aw.get()
    return sample_aw

def get_sample_dil_out(exp: Experiment):
    cat_dict = exp.linked_researchitems
    sample_do = cat_dict["Samples_DilOut"][0]
    sample_do = sample_do.get()
    return sample_do
        


def set_result(result_dict, fm):
    url = f"{ fm.base_url }/set-result/{config['fieldId']}"

if __name__ == "__main__":
    import os
    home = os.path.expanduser("~")
    api_key_path = os.path.join(home, "furthrmind_avt")
    with open(api_key_path, "r") as f:
        api_key = f.read()
        
    config = {
        "projectId": "65f1a25742983e7643bb4734",
        "callbackUrl": "https://furthrmind.avt.rwth-aachen.de",
        "apiKey": api_key,
        "researchItemId": "rtm-xe0p0k"
    }
    
    calc(config)
    print(1)