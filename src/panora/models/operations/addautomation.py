"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import unifiedautomationinput as components_unifiedautomationinput
from ...models.components import unifiedautomationoutput as components_unifiedautomationoutput
from dataclasses_json import Undefined, dataclass_json
from panora import utils
from typing import Optional


@dataclasses.dataclass
class AddAutomationRequest:
    x_connection_token: str = dataclasses.field(metadata={'header': { 'field_name': 'x-connection-token', 'style': 'simple', 'explode': False }})
    r"""The connection token"""
    unified_automation_input: components_unifiedautomationinput.UnifiedAutomationInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    remote_data: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'remote_data', 'style': 'form', 'explode': True }})
    r"""Set to true to include data from the original Marketingautomation software."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddAutomationResponseBody:
    status_code: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    data: Optional[components_unifiedautomationoutput.UnifiedAutomationOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddAutomationResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    object: Optional[AddAutomationResponseBody] = dataclasses.field(default=None)
    unified_automation_output: Optional[components_unifiedautomationoutput.UnifiedAutomationOutput] = dataclasses.field(default=None)
    

