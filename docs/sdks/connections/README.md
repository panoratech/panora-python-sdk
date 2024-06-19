# Connections
(*connections*)

### Available Operations

* [handle_o_auth_callback](#handle_o_auth_callback) - Capture oAuth callback
* [connections_controller_handle_gorgias_auth_url](#connections_controller_handle_gorgias_auth_url)
* [handle_api_key_callback](#handle_api_key_callback) - Capture api key callback
* [get_connections](#get_connections) - List Connections

## handle_o_auth_callback

Capture oAuth callback

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.connections.handle_o_auth_callback(code='<value>', state='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `code`             | *str*              | :heavy_check_mark: | N/A                |
| `state`            | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.HandleOAuthCallbackResponse](../../models/operations/handleoauthcallbackresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## connections_controller_handle_gorgias_auth_url

### Example Usage

```python
import panora
from panora.models import operations

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.connections.connections_controller_handle_gorgias_auth_url(request=operations.ConnectionsControllerHandleGorgiasAuthURLRequest(
    account='81441797',
    response_type='<value>',
    nonce='<value>',
    scope='<value>',
    client_id='<value>',
    redirect_uri='<value>',
    state='Massachusetts',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.ConnectionsControllerHandleGorgiasAuthURLRequest](../../models/operations/connectionscontrollerhandlegorgiasauthurlrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.ConnectionsControllerHandleGorgiasAuthURLResponse](../../models/operations/connectionscontrollerhandlegorgiasauthurlresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## handle_api_key_callback

Capture api key callback

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.connections.handle_api_key_callback(state='<value>', body_data_type=components.BodyDataType())

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `state`                                                            | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `body_data_type`                                                   | [components.BodyDataType](../../models/components/bodydatatype.md) | :heavy_check_mark:                                                 | N/A                                                                |


### Response

**[operations.HandleAPIKeyCallbackResponse](../../models/operations/handleapikeycallbackresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_connections

List Connections

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.connections.get_connections()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetConnectionsResponse](../../models/operations/getconnectionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
