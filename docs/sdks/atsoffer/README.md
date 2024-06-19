# AtsOffer
(*ats_offer*)

### Available Operations

* [get_offers](#get_offers) - List a batch of Offers
* [add_offer](#add_offer) - Create a Offer
* [get_offer](#get_offer) - Retrieve a Offer
* [add_offers](#add_offers) - Add a batch of Offers

## get_offers

List a batch of Offers

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_offer.get_offers(x_connection_token='<value>', remote_data=False)

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

**[operations.GetOffersResponse](../../models/operations/getoffersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_offer

Create a offer in any supported Ats software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_offer.add_offer(x_connection_token='<value>', unified_offer_input=components.UnifiedOfferInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `x_connection_token`                                                         | *str*                                                                        | :heavy_check_mark:                                                           | The connection token                                                         |
| `unified_offer_input`                                                        | [components.UnifiedOfferInput](../../models/components/unifiedofferinput.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `remote_data`                                                                | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Set to true to include data from the original Ats software.                  |


### Response

**[operations.AddOfferResponse](../../models/operations/addofferresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_offer

Retrieve a offer from any connected Ats software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_offer.get_offer(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the offer you want to retrieve.                       |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Ats software. |


### Response

**[operations.GetOfferResponse](../../models/operations/getofferresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_offers

Add a batch of Offers

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ats_offer.add_offers(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedOfferInput(),
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
| `request_body`                                                                     | List[[components.UnifiedOfferInput](../../models/components/unifiedofferinput.md)] | :heavy_check_mark:                                                                 | N/A                                                                                |
| `remote_data`                                                                      | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Set to true to include data from the original Ats software.                        |


### Response

**[operations.AddOffersResponse](../../models/operations/addoffersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
