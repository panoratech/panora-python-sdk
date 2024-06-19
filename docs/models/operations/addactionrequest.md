# AddActionRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `x_connection_token`                                                           | *str*                                                                          | :heavy_check_mark:                                                             | The connection token                                                           |
| `unified_action_input`                                                         | [components.UnifiedActionInput](../../models/components/unifiedactioninput.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `remote_data`                                                                  | *Optional[bool]*                                                               | :heavy_minus_sign:                                                             | Set to true to include data from the original Marketingautomation software.    |