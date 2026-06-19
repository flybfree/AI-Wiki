---
title: "Lesson 3 — Abstraction Layer: Model Swapping & Normalization"
created: 2026-06-10
module: Self Improving AI Loops
lesson: 3
tags: [abstraction, litellm, model-routing, vendor-lock-in]
---

## Summary

Placeholder summary — please add a concise summary.


# Lesson 3: Abstraction Layer — Model Swapping & Normalization



**Source**: [Original Article](http://localhost:11434)
## Core Idea

**LiteLLM** runs as a proxy server that normalizes 100+ LLM providers (including local models) to a single OpenAI-compatible API. This is the critical layer that lets you swap models without rewriting agent code.

## Why You Need This Layer

### Model Version Brittleness
**Definition:** When a foundation model provider updates their API (e.g., GPT-4 to GPT-4o, Claude 3.5 to Claude 3.7), your agents break. Benchmarks show overall improvement, but local benchmarks can go down. Every model upgrade requires prompt changes and investigation.

**Enterprise reality:** "Just switching from one API to another" does not work. There is always some prompt changes and investigation required.

### Vendor Lock-In
Building agents against one provider's API means you're tied to that provider's pricing, availability, and model roadmap. If they deprecate your model or raise prices 10x, you have no leverage.

### The "Swap Without Breaking" Pattern
With LiteLLM, your agent code never changes. You only change configuration:

```
Agent code → LiteLLM proxy → Model A (dev) or Model B (prod)
```

The agent doesn't know or care which model it's talking to.

## LiteLLM Setup

### Installation

```bash
pip install litellm
```

### Configuration

Create `config.yaml`:

```yaml
model_list:
  # Development: local Ollama
  - model_name: my-agent
    litellm_params:
      model: ollama/llama3.3
      api_base: http://localhost:11434

  # Production: cloud Claude
  - model_name: my-agent
    litellm_params:
      model: anthropic/claude-sonnet-4-20250514
      api_key: sk-ant-xxx

  # Fallback: if Claude is down
  - model_name: my-agent
    litellm_params:
      model: openai/gpt-4o
      api_key: sk-xxx
```

### Start the Proxy

```bash
litellm --config config.yaml --port 4000
```

### Agent Code (Never Changes)

```python
import openai  # Standard OpenAI client

client = openai.OpenAI(
    api_key="anything",  # LiteLLM ignores this
    base_url="http://localhost:4000/v1"  # Points to LiteLLM proxy
)

response = client.chat.completions.create(
    model="my-agent",  # Resolves to whichever model config.yaml says
    messages=[{"role": "user", "content": "Implement ticket 001"}]
)
```

## Model Routing Strategies

### Strategy 1: Dev Local → Prod Cloud
```yaml
model_list:
  - model_name: dev-agent
    litellm_params:
      model: ollama/mistral-small-3.1
      api_base: http://localhost:11434
  - model_name: prod-agent
    litellm_params:
      model: anthropic/claude-sonnet-4-20250514
      api_key: ${ANTHROPIC_API_KEY}
```

### Strategy 2: Primary + Fallback
```yaml
model_list:
  - model_name: my-agent
    litellm_params:
      model: ollama/llama3.3
      api_base: http://localhost:11434
  - model_name: my-agent
    litellm_params:
      model: openai/gpt-4o
      api_key: ${OPENAI_API_KEY}
```

### Strategy 3: Cost Optimization
```yaml
model_list:
  - model_name: simple-tasks
    litellm_params:
      model: ollama/phi-4-mini  # Cheap, fast, local
  - model_name: complex-tasks
    litellm_params:
      model: anthropic/claude-opus-4-20250514  # Expensive, powerful
```

## Environment Variable Management

**Never hardcode API keys.** Use environment variables:

```bash
# In ~/.hermes/.env or your shell profile
export ANTHROPIC_API_KEY="sk-ant-xxx"
export OPENAI_API_KEY="sk-xxx"
export OLLAMA_HOST="http://localhost:11434"
```

LiteLLM reads these automatically from `os.environ`.

## Reducing Model Version Brittleness

Raj Shukla's observation: every time a model version updates, reliability metrics break. You can't just switch APIs.

**How the abstraction layer helps:**

1. **Pin models explicitly** — Don't use `model: claude-sonnet-4` (auto-updates). Use `model: anthropic/claude-sonnet-4-20250514` (specific version).

2. **Test before deploying** — Run your evaluation suite against the new model before switching the proxy config.

3. **Feature flags** — Use environment variables to toggle between model versions:
```bash
# Dev: test new model
export AGENT_MODEL=ollama/gemma-4

# Prod: stable model
export AGENT_MODEL=anthropic/claude-sonnet-4-20250514
```

4. **Local models reduce this risk** — When you self-host, you control when (and if) to upgrade. No surprise breaks from provider updates.

## The "Swap Without Breaking" Checklist

- [ ] LiteLLM proxy installed and running
- [ ] `config.yaml` has your model list with pinned versions
- [ ] Agent code uses `openai.OpenAI()` with proxy `base_url`
- [ ] API keys in environment variables, never in code
- [ ] Evaluation suite runs against both dev and prod models
- [ ] Feature flag for model version switching
- [ ] Fallback model configured for redundancy

## Key Takeaway

The abstraction layer is where you buy freedom. Your agents talk to LiteLLM. LiteLLM talks to whatever model you configure. Swap models in config, not in code. Pin versions. Test before deploying. Self-host to control your upgrade schedule.

## Related Concepts
- [[Self-Improving AI Loops]]
- [[Model Version Brittleness]]
- [[Inference Layer]]
