"""Tests for the server module."""

import pytest
from mcp_analyst_serv.server import create_server


def test_create_server():
    """Test that the server is created with the correct name and tools."""
    server = create_server()
    assert server.name == "AnalyticsServer"
    assert any(tool.name == "add" for tool in server.tools)
    assert any(resource.pattern == "greeting://{name}" for resource in server.resources)
