# FilestorageDrive
(*filestorage_drive*)

### Available Operations

* [get_drives](#get_drives) - List a batch of Drives
* [add_drive](#add_drive) - Create a Drive
* [get_drive](#get_drive) - Retrieve a Drive

## get_drives

List a batch of Drives

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_drive.get_drives(x_connection_token='<value>', remote_data=False)

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

**[operations.GetDrivesResponse](../../models/operations/getdrivesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_drive

Create a drive in any supported Filestorage software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_drive.add_drive(x_connection_token='<value>', unified_drive_input=components.UnifiedDriveInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `x_connection_token`                                                         | *str*                                                                        | :heavy_check_mark:                                                           | The connection token                                                         |
| `unified_drive_input`                                                        | [components.UnifiedDriveInput](../../models/components/unifieddriveinput.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `remote_data`                                                                | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Set to true to include data from the original Filestorage software.          |


### Response

**[operations.AddDriveResponse](../../models/operations/adddriveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_drive

Retrieve a drive from any connected Filestorage software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_drive.get_drive(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the drive you want to retrieve.                               |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Filestorage software. |


### Response

**[operations.GetDriveResponse](../../models/operations/getdriveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
