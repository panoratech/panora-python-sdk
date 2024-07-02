# AtsInterview
(*ats_interview*)

### Available Operations

* [get_interviews](#get_interviews) - List a batch of Interviews
* [add_interview](#add_interview) - Create a Interview
* [get_interview](#get_interview) - Retrieve a Interview

## get_interviews

List a batch of Interviews

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_interview.get_interviews(x_connection_token='<value>', remote_data=False)

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

**[operations.GetInterviewsResponse](../../models/operations/getinterviewsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_interview

Create a interview in any supported Ats software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_interview.add_interview(x_connection_token='<value>', unified_interview_input=components.UnifiedInterviewInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `x_connection_token`                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | The connection token                                                                 |
| `unified_interview_input`                                                            | [components.UnifiedInterviewInput](../../models/components/unifiedinterviewinput.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `remote_data`                                                                        | *Optional[bool]*                                                                     | :heavy_minus_sign:                                                                   | Set to true to include data from the original Ats software.                          |


### Response

**[operations.AddInterviewResponse](../../models/operations/addinterviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_interview

Retrieve a interview from any connected Ats software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_interview.get_interview(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the interview you want to retrieve.                   |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetInterviewResponse](../../models/operations/getinterviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
