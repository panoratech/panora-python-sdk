"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import unifieddealoutput as components_unifieddealoutput
from dataclasses_json import Undefined, dataclass_json
from panora import utils
from typing import Optional


@dataclasses.dataclass
class UpdateDealRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateDealResponseBody:
    status_code: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    data: Optional[components_unifieddealoutput.UnifiedDealOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateDealResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    object: Optional[UpdateDealResponseBody] = dataclasses.field(default=None)
    

