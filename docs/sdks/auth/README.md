# Auth
(*auth*)

### Available Operations

* [sign_up](#sign_up) - Register
* [sign_in](#sign_in) - Log In
* [get_panora_core_users](#get_panora_core_users) - Get users
* [auth_controller_get_profile](#auth_controller_get_profile)
* [get_api_keys](#get_api_keys) - Retrieve API Keys
* [delete_api_key](#delete_api_key) - Delete API Keys
* [generate_api_key](#generate_api_key) - Create API Key
* [refresh_access_token](#refresh_access_token) - Refresh Access Token

## sign_up

Register

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.auth.sign_up(request=components.CreateUserDto(
    first_name='Tia',
    last_name='Carter',
    email='Ola76@hotmail.com',
    strategy='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [components.CreateUserDto](../../models/components/createuserdto.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.SignUpResponse](../../models/operations/signupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## sign_in

Log In

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.auth.sign_in(request=components.LoginDto(
    email='Oda.Treutel97@hotmail.com',
    password_hash='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [components.LoginDto](../../models/components/logindto.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.SignInResponse](../../models/operations/signinresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_panora_core_users

Get users

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.auth.get_panora_core_users()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetPanoraCoreUsersResponse](../../models/operations/getpanoracoreusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## auth_controller_get_profile

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.auth.auth_controller_get_profile()

if res.verify_user_dto is not None:
    # handle response
    pass

```


### Response

**[operations.AuthControllerGetProfileResponse](../../models/operations/authcontrollergetprofileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_api_keys

Retrieve API Keys

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.auth.get_api_keys()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetAPIKeysResponse](../../models/operations/getapikeysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_api_key

Delete API Keys

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.auth.delete_api_key(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIKeyResponse](../../models/operations/deleteapikeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## generate_api_key

Create API Key

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.auth.generate_api_key(request=components.APIKeyDto(
    project_id='<value>',
    user_id='<value>',
    key_name='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [components.APIKeyDto](../../models/components/apikeydto.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.GenerateAPIKeyResponse](../../models/operations/generateapikeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## refresh_access_token

Refresh Access Token

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.auth.refresh_access_token(request=components.RefreshDto(
    project_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [components.RefreshDto](../../models/components/refreshdto.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.RefreshAccessTokenResponse](../../models/operations/refreshaccesstokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
