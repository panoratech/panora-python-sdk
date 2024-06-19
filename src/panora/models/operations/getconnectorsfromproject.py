"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json


@dataclasses.dataclass
class GetConnectorsFromProjectRequest:
    project_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'projectId', 'style': 'form', 'explode': True }})
    get_connectors_from_project: str = dataclasses.field(metadata={'query_param': { 'field_name': 'getConnectorsFromProject', 'style': 'form', 'explode': True }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetConnectorsFromProjectResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    
