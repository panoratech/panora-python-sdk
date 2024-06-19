# MarketingautomationContact
(*marketingautomation_contact*)

### Available Operations

* [get_marketing_automation_contacts](#get_marketing_automation_contacts) - List a batch of Contacts
* [add_marketing_automation_contact](#add_marketing_automation_contact) - Create a Contact
* [get_marketing_automation_contact](#get_marketing_automation_contact) - Retrieve a Contact
* [add_marketing_automation_contacts](#add_marketing_automation_contacts) - Add a batch of Contacts

## get_marketing_automation_contacts

List a batch of Contacts

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_contact.get_marketing_automation_contacts(x_connection_token='<value>', remote_data=False)

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

**[operations.GetMarketingAutomationContactsResponse](../../models/operations/getmarketingautomationcontactsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_marketing_automation_contact

Create a contact in any supported Marketingautomation software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_contact.add_marketing_automation_contact(x_connection_token='<value>', unified_contact_input=components.UnifiedContactInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `x_connection_token`                                                             | *str*                                                                            | :heavy_check_mark:                                                               | The connection token                                                             |
| `unified_contact_input`                                                          | [components.UnifiedContactInput](../../models/components/unifiedcontactinput.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `remote_data`                                                                    | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | Set to true to include data from the original Marketingautomation software.      |


### Response

**[operations.AddMarketingAutomationContactResponse](../../models/operations/addmarketingautomationcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_marketing_automation_contact

Retrieve a contact from any connected Marketingautomation software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_contact.get_marketing_automation_contact(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | id of the contact you want to retrieve.                                     |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Marketingautomation software. |


### Response

**[operations.GetMarketingAutomationContactResponse](../../models/operations/getmarketingautomationcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_marketing_automation_contacts

Add a batch of Contacts

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_contact.add_marketing_automation_contacts(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedContactInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `connection_token`                                                                     | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `x_connection_token`                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | The connection token                                                                   |
| `request_body`                                                                         | List[[components.UnifiedContactInput](../../models/components/unifiedcontactinput.md)] | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `remote_data`                                                                          | *Optional[bool]*                                                                       | :heavy_minus_sign:                                                                     | Set to true to include data from the original Marketingautomation software.            |


### Response

**[operations.AddMarketingAutomationContactsResponse](../../models/operations/addmarketingautomationcontactsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
