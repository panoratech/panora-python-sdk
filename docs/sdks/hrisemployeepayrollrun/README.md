# HrisEmployeepayrollrun
(*hris_employeepayrollrun*)

### Available Operations

* [get_employee_payroll_runs](#get_employee_payroll_runs) - List a batch of EmployeePayrollRuns
* [add_employee_payroll_run](#add_employee_payroll_run) - Create a EmployeePayrollRun
* [get_employee_payroll_run](#get_employee_payroll_run) - Retrieve a EmployeePayrollRun
* [add_employee_payroll_runs](#add_employee_payroll_runs) - Add a batch of EmployeePayrollRuns

## get_employee_payroll_runs

List a batch of EmployeePayrollRuns

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_employeepayrollrun.get_employee_payroll_runs(x_connection_token='<value>', remote_data=False)

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

**[operations.GetEmployeePayrollRunsResponse](../../models/operations/getemployeepayrollrunsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_employee_payroll_run

Create a employeepayrollrun in any supported Hris software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_employeepayrollrun.add_employee_payroll_run(x_connection_token='<value>', unified_employee_payroll_run_input=components.UnifiedEmployeePayrollRunInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `x_connection_token`                                                                                   | *str*                                                                                                  | :heavy_check_mark:                                                                                     | The connection token                                                                                   |
| `unified_employee_payroll_run_input`                                                                   | [components.UnifiedEmployeePayrollRunInput](../../models/components/unifiedemployeepayrollruninput.md) | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `remote_data`                                                                                          | *Optional[bool]*                                                                                       | :heavy_minus_sign:                                                                                     | Set to true to include data from the original Hris software.                                           |


### Response

**[operations.AddEmployeePayrollRunResponse](../../models/operations/addemployeepayrollrunresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_employee_payroll_run

Retrieve a employeepayrollrun from any connected Hris software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_employeepayrollrun.get_employee_payroll_run(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | id of the employeepayrollrun you want to retrieve.           |
| `remote_data`                                                | *Optional[bool]*                                             | :heavy_minus_sign:                                           | Set to true to include data from the original Hris software. |


### Response

**[operations.GetEmployeePayrollRunResponse](../../models/operations/getemployeepayrollrunresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_employee_payroll_runs

Add a batch of EmployeePayrollRuns

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.hris_employeepayrollrun.add_employee_payroll_runs(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedEmployeePayrollRunInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `connection_token`                                                                                           | *str*                                                                                                        | :heavy_check_mark:                                                                                           | N/A                                                                                                          |
| `x_connection_token`                                                                                         | *str*                                                                                                        | :heavy_check_mark:                                                                                           | The connection token                                                                                         |
| `request_body`                                                                                               | List[[components.UnifiedEmployeePayrollRunInput](../../models/components/unifiedemployeepayrollruninput.md)] | :heavy_check_mark:                                                                                           | N/A                                                                                                          |
| `remote_data`                                                                                                | *Optional[bool]*                                                                                             | :heavy_minus_sign:                                                                                           | Set to true to include data from the original Hris software.                                                 |


### Response

**[operations.AddEmployeePayrollRunsResponse](../../models/operations/addemployeepayrollrunsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
