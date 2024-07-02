# AccountingCompanyinfo
(*accounting_companyinfo*)

### Available Operations

* [get_company_infos](#get_company_infos) - List a batch of CompanyInfos
* [add_company_info](#add_company_info) - Create a CompanyInfo
* [get_company_info](#get_company_info) - Retrieve a CompanyInfo

## get_company_infos

List a batch of CompanyInfos

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_companyinfo.get_company_infos(x_connection_token='<value>', remote_data=False)

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

**[operations.GetCompanyInfosResponse](../../models/operations/getcompanyinfosresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_company_info

Create a companyinfo in any supported Accounting software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_companyinfo.add_company_info(x_connection_token='<value>', unified_company_info_input=components.UnifiedCompanyInfoInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                     | *str*                                                                                    | :heavy_check_mark:                                                                       | The connection token                                                                     |
| `unified_company_info_input`                                                             | [components.UnifiedCompanyInfoInput](../../models/components/unifiedcompanyinfoinput.md) | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `remote_data`                                                                            | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | Set to true to include data from the original Accounting software.                       |


### Response

**[operations.AddCompanyInfoResponse](../../models/operations/addcompanyinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_company_info

Retrieve a companyinfo from any connected Accounting software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_companyinfo.get_company_info(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | id of the companyinfo you want to retrieve.                        |
| `remote_data`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Set to true to include data from the original Accounting software. |


### Response

**[operations.GetCompanyInfoResponse](../../models/operations/getcompanyinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
