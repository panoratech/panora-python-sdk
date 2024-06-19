"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from panora import utils


@dataclasses.dataclass
class UnifiedAttachmentInputFieldMappings:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UnifiedAttachmentInput:
    file_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name') }})
    r"""The file name of the attachment"""
    file_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_url') }})
    r"""The file url of the attachment"""
    uploader: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uploader') }})
    r"""The uploader's uuid of the attachment"""
    field_mappings: UnifiedAttachmentInputFieldMappings = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field_mappings') }})
    
