# Projects
(*projects*)

### Available Operations

* [get_projects](#get_projects) - Retrieve projects
* [create_project](#create_project) - Create a project

## get_projects

Retrieve projects

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.projects.get_projects()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetProjectsResponse](../../models/operations/getprojectsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_project

Create a project

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.projects.create_project(request=components.CreateProjectDto(
    name='<value>',
    id_user='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [components.CreateProjectDto](../../models/components/createprojectdto.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreateProjectResponse](../../models/operations/createprojectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
