# AccountingJournalentry
(*accounting_journalentry*)

### Available Operations

* [get_journal_entrys](#get_journal_entrys) - List a batch of JournalEntrys
* [add_journal_entry](#add_journal_entry) - Create a JournalEntry
* [get_journal_entry](#get_journal_entry) - Retrieve a JournalEntry
* [add_journal_entrys](#add_journal_entrys) - Add a batch of JournalEntrys

## get_journal_entrys

List a batch of JournalEntrys

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_journalentry.get_journal_entrys(x_connection_token='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `x_connection_token`                                               | *str*                                                              | :heavy_check_mark:                                                 | The connection token                                               |
| `remote_data`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Set to true to include data from the original Accounting software. |


### Response

**[operations.GetJournalEntrysResponse](../../models/operations/getjournalentrysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_journal_entry

Create a journalentry in any supported Accounting software

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_journalentry.add_journal_entry(x_connection_token='<value>', unified_journal_entry_input=components.UnifiedJournalEntryInput(), remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `x_connection_token`                                                                       | *str*                                                                                      | :heavy_check_mark:                                                                         | The connection token                                                                       |
| `unified_journal_entry_input`                                                              | [components.UnifiedJournalEntryInput](../../models/components/unifiedjournalentryinput.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `remote_data`                                                                              | *Optional[bool]*                                                                           | :heavy_minus_sign:                                                                         | Set to true to include data from the original Accounting software.                         |


### Response

**[operations.AddJournalEntryResponse](../../models/operations/addjournalentryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_journal_entry

Retrieve a journalentry from any connected Accounting software

### Example Usage

```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_journalentry.get_journal_entry(id='<value>', remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | id of the journalentry you want to retrieve.                       |
| `remote_data`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Set to true to include data from the original Accounting software. |


### Response

**[operations.GetJournalEntryResponse](../../models/operations/getjournalentryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_journal_entrys

Add a batch of JournalEntrys

### Example Usage

```python
import panora
from panora.models import components

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.accounting_journalentry.add_journal_entrys(connection_token='<value>', x_connection_token='<value>', request_body=[
    components.UnifiedJournalEntryInput(),
], remote_data=False)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `connection_token`                                                                               | *str*                                                                                            | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `x_connection_token`                                                                             | *str*                                                                                            | :heavy_check_mark:                                                                               | The connection token                                                                             |
| `request_body`                                                                                   | List[[components.UnifiedJournalEntryInput](../../models/components/unifiedjournalentryinput.md)] | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `remote_data`                                                                                    | *Optional[bool]*                                                                                 | :heavy_minus_sign:                                                                               | Set to true to include data from the original Accounting software.                               |


### Response

**[operations.AddJournalEntrysResponse](../../models/operations/addjournalentrysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
