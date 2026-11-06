# Katalyz plugins

This repository contains the public source for Katalyz's Claude and ChatGPT plugins. Both connect to the Katalyz MCP server at https://mcp.katalyz.co/mcp. Sellers authorize access to their own Katalyz tenant through OAuth.

- [Claude](claude/README.md) bundles the MCP connector with workflow skills. For the Claude directory, use this repository's main branch and set the plugin path to claude.
- [ChatGPT](chatgpt/plugin.json) contains the OpenAI plugin package source. Upload a ZIP of this folder through the OpenAI plugin dashboard.

The MCP server and application code are maintained separately. Generated ZIPs and reviewer materials stay out of this public repository.
