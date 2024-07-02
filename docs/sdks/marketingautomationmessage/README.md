# MarketingautomationMessage
(*marketingautomation_message*)

### Available Operations

* [get_messages](#get_messages) - List a batch of Messages
* [add_message](#add_message) - Create a Message
* [get_message](#get_message) - Retrieve a Message

## get_messages

List a batch of Messages

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_message.get_messages(x_connection_token='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `x_connection_token`                                                        | *str*                                                                       | :heavy_check_mark:                                                          | The connection token                                                        |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Marketingautomation software. |


### Response

**[operations.GetMessagesResponse](../../models/operations/getmessagesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_message

Create a message in any supported Marketingautomation software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_message.add_message(x_connection_token='<value>', unified_message_input=components.UnifiedMessageInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `x_connection_token`                                                             | *str*                                                                            | :heavy_check_mark:                                                               | The connection token                                                             |
| `unified_message_input`                                                          | [components.UnifiedMessageInput](../../models/components/unifiedmessageinput.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `remote_data`                                                                    | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | Set to true to include data from the original Marketingautomation software.      |


### Response

**[operations.AddMessageResponse](../../models/operations/addmessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_message

Retrieve a message from any connected Marketingautomation software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_message.get_message(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | id of the message you want to retrieve.                                     |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Marketingautomation software. |


### Response

**[operations.GetMessageResponse](../../models/operations/getmessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
