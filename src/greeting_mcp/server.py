from mcp.server.fastmcp import FastMCP
from greeting_mcp.tools.time import get_current_time
from greeting_mcp.tools.greeting import say_hello

# Define the MCP server
mcp = FastMCP("greeting-mcp")

mcp.add_tool(get_current_time)
mcp.add_tool(say_hello)