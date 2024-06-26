"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import unifiedcompanyinput as components_unifiedcompanyinput
from ...models.components import unifiedcompanyoutput as components_unifiedcompanyoutput
from dataclasses_json import Undefined, dataclass_json
from panora import utils
from typing import Optional


@dataclasses.dataclass
class AddHrisCompanyRequest:
    x_connection_token: str = dataclasses.field(metadata={'header': { 'field_name': 'x-connection-token', 'style': 'simple', 'explode': False }})
    r"""The connection token"""
    unified_company_input: components_unifiedcompanyinput.UnifiedCompanyInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    remote_data: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'remote_data', 'style': 'form', 'explode': True }})
    r"""Set to true to include data from the original Hris software."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddHrisCompanyResponseBody:
    status_code: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    data: Optional[components_unifiedcompanyoutput.UnifiedCompanyOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddHrisCompanyResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    object: Optional[AddHrisCompanyResponseBody] = dataclasses.field(default=None)
    unified_company_output: Optional[components_unifiedcompanyoutput.UnifiedCompanyOutput] = dataclasses.field(default=None)
    

