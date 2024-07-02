# Panora SDK


## Overview

Unified Panora API: The Panora API description

### Available Operations

* [app_controller_hello](#app_controller_hello)
* [get_health](#get_health)
* [get_hello_protected](#get_hello_protected)

## app_controller_hello

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.app_controller_hello()

if res.string is not None:
    # handle response
    pass

```


### Response

**[operations.AppControllerHelloResponse](../../models/operations/appcontrollerhelloresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_health

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.get_health()

if res.number is not None:
    # handle response
    pass

```


### Response

**[operations.GetHealthResponse](../../models/operations/gethealthresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_hello_protected

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.get_hello_protected()

if res.string is not None:
    # handle response
    pass

```


### Response

**[operations.GetHelloProtectedResponse](../../models/operations/gethelloprotectedresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
