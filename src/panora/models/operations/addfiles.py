"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import unifiedfileinput as components_unifiedfileinput
from ...models.components import unifiedfileoutput as components_unifiedfileoutput
from dataclasses_json import Undefined, dataclass_json
from panora import utils
from typing import List, Optional


@dataclasses.dataclass
class AddFilesRequest:
    connection_token: str = dataclasses.field(metadata={'header': { 'field_name': 'connection_token', 'style': 'simple', 'explode': False }})
    x_connection_token: str = dataclasses.field(metadata={'header': { 'field_name': 'x-connection-token', 'style': 'simple', 'explode': False }})
    r"""The connection token"""
    request_body: List[components_unifiedfileinput.UnifiedFileInput] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    remote_data: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'remote_data', 'style': 'form', 'explode': True }})
    r"""Set to true to include data from the original Filestorage software."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddFilesResponseBody:
    status_code: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    data: Optional[components_unifiedfileoutput.UnifiedFileOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddFilesResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    object: Optional[AddFilesResponseBody] = dataclasses.field(default=None)
    unified_file_outputs: Optional[List[components_unifiedfileoutput.UnifiedFileOutput]] = dataclasses.field(default=None)
    

