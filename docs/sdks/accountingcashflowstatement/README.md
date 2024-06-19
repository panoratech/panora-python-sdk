# AccountingCashflowstatement
(*accounting_cashflowstatement*)

### Available Operations

* [get_cashflow_statements](#get_cashflow_statements) - List a batch of CashflowStatements
* [add_cashflow_statement](#add_cashflow_statement) - Create a CashflowStatement
* [get_cashflow_statement](#get_cashflow_statement) - Retrieve a CashflowStatement
* [add_cashflow_statements](#add_cashflow_statements) - Add a batch of CashflowStatements

## get_cashflow_statements

List a batch of CashflowStatements

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_cashflowstatement.get_cashflow_statements(x_connection_token='<value>', remote_data=False)

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

**[operations.GetCashflowStatementsResponse](../../models/operations/getcashflowstatementsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_cashflow_statement

Create a cashflowstatement in any supported Accounting software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_cashflowstatement.add_cashflow_statement(x_connection_token='<value>', unified_cashflow_statement_input=components.UnifiedCashflowStatementInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | The connection token                                                                                 |
| `unified_cashflow_statement_input`                                                                   | [components.UnifiedCashflowStatementInput](../../models/components/unifiedcashflowstatementinput.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `remote_data`                                                                                        | *Optional[bool]*                                                                                     | :heavy_minus_sign:                                                                                   | Set to true to include data from the original Accounting software.                                   |


### Response

**[operations.AddCashflowStatementResponse](../../models/operations/addcashflowstatementresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_cashflow_statement

Retrieve a cashflowstatement from any connected Accounting software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_cashflowstatement.get_cashflow_statement(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | id of the cashflowstatement you want to retrieve.                  |
| `remote_data`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Set to true to include data from the original Accounting software. |


### Response

**[operations.GetCashflowStatementResponse](../../models/operations/getcashflowstatementresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_cashflow_statements

Add a batch of CashflowStatements

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_cashflowstatement.add_cashflow_statements(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedCashflowStatementInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `connection_token`                                                                                         | *str*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `x_connection_token`                                                                                       | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The connection token                                                                                       |
| `request_body`                                                                                             | List[[components.UnifiedCashflowStatementInput](../../models/components/unifiedcashflowstatementinput.md)] | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `remote_data`                                                                                              | *Optional[bool]*                                                                                           | :heavy_minus_sign:                                                                                         | Set to true to include data from the original Accounting software.                                         |


### Response

**[operations.AddCashflowStatementsResponse](../../models/operations/addcashflowstatementsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
