---
title: Lesson 8 — Putting It All Together: DIY Architecture
created: 2026-06-10
module: Self Improving AI Loops
lesson: 8
tags: [architecture, diy-stack, production-readiness, pitfalls]
---

# Lesson 8: Putting It All Together — DIY Architecture

## Core Idea

This lesson ties all 7 previous lessons into a complete, working self-hosted stack. You'll see how each layer connects, a working Ralph loop script, integration patterns, and the production readiness checklist.

## Complete Stack Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Orchestration Layer                       │
│              Dify / Flowise / LangGraph                      │
│         (Visual workflow OR code-based state machine)        │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                    Agent Layer                               │
│            SmolAgents / OpenDevin / Aider                    │
│         (CodeAgent writes actions as code)                   │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                 Evaluation Layer                             │
│             DeepEval → Arize Phoenix → Promptfoo             │
│         (LLM-as-judge → drift detection → CI evals)          │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                 Knowledge Layer                              │
│              Mozilla cq → Qdrant / SQLite                    │
│         (Knowledge Units → vector DB / structured store)     │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                 Abstraction Layer                            │
│                       LiteLLM Proxy                          │
│         (Swap ollama/llama3.3 ↔ cloud Claude without         │
│          changing agent code)                                │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                   Inference Layer                            │
│        Ollama (dev) / vLLM (prod) / LM Studio              │
│         Llama 4 Scout / Gemma 4 / Mistral S3.1 / Phi-4     │
└─────────────────────────────────────────────────────────────┘
```

## Working Ralph Loop Script

```bash
#!/bin/bash
# Ralph loop with self-hosted LLM + evaluation + knowledge storage
# Save as ~/scripts/ralph-loop.sh and chmod +x

set -e

# Configuration
export OPENAI_API_KEY="sk-fake-key-for-litellm"
export OPENAI_BASE_URL="http://localhost:4000/v1"  # LiteLLM proxy
TICKET_DIR="/home/rich/projects/doc/tickets"
DONE_DIR="/home/rich/projects/doc/tickets/done"
EVAL_DIR="/home/rich/projects/evals"

# Ensure directories exist
mkdir -p "$DONE_DIR" "$EVAL_DIR"

# Function: evaluate agent output
evaluate_output() {
    local output_file=$1
    local ticket_id=$(basename $output_file .md)
    
    # Run DeepEval metrics
    python3 << PYEOF
from deepeval import test_case
from deepeval.metrics import HallucinationMetric, AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

with open("$output_file") as f:
    output = f.read()

test = LLMTestCase(
    input="Implement ticket $ticket_id",
    output=output
)

hallucination = HallucinationMetric(threshold=0.3)
relevancy = AnswerRelevancyMetric(threshold=0.7)

hallucination.measure(test)
relevancy.measure(test)

print(f"Hallucination: {hallucination.score}")
print(f"Relevancy: {relevancy.score}")

if hallucination.score > 0.3:
    exit(1)  # Fail
PYEOF
    
    # Run unit tests
    cd /home/rich/projects && pytest tests/ -q
}

# Function: store knowledge unit
store_knowledge() {
    local lesson=$1
    python3 << PYEOF
import sqlite3

conn = sqlite3.connect("/home/rich/wiki/ai-research/agent_knowledge.db")
conn.execute("""
  INSERT INTO knowledge_units (topic, content, confidence)
  VALUES (?, ?, 0.5)
""", ("ralph-loop-lesson", "$lesson", 0.5))
conn.commit()
PYEOF
}

# Main loop
echo "Starting Ralph loop..."
echo "Press Ctrl+C to stop"

while true; do
    # Get next ticket
    NEXT_TICKET=$(ls "$TICKET_DIR"/*.md 2>/dev/null | head -1)
    
    if [ -z "$NEXT_TICKET" ]; then
        echo "No more tickets. Exiting."
        break
    fi
    
    TICKET_ID=$(basename "$NEXT_TICKET" .md)
    echo "=== Processing ticket: $TICKET_ID ==="
    
    # Run Aider to implement the ticket
    aider --model openai/my-agent \
        --file "$NEXT_TICKET" \
        --yes-always \
        --no-auto-commit \
        --commit-message "implement $TICKET_ID" \
        --output "/home/rich/projects/output/${TICKET_ID}.md"
    
    # Evaluate the output
    if evaluate_output "/home/rich/projects/output/${TICKET_ID}.md"; then
        echo "✓ Ticket $TICKET_ID passed evaluation"
        mv "$NEXT_TICKET" "$DONE_DIR/"
        
        # Store knowledge unit from this session
        store_knowledge "Ticket $TICKET_ID implemented successfully with Aider + local LLM"
    else
        echo "✗ Ticket $TICKET_ID failed evaluation, retrying..."
        sleep 5
    fi
done

echo "Ralph loop complete."
```

## Integration Patterns

### Pattern 1: Dev Local → Prod Cloud
```yaml
# LiteLLM config.yaml
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

### Pattern 2: Primary + Fallback
```yaml
model_list:
  - model_name: my-agent
    litellm_params:
      model: ollama/llama3.3
      api_base: http://localhost:11434
  
  - model_name: my-agent-fallback
    litellm_params:
      model: openai/gpt-4o
      api_key: ${OPENAI_API_KEY}
```

### Pattern 3: Cost Optimization
```yaml
model_list:
  - model_name: simple-tasks
    litellm_params:
      model: ollama/phi-4-mini  # Cheap, fast, local
  
  - model_name: complex-tasks
    litellm_params:
      model: anthropic/claude-opus-4-20250514  # Expensive, powerful
```

## Production Readiness Checklist

### Infrastructure
- [ ] LiteLLM proxy running and tested
- [ ] Model server (Ollama/vLLM) running and tested
- [ ] Agent framework (SmolAgents/LangGraph) configured
- [ ] Evaluation suite (DeepEval) running against both dev and prod models
- [ ] Drift detection (Arize Phoenix) running continuously
- [ ] Knowledge store (Mozilla cq/SQLite) configured
- [ ] Orchestration layer (Dify/LangGraph) configured

### Safety
- [ ] Ralph loops are repo-contained with toolchain as judge
- [ ] Irreversible actions (terraform destroy, database drops) require manual review
- [ ] Agent has proper auth and RBAC (not running as root)
- [ ] Sandboxed code execution environment
- [ ] Fallback model configured for redundancy

### Monitoring
- [ ] Output distribution tracking (Arize Phoenix)
- [ ] Semantic drift detection running
- [ ] Prompt versioning (Promptfoo) configured
- [ ] Experiment tracking (MLflow) configured
- [ ] Agent activity visible in orchestration UI

### Maintenance
- [ ] Model version pinning (no auto-updates)
- [ ] Evaluation suite runs before every model change
- [ ] Knowledge unit review process (humans confirm KUs before promoting)
- [ ] Staged rollout for new agents (narrow scope → expand)
- [ ] Cold start strategy documented

## Pitfalls & Risks

### 1. Drift is the #1 Failure Mode
Analysis of 4M+ production agent calls shows drift (compliance, length, semantic, regression) is the most common failure mode. Most teams only track error rates and latency — the drift that actually destroys business value goes unnoticed.

**Fix:** Arize Phoenix for continuous drift detection. Track output distributions, not just errors.

### 2. Feedback-to-Node Routing
When a user says "this is wrong" in a 15-node workflow, tracing it back to the specific step that failed is hard. Task-level feedback without node-level routing is like telling a chef "the meal was bad" without saying which dish.

**Fix:** Maintain full execution traces. Build a probabilistic model that attributes outcome-level errors to specific nodes.

### 3. Cold Start
New agents have no feedback data. They need production feedback to improve but need to be good enough to generate useful feedback.

**Fix:** Staged deployment on narrow scope first. Collect feedback on the edges. Expand scope as accuracy improves.

### 4. Model Version Brittleness
Every foundation model update breaks your agents. Benchmarks show overall improvement, but local benchmarks can go down.

**Fix:** Pin model versions. Test before deploying. Self-host to control your upgrade schedule.

### 5. Verification Gap
"Does it compile?" ≠ "Does it work?" Need real API keys, browser automation, database queries — not mocks.

**Fix:** Give agents browser debugging, database query skills, log access, OTel traces, real API keys.

### 6. Safety
Ralph loops are safe when repo-contained with toolchain as judge. Dangerous with irreversible side effects (e.g., terraform destroy).

**Fix:** Review every plan manually for irreversible actions. Sandboxed code execution. Proper auth and RBAC.

## Key Takeaway

The stack is: Ollama → LiteLLM → SmolAgents/LangGraph → DeepEval → Mozilla cq → Dify/LangGraph. Start with a Ralph loop (bash `while true`), add layers as you scale. The harness matters more than the model. Build the judge node first. Track drift, not just errors. Self-host to control your upgrade schedule.

## Related Concepts
- [[Self-Improving AI Loops]]
- [[Feedback Loop Engineering]]
- [[Harness Engineering]]
- [[Drift Detection]]
- [[Model Version Brittleness]]
