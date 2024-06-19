# AccountingPurchaseorder
(*accounting_purchaseorder*)

### Available Operations

* [get_purchase_orders](#get_purchase_orders) - List a batch of PurchaseOrders
* [add_purchase_order](#add_purchase_order) - Create a PurchaseOrder
* [get_purchase_order](#get_purchase_order) - Retrieve a PurchaseOrder
* [add_purchase_orders](#add_purchase_orders) - Add a batch of PurchaseOrders

## get_purchase_orders

List a batch of PurchaseOrders

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_purchaseorder.get_purchase_orders(x_connection_token='<value>', remote_data=False)

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

**[operations.GetPurchaseOrdersResponse](../../models/operations/getpurchaseordersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_purchase_order

Create a purchaseorder in any supported Accounting software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_purchaseorder.add_purchase_order(x_connection_token='<value>', unified_purchase_order_input=components.UnifiedPurchaseOrderInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                         | *str*                                                                                        | :heavy_check_mark:                                                                           | The connection token                                                                         |
| `unified_purchase_order_input`                                                               | [components.UnifiedPurchaseOrderInput](../../models/components/unifiedpurchaseorderinput.md) | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `remote_data`                                                                                | *Optional[bool]*                                                                             | :heavy_minus_sign:                                                                           | Set to true to include data from the original Accounting software.                           |


### Response

**[operations.AddPurchaseOrderResponse](../../models/operations/addpurchaseorderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_purchase_order

Retrieve a purchaseorder from any connected Accounting software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_purchaseorder.get_purchase_order(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | id of the purchaseorder you want to retrieve.                      |
| `remote_data`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Set to true to include data from the original Accounting software. |


### Response

**[operations.GetPurchaseOrderResponse](../../models/operations/getpurchaseorderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_purchase_orders

Add a batch of PurchaseOrders

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_purchaseorder.add_purchase_orders(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedPurchaseOrderInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `connection_token`                                                                                 | *str*                                                                                              | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `x_connection_token`                                                                               | *str*                                                                                              | :heavy_check_mark:                                                                                 | The connection token                                                                               |
| `request_body`                                                                                     | List[[components.UnifiedPurchaseOrderInput](../../models/components/unifiedpurchaseorderinput.md)] | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `remote_data`                                                                                      | *Optional[bool]*                                                                                   | :heavy_minus_sign:                                                                                 | Set to true to include data from the original Accounting software.                                 |


### Response

**[operations.AddPurchaseOrdersResponse](../../models/operations/addpurchaseordersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
