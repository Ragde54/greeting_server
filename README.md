# Greeting MCP Server (Basic MCP Blueprint)

This is a basic blueprint showcasing how to build and containerize a Model Context Protocol (MCP) server using Python and the `FastMCP` framework. It provides a simple set of tools that an MCP client (like Claude Desktop) can use to interact with your system.

## Features

This server exposes the following MCP tools:
- `say_hello`: Returns a friendly greeting message.
- `get_current_time`: Returns the current system time.

## Project Structure

```text
greeting-server/
├── .env.example        # Example environment variables required to run the server
├── README.md           # Project documentation
├── pyproject.toml      # Python project configuration (Hatchling build system)
├── uv.lock             # Python dependencies lockfile
├── docker/
│   └── Dockerfile      # Instructions to build the server into a Docker image
├── src/
│   └── greeting_mcp/
│       ├── main.py     # Application entry point and transport configuration (stdio vs sse)
│       ├── server.py   # FastMCP server definition and tool registration
│       └── tools/      # Directory containing the individual MCP tools
└── tests/              # Test suite for the application
```

## Running the Server with Claude Desktop

You can run this MCP server locally with Claude Desktop in two different ways depending on your preference.

### Option 1: Running with Docker (Recommended)

1. **Build the Docker image:**
   ```bash
   docker build -f docker/Dockerfile -t greeting-mcp .
   ```

2. **Configure Claude Desktop:**
   Open your Claude Desktop configuration file (typically located at `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS) and add the following entry:
   ```json
   "mcpServers": {
     "greeting-mcp": {
       "command": "docker",
       "args": [
         "run",
         "-i",
         "--rm",
         "--env-file",
         "/ABSOLUTE/PATH/TO/greeting_server/.env",
         "greeting-mcp"
       ],
       "env": {
         "TIME_FORMAT": "%H:%M:%S",
         "MCP_TRANSPORT": "stdio"
       }
     }
   }
   ```
   *Note: Ensure you replace `/ABSOLUTE/PATH/TO/` with the actual path to the repository on your machine.*

### Option 2: Running with `uv` directly

If you prefer not to use Docker, you can run the server directly using the `uv` Python package manager.

1. **Configure Claude Desktop:**
   ```json
   "mcpServers": {
     "greeting-mcp": {
       "command": "uv",
       "args": [
         "run",
         "--directory",
         "/ABSOLUTE/PATH/TO/greeting_server",
         "greeting-mcp"
       ],
       "env": {
         "TIME_FORMAT": "%H:%M:%S",
         "MCP_TRANSPORT": "stdio"
       }
     }
   }
   ```

## Deployment Considerations

If you intend to deploy this code to a real production server (e.g., AWS, Render, Google Cloud Run) rather than running it locally as a desktop integration, you must make a few important changes:

1. **Switch the Transport Layer (Critical)**: Local desktop integrations use the `stdio` (Standard Input/Output) transport. For a remote server, you must use Server-Sent Events (SSE) over HTTP. Update your environment variables to set `MCP_TRANSPORT=sse`. The `main.py` entry point is already configured to automatically bind the server to `0.0.0.0:8000` when this mode is enabled.

2. **Network Port Mapping**: When running via Docker in SSE mode, you will need to map the container's port to your host machine's port. E.g. `docker run -p 8000:8000 ...`. Your deployment platform will need to be configured to route HTTP traffic to this port.

3. **Add Authentication**: Currently, running this server remotely over HTTP allows *anyone* who knows the URL to connect to the MCP server. Before deploying, you should add an authentication layer (such as checking for an API key or Bearer token header) inside `main.py` to prevent unauthorized access to your tools.
