"""MCP Server implementation for analytics tools."""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("AnalyticsServer")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting."""
    return f"Hello, {name}!"


def create_server():
    """Create and return the MCP server instance.
    
    Returns:
        FastMCP: The configured MCP server instance
    """
    return mcp
