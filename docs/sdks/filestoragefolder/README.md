# FilestorageFolder
(*filestorage_folder*)

### Available Operations

* [get_folders](#get_folders) - List a batch of Folders
* [add_folder](#add_folder) - Create a Folder
* [get_folder](#get_folder) - Retrieve a Folder

## get_folders

List a batch of Folders

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_folder.get_folders(x_connection_token='<value>', remote_data=False)

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

**[operations.GetFoldersResponse](../../models/operations/getfoldersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_folder

Create a folder in any supported Filestorage software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_folder.add_folder(x_connection_token='<value>', unified_folder_input=components.UnifiedFolderInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `x_connection_token`                                                           | *str*                                                                          | :heavy_check_mark:                                                             | The connection token                                                           |
| `unified_folder_input`                                                         | [components.UnifiedFolderInput](../../models/components/unifiedfolderinput.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `remote_data`                                                                  | *Optional[bool]*                                                               | :heavy_minus_sign:                                                             | Set to true to include data from the original Filestorage software.            |


### Response

**[operations.AddFolderResponse](../../models/operations/addfolderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_folder

Retrieve a folder from any connected Filestorage software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_folder.get_folder(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the folder you want to retrieve.                              |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Filestorage software. |


### Response

**[operations.GetFolderResponse](../../models/operations/getfolderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
