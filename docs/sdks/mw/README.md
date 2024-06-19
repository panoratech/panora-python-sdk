# Mw
(*mw*)

### Available Operations

* [handle_third_party_webhook](#handle_third_party_webhook) - Handle Third Party Webhook

## handle_third_party_webhook

Handle Third Party Webhook

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.mw.handle_third_party_webhook(endpoint_uuid='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `endpoint_uuid`    | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.HandleThirdPartyWebhookResponse](../../models/operations/handlethirdpartywebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
