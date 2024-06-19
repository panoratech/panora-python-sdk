# AtsJobinterviewstage
(*ats_jobinterviewstage*)

### Available Operations

* [get_job_interview_stages](#get_job_interview_stages) - List a batch of JobInterviewStages
* [add_job_interview_stage](#add_job_interview_stage) - Create a JobInterviewStage
* [get_job_interview_stage](#get_job_interview_stage) - Retrieve a JobInterviewStage
* [add_job_interview_stages](#add_job_interview_stages) - Add a batch of JobInterviewStages

## get_job_interview_stages

List a batch of JobInterviewStages

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_jobinterviewstage.get_job_interview_stages(x_connection_token='<value>', remote_data=False)

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

**[operations.GetJobInterviewStagesResponse](../../models/operations/getjobinterviewstagesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_job_interview_stage

Create a jobinterviewstage in any supported Ats software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_jobinterviewstage.add_job_interview_stage(x_connection_token='<value>', unified_job_interview_stage_input=components.UnifiedJobInterviewStageInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | The connection token                                                                                 |
| `unified_job_interview_stage_input`                                                                  | [components.UnifiedJobInterviewStageInput](../../models/components/unifiedjobinterviewstageinput.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `remote_data`                                                                                        | *Optional[bool]*                                                                                     | :heavy_minus_sign:                                                                                   | Set to true to include data from the original Ats software.                                          |


### Response

**[operations.AddJobInterviewStageResponse](../../models/operations/addjobinterviewstageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_job_interview_stage

Retrieve a jobinterviewstage from any connected Ats software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_jobinterviewstage.get_job_interview_stage(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the jobinterviewstage you want to retrieve.           |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetJobInterviewStageResponse](../../models/operations/getjobinterviewstageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_job_interview_stages

Add a batch of JobInterviewStages

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_jobinterviewstage.add_job_interview_stages(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedJobInterviewStageInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `connection_token`                                                                                         | *str*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `x_connection_token`                                                                                       | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The connection token                                                                                       |
| `request_body`                                                                                             | List[[components.UnifiedJobInterviewStageInput](../../models/components/unifiedjobinterviewstageinput.md)] | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `remote_data`                                                                                              | *Optional[bool]*                                                                                           | :heavy_minus_sign:                                                                                         | Set to true to include data from the original Ats software.                                                |


### Response

**[operations.AddJobInterviewStagesResponse](../../models/operations/addjobinterviewstagesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
