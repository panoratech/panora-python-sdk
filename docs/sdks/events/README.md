# Events
(*events*)

### Available Operations

* [get_panora_core_events](#get_panora_core_events) - Retrieve Events
* [get_events_count](#get_events_count) - Retrieve Events Count

## get_panora_core_events

Retrieve Events

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.events.get_panora_core_events(page=1, limit=10)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `page`             | *Optional[float]*  | :heavy_minus_sign: | N/A                |
| `limit`            | *Optional[float]*  | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetPanoraCoreEventsResponse](../../models/operations/getpanoracoreeventsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_events_count

Retrieve Events Count

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.events.get_events_count()

if res.number is not None:
    # handle response
    pass

```


### Response

**[operations.GetEventsCountResponse](../../models/operations/geteventscountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
