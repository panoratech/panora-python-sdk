# AtsOffice
(*ats_office*)

### Available Operations

* [get_offices](#get_offices) - List a batch of Offices
* [add_office](#add_office) - Create a Office
* [get_office](#get_office) - Retrieve a Office

## get_offices

List a batch of Offices

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_office.get_offices(x_connection_token='<value>', remote_data=False)

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

**[operations.GetOfficesResponse](../../models/operations/getofficesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_office

Create a office in any supported Ats software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_office.add_office(x_connection_token='<value>', unified_office_input=components.UnifiedOfficeInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `x_connection_token`                                                           | *str*                                                                          | :heavy_check_mark:                                                             | The connection token                                                           |
| `unified_office_input`                                                         | [components.UnifiedOfficeInput](../../models/components/unifiedofficeinput.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `remote_data`                                                                  | *Optional[bool]*                                                               | :heavy_minus_sign:                                                             | Set to true to include data from the original Ats software.                    |


### Response

**[operations.AddOfficeResponse](../../models/operations/addofficeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_office

Retrieve a office from any connected Ats software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_office.get_office(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the office you want to retrieve.                      |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetOfficeResponse](../../models/operations/getofficeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
