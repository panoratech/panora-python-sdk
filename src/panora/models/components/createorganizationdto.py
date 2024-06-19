"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from panora import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateOrganizationDto:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    stripe_customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stripe_customer_id') }})
    
