---
title: Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs
published: 2026-10-16T16:30:38Z
authors: Sam Partee, River Stevens, Thierry Damiba, Valerie Fanelle
url: http://arxiv.org/abs/2610.23707v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs

## Abstract
A multi-step agent task fails when a single tool it needs is missing, yet the tools an agent may need are too many to list: the roughly 8,200 tools on the platform we study have definitions that together exceed the context window of any model we evaluate. We present Tool Recommendation, a deployed system that gives an agent all of them, hundreds of times more than a typical MCP server exposes, through a fixed interface of three tools. It runs at the gateway between agent and tools, executing every call under the end user's own credentials and checking it against the user's consent for each service and the tools the agent may use. We evaluate it on both a public retrieval benchmark and billed end-to-end session cost. On ToolRet, Tool Recommendation places every tool a query needs in the top ten 57% more often than BM25, a lexical ranking that commercial tool search offers, and compares favorably with published systems up to nine times its size. In paired multi-step workflows, its first recommendation covered every required tool in 93% of Codex sessions, and against a fixed list of 100 tools it cut input tokens by 17% with Codex and 40% with Claude Code and the total bill in all 14 runs, by up to 40%, with no change in task completion.

## Metadata
- **Published**: 2026-10-16T16:30:38Z
- **Authors**: Sam Partee, River Stevens, Thierry Damiba, Valerie Fanelle
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.23707v1)