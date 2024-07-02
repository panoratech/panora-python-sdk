# TicketingComments
(*ticketing_comments*)

### Available Operations

* [get_comments](#get_comments) - List a batch of Comments
* [add_comment](#add_comment) - Create a Comment
* [get_comment](#get_comment) - Retrieve a Comment

## get_comments

List a batch of Comments

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ticketing_comments.get_comments(x_connection_token='<value>', remote_data=False, limit=50, cursor='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                               | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `x_connection_token`                                    | *str*                                                   | :heavy_check_mark:                                      | The connection token                                    |
| `remote_data`                                           | *Optional[bool]*                                        | :heavy_minus_sign:                                      | Set to true to include data from the original software. |
| `limit`                                                 | *Optional[float]*                                       | :heavy_minus_sign:                                      | Set to get the number of records.                       |
| `cursor`                                                | *Optional[str]*                                         | :heavy_minus_sign:                                      | Set to get the number of records after this cursor.     |


### Response

**[operations.GetCommentsResponse](../../models/operations/getcommentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_comment

Create a comment in any supported Ticketing software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ticketing_comments.add_comment(x_connection_token='<value>', unified_comment_input=components.UnifiedCommentInput(
    body='<value>',
), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `x_connection_token`                                                             | *str*                                                                            | :heavy_check_mark:                                                               | The connection token                                                             |
| `unified_comment_input`                                                          | [components.UnifiedCommentInput](../../models/components/unifiedcommentinput.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `remote_data`                                                                    | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | Set to true to include data from the original Ticketing software.                |


### Response

**[operations.AddCommentResponse](../../models/operations/addcommentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_comment

Retrieve a comment from any connected Ticketing software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ticketing_comments.get_comment(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `id`                                                              | *str*                                                             | :heavy_check_mark:                                                | id of the `comment` you want to retrive.                          |
| `remote_data`                                                     | *Optional[bool]*                                                  | :heavy_minus_sign:                                                | Set to true to include data from the original Ticketing software. |


### Response

**[operations.GetCommentResponse](../../models/operations/getcommentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
