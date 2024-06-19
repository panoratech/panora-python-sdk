# TicketingAttachments
(*ticketing_attachments*)

### Available Operations

* [get_ticketing_attachments](#get_ticketing_attachments) - List a batch of Attachments
* [add_ticketing_attachment](#add_ticketing_attachment) - Create a Attachment
* [get_ticketing_attachment](#get_ticketing_attachment) - Retrieve a Attachment
* [download_attachment](#download_attachment) - Download a Attachment
* [add_ticketing_attachments](#add_ticketing_attachments) - Add a batch of Attachments

## get_ticketing_attachments

List a batch of Attachments

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ticketing_attachments.get_ticketing_attachments(x_connection_token='<value>', remote_data=False, page_size=50, cursor='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                               | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `x_connection_token`                                    | *str*                                                   | :heavy_check_mark:                                      | The connection token                                    |
| `remote_data`                                           | *Optional[bool]*                                        | :heavy_minus_sign:                                      | Set to true to include data from the original software. |
| `page_size`                                             | *Optional[float]*                                       | :heavy_minus_sign:                                      | Set to get the number of records.                       |
| `cursor`                                                | *Optional[str]*                                         | :heavy_minus_sign:                                      | Set to get the number of records after this cursor.     |


### Response

**[operations.GetTicketingAttachmentsResponse](../../models/operations/getticketingattachmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_ticketing_attachment

Create a attachment in any supported Ticketing software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ticketing_attachments.add_ticketing_attachment(x_connection_token='<value>', unified_attachment_input=components.UnifiedAttachmentInput(
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
| `remote_data`                                                                          | *Optional[bool]*                                                                       | :heavy_minus_sign:                                                                     | Set to true to include data from the original Ticketing software.                      |


### Response

**[operations.AddTicketingAttachmentResponse](../../models/operations/addticketingattachmentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_ticketing_attachment

Retrieve a attachment from any connected Ticketing software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ticketing_attachments.get_ticketing_attachment(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `id`                                                              | *str*                                                             | :heavy_check_mark:                                                | id of the attachment you want to retrive.                         |
| `remote_data`                                                     | *Optional[bool]*                                                  | :heavy_minus_sign:                                                | Set to true to include data from the original Ticketing software. |


### Response

**[operations.GetTicketingAttachmentResponse](../../models/operations/getticketingattachmentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## download_attachment

Download a attachment from any connected Ticketing software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ticketing_attachments.download_attachment(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `id`                                                              | *str*                                                             | :heavy_check_mark:                                                | id of the attachment you want to retrive.                         |
| `remote_data`                                                     | *Optional[bool]*                                                  | :heavy_minus_sign:                                                | Set to true to include data from the original Ticketing software. |


### Response

**[operations.DownloadAttachmentResponse](../../models/operations/downloadattachmentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_ticketing_attachments

Add a batch of Attachments

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ticketing_attachments.add_ticketing_attachments(x_connection_token='<value>', request_body=[
    components.UnifiedAttachmentInput(
        file_name='your_file_here',
        file_url='<value>',
        uploader='<value>',
        field_mappings=components.UnifiedAttachmentInputFieldMappings(),
    ),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                         | *str*                                                                                        | :heavy_check_mark:                                                                           | The connection token                                                                         |
| `request_body`                                                                               | List[[components.UnifiedAttachmentInput](../../models/components/unifiedattachmentinput.md)] | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `remote_data`                                                                                | *Optional[bool]*                                                                             | :heavy_minus_sign:                                                                           | Set to true to include data from the original Ticketing software.                            |


### Response

**[operations.AddTicketingAttachmentsResponse](../../models/operations/addticketingattachmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
