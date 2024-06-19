# AccountingVendorcredit
(*accounting_vendorcredit*)

### Available Operations

* [get_vendor_credits](#get_vendor_credits) - List a batch of VendorCredits
* [add_vendor_credit](#add_vendor_credit) - Create a VendorCredit
* [get_vendor_credit](#get_vendor_credit) - Retrieve a VendorCredit
* [add_vendor_credits](#add_vendor_credits) - Add a batch of VendorCredits

## get_vendor_credits

List a batch of VendorCredits

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_vendorcredit.get_vendor_credits(x_connection_token='<value>', remote_data=False)

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

**[operations.GetVendorCreditsResponse](../../models/operations/getvendorcreditsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_vendor_credit

Create a vendorcredit in any supported Accounting software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_vendorcredit.add_vendor_credit(x_connection_token='<value>', unified_vendor_credit_input=components.UnifiedVendorCreditInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `x_connection_token`                                                                       | *str*                                                                                      | :heavy_check_mark:                                                                         | The connection token                                                                       |
| `unified_vendor_credit_input`                                                              | [components.UnifiedVendorCreditInput](../../models/components/unifiedvendorcreditinput.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `remote_data`                                                                              | *Optional[bool]*                                                                           | :heavy_minus_sign:                                                                         | Set to true to include data from the original Accounting software.                         |


### Response

**[operations.AddVendorCreditResponse](../../models/operations/addvendorcreditresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_vendor_credit

Retrieve a vendorcredit from any connected Accounting software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_vendorcredit.get_vendor_credit(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | id of the vendorcredit you want to retrieve.                       |
| `remote_data`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Set to true to include data from the original Accounting software. |


### Response

**[operations.GetVendorCreditResponse](../../models/operations/getvendorcreditresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_vendor_credits

Add a batch of VendorCredits

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_vendorcredit.add_vendor_credits(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedVendorCreditInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `connection_token`                                                                               | *str*                                                                                            | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `x_connection_token`                                                                             | *str*                                                                                            | :heavy_check_mark:                                                                               | The connection token                                                                             |
| `request_body`                                                                                   | List[[components.UnifiedVendorCreditInput](../../models/components/unifiedvendorcreditinput.md)] | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `remote_data`                                                                                    | *Optional[bool]*                                                                                 | :heavy_minus_sign:                                                                               | Set to true to include data from the original Accounting software.                               |


### Response

**[operations.AddVendorCreditsResponse](../../models/operations/addvendorcreditsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
