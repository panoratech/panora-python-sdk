"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import unifiedeventinput as components_unifiedeventinput
from ...models.components import unifiedeventoutput as components_unifiedeventoutput
from dataclasses_json import Undefined, dataclass_json
from panora import utils
from typing import List, Optional


@dataclasses.dataclass
class AddEventsRequest:
    connection_token: str = dataclasses.field(metadata={'header': { 'field_name': 'connection_token', 'style': 'simple', 'explode': False }})
    x_connection_token: str = dataclasses.field(metadata={'header': { 'field_name': 'x-connection-token', 'style': 'simple', 'explode': False }})
    r"""The connection token"""
    request_body: List[components_unifiedeventinput.UnifiedEventInput] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    remote_data: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'remote_data', 'style': 'form', 'explode': True }})
    r"""Set to true to include data from the original Marketingautomation software."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddEventsResponseBody:
    status_code: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    data: Optional[components_unifiedeventoutput.UnifiedEventOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddEventsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    object: Optional[AddEventsResponseBody] = dataclasses.field(default=None)
    unified_event_outputs: Optional[List[components_unifiedeventoutput.UnifiedEventOutput]] = dataclasses.field(default=None)
    

