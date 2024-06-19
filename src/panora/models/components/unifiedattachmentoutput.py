"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from panora import utils
from typing import Optional


@dataclasses.dataclass
class UnifiedAttachmentOutputFieldMappings:
    pass


@dataclasses.dataclass
class UnifiedAttachmentOutputRemoteData:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UnifiedAttachmentOutput:
    file_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name') }})
    r"""The file name of the attachment"""
    file_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_url') }})
    r"""The file url of the attachment"""
    uploader: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uploader') }})
    r"""The uploader's uuid of the attachment"""
    field_mappings: UnifiedAttachmentOutputFieldMappings = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field_mappings') }})
    remote_data: UnifiedAttachmentOutputRemoteData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_data') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The uuid of the attachment"""
    remote_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_id'), 'exclude': lambda f: f is None }})
    r"""The id of the attachment in the context of the 3rd Party"""
    

