# MarketingautomationUser
(*marketingautomation_user*)

### Available Operations

* [get_marketing_automation_users](#get_marketing_automation_users) - List a batch of Users
* [add_marketing_automation_user](#add_marketing_automation_user) - Create a User
* [get_marketing_automation_user](#get_marketing_automation_user) - Retrieve a User
* [add_marketing_automation_users](#add_marketing_automation_users) - Add a batch of Users

## get_marketing_automation_users

List a batch of Users

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_user.get_marketing_automation_users(x_connection_token='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `x_connection_token`                                                        | *str*                                                                       | :heavy_check_mark:                                                          | The connection token                                                        |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Marketingautomation software. |


### Response

**[operations.GetMarketingAutomationUsersResponse](../../models/operations/getmarketingautomationusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_marketing_automation_user

Create a user in any supported Marketingautomation software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_user.add_marketing_automation_user(x_connection_token='<value>', unified_user_input=components.UnifiedUserInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `x_connection_token`                                                        | *str*                                                                       | :heavy_check_mark:                                                          | The connection token                                                        |
| `unified_user_input`                                                        | [components.UnifiedUserInput](../../models/components/unifieduserinput.md)  | :heavy_check_mark:                                                          | N/A                                                                         |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Marketingautomation software. |


### Response

**[operations.AddMarketingAutomationUserResponse](../../models/operations/addmarketingautomationuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_marketing_automation_user

Retrieve a user from any connected Marketingautomation software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_user.get_marketing_automation_user(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | id of the user you want to retrieve.                                        |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Marketingautomation software. |


### Response

**[operations.GetMarketingAutomationUserResponse](../../models/operations/getmarketingautomationuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_marketing_automation_users

Add a batch of Users

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_user.add_marketing_automation_users(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedUserInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `connection_token`                                                               | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              |
| `x_connection_token`                                                             | *str*                                                                            | :heavy_check_mark:                                                               | The connection token                                                             |
| `request_body`                                                                   | List[[components.UnifiedUserInput](../../models/components/unifieduserinput.md)] | :heavy_check_mark:                                                               | N/A                                                                              |
| `remote_data`                                                                    | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | Set to true to include data from the original Marketingautomation software.      |


### Response

**[operations.AddMarketingAutomationUsersResponse](../../models/operations/addmarketingautomationusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
