# FieldMappings
(*field_mappings*)

### Available Operations

* [get_field_mappings_entities](#get_field_mappings_entities) - Retrieve field mapping entities
* [get_field_mappings](#get_field_mappings) - Retrieve field mappings
* [get_field_mapping_values](#get_field_mapping_values) - Retrieve field mappings values
* [define_target_field](#define_target_field) - Define target Field
* [create_custom_field](#create_custom_field) - Create Custom Field
* [map_field](#map_field) - Map Custom Field
* [get_custom_provider_properties](#get_custom_provider_properties) - Retrieve Custom Properties

## get_field_mappings_entities

Retrieve field mapping entities

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.field_mappings.get_field_mappings_entities()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetFieldMappingsEntitiesResponse](../../models/operations/getfieldmappingsentitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_field_mappings

Retrieve field mappings

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.field_mappings.get_field_mappings()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetFieldMappingsResponse](../../models/operations/getfieldmappingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_field_mapping_values

Retrieve field mappings values

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.field_mappings.get_field_mapping_values()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetFieldMappingValuesResponse](../../models/operations/getfieldmappingvaluesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## define_target_field

Define target Field

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.field_mappings.define_target_field(request=components.DefineTargetFieldDto(
    object_type_owner='<value>',
    name='<value>',
    description='Inverse radical firmware',
    data_type='date',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.DefineTargetFieldDto](../../models/components/definetargetfielddto.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.DefineTargetFieldResponse](../../models/operations/definetargetfieldresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_custom_field

Create Custom Field

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.field_mappings.create_custom_field(request=components.CustomFieldCreateDto(
    object_type_owner='<value>',
    name='<value>',
    description='Synergistic regional solution',
    data_type='time',
    source_custom_field_id='<value>',
    source_provider='<value>',
    linked_user_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.CustomFieldCreateDto](../../models/components/customfieldcreatedto.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateCustomFieldResponse](../../models/operations/createcustomfieldresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## map_field

Map Custom Field

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.field_mappings.map_field(request=components.MapFieldToProviderDto(
    attribute_id='<value>',
    source_custom_field_id='<value>',
    source_provider='<value>',
    linked_user_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.MapFieldToProviderDto](../../models/components/mapfieldtoproviderdto.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.MapFieldResponse](../../models/operations/mapfieldresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_custom_provider_properties

Retrieve Custom Properties

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.field_mappings.get_custom_provider_properties(linked_user_id='<value>', provider_id='<value>', vertical='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `linked_user_id`   | *str*              | :heavy_check_mark: | N/A                |
| `provider_id`      | *str*              | :heavy_check_mark: | N/A                |
| `vertical`         | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetCustomProviderPropertiesResponse](../../models/operations/getcustomproviderpropertiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
