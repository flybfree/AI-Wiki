---

title: "Summary: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks"
url: http://arxiv.org/abs/2604.22750v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-04-24_17-54-47Z_HowDoAIAgentsSpendYourMoney_AnalyzingandPredicting.md
generated_at: "2026-06-11 10:27"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-04-24 17-54-47Z Howdoaiagentsspendyourmoney Analyzingandpredicting


## Summary
This paper investigates how AI agents allocate and consume tokens during coding tasks, revealing that token usage is dominated by input rather than output and varies widely across models. It shows that while some models appear more efficient, all frontier LLMs struggle to predict their own token costs accurately.

## Key Takeaways
- Agentic tasks consume roughly 1000 times more tokens than simple code reasoning or chat, with input tokens driving the cost.
- Token usage is stochastic and can differ by up to 30x between runs on the same task, often peaking at intermediate costs before saturating.
- Models like Kimi-K2 and Claude-Sonnet-4.5 use significantly more tokens than GPT-5 on identical tasks.

## Context
The rapid deployment of AI agents in workflows has led to an explosion in LLM token consumption, yet existing research lacks systematic analysis of where these tokens are spent and how models behave under variable conditions.

## Implications
Understanding token economics helps industry stakeholders manage costs and developers design more efficient agentic systems. The findings also highlight the need for better cost‑prediction tools to align human expectations with actual computational effort.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2604.22750v1)
