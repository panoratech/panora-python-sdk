"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from panora import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProjectConnectorsDto:
    column: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('column') }})
    status: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

