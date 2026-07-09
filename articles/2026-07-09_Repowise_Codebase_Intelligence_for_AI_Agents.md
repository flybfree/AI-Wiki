---
title: "Repowise: Codebase Intelligence for AI Agents and Humans"
date: 2026-07-09
source: https://github.com/repowise-dev/repowise
tags: ['ai-agents', 'code-intelligence', 'mcp', 'self-hosting']
---

# Repowise: Codebase Intelligence for AI Agents and Humans

**Source**: [Repowise GitHub](https://github.com/repowise-dev/repowise) | [Website](https://www.repowise.dev/) | [Docs](https://docs.repowise.dev/)

> Repowise turns any Git repository into a queryable knowledge graph that AI coding agents and humans can reason over through precisely designed tools.

## What is Repowise?

Repowise is a **codebase intelligence layer** for the AI era. It indexes your repository once and serves both:

- **AI coding agents** (Claude Code, Cursor, Windsurf, VS Code) via nine MCP tools
- **Humans** accountable for the code via a defect-validated code-health score and change risk assessment

Think of it as an architecture-aware wiki that lives alongside your code, giving agents deep contextual understanding without manual setup.

## Core Intelligence Layers

Repowise indexes your repo into four layers:

1. **Dependency graph** – Understands how modules relate to each other
2. **Git history** – Tracks evolution and provides historical context  
3. **Auto-generated documentation** – Creates up-to-date docs directly from code
4. **Architectural decisions** – Captures why things were built that way

## Key Features

- **Code health scores** – Defect-validated metrics on code quality
- **Dead code detection** – Identifies unused or obsolete code paths
- **Git analytics** – Tracks commit patterns, author contributions, and change risk
- **Architectural decision tracking** – Maintains a history of design choices
- **MCP tools integration** – Nine precisely designed tools for agent reasoning

## Self-Hosted Setup Tutorial

### Prerequisites

- Docker and Docker Compose installed
- Git repository to index (local or remote)
- 4GB+ RAM recommended for indexing

### Step 1: Clone the Repository

```bash
git clone https://github.com/repowise-dev/repowise.git
cd repowise
```

### Step 2: Configure Environment Variables

Create a `.env` file in the project root:

```env
# Repowise configuration
REPOWISE_PORT=3000
REPOWISE_DATA_DIR=./data
REPOWISE_INDEX_DIR=./index

# Database (optional - uses SQLite by default)
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=repowise
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=repowise

# GitHub integration (optional)
GITHUB_TOKEN=your_github_token
```

### Step 3: Start with Docker Compose

```bash
docker compose up -d
```

This starts the Repowise service and any required dependencies.

### Step 4: Connect Your Repository

1. Open `http://localhost:3000` in your browser
2. Click "Connect Repository"
3. Choose GitHub, Bitbucket, or GitLab
4. Select repositories to grant access to
5. Wait for context generation to complete

### Step 5: Configure MCP Tools

For AI agents, add Repowise as an MCP server. Example for Claude Code:

```json
{
  "mcpServers": {
    "repowise": {
      "command": "npx",
      "args": ["-y", "@repowise/mcp-server"],
      "env": {
        "REPOWISE_URL": "http://localhost:3000"
      }
    }
  }
}
```

### Step 6: Verify Installation

Check service status:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f repowise
```

Test the API:

```bash
curl http://localhost:3000/api/health
```

## MCP Tools Reference

Repowise exposes nine tools for agent reasoning:

1. `repowise.read_file` – Read file contents with context
2. `repowise.search_code` – Search codebase for patterns
3. `repowise.get_dependencies` – Retrieve dependency graph
4. `repowise.get_git_history` – Access commit history and changes
5. `repowise.get_architecture` – Understand system architecture
6. `repowise.get_decisions` – Query architectural decisions
7. `repowise.get_health_score` – Check code quality metrics
8. `repowise.find_dead_code` – Identify unused code paths
9. `repowise.analyze_risk` – Assess change risk

## Use Cases

### For AI Agents

- **Context-aware coding** – Agents understand the full codebase context
- **Dependency reasoning** – Make changes with awareness of impacts
- **Architecture preservation** – Maintain design patterns and decisions
- **Risk assessment** – Evaluate potential side effects before modifying code

### For Humans

- **Code health monitoring** – Track quality metrics over time
- **Change risk evaluation** – Understand impact before committing
- **Documentation generation** – Auto-generated docs stay current
- **Decision history** – Know why systems were built certain ways

## Troubleshooting

### Indexing Issues

If indexing fails:

```bash
docker compose exec repowise python -m repowise.index --force
```

### Connection Problems

Check network accessibility:

```bash
docker compose port repowise 3000
```

### Performance Optimization

For large repos, increase resources:

```yaml
# docker-compose.yml
services:
  repowise:
    deploy:
      resources:
        limits:
          memory: 8G
```

## Further Reading

- [Official Documentation](https://docs.repowise.dev/)
- [GitHub Repository](https://github.com/repowise-dev/repowise)
- [MCP Server Implementation](https://github.com/repowise-dev/mcp-server)
- [Self-Hosting Guide](https://docs.repowise.dev/self-hosting)

## Related Concepts

- **MCP (Model Context Protocol)** – Standard for AI agent tool integration
- **Codebase Intelligence** – Understanding code structure and context
- **AI Coding Agents** – Autonomous or assisted programming tools
- **Self-Hosted Services** – Running software on local infrastructure

---

*This article was generated as part of the AI Research Wiki. For questions or contributions, see the [wiki guidelines](https://github.com/flybfree/AI-Wiki).*