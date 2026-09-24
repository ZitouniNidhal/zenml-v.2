#  Copyright (c) ZenML GmbH 2026. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

"""Unit tests for custom ZenML types and validation helpers."""

from uuid import UUID, uuid4

import pytest
from zenml.types import HTMLString, JSONString, MarkdownString, is_valid_uuid


def test_is_valid_uuid_helper():
    """Test is_valid_uuid validation with valid UUIDs, strings, and invalid inputs."""
    random_uuid = uuid4()
    assert is_valid_uuid(random_uuid)
    assert is_valid_uuid(str(random_uuid))

    assert not is_valid_uuid("not-a-valid-uuid")
    assert not is_valid_uuid(12345)
    assert not is_valid_uuid(None)


def test_custom_string_types():
    """Test HTMLString, MarkdownString, JSONString behavior."""
    html = HTMLString("<h1>Title</h1>")
    md = MarkdownString("# Title")
    js = JSONString('{"key": "value"}')

    assert isinstance(html, str)
    assert isinstance(md, str)
    assert isinstance(js, str)
