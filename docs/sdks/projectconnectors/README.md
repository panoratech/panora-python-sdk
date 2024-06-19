# ProjectConnectors
(*project_connectors*)

### Available Operations

* [update_connectors_to_project](#update_connectors_to_project) - Update Connectors for a project
* [get_connectors_from_project](#get_connectors_from_project) - Retrieve connectors by Project Id

## update_connectors_to_project

Update Connectors for a project

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.project_connectors.update_connectors_to_project(request=components.ProjectConnectorsDto(
    column='<value>',
    status=False,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.ProjectConnectorsDto](../../models/components/projectconnectorsdto.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateConnectorsToProjectResponse](../../models/operations/updateconnectorstoprojectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_connectors_from_project

Retrieve connectors by Project Id

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.project_connectors.get_connectors_from_project(project_id='<value>', get_connectors_from_project='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `project_id`                  | *str*                         | :heavy_check_mark:            | N/A                           |
| `get_connectors_from_project` | *str*                         | :heavy_check_mark:            | N/A                           |


### Response

**[operations.GetConnectorsFromProjectResponse](../../models/operations/getconnectorsfromprojectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
