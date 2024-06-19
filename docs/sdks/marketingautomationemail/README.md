# MarketingautomationEmail
(*marketingautomation_email*)

### Available Operations

* [get_emails](#get_emails) - List a batch of Emails
* [add_email](#add_email) - Create a Email
* [get_email](#get_email) - Retrieve a Email
* [add_emails](#add_emails) - Add a batch of Emails

## get_emails

List a batch of Emails

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_email.get_emails(x_connection_token='<value>', remote_data=False)

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

**[operations.GetEmailsResponse](../../models/operations/getemailsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_email

Create a email in any supported Marketingautomation software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_email.add_email(x_connection_token='<value>', unified_email_input=components.UnifiedEmailInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `x_connection_token`                                                         | *str*                                                                        | :heavy_check_mark:                                                           | The connection token                                                         |
| `unified_email_input`                                                        | [components.UnifiedEmailInput](../../models/components/unifiedemailinput.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `remote_data`                                                                | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Set to true to include data from the original Marketingautomation software.  |


### Response

**[operations.AddEmailResponse](../../models/operations/addemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_email

Retrieve a email from any connected Marketingautomation software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_email.get_email(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | id of the email you want to retrieve.                                       |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Marketingautomation software. |


### Response

**[operations.GetEmailResponse](../../models/operations/getemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_emails

Add a batch of Emails

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.marketingautomation_email.add_emails(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedEmailInput(),
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
| `request_body`                                                                     | List[[components.UnifiedEmailInput](../../models/components/unifiedemailinput.md)] | :heavy_check_mark:                                                                 | N/A                                                                                |
| `remote_data`                                                                      | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Set to true to include data from the original Marketingautomation software.        |


### Response

**[operations.AddEmailsResponse](../../models/operations/addemailsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
