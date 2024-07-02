# CrmTasks
(*crm_tasks*)

### Available Operations

* [get_tasks](#get_tasks) - List a batch of Tasks
* [add_task](#add_task) - Create a Task
* [get_task](#get_task) - Retrieve a Task

## get_tasks

List a batch of Tasks

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_tasks.get_tasks(x_connection_token='<value>', remote_data=False, limit=50, cursor='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                               | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `x_connection_token`                                    | *str*                                                   | :heavy_check_mark:                                      | The connection token                                    |
| `remote_data`                                           | *Optional[bool]*                                        | :heavy_minus_sign:                                      | Set to true to include data from the original software. |
| `limit`                                                 | *Optional[float]*                                       | :heavy_minus_sign:                                      | Set to get the number of records.                       |
| `cursor`                                                | *Optional[str]*                                         | :heavy_minus_sign:                                      | Set to get the number of records after this cursor.     |


### Response

**[operations.GetTasksResponse](../../models/operations/gettasksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_task

Create a task in any supported Crm software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_tasks.add_task(x_connection_token='<value>', unified_task_input=components.UnifiedTaskInput(
    subject='<value>',
    content='<value>',
    status='<value>',
    field_mappings=components.UnifiedTaskInputFieldMappings(),
), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `x_connection_token`                                                       | *str*                                                                      | :heavy_check_mark:                                                         | The connection token                                                       |
| `unified_task_input`                                                       | [components.UnifiedTaskInput](../../models/components/unifiedtaskinput.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `remote_data`                                                              | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | Set to true to include data from the original Crm software.                |


### Response

**[operations.AddTaskResponse](../../models/operations/addtaskresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_task

Retrieve a task from any connected Crm software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_tasks.get_task(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the task you want to retrieve.                        |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Crm software. |


### Response

**[operations.GetTaskResponse](../../models/operations/gettaskresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
