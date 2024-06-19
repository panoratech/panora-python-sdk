"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from panora import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateConnectionStrategyDto:
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    attributes: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes') }})
    values: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('values') }})
    

