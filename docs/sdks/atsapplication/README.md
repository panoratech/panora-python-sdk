# AtsApplication
(*ats_application*)

### Available Operations

* [get_applications](#get_applications) - List a batch of Applications
* [add_application](#add_application) - Create a Application
* [get_application](#get_application) - Retrieve a Application
* [add_applications](#add_applications) - Add a batch of Applications

## get_applications

List a batch of Applications

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_application.get_applications(x_connection_token='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `x_connection_token`                                        | *str*                                                       | :heavy_check_mark:                                          | The connection token                                        |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetApplicationsResponse](../../models/operations/getapplicationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_application

Create a application in any supported Ats software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_application.add_application(x_connection_token='<value>', unified_application_input=components.UnifiedApplicationInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                     | *str*                                                                                    | :heavy_check_mark:                                                                       | The connection token                                                                     |
| `unified_application_input`                                                              | [components.UnifiedApplicationInput](../../models/components/unifiedapplicationinput.md) | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `remote_data`                                                                            | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | Set to true to include data from the original Ats software.                              |


### Response

**[operations.AddApplicationResponse](../../models/operations/addapplicationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_application

Retrieve a application from any connected Ats software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_application.get_application(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the application you want to retrieve.                 |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetApplicationResponse](../../models/operations/getapplicationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_applications

Add a batch of Applications

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_application.add_applications(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedApplicationInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `connection_token`                                                                             | *str*                                                                                          | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `x_connection_token`                                                                           | *str*                                                                                          | :heavy_check_mark:                                                                             | The connection token                                                                           |
| `request_body`                                                                                 | List[[components.UnifiedApplicationInput](../../models/components/unifiedapplicationinput.md)] | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `remote_data`                                                                                  | *Optional[bool]*                                                                               | :heavy_minus_sign:                                                                             | Set to true to include data from the original Ats software.                                    |


### Response

**[operations.AddApplicationsResponse](../../models/operations/addapplicationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
