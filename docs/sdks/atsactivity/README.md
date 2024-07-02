# AtsActivity
(*ats_activity*)

### Available Operations

* [get_activitys](#get_activitys) - List a batch of Activitys
* [add_activity](#add_activity) - Create a Activity
* [get_activity](#get_activity) - Retrieve a Activity

## get_activitys

List a batch of Activitys

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_activity.get_activitys(x_connection_token='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `x_connection_token`                                        | *str*                                                       | :heavy_check_mark:                                          | The connection token                                        |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetActivitysResponse](../../models/operations/getactivitysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_activity

Create a activity in any supported Ats software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_activity.add_activity(x_connection_token='<value>', unified_activity_input=components.UnifiedActivityInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `x_connection_token`                                                               | *str*                                                                              | :heavy_check_mark:                                                                 | The connection token                                                               |
| `unified_activity_input`                                                           | [components.UnifiedActivityInput](../../models/components/unifiedactivityinput.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `remote_data`                                                                      | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Set to true to include data from the original Ats software.                        |


### Response

**[operations.AddActivityResponse](../../models/operations/addactivityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_activity

Retrieve a activity from any connected Ats software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_activity.get_activity(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the activity you want to retrieve.                    |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetActivityResponse](../../models/operations/getactivityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
