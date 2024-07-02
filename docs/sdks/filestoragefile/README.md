# FilestorageFile
(*filestorage_file*)

### Available Operations

* [get_files](#get_files) - List a batch of Files
* [add_file](#add_file) - Create a File
* [get_file](#get_file) - Retrieve a File

## get_files

List a batch of Files

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_file.get_files(x_connection_token='<value>', remote_data=False)

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

**[operations.GetFilesResponse](../../models/operations/getfilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_file

Create a file in any supported Filestorage software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_file.add_file(x_connection_token='<value>', unified_file_input=components.UnifiedFileInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `x_connection_token`                                                       | *str*                                                                      | :heavy_check_mark:                                                         | The connection token                                                       |
| `unified_file_input`                                                       | [components.UnifiedFileInput](../../models/components/unifiedfileinput.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `remote_data`                                                              | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | Set to true to include data from the original Filestorage software.        |


### Response

**[operations.AddFileResponse](../../models/operations/addfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_file

Retrieve a file from any connected Filestorage software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_file.get_file(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the file you want to retrieve.                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Filestorage software. |


### Response

**[operations.GetFileResponse](../../models/operations/getfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
