# HrisLocation
(*hris_location*)

### Available Operations

* [get_locations](#get_locations) - List a batch of Locations
* [add_location](#add_location) - Create a Location
* [get_location](#get_location) - Retrieve a Location

## get_locations

List a batch of Locations

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_location.get_locations(x_connection_token='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `x_connection_token`                                         | *str*                                                        | :heavy_check_mark:                                           | The connection token                                         |
| `remote_data`                                                | *Optional[bool]*                                             | :heavy_minus_sign:                                           | Set to true to include data from the original Hris software. |


### Response

**[operations.GetLocationsResponse](../../models/operations/getlocationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_location

Create a location in any supported Hris software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_location.add_location(x_connection_token='<value>', unified_location_input=components.UnifiedLocationInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `x_connection_token`                                                               | *str*                                                                              | :heavy_check_mark:                                                                 | The connection token                                                               |
| `unified_location_input`                                                           | [components.UnifiedLocationInput](../../models/components/unifiedlocationinput.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `remote_data`                                                                      | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Set to true to include data from the original Hris software.                       |


### Response

**[operations.AddLocationResponse](../../models/operations/addlocationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_location

Retrieve a location from any connected Hris software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_location.get_location(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | id of the location you want to retrieve.                     |
| `remote_data`                                                | *Optional[bool]*                                             | :heavy_minus_sign:                                           | Set to true to include data from the original Hris software. |


### Response

**[operations.GetLocationResponse](../../models/operations/getlocationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
