# Passthrough
(*passthrough*)

### Available Operations

* [passthrough_request](#passthrough_request) - Make a passthrough request

## passthrough_request

Make a passthrough request

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.passthrough.passthrough_request(integration_id='<value>', linked_user_id='<value>', vertical='<value>', pass_through_request_dto=components.PassThroughRequestDto(
    method=components.Method.DELETE,
    path='/rescue',
))

if res.pass_through_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `integration_id`                                                                     | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `linked_user_id`                                                                     | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `vertical`                                                                           | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `pass_through_request_dto`                                                           | [components.PassThroughRequestDto](../../models/components/passthroughrequestdto.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |


### Response

**[operations.PassthroughRequestResponse](../../models/operations/passthroughrequestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
