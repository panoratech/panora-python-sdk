# AccountingTrackingcategory
(*accounting_trackingcategory*)

### Available Operations

* [get_tracking_categorys](#get_tracking_categorys) - List a batch of TrackingCategorys
* [add_tracking_category](#add_tracking_category) - Create a TrackingCategory
* [get_tracking_category](#get_tracking_category) - Retrieve a TrackingCategory

## get_tracking_categorys

List a batch of TrackingCategorys

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_trackingcategory.get_tracking_categorys(x_connection_token='<value>', remote_data=False)

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

**[operations.GetTrackingCategorysResponse](../../models/operations/gettrackingcategorysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_tracking_category

Create a trackingcategory in any supported Accounting software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_trackingcategory.add_tracking_category(x_connection_token='<value>', unified_tracking_category_input=components.UnifiedTrackingCategoryInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                               | *str*                                                                                              | :heavy_check_mark:                                                                                 | The connection token                                                                               |
| `unified_tracking_category_input`                                                                  | [components.UnifiedTrackingCategoryInput](../../models/components/unifiedtrackingcategoryinput.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `remote_data`                                                                                      | *Optional[bool]*                                                                                   | :heavy_minus_sign:                                                                                 | Set to true to include data from the original Accounting software.                                 |


### Response

**[operations.AddTrackingCategoryResponse](../../models/operations/addtrackingcategoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_tracking_category

Retrieve a trackingcategory from any connected Accounting software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_trackingcategory.get_tracking_category(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | id of the trackingcategory you want to retrieve.                   |
| `remote_data`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Set to true to include data from the original Accounting software. |


### Response

**[operations.GetTrackingCategoryResponse](../../models/operations/gettrackingcategoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
