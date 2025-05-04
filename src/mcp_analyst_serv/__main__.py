"""Command-line entry point for the MCP Analytics Server."""

from mcp_analyst_serv.server import create_server

def main():
    """Run the MCP Analytics Server."""
    server = create_server()
    print(f"MCP Analytics Server '{server.name}' is ready to use")
    print("Server provides the following tools and resources:")
    print(f"Tools: {', '.join(tool.name for tool in server.tools)}")
    print(f"Resources: {', '.join(resource.pattern for resource in server.resources)}")
    
    # Keep the process running
    try:
        print("\nPress Ctrl+C to stop the server...")
        while True:
            pass
    except KeyboardInterrupt:
        print("\nServer stopped")

if __name__ == "__main__":
    main()
