"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import unifiedticketoutput as components_unifiedticketoutput
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class UpdateTicketRequest:
    id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'id', 'style': 'form', 'explode': True }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateTicketResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    unified_ticket_output: Optional[components_unifiedticketoutput.UnifiedTicketOutput] = dataclasses.field(default=None)
    
