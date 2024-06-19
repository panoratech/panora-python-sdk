# HrisPaygroup
(*hris_paygroup*)

### Available Operations

* [get_pay_groups](#get_pay_groups) - List a batch of PayGroups
* [add_pay_group](#add_pay_group) - Create a PayGroup
* [get_pay_group](#get_pay_group) - Retrieve a PayGroup
* [add_pay_groups](#add_pay_groups) - Add a batch of PayGroups

## get_pay_groups

List a batch of PayGroups

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_paygroup.get_pay_groups(x_connection_token='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `x_connection_token`                                         | *str*                                                        | :heavy_check_mark:                                           | The connection token                                         |
| `remote_data`                                                | *Optional[bool]*                                             | :heavy_minus_sign:                                           | Set to true to include data from the original Hris software. |


### Response

**[operations.GetPayGroupsResponse](../../models/operations/getpaygroupsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_pay_group

Create a paygroup in any supported Hris software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_paygroup.add_pay_group(x_connection_token='<value>', unified_pay_group_input=components.UnifiedPayGroupInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `x_connection_token`                                                               | *str*                                                                              | :heavy_check_mark:                                                                 | The connection token                                                               |
| `unified_pay_group_input`                                                          | [components.UnifiedPayGroupInput](../../models/components/unifiedpaygroupinput.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `remote_data`                                                                      | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Set to true to include data from the original Hris software.                       |


### Response

**[operations.AddPayGroupResponse](../../models/operations/addpaygroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_pay_group

Retrieve a paygroup from any connected Hris software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_paygroup.get_pay_group(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | id of the paygroup you want to retrieve.                     |
| `remote_data`                                                | *Optional[bool]*                                             | :heavy_minus_sign:                                           | Set to true to include data from the original Hris software. |


### Response

**[operations.GetPayGroupResponse](../../models/operations/getpaygroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_pay_groups

Add a batch of PayGroups

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_paygroup.add_pay_groups(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedPayGroupInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `connection_token`                                                                       | *str*                                                                                    | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `x_connection_token`                                                                     | *str*                                                                                    | :heavy_check_mark:                                                                       | The connection token                                                                     |
| `request_body`                                                                           | List[[components.UnifiedPayGroupInput](../../models/components/unifiedpaygroupinput.md)] | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `remote_data`                                                                            | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | Set to true to include data from the original Hris software.                             |


### Response

**[operations.AddPayGroupsResponse](../../models/operations/addpaygroupsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
