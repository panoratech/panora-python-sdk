# LinkedUsers
(*linked_users*)

### Available Operations

* [add_linked_user](#add_linked_user) - Add Linked User
* [fetch_linked_users](#fetch_linked_users) - Retrieve Linked Users
* [add_batch_linked_users](#add_batch_linked_users) - Add Batch Linked Users
* [get_linked_user](#get_linked_user) - Retrieve a Linked User
* [linked_user_from_remote_id](#linked_user_from_remote_id) - Retrieve a Linked User From A Remote Id

## add_linked_user

Add Linked User

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.linked_users.add_linked_user(request=components.CreateLinkedUserDto(
    linked_user_origin_id='<value>',
    alias='<value>',
    id_project='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.CreateLinkedUserDto](../../models/components/createlinkeduserdto.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.AddLinkedUserResponse](../../models/operations/addlinkeduserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## fetch_linked_users

Retrieve Linked Users

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.linked_users.fetch_linked_users()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.FetchLinkedUsersResponse](../../models/operations/fetchlinkedusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_batch_linked_users

Add Batch Linked Users

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.linked_users.add_batch_linked_users(request=components.CreateBatchLinkedUserDto(
    linked_user_origin_ids=[
        '<value>',
    ],
    alias='<value>',
    id_project='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.CreateBatchLinkedUserDto](../../models/components/createbatchlinkeduserdto.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.AddBatchLinkedUsersResponse](../../models/operations/addbatchlinkedusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_linked_user

Retrieve a Linked User

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.linked_users.get_linked_user(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetLinkedUserResponse](../../models/operations/getlinkeduserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## linked_user_from_remote_id

Retrieve a Linked User From A Remote Id

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.linked_users.linked_user_from_remote_id(remote_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `remote_id`        | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.LinkedUserFromRemoteIDResponse](../../models/operations/linkeduserfromremoteidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
