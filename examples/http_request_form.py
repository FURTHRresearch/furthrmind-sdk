from urllib import parse

shortid = name = category_name = category_id = parent_group_id = "aaa"
query = []
if shortid:
    query.append(("shortid", shortid))
if name:
    query.append(("name", name))
if category_name:
    query.append(("category_name", category_name))
if category_id:
    query.append(("category_id", category_id))
if parent_group_id:
    query.append(("parent_group_id", parent_group_id))
    
    
url_query = parse.urlencode(query)
print(url_query)