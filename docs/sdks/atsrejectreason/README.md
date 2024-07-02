# AtsRejectreason
(*ats_rejectreason*)

### Available Operations

* [get_reject_reasons](#get_reject_reasons) - List a batch of RejectReasons
* [add_reject_reason](#add_reject_reason) - Create a RejectReason
* [get_reject_reason](#get_reject_reason) - Retrieve a RejectReason

## get_reject_reasons

List a batch of RejectReasons

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_rejectreason.get_reject_reasons(x_connection_token='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `x_connection_token`                                        | *str*                                                       | :heavy_check_mark:                                          | The connection token                                        |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetRejectReasonsResponse](../../models/operations/getrejectreasonsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_reject_reason

Create a rejectreason in any supported Ats software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_rejectreason.add_reject_reason(x_connection_token='<value>', unified_reject_reason_input=components.UnifiedRejectReasonInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `x_connection_token`                                                                       | *str*                                                                                      | :heavy_check_mark:                                                                         | The connection token                                                                       |
| `unified_reject_reason_input`                                                              | [components.UnifiedRejectReasonInput](../../models/components/unifiedrejectreasoninput.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `remote_data`                                                                              | *Optional[bool]*                                                                           | :heavy_minus_sign:                                                                         | Set to true to include data from the original Ats software.                                |


### Response

**[operations.AddRejectReasonResponse](../../models/operations/addrejectreasonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_reject_reason

Retrieve a rejectreason from any connected Ats software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_rejectreason.get_reject_reason(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the rejectreason you want to retrieve.                |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetRejectReasonResponse](../../models/operations/getrejectreasonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
