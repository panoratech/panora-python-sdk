"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import unifiedmessageoutput as components_unifiedmessageoutput
from dataclasses_json import Undefined, dataclass_json
from panora import utils
from typing import Optional


@dataclasses.dataclass
class GetMessagesRequest:
    x_connection_token: str = dataclasses.field(metadata={'header': { 'field_name': 'x-connection-token', 'style': 'simple', 'explode': False }})
    r"""The connection token"""
    remote_data: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'remote_data', 'style': 'form', 'explode': True }})
    r"""Set to true to include data from the original Marketingautomation software."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetMessagesResponseBody:
    status_code: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    data: Optional[components_unifiedmessageoutput.UnifiedMessageOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetMessagesResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    object: Optional[GetMessagesResponseBody] = dataclasses.field(default=None)
    

