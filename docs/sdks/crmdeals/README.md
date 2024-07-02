# CrmDeals
(*crm_deals*)

### Available Operations

* [get_deals](#get_deals) - List a batch of Deals
* [add_deal](#add_deal) - Create a Deal
* [get_deal](#get_deal) - Retrieve a Deal

## get_deals

List a batch of Deals

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_deals.get_deals(x_connection_token='<value>', remote_data=False, limit=50, cursor='<value>')

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

**[operations.GetDealsResponse](../../models/operations/getdealsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_deal

Create a deal in any supported Crm software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_deals.add_deal(x_connection_token='<value>', unified_deal_input=components.UnifiedDealInput(
    name='<value>',
    description='Optional zero defect extranet',
    amount=6413.89,
    field_mappings=components.UnifiedDealInputFieldMappings(),
), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `x_connection_token`                                                       | *str*                                                                      | :heavy_check_mark:                                                         | The connection token                                                       |
| `unified_deal_input`                                                       | [components.UnifiedDealInput](../../models/components/unifieddealinput.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `remote_data`                                                              | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | Set to true to include data from the original Crm software.                |


### Response

**[operations.AddDealResponse](../../models/operations/adddealresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_deal

Retrieve a deal from any connected Crm software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_deals.get_deal(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the deal you want to retrieve.                        |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Crm software. |


### Response

**[operations.GetDealResponse](../../models/operations/getdealresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
