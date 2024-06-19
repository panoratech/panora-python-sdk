# AtsCandidate
(*ats_candidate*)

### Available Operations

* [get_candidates](#get_candidates) - List a batch of Candidates
* [add_candidate](#add_candidate) - Create a Candidate
* [get_candidate](#get_candidate) - Retrieve a Candidate
* [add_candidates](#add_candidates) - Add a batch of Candidates

## get_candidates

List a batch of Candidates

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_candidate.get_candidates(x_connection_token='<value>', remote_data=False)

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

**[operations.GetCandidatesResponse](../../models/operations/getcandidatesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_candidate

Create a candidate in any supported Ats software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_candidate.add_candidate(x_connection_token='<value>', unified_candidate_input=components.UnifiedCandidateInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `x_connection_token`                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | The connection token                                                                 |
| `unified_candidate_input`                                                            | [components.UnifiedCandidateInput](../../models/components/unifiedcandidateinput.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `remote_data`                                                                        | *Optional[bool]*                                                                     | :heavy_minus_sign:                                                                   | Set to true to include data from the original Ats software.                          |


### Response

**[operations.AddCandidateResponse](../../models/operations/addcandidateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_candidate

Retrieve a candidate from any connected Ats software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_candidate.get_candidate(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the candidate you want to retrieve.                   |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetCandidateResponse](../../models/operations/getcandidateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_candidates

Add a batch of Candidates

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_candidate.add_candidates(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedCandidateInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `connection_token`                                                                         | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `x_connection_token`                                                                       | *str*                                                                                      | :heavy_check_mark:                                                                         | The connection token                                                                       |
| `request_body`                                                                             | List[[components.UnifiedCandidateInput](../../models/components/unifiedcandidateinput.md)] | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `remote_data`                                                                              | *Optional[bool]*                                                                           | :heavy_minus_sign:                                                                         | Set to true to include data from the original Ats software.                                |


### Response

**[operations.AddCandidatesResponse](../../models/operations/addcandidatesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
