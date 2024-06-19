# Organisations
(*organisations*)

### Available Operations

* [get_organisations](#get_organisations) - Retrieve Organisations
* [create_organisation](#create_organisation) - Create an Organisation

## get_organisations

Retrieve Organisations

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.organisations.get_organisations()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetOrganisationsResponse](../../models/operations/getorganisationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_organisation

Create an Organisation

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.organisations.create_organisation(request=components.CreateOrganizationDto(
    name='<value>',
    stripe_customer_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.CreateOrganizationDto](../../models/components/createorganizationdto.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateOrganisationResponse](../../models/operations/createorganisationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
