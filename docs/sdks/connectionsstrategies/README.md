# ConnectionsStrategies
(*connections_strategies*)

### Available Operations

* [create_connection_strategy](#create_connection_strategy) - Create Connection Strategy
* [toggle_connection_strategy](#toggle_connection_strategy) - Activate/Deactivate Connection Strategy
* [delete_connection_strategy](#delete_connection_strategy) - Delete Connection Strategy
* [update_connection_strategy](#update_connection_strategy) - Update Connection Strategy
* [get_connection_strategy_credentials](#get_connection_strategy_credentials) - Get Connection Strategy Credential
* [get_credentials](#get_credentials) - Fetch credentials info needed for connections
* [get_connection_strategies_for_project](#get_connection_strategies_for_project) - Fetch All Connection Strategies for Project

## create_connection_strategy

Create Connection Strategy

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.connections_strategies.create_connection_strategy(request=components.CreateConnectionStrategyDto(
    type='<value>',
    attributes=[
        '<value>',
    ],
    values=[
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
| `request`                                                                                        | [components.CreateConnectionStrategyDto](../../models/components/createconnectionstrategydto.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CreateConnectionStrategyResponse](../../models/operations/createconnectionstrategyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## toggle_connection_strategy

Activate/Deactivate Connection Strategy

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.connections_strategies.toggle_connection_strategy(request=components.ToggleStrategyDto(
    id_cs='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.ToggleStrategyDto](../../models/components/togglestrategydto.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.ToggleConnectionStrategyResponse](../../models/operations/toggleconnectionstrategyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_connection_strategy

Delete Connection Strategy

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.connections_strategies.delete_connection_strategy(request=components.DeleteCSDto(
    id='<id>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [components.DeleteCSDto](../../models/components/deletecsdto.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.DeleteConnectionStrategyResponse](../../models/operations/deleteconnectionstrategyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_connection_strategy

Update Connection Strategy

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.connections_strategies.update_connection_strategy(request=components.UpdateCSDto(
    id_cs='<value>',
    status=False,
    attributes=[
        '<value>',
    ],
    values=[
        '<value>',
    ],
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [components.UpdateCSDto](../../models/components/updatecsdto.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.UpdateConnectionStrategyResponse](../../models/operations/updateconnectionstrategyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_connection_strategy_credentials

Get Connection Strategy Credential

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.connections_strategies.get_connection_strategy_credentials(request=components.ConnectionStrategyCredentials(
    type='<value>',
    attributes=[
        '<value>',
    ],
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [components.ConnectionStrategyCredentials](../../models/components/connectionstrategycredentials.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetConnectionStrategyCredentialsResponse](../../models/operations/getconnectionstrategycredentialsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_credentials

Fetch credentials info needed for connections

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.connections_strategies.get_credentials(project_id='<value>', type='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `project_id`       | *str*              | :heavy_check_mark: | N/A                |
| `type`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetCredentialsResponse](../../models/operations/getcredentialsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_connection_strategies_for_project

Fetch All Connection Strategies for Project

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.connections_strategies.get_connection_strategies_for_project()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetConnectionStrategiesForProjectResponse](../../models/operations/getconnectionstrategiesforprojectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
