# Project

## Attributes

Projects do have the following attributes:

- `id`: id of the project
- `name`: name of the project
- `info`: Detailed information belonging to the project
- `shortid`: shortid of the project
- `groups`: This is a list of all groups related to this project. Each entry is a partially fetched `group` object,
  containing just the name and id. More details on this can be found in the section
  on [nested objects](../README.md#nested-objects).
- `samples`: This is a list of all samples associated with this project. Each entry is a partially fetched `sample`
  object, containing just the name and id. More details on this can be found in the section
  on [nested objects](../README.md#nested-objects).
- `experiments`: This is a list of all experiments linked to this project. Each entry is a partially
  fetched `experiment` object, containing just the name and id. More details on this can be found in the section
  on [nested objects](../README.md#nested-objects).
- `resarchitems`: This is a dictionary with category name as keys and lists and the corresponding researchitem objects
  as values.
  Each list entry is a partially fetched `researchitem` object, containing just the name and id.
  More details on this can be found in the section on [nested objects](../README.md#nested-objects).
- `fields`: This is a list of all fields associated with this project. Each item in the list is a completely
  fetched `field` object.
- `units`: This is a list of all units belonging to this project. Each item in the list is a completely fetched `unit`
  object
- `permissions`: This is a dictionary containing various keys. The `owner` key represents the owner of the project.
  The `users` key refers to a list of users granted access to this project, including their respective access levels.
  Lastly, the `usergroups` key relates to a list of usergroups with access privileges to this project, also presenting
  their respective access levels.
- `_fetched`: This is a Boolean attribute indicating whether all attributes have been retrieved from the server or only
  the name and ID are present. For more details, refer to the section on [nested objects](../README.md#nested-objects).

## Methods

- get(id="", name=""): This method can be called on the instance of an object