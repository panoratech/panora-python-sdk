"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from panora import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateBatchLinkedUserDto:
    linked_user_origin_ids: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('linked_user_origin_ids') }})
    alias: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alias') }})
    id_project: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id_project') }})
    
