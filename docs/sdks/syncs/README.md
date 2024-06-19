# Syncs
(*syncs*)

### Available Operations

* [get_sync_status](#get_sync_status) - Retrieve sync status of a certain vertical
* [resync](#resync) - Resync common objects across a vertical

## get_sync_status

Retrieve sync status of a certain vertical

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.syncs.get_sync_status(vertical='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vertical`         | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetSyncStatusResponse](../../models/operations/getsyncstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## resync

Resync common objects across a vertical

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.syncs.resync(vertical='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vertical`         | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.ResyncResponse](../../models/operations/resyncresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
