# AtsTag
(*ats_tag*)

### Available Operations

* [get_ats_tags](#get_ats_tags) - List a batch of Tags
* [add_tag](#add_tag) - Create a Tag
* [get_ats_tag](#get_ats_tag) - Retrieve a Tag

## get_ats_tags

List a batch of Tags

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_tag.get_ats_tags(x_connection_token='<value>', remote_data=False)

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

**[operations.GetAtsTagsResponse](../../models/operations/getatstagsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_tag

Create a tag in any supported Ats software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_tag.add_tag(x_connection_token='<value>', unified_tag_input=components.UnifiedTagInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `x_connection_token`                                                     | *str*                                                                    | :heavy_check_mark:                                                       | The connection token                                                     |
| `unified_tag_input`                                                      | [components.UnifiedTagInput](../../models/components/unifiedtaginput.md) | :heavy_check_mark:                                                       | N/A                                                                      |
| `remote_data`                                                            | *Optional[bool]*                                                         | :heavy_minus_sign:                                                       | Set to true to include data from the original Ats software.              |


### Response

**[operations.AddTagResponse](../../models/operations/addtagresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_ats_tag

Retrieve a tag from any connected Ats software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_tag.get_ats_tag(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the tag you want to retrieve.                         |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetAtsTagResponse](../../models/operations/getatstagresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
