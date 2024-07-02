# AtsScreeningquestion
(*ats_screeningquestion*)

### Available Operations

* [get_screening_questions](#get_screening_questions) - List a batch of ScreeningQuestions
* [add_screening_question](#add_screening_question) - Create a ScreeningQuestion
* [get_screening_question](#get_screening_question) - Retrieve a ScreeningQuestion

## get_screening_questions

List a batch of ScreeningQuestions

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_screeningquestion.get_screening_questions(x_connection_token='<value>', remote_data=False)

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

**[operations.GetScreeningQuestionsResponse](../../models/operations/getscreeningquestionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_screening_question

Create a screeningquestion in any supported Ats software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_screeningquestion.add_screening_question(x_connection_token='<value>', unified_screening_question_input=components.UnifiedScreeningQuestionInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | The connection token                                                                                 |
| `unified_screening_question_input`                                                                   | [components.UnifiedScreeningQuestionInput](../../models/components/unifiedscreeningquestioninput.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `remote_data`                                                                                        | *Optional[bool]*                                                                                     | :heavy_minus_sign:                                                                                   | Set to true to include data from the original Ats software.                                          |


### Response

**[operations.AddScreeningQuestionResponse](../../models/operations/addscreeningquestionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_screening_question

Retrieve a screeningquestion from any connected Ats software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_screeningquestion.get_screening_question(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the screeningquestion you want to retrieve.           |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetScreeningQuestionResponse](../../models/operations/getscreeningquestionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
