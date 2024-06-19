# AccountingTransaction
(*accounting_transaction*)

### Available Operations

* [get_transactions](#get_transactions) - List a batch of Transactions
* [add_transaction](#add_transaction) - Create a Transaction
* [get_transaction](#get_transaction) - Retrieve a Transaction
* [add_transactions](#add_transactions) - Add a batch of Transactions

## get_transactions

List a batch of Transactions

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_transaction.get_transactions(x_connection_token='<value>', remote_data=False)

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

**[operations.GetTransactionsResponse](../../models/operations/gettransactionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_transaction

Create a transaction in any supported Accounting software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_transaction.add_transaction(x_connection_token='<value>', unified_transaction_input=components.UnifiedTransactionInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                     | *str*                                                                                    | :heavy_check_mark:                                                                       | The connection token                                                                     |
| `unified_transaction_input`                                                              | [components.UnifiedTransactionInput](../../models/components/unifiedtransactioninput.md) | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `remote_data`                                                                            | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | Set to true to include data from the original Accounting software.                       |


### Response

**[operations.AddTransactionResponse](../../models/operations/addtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_transaction

Retrieve a transaction from any connected Accounting software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_transaction.get_transaction(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | id of the transaction you want to retrieve.                        |
| `remote_data`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Set to true to include data from the original Accounting software. |


### Response

**[operations.GetTransactionResponse](../../models/operations/gettransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_transactions

Add a batch of Transactions

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_transaction.add_transactions(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedTransactionInput(),
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
| `request_body`                                                                                 | List[[components.UnifiedTransactionInput](../../models/components/unifiedtransactioninput.md)] | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `remote_data`                                                                                  | *Optional[bool]*                                                                               | :heavy_minus_sign:                                                                             | Set to true to include data from the original Accounting software.                             |


### Response

**[operations.AddTransactionsResponse](../../models/operations/addtransactionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
