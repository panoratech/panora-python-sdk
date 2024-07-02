# AccountingTaxrate
(*accounting_taxrate*)

### Available Operations

* [get_tax_rates](#get_tax_rates) - List a batch of TaxRates
* [add_tax_rate](#add_tax_rate) - Create a TaxRate
* [get_tax_rate](#get_tax_rate) - Retrieve a TaxRate

## get_tax_rates

List a batch of TaxRates

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_taxrate.get_tax_rates(x_connection_token='<value>', remote_data=False)

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

**[operations.GetTaxRatesResponse](../../models/operations/gettaxratesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_tax_rate

Create a taxrate in any supported Accounting software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_taxrate.add_tax_rate(x_connection_token='<value>', unified_tax_rate_input=components.UnifiedTaxRateInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `x_connection_token`                                                             | *str*                                                                            | :heavy_check_mark:                                                               | The connection token                                                             |
| `unified_tax_rate_input`                                                         | [components.UnifiedTaxRateInput](../../models/components/unifiedtaxrateinput.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `remote_data`                                                                    | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | Set to true to include data from the original Accounting software.               |


### Response

**[operations.AddTaxRateResponse](../../models/operations/addtaxrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_tax_rate

Retrieve a taxrate from any connected Accounting software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_taxrate.get_tax_rate(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | id of the taxrate you want to retrieve.                            |
| `remote_data`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Set to true to include data from the original Accounting software. |


### Response

**[operations.GetTaxRateResponse](../../models/operations/gettaxrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
