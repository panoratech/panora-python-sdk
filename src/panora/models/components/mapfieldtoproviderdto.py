"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from panora import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MapFieldToProviderDto:
    attribute_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributeId') }})
    source_custom_field_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_custom_field_id') }})
    source_provider: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_provider') }})
    linked_user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('linked_user_id') }})
    
