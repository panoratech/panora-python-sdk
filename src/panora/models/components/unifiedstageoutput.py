"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from panora import utils
from typing import Optional


@dataclasses.dataclass
class UnifiedStageOutputFieldMappings:
    pass


@dataclasses.dataclass
class UnifiedStageOutputRemoteData:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UnifiedStageOutput:
    stage_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stage_name') }})
    r"""The name of the stage"""
    field_mappings: UnifiedStageOutputFieldMappings = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field_mappings') }})
    remote_data: UnifiedStageOutputRemoteData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_data') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The uuid of the stage"""
    remote_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_id'), 'exclude': lambda f: f is None }})
    r"""The id of the stage in the context of the Crm 3rd Party"""
    
