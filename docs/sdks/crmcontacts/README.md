# CrmContacts
(*crm_contacts*)

### Available Operations

* [list_crm_contacts](#list_crm_contacts) - List CRM Contacts
* [add_crm_contact](#add_crm_contact) - Create CRM Contact
* [get_crm_contact](#get_crm_contact) - Retrieve a CRM Contact

## list_crm_contacts

List CRM Contacts

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_contacts.list_crm_contacts(x_connection_token='<value>', remote_data=False, limit=50, cursor='<value>')

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

**[operations.ListCrmContactsResponse](../../models/operations/listcrmcontactsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_crm_contact

Create a contact in any supported CRM

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_contacts.add_crm_contact(x_connection_token='<value>', unified_contact_input=components.UnifiedContactInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `x_connection_token`                                                             | *str*                                                                            | :heavy_check_mark:                                                               | The connection token                                                             |
| `unified_contact_input`                                                          | [components.UnifiedContactInput](../../models/components/unifiedcontactinput.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `remote_data`                                                                    | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | Set to true to include data from the original CRM software.                      |


### Response

**[operations.AddCrmContactResponse](../../models/operations/addcrmcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_crm_contact

Retrieve a contact from any connected CRM

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_contacts.get_crm_contact(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the `contact` you want to retrive.                    |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original CRM software. |


### Response

**[operations.GetCrmContactResponse](../../models/operations/getcrmcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
