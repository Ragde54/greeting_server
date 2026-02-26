import os
from dotenv import load_dotenv
from greeting_mcp.server import mcp

load_dotenv()

def main():
    # Get the transport type from the environment variables
    transport_type = os.getenv("MCP_TRANSPORT", "stdio")
    if transport_type == "sse":
        # Run the MCP server in SSE mode
        mcp.run(transport="sse", host=os.getenv("HOST", "0.0.0.0"), port=os.getenv("PORT", 8000))
    else:
        # Run the MCP server in stdio mode
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
    