# Webhook
(*webhook*)

### Available Operations

* [get_webhooks_metadata](#get_webhooks_metadata) - Retrieve webhooks metadata 
* [create_webhook_metadata](#create_webhook_metadata) - Add webhook metadata
* [delete_webhook](#delete_webhook) - Delete Webhook
* [update_webhook_status](#update_webhook_status) - Update webhook status
* [verify_event](#verify_event) - Verify payload sgnature of the webhook

## get_webhooks_metadata

Retrieve webhooks metadata 

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.webhook.get_webhooks_metadata()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetWebhooksMetadataResponse](../../models/operations/getwebhooksmetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_webhook_metadata

Add webhook metadata

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.webhook.create_webhook_metadata(request=components.WebhookDto(
    url='http://wild-flanker.biz',
    id_project='<value>',
    scope=[
        '<value>',
    ],
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [components.WebhookDto](../../models/components/webhookdto.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.CreateWebhookMetadataResponse](../../models/operations/createwebhookmetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_webhook

Delete Webhook

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.webhook.delete_webhook(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteWebhookResponse](../../models/operations/deletewebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_webhook_status

Update webhook status

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.webhook.update_webhook_status(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateWebhookStatusResponse](../../models/operations/updatewebhookstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## verify_event

Verify payload sgnature of the webhook

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.webhook.verify_event(request=components.SignatureVerificationDto(
    signature='<value>',
    secret='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.SignatureVerificationDto](../../models/components/signatureverificationdto.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.VerifyEventResponse](../../models/operations/verifyeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
