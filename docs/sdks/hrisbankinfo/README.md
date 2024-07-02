# HrisBankinfo
(*hris_bankinfo*)

### Available Operations

* [get_bankinfos](#get_bankinfos) - List a batch of Bankinfos
* [add_bankinfo](#add_bankinfo) - Create a Bankinfo
* [get_bankinfo](#get_bankinfo) - Retrieve a Bankinfo

## get_bankinfos

List a batch of Bankinfos

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_bankinfo.get_bankinfos(x_connection_token='<value>', remote_data=False)

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

**[operations.GetBankinfosResponse](../../models/operations/getbankinfosresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_bankinfo

Create a bankinfo in any supported Hris software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_bankinfo.add_bankinfo(x_connection_token='<value>', unified_bank_info_input=components.UnifiedBankInfoInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `x_connection_token`                                                               | *str*                                                                              | :heavy_check_mark:                                                                 | The connection token                                                               |
| `unified_bank_info_input`                                                          | [components.UnifiedBankInfoInput](../../models/components/unifiedbankinfoinput.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `remote_data`                                                                      | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Set to true to include data from the original Hris software.                       |


### Response

**[operations.AddBankinfoResponse](../../models/operations/addbankinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_bankinfo

Retrieve a bankinfo from any connected Hris software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_bankinfo.get_bankinfo(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | id of the bankinfo you want to retrieve.                     |
| `remote_data`                                                | *Optional[bool]*                                             | :heavy_minus_sign:                                           | Set to true to include data from the original Hris software. |


### Response

**[operations.GetBankinfoResponse](../../models/operations/getbankinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
