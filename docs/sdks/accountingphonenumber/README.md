# AccountingPhonenumber
(*accounting_phonenumber*)

### Available Operations

* [get_phone_numbers](#get_phone_numbers) - List a batch of PhoneNumbers
* [add_phone_number](#add_phone_number) - Create a PhoneNumber
* [get_phone_number](#get_phone_number) - Retrieve a PhoneNumber
* [add_phone_numbers](#add_phone_numbers) - Add a batch of PhoneNumbers

## get_phone_numbers

List a batch of PhoneNumbers

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_phonenumber.get_phone_numbers(x_connection_token='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `x_connection_token`                                               | *str*                                                              | :heavy_check_mark:                                                 | The connection token                                               |
| `remote_data`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Set to true to include data from the original Accounting software. |


### Response

**[operations.GetPhoneNumbersResponse](../../models/operations/getphonenumbersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_phone_number

Create a phonenumber in any supported Accounting software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_phonenumber.add_phone_number(x_connection_token='<value>', unified_phone_number_input=components.UnifiedPhoneNumberInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                     | *str*                                                                                    | :heavy_check_mark:                                                                       | The connection token                                                                     |
| `unified_phone_number_input`                                                             | [components.UnifiedPhoneNumberInput](../../models/components/unifiedphonenumberinput.md) | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `remote_data`                                                                            | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | Set to true to include data from the original Accounting software.                       |


### Response

**[operations.AddPhoneNumberResponse](../../models/operations/addphonenumberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_phone_number

Retrieve a phonenumber from any connected Accounting software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_phonenumber.get_phone_number(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | id of the phonenumber you want to retrieve.                        |
| `remote_data`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Set to true to include data from the original Accounting software. |


### Response

**[operations.GetPhoneNumberResponse](../../models/operations/getphonenumberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_phone_numbers

Add a batch of PhoneNumbers

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_phonenumber.add_phone_numbers(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedPhoneNumberInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `connection_token`                                                                             | *str*                                                                                          | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `x_connection_token`                                                                           | *str*                                                                                          | :heavy_check_mark:                                                                             | The connection token                                                                           |
| `request_body`                                                                                 | List[[components.UnifiedPhoneNumberInput](../../models/components/unifiedphonenumberinput.md)] | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `remote_data`                                                                                  | *Optional[bool]*                                                                               | :heavy_minus_sign:                                                                             | Set to true to include data from the original Accounting software.                             |


### Response

**[operations.AddPhoneNumbersResponse](../../models/operations/addphonenumbersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
