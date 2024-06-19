# ManagedWebhooks
(*managed_webhooks*)

### Available Operations

* [get_managed_webhooks](#get_managed_webhooks) - Retrieve managed webhooks
* [update_managed_webhooks_status](#update_managed_webhooks_status) - Update managed webhook status
* [create_managed_webhook](#create_managed_webhook) - Create managed webhook
* [create_remote_third_party_webhook](#create_remote_third_party_webhook) - Create Remote Third Party Webhook

## get_managed_webhooks

Retrieve managed webhooks

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.managed_webhooks.get_managed_webhooks(id_connection='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id_connection`    | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetManagedWebhooksResponse](../../models/operations/getmanagedwebhooksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_managed_webhooks_status

Update managed webhook status

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.managed_webhooks.update_managed_webhooks_status(id_connection='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id_connection`    | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateManagedWebhooksStatusResponse](../../models/operations/updatemanagedwebhooksstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_managed_webhook

Create managed webhook

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.managed_webhooks.create_managed_webhook(request=components.ManagedWebhooksDto(
    id_connection='<value>',
    scopes=[
        '<value>',
    ],
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.ManagedWebhooksDto](../../models/components/managedwebhooksdto.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateManagedWebhookResponse](../../models/operations/createmanagedwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_remote_third_party_webhook

Create Remote Third Party Webhook

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.managed_webhooks.create_remote_third_party_webhook(request=components.RemoteThirdPartyCreationDto(
    id_connection='<value>',
    mw_ids=[
        '<value>',
    ],
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.RemoteThirdPartyCreationDto](../../models/components/remotethirdpartycreationdto.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CreateRemoteThirdPartyWebhookResponse](../../models/operations/createremotethirdpartywebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
