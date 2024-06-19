# AccountingIncomestatement
(*accounting_incomestatement*)

### Available Operations

* [get_income_statements](#get_income_statements) - List a batch of IncomeStatements
* [add_income_statement](#add_income_statement) - Create a IncomeStatement
* [get_income_statement](#get_income_statement) - Retrieve a IncomeStatement
* [add_income_statements](#add_income_statements) - Add a batch of IncomeStatements

## get_income_statements

List a batch of IncomeStatements

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_incomestatement.get_income_statements(x_connection_token='<value>', remote_data=False)

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

**[operations.GetIncomeStatementsResponse](../../models/operations/getincomestatementsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_income_statement

Create a incomestatement in any supported Accounting software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_incomestatement.add_income_statement(x_connection_token='<value>', unified_income_statement_input=components.UnifiedIncomeStatementInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `x_connection_token`                                                                             | *str*                                                                                            | :heavy_check_mark:                                                                               | The connection token                                                                             |
| `unified_income_statement_input`                                                                 | [components.UnifiedIncomeStatementInput](../../models/components/unifiedincomestatementinput.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `remote_data`                                                                                    | *Optional[bool]*                                                                                 | :heavy_minus_sign:                                                                               | Set to true to include data from the original Accounting software.                               |


### Response

**[operations.AddIncomeStatementResponse](../../models/operations/addincomestatementresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_income_statement

Retrieve a incomestatement from any connected Accounting software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_incomestatement.get_income_statement(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | id of the incomestatement you want to retrieve.                    |
| `remote_data`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Set to true to include data from the original Accounting software. |


### Response

**[operations.GetIncomeStatementResponse](../../models/operations/getincomestatementresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_income_statements

Add a batch of IncomeStatements

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_incomestatement.add_income_statements(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedIncomeStatementInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `connection_token`                                                                                     | *str*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `x_connection_token`                                                                                   | *str*                                                                                                  | :heavy_check_mark:                                                                                     | The connection token                                                                                   |
| `request_body`                                                                                         | List[[components.UnifiedIncomeStatementInput](../../models/components/unifiedincomestatementinput.md)] | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `remote_data`                                                                                          | *Optional[bool]*                                                                                       | :heavy_minus_sign:                                                                                     | Set to true to include data from the original Accounting software.                                     |


### Response

**[operations.AddIncomeStatementsResponse](../../models/operations/addincomestatementsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
