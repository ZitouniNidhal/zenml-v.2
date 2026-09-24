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

"""Unit tests for custom ZenML exceptions."""

import pytest
from zenml.exceptions import (
    AuthorizationException,
    CredentialsNotValid,
    InitializationException,
    ZenMLBaseException,
)


def test_zenml_base_exception_formatting():
    """Test ZenMLBaseException message formatting with and without URL."""
    exc = ZenMLBaseException(message="Test error")
    assert "Test error" in str(exc)

    exc_with_url = ZenMLBaseException(
        message="Test error", url="https://docs.zenml.io"
    )
    assert "For more information, visit https://docs.zenml.io" in str(exc_with_url)


def test_exception_hierarchy():
    """Test exception class inheritance relationships."""
    assert issubclass(InitializationException, ZenMLBaseException)
    assert issubclass(AuthorizationException, ZenMLBaseException)
    assert issubclass(CredentialsNotValid, AuthorizationException)
