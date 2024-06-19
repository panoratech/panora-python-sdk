# MarketingautomationEvent
(*marketingautomation_event*)

### Available Operations

* [get_marketing_automation_events](#get_marketing_automation_events) - List a batch of Events
* [add_event](#add_event) - Create a Event
* [get_event](#get_event) - Retrieve a Event
* [add_events](#add_events) - Add a batch of Events

## get_marketing_automation_events

List a batch of Events

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_event.get_marketing_automation_events(x_connection_token='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `x_connection_token`                                                        | *str*                                                                       | :heavy_check_mark:                                                          | The connection token                                                        |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Marketingautomation software. |


### Response

**[operations.GetMarketingAutomationEventsResponse](../../models/operations/getmarketingautomationeventsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_event

Create a event in any supported Marketingautomation software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_event.add_event(x_connection_token='<value>', unified_event_input=components.UnifiedEventInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `x_connection_token`                                                         | *str*                                                                        | :heavy_check_mark:                                                           | The connection token                                                         |
| `unified_event_input`                                                        | [components.UnifiedEventInput](../../models/components/unifiedeventinput.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `remote_data`                                                                | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Set to true to include data from the original Marketingautomation software.  |


### Response

**[operations.AddEventResponse](../../models/operations/addeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_event

Retrieve a event from any connected Marketingautomation software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_event.get_event(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | id of the event you want to retrieve.                                       |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Marketingautomation software. |


### Response

**[operations.GetEventResponse](../../models/operations/geteventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_events

Add a batch of Events

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_event.add_events(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedEventInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `connection_token`                                                                 | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `x_connection_token`                                                               | *str*                                                                              | :heavy_check_mark:                                                                 | The connection token                                                               |
| `request_body`                                                                     | List[[components.UnifiedEventInput](../../models/components/unifiedeventinput.md)] | :heavy_check_mark:                                                                 | N/A                                                                                |
| `remote_data`                                                                      | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Set to true to include data from the original Marketingautomation software.        |


### Response

**[operations.AddEventsResponse](../../models/operations/addeventsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
