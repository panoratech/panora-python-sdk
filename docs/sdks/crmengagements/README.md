# CrmEngagements
(*crm_engagements*)

### Available Operations

* [get_engagements](#get_engagements) - List a batch of Engagements
* [add_engagement](#add_engagement) - Create a Engagement
* [update_engagement](#update_engagement) - Update a Engagement
* [get_engagement](#get_engagement) - Retrieve a Engagement
* [add_engagements](#add_engagements) - Add a batch of Engagements

## get_engagements

List a batch of Engagements

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_engagements.get_engagements(x_connection_token='<value>', remote_data=False, page_size=50, cursor='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                               | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `x_connection_token`                                    | *str*                                                   | :heavy_check_mark:                                      | The connection token                                    |
| `remote_data`                                           | *Optional[bool]*                                        | :heavy_minus_sign:                                      | Set to true to include data from the original software. |
| `page_size`                                             | *Optional[float]*                                       | :heavy_minus_sign:                                      | Set to get the number of records.                       |
| `cursor`                                                | *Optional[str]*                                         | :heavy_minus_sign:                                      | Set to get the number of records after this cursor.     |


### Response

**[operations.GetEngagementsResponse](../../models/operations/getengagementsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_engagement

Create a engagement in any supported Crm software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_engagements.add_engagement(x_connection_token='<value>', unified_engagement_input=components.UnifiedEngagementInput(
    type='<value>',
    field_mappings=components.UnifiedEngagementInputFieldMappings(),
), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | The connection token                                                                   |
| `unified_engagement_input`                                                             | [components.UnifiedEngagementInput](../../models/components/unifiedengagementinput.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `remote_data`                                                                          | *Optional[bool]*                                                                       | :heavy_minus_sign:                                                                     | Set to true to include data from the original Crm software.                            |


### Response

**[operations.AddEngagementResponse](../../models/operations/addengagementresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_engagement

Update a Engagement

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_engagements.update_engagement(id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateEngagementResponse](../../models/operations/updateengagementresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_engagement

Retrieve a engagement from any connected Crm software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_engagements.get_engagement(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the engagement you want to retrieve.                  |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Crm software. |


### Response

**[operations.GetEngagementResponse](../../models/operations/getengagementresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_engagements

Add a batch of Engagements

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.crm_engagements.add_engagements(x_connection_token='<value>', request_body=[
    components.UnifiedEngagementInput(
        type='<value>',
        field_mappings=components.UnifiedEngagementInputFieldMappings(),
    ),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                         | *str*                                                                                        | :heavy_check_mark:                                                                           | The connection token                                                                         |
| `request_body`                                                                               | List[[components.UnifiedEngagementInput](../../models/components/unifiedengagementinput.md)] | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `remote_data`                                                                                | *Optional[bool]*                                                                             | :heavy_minus_sign:                                                                           | Set to true to include data from the original Crm software.                                  |


### Response

**[operations.AddEngagementsResponse](../../models/operations/addengagementsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
