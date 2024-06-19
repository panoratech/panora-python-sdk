# FilestorageSharedlink
(*filestorage_sharedlink*)

### Available Operations

* [get_sharedlinks](#get_sharedlinks) - List a batch of Sharedlinks
* [add_sharedlink](#add_sharedlink) - Create a Sharedlink
* [get_sharedlink](#get_sharedlink) - Retrieve a Sharedlink
* [add_sharedlinks](#add_sharedlinks) - Add a batch of Sharedlinks

## get_sharedlinks

List a batch of Sharedlinks

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_sharedlink.get_sharedlinks(x_connection_token='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Filestorage software. |


### Response

**[operations.GetSharedlinksResponse](../../models/operations/getsharedlinksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_sharedlink

Create a sharedlink in any supported Filestorage software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_sharedlink.add_sharedlink(x_connection_token='<value>', unified_shared_link_input=components.UnifiedSharedLinkInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | The connection token                                                                   |
| `unified_shared_link_input`                                                            | [components.UnifiedSharedLinkInput](../../models/components/unifiedsharedlinkinput.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `remote_data`                                                                          | *Optional[bool]*                                                                       | :heavy_minus_sign:                                                                     | Set to true to include data from the original Filestorage software.                    |


### Response

**[operations.AddSharedlinkResponse](../../models/operations/addsharedlinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_sharedlink

Retrieve a sharedlink from any connected Filestorage software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_sharedlink.get_sharedlink(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the sharedlink you want to retrieve.                          |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Filestorage software. |


### Response

**[operations.GetSharedlinkResponse](../../models/operations/getsharedlinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_sharedlinks

Add a batch of Sharedlinks

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_sharedlink.add_sharedlinks(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedSharedLinkInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `connection_token`                                                                           | *str*                                                                                        | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `x_connection_token`                                                                         | *str*                                                                                        | :heavy_check_mark:                                                                           | The connection token                                                                         |
| `request_body`                                                                               | List[[components.UnifiedSharedLinkInput](../../models/components/unifiedsharedlinkinput.md)] | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `remote_data`                                                                                | *Optional[bool]*                                                                             | :heavy_minus_sign:                                                                           | Set to true to include data from the original Filestorage software.                          |


### Response

**[operations.AddSharedlinksResponse](../../models/operations/addsharedlinksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
