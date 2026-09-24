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

"""Unit tests for logger module and color formatting flags."""

import logging
import os
import pytest
from zenml.logger import CustomFormatter, get_logger


def test_get_logger_returns_logging_logger():
    """Test get_logger returns a logging.Logger instance with proper name."""
    log = get_logger("test_logger")
    assert isinstance(log, logging.Logger)
    assert log.name == "test_logger"


def test_custom_formatter_no_color_flag(monkeypatch):
    """Test CustomFormatter detects NO_COLOR environment variable."""
    monkeypatch.setenv("NO_COLOR", "true")
    formatter = CustomFormatter()
    assert formatter._colors_disabled is True
