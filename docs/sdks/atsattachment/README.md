# AtsAttachment
(*ats_attachment*)

### Available Operations

* [get_ats_attachments](#get_ats_attachments) - List a batch of Attachments
* [add_ats_attachment](#add_ats_attachment) - Create a Attachment
* [get_ats_attachment](#get_ats_attachment) - Retrieve a Attachment

## get_ats_attachments

List a batch of Attachments

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_attachment.get_ats_attachments(x_connection_token='<value>', remote_data=False)

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

**[operations.GetAtsAttachmentsResponse](../../models/operations/getatsattachmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_ats_attachment

Create a attachment in any supported Ats software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_attachment.add_ats_attachment(x_connection_token='<value>', unified_attachment_input=components.UnifiedAttachmentInput(
    file_name='your_file_here',
    file_url='<value>',
    uploader='<value>',
    field_mappings=components.UnifiedAttachmentInputFieldMappings(),
), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | The connection token                                                                   |
| `unified_attachment_input`                                                             | [components.UnifiedAttachmentInput](../../models/components/unifiedattachmentinput.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `remote_data`                                                                          | *Optional[bool]*                                                                       | :heavy_minus_sign:                                                                     | Set to true to include data from the original Ats software.                            |


### Response

**[operations.AddAtsAttachmentResponse](../../models/operations/addatsattachmentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_ats_attachment

Retrieve a attachment from any connected Ats software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_attachment.get_ats_attachment(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the attachment you want to retrieve.                  |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetAtsAttachmentResponse](../../models/operations/getatsattachmentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
