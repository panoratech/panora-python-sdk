# TicketingTickets
(*ticketing_tickets*)

### Available Operations

* [get_tickets](#get_tickets) - List a batch of Tickets
* [add_ticket](#add_ticket) - Create a Ticket
* [get_ticket](#get_ticket) - Retrieve a Ticket

## get_tickets

List a batch of Tickets

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ticketing_tickets.get_tickets(x_connection_token='<value>', remote_data=False, limit=50, cursor='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                               | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `x_connection_token`                                    | *str*                                                   | :heavy_check_mark:                                      | The connection token                                    |
| `remote_data`                                           | *Optional[bool]*                                        | :heavy_minus_sign:                                      | Set to true to include data from the original software. |
| `limit`                                                 | *Optional[float]*                                       | :heavy_minus_sign:                                      | Set to get the number of records.                       |
| `cursor`                                                | *Optional[str]*                                         | :heavy_minus_sign:                                      | Set to get the number of records after this cursor.     |


### Response

**[operations.GetTicketsResponse](../../models/operations/getticketsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_ticket

Create a ticket in any supported Ticketing software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ticketing_tickets.add_ticket(x_connection_token='<value>', unified_ticket_input=components.UnifiedTicketInput(
    name='<value>',
    description='Synergized secondary capacity',
    field_mappings=components.UnifiedTicketInputFieldMappings(),
), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `x_connection_token`                                                           | *str*                                                                          | :heavy_check_mark:                                                             | The connection token                                                           |
| `unified_ticket_input`                                                         | [components.UnifiedTicketInput](../../models/components/unifiedticketinput.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `remote_data`                                                                  | *Optional[bool]*                                                               | :heavy_minus_sign:                                                             | Set to true to include data from the original Ticketing software.              |


### Response

**[operations.AddTicketResponse](../../models/operations/addticketresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_ticket

Retrieve a ticket from any connected Ticketing software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ticketing_tickets.get_ticket(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `id`                                                              | *str*                                                             | :heavy_check_mark:                                                | id of the `ticket` you want to retrive.                           |
| `remote_data`                                                     | *Optional[bool]*                                                  | :heavy_minus_sign:                                                | Set to true to include data from the original Ticketing software. |


### Response

**[operations.GetTicketResponse](../../models/operations/getticketresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
