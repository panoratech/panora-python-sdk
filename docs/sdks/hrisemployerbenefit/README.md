# HrisEmployerbenefit
(*hris_employerbenefit*)

### Available Operations

* [get_employer_benefits](#get_employer_benefits) - List a batch of EmployerBenefits
* [add_employer_benefit](#add_employer_benefit) - Create a EmployerBenefit
* [get_employer_benefit](#get_employer_benefit) - Retrieve a EmployerBenefit
* [add_employer_benefits](#add_employer_benefits) - Add a batch of EmployerBenefits

## get_employer_benefits

List a batch of EmployerBenefits

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_employerbenefit.get_employer_benefits(x_connection_token='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `x_connection_token`                                         | *str*                                                        | :heavy_check_mark:                                           | The connection token                                         |
| `remote_data`                                                | *Optional[bool]*                                             | :heavy_minus_sign:                                           | Set to true to include data from the original Hris software. |


### Response

**[operations.GetEmployerBenefitsResponse](../../models/operations/getemployerbenefitsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_employer_benefit

Create a employerbenefit in any supported Hris software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_employerbenefit.add_employer_benefit(x_connection_token='<value>', unified_employer_benefit_input=components.UnifiedEmployerBenefitInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `x_connection_token`                                                                             | *str*                                                                                            | :heavy_check_mark:                                                                               | The connection token                                                                             |
| `unified_employer_benefit_input`                                                                 | [components.UnifiedEmployerBenefitInput](../../models/components/unifiedemployerbenefitinput.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `remote_data`                                                                                    | *Optional[bool]*                                                                                 | :heavy_minus_sign:                                                                               | Set to true to include data from the original Hris software.                                     |


### Response

**[operations.AddEmployerBenefitResponse](../../models/operations/addemployerbenefitresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_employer_benefit

Retrieve a employerbenefit from any connected Hris software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_employerbenefit.get_employer_benefit(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | id of the employerbenefit you want to retrieve.              |
| `remote_data`                                                | *Optional[bool]*                                             | :heavy_minus_sign:                                           | Set to true to include data from the original Hris software. |


### Response

**[operations.GetEmployerBenefitResponse](../../models/operations/getemployerbenefitresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_employer_benefits

Add a batch of EmployerBenefits

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_employerbenefit.add_employer_benefits(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedEmployerBenefitInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `connection_token`                                                                                     | *str*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `x_connection_token`                                                                                   | *str*                                                                                                  | :heavy_check_mark:                                                                                     | The connection token                                                                                   |
| `request_body`                                                                                         | List[[components.UnifiedEmployerBenefitInput](../../models/components/unifiedemployerbenefitinput.md)] | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `remote_data`                                                                                          | *Optional[bool]*                                                                                       | :heavy_minus_sign:                                                                                     | Set to true to include data from the original Hris software.                                           |


### Response

**[operations.AddEmployerBenefitsResponse](../../models/operations/addemployerbenefitsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
