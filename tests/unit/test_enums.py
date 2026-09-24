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

"""Unit tests for StrEnum and ZenML enums."""

import pytest
from zenml.enums import ArtifactType
from zenml.utils.enum_utils import StrEnum


def test_str_enum_values_and_names():
    """Test StrEnum values, names, and string conversion."""
    values = ArtifactType.values()
    names = ArtifactType.names()

    assert "DataArtifact" in values
    assert "DATA" in names
    assert ArtifactType.has_value("DataArtifact")
    assert not ArtifactType.has_value("NonExistentType")


def test_str_enum_names_str():
    """Test StrEnum names_str helper method."""
    names_str = ArtifactType.names_str()
    assert "DataArtifact" in names_str
    assert isinstance(names_str, str)
