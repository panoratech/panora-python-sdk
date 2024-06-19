# MagicLinks
(*magic_links*)

### Available Operations

* [create_magic_link](#create_magic_link) - Create a Magic Link
* [get_magic_links](#get_magic_links) - Retrieve Magic Links
* [get_magic_link](#get_magic_link) - Retrieve a Magic Link

## create_magic_link

Create a Magic Link

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.magic_links.create_magic_link(request=components.CreateMagicLinkDto(
    linked_user_origin_id='<value>',
    email='Elda_Spinka@hotmail.com',
    alias='<value>',
    id_project='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.CreateMagicLinkDto](../../models/components/createmagiclinkdto.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateMagicLinkResponse](../../models/operations/createmagiclinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_magic_links

Retrieve Magic Links

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.magic_links.get_magic_links()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetMagicLinksResponse](../../models/operations/getmagiclinksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_magic_link

Retrieve a Magic Link

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.magic_links.get_magic_link(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetMagicLinkResponse](../../models/operations/getmagiclinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
