# AtsScorecard
(*ats_scorecard*)

### Available Operations

* [get_score_cards](#get_score_cards) - List a batch of ScoreCards
* [add_score_card](#add_score_card) - Create a ScoreCard
* [get_score_card](#get_score_card) - Retrieve a ScoreCard
* [add_score_cards](#add_score_cards) - Add a batch of ScoreCards

## get_score_cards

List a batch of ScoreCards

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_scorecard.get_score_cards(x_connection_token='<value>', remote_data=False)

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

**[operations.GetScoreCardsResponse](../../models/operations/getscorecardsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_score_card

Create a scorecard in any supported Ats software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_scorecard.add_score_card(x_connection_token='<value>', unified_score_card_input=components.UnifiedScoreCardInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `x_connection_token`                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | The connection token                                                                 |
| `unified_score_card_input`                                                           | [components.UnifiedScoreCardInput](../../models/components/unifiedscorecardinput.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `remote_data`                                                                        | *Optional[bool]*                                                                     | :heavy_minus_sign:                                                                   | Set to true to include data from the original Ats software.                          |


### Response

**[operations.AddScoreCardResponse](../../models/operations/addscorecardresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_score_card

Retrieve a scorecard from any connected Ats software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_scorecard.get_score_card(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the scorecard you want to retrieve.                   |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetScoreCardResponse](../../models/operations/getscorecardresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_score_cards

Add a batch of ScoreCards

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_scorecard.add_score_cards(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedScoreCardInput(),
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
| `request_body`                                                                             | List[[components.UnifiedScoreCardInput](../../models/components/unifiedscorecardinput.md)] | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `remote_data`                                                                              | *Optional[bool]*                                                                           | :heavy_minus_sign:                                                                         | Set to true to include data from the original Ats software.                                |


### Response

**[operations.AddScoreCardsResponse](../../models/operations/addscorecardsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
