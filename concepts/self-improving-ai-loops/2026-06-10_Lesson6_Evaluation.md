---
title: "Lesson 6 — Evaluation & Verification: The Judge Node"
created: 2026-06-10
module: Self Improving AI Loops
lesson: 6
tags: [evaluation, verification, deepeval, arize-phoenix, promptfoo, drift-detection]
---

## Summary

Placeholder summary — please add a concise summary.


# Lesson 6: Evaluation & Verification — The Judge Node



**Source**: [Original Article](http://localhost:6006)

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-15-evaluation-overfitting-and-limits.md|AI/ML Foundations Lesson 15 - Evaluation, Overfitting, and Limits]] — 2 title terms overlap, shared tags: evaluation, 7 topic terms overlap
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson5_KnowledgeMemory.md|Lesson 5 — Knowledge & Memory: The Outer Loop]] — 2 title terms overlap, 7 topic terms overlap, same area: home
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson4_AgentFrameworks.md|Lesson 4 — Agent Frameworks: The Loop Engine]] — 2 title terms overlap, 7 topic terms overlap, same area: home

## Core Idea

**"Does it compile?" ≠ "Does it work?"** Verification is the gap between syntax and semantics. Your judge node needs to check that the agent's output actually works in a running system and fails gracefully — not just that it passes basic checks.

## The Verification Gap

Most self-hosted teams stop at:
- ✅ Code compiles
- ✅ Unit tests pass
- ✅ Linting is clean

But they miss:
- ❌ Does it work as part of the system?
- ❌ Does it handle edge cases?
- ❌ Does it fail gracefully?
- ❌ Is the output semantically correct?

## DeepEval: LLM-as-Judge Evaluation

**Definition:** An open-source LLM evaluation framework from Confident AI that uses LLMs to assess the quality of AI application outputs.

**Key metrics:**
- **Response quality** — Does the output meet the requirements?
- **Context relevance** — Is the agent using the right information?
- **Hallucination detection** — Is the agent making things up?

```python
from deepeval import test_case
from deepeval.metrics import HallucinationMetric, AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

# Define what "good" looks like
test = LLMTestCase(
    input="Implement user authentication",
    output=agent.run("Implement user authentication"),
    expected="JWT-based auth with refresh tokens"
)

# Run LLM-as-judge
hallucination_metric = HallucinationMetric(threshold=0.3)
answer_relevancy = AnswerRelevancyMetric(threshold=0.7)

hallucination_metric.measure(test)
answer_relevancy.measure(test)

print(f"Hallucination score: {hallucination_metric.score}")
print(f"Relevancy score: {answer_relevancy.score}")
```

**Self-hosted:** Yes, pip install
**Best for:** Python testing workflow, custom metrics, hallucination detection

## Arize Phoenix: Observability for Drift Detection

**Definition:** A self-hosted observability platform for tracking LLM outputs over time.

**The critical insight:** Analysis of 4M+ production agent calls shows that **drift** (not errors) is the most common failure mode.

### Four Types of Drift:
1. **Compliance drift** — Agent stops following its own rules
2. **Length drift** — Responses get longer or shorter over time
3. **Semantic drift** — Meaning of outputs shifts gradually
4. **Regression** — Performance drops on tasks that previously worked

**Most observability tools track error rates and latency. Almost none track semantic drift — the kind that actually destroys business value.**

```python
# Arize Phoenix tracks output distributions over time
from arize_phoenix import Client

client = Client(endpoint="http://localhost:6006")

# Log agent outputs
client.log(
    model_id="my-agent",
    predictions=[
        {"output": agent.run("task 1"), "timestamp": "2026-06-10T10:00:00Z"},
        {"output": agent.run("task 2"), "timestamp": "2026-06-10T10:05:00Z"},
    ]
)

# Check for drift
drift_report = client.get_drift_report(
    model_id="my-agent",
    metric="semantic_similarity",
    baseline="2026-06-01"
)
```

**Self-hosted:** Yes, Docker-based
**Best for:** Continuous monitoring, drift detection, output distribution tracking

## Promptfoo: CI Pipeline Evals

**Definition:** An open-source tool for running LLM evaluations in CI pipelines.

**Key features:**
- Run evals in CI before deploying
- Security checks
- Prompt versioning and A/B testing
- Compare prompt changes across versions

```yaml
# promptfooconfig.yaml
prompts:
  - "Implement ticket {{ticket_id}} from doc/tickets/"
  - "Implement ticket {{ticket_id}} from doc/tickets/ (v2)"

providers:
  - openai:gpt-4o
  - ollama:llama3.3

tests:
  - vars:
      ticket_id: 001
    assert:
      - type: contains
        value: "def authenticate"
      - type: llm-rubric
        value: "Code should handle invalid input gracefully"
```

```bash
# Run evals in CI
promptfoo eval

# Compare versions
promptfoo compare runs/2026-06-10 runs/2026-06-09
```

**Self-hosted:** Yes, pip install
**Best for:** CI/CD integration, prompt versioning, A/B testing

## MLflow: Experiment Tracking

**Definition:** An open-source platform for managing the ML lifecycle, including experiment tracking and model registry.

**Use for:** Tracking prompt experiments, comparing model versions, logging evaluation scores

```python
import mlflow

with mlflow.start_run():
    mlflow.log_param("model", "ollama/llama3.3")
    mlflow.log_param("prompt_version", "v2")
    mlflow.log_metric("hallucination_score", 0.15)
    mlflow.log_metric("relevancy_score", 0.82)
    mlflow.log_metric("drift_score", 0.03)
```

## The Judge Node Pattern

In LangGraph, the judge node is explicit:

```python
from langgraph.graph import StateGraph

def judge_node(state):
    """Judge node: checks if agent output meets criteria"""
    
    # 1. Run DeepEval metrics
    hallucination = check_hallucination(state.output)
    relevancy = check_relevancy(state.output, state.input)
    
    # 2. Run unit tests
    test_result = run_tests(state.output)
    
    # 3. Check for drift
    drift = check_drift(state.output)
    
    if hallucination.score > 0.3:
        return "fix_hallucination"
    if not test_result.passed:
        return "fix_tests"
    if drift > 0.1:
        return "alert_drift"
    return "pass"

# Add to graph
workflow.add_node("judge", judge_node)
workflow.add_conditional_edges(
    "judge",
    lambda s: judge_node(s),
    {"fix_hallucination": "agent", "fix_tests": "agent", "alert_drift": "alert", "pass": END}
)
```

## Verification Checklist

| Check | Tool | Frequency |
|-------|------|-----------|
| Code compiles | Compiler | Every run |
| Unit tests pass | pytest | Every run |
| Linting clean | ruff/flake8 | Every run |
| Hallucination check | DeepEval | Every run |
| Context relevance | DeepEval | Every run |
| Semantic drift | Arize Phoenix | Continuous |
| Output distribution | Arize Phoenix | Continuous |
| Prompt versioning | Promptfoo | Before deploy |
| A/B test results | Promptfoo | Before deploy |

## Key Takeaway

Build the judge node as a first-class component, not an afterthought. DeepEval for LLM-as-judge metrics. Arize Phoenix for drift detection. Promptfoo for CI evals. MLflow for experiment tracking. Track output distributions, not just error rates. The judge node is what turns a fragile agent into a self-correcting one.

## Related Concepts
- [[2026-06-10_Self-Improving-AI-Loops.md]]
- [[2026-06-10_Self-Improving-AI-Loops.md]]
- [[2026-07-26_LangChain_Harness_and_Loop_Engineering_References.md]]
- [[2026-06-10_Lesson8_DIYArchitecture.md]]
