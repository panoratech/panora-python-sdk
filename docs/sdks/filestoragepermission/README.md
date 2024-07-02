# FilestoragePermission
(*filestorage_permission*)

### Available Operations

* [get_permissions](#get_permissions) - List a batch of Permissions
* [add_permission](#add_permission) - Create a Permission
* [get_permission](#get_permission) - Retrieve a Permission

## get_permissions

List a batch of Permissions

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_permission.get_permissions(x_connection_token='<value>', remote_data=False)

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

**[operations.GetPermissionsResponse](../../models/operations/getpermissionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_permission

Create a permission in any supported Filestorage software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_permission.add_permission(x_connection_token='<value>', unified_permission_input=components.UnifiedPermissionInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | The connection token                                                                   |
| `unified_permission_input`                                                             | [components.UnifiedPermissionInput](../../models/components/unifiedpermissioninput.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `remote_data`                                                                          | *Optional[bool]*                                                                       | :heavy_minus_sign:                                                                     | Set to true to include data from the original Filestorage software.                    |


### Response

**[operations.AddPermissionResponse](../../models/operations/addpermissionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_permission

Retrieve a permission from any connected Filestorage software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.filestorage_permission.get_permission(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the permission you want to retrieve.                          |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Filestorage software. |


### Response

**[operations.GetPermissionResponse](../../models/operations/getpermissionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
