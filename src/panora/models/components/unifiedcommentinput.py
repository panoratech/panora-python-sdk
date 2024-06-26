"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from panora import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UnifiedCommentInput:
    body: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('body') }})
    r"""The body of the comment"""
    html_body: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('html_body'), 'exclude': lambda f: f is None }})
    r"""The html body of the comment"""
    is_private: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_private'), 'exclude': lambda f: f is None }})
    r"""The public status of the comment"""
    creator_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creator_type'), 'exclude': lambda f: f is None }})
    r"""The creator type of the comment. Authorized values are either USER or CONTACT"""
    ticket_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ticket_id'), 'exclude': lambda f: f is None }})
    r"""The uuid of the ticket the comment is tied to"""
    contact_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contact_id'), 'exclude': lambda f: f is None }})
    r"""The uuid of the contact which the comment belongs to (if no user_id specified)"""
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id'), 'exclude': lambda f: f is None }})
    r"""The uuid of the user which the comment belongs to (if no contact_id specified)"""
    attachments: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachments'), 'exclude': lambda f: f is None }})
    r"""The attachements uuids tied to the comment"""
    

