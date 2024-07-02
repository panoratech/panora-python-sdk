# HrisTimeoffbalance
(*hris_timeoffbalance*)

### Available Operations

* [get_timeoff_balances](#get_timeoff_balances) - List a batch of TimeoffBalances
* [add_timeoff_balance](#add_timeoff_balance) - Create a TimeoffBalance
* [get_timeoff_balance](#get_timeoff_balance) - Retrieve a TimeoffBalance

## get_timeoff_balances

List a batch of TimeoffBalances

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_timeoffbalance.get_timeoff_balances(x_connection_token='<value>', remote_data=False)

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

**[operations.GetTimeoffBalancesResponse](../../models/operations/gettimeoffbalancesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_timeoff_balance

Create a timeoffbalance in any supported Hris software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_timeoffbalance.add_timeoff_balance(x_connection_token='<value>', unified_timeoff_balance_input=components.UnifiedTimeoffBalanceInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                           | *str*                                                                                          | :heavy_check_mark:                                                                             | The connection token                                                                           |
| `unified_timeoff_balance_input`                                                                | [components.UnifiedTimeoffBalanceInput](../../models/components/unifiedtimeoffbalanceinput.md) | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `remote_data`                                                                                  | *Optional[bool]*                                                                               | :heavy_minus_sign:                                                                             | Set to true to include data from the original Hris software.                                   |


### Response

**[operations.AddTimeoffBalanceResponse](../../models/operations/addtimeoffbalanceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_timeoff_balance

Retrieve a timeoffbalance from any connected Hris software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_timeoffbalance.get_timeoff_balance(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | id of the timeoffbalance you want to retrieve.               |
| `remote_data`                                                | *Optional[bool]*                                             | :heavy_minus_sign:                                           | Set to true to include data from the original Hris software. |


### Response

**[operations.GetTimeoffBalanceResponse](../../models/operations/gettimeoffbalanceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
