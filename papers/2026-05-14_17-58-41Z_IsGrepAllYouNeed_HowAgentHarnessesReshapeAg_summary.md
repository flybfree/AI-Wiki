---
title: "Summary: 2026-05-14_17-58-41Z_IsGrepAllYouNeed_HowAgentHarnessesReshapeAgenticSe.md"
date: 2026-05-14
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-14_17-58-41Z_IsGrepAllYouNeed_HowAgentHarnessesReshapeAgenticSe.md


**Source**: [Original Paper](http://arxiv.org/abs/2605.15184v1)
Saved: 2026-05-15 00:02
Source: 2026-05-14_17-58-41Z_IsGrepAllYouNeed_HowAgentHarnessesReshapeAgenticSe.md
Model: None

---

## Summary
This paper investigates the critical yet under-explored interaction between retrieval strategies and agent architectures in agentic search systems. The authors conduct a systematic empirical study to determine whether traditional keyword-based retrieval (grep) outperforms modern semantic vector retrieval in complex, multi-step agent workflows. By utilizing a custom agent harness named Chronos alongside provider-native CLI tools, the study evaluates performance across varying tool-calling paradigms and levels of contextual noise. The research aims to fill the gap in literature regarding how practical dimensions, such as output presentation and distractor resistance, influence the efficacy of LLM agents.

## Key Contributions
- The study provides a rigorous comparative analysis demonstrating that grep-based retrieval generally achieves higher accuracy than vector-based retrieval when used within specific agentic loops, challenging the assumption that semantic search is universally superior for tool-use scenarios.
- It reveals that the choice of agent harness and the specific style of tool-calling (inline results versus file-based reading) significantly impact performance, often outweighing the impact of the retrieval method itself.
- The paper introduces a novel experimental design that progressively increases contextual noise by mixing unrelated conversation history, thereby quantifying the robustness of different retrieval strategies against distracting material.

## Methodology
The authors organized their empirical study into two distinct experiments. Experiment 1 utilized a 116-question sample from the LongMemEval dataset to compare grep and vector retrieval methods. This comparison was executed using a custom-built agent harness called Chronos, as well as provider-native CLI harnesses including Claude Code, Codex, and Gemini CLI. The experiment specifically tested two modes of tool result presentation: inline tool results provided directly in the context window and file-based tool results where the model reads separate files. Experiment 2 focused on robustness by comparing grep-only and vector-only retrieval while progressively injecting additional, unrelated conversation history. This allowed the researchers to measure how well each strategy maintained performance as the signal-to-noise ratio decreased due to increasing distractors.

## Results
The experimental results indicate that grep generally yields higher accuracy than vector retrieval across the tested harnesses in Experiment 1. However, the study highlights that overall scores are strongly dependent on the specific harness and tool-calling style employed, even when the underlying conversation data remains identical. In Experiment 2, the performance degradation due to irrelevant surrounding text varied significantly between grep and vector methods, suggesting that grep may offer better resilience in certain noisy contexts, although the absolute performance remains tied to the agent's architectural implementation.

## Significance
This research is significant because it challenges the prevailing trend of blindly adopting vector retrieval for all agentic tasks. It provides practical guidance for developers by showing that the choice of retrieval strategy must be tightly coupled with the agent architecture and tool interface. Understanding these interactions helps in designing more efficient and accurate agentic systems, particularly in environments where computational efficiency or specific text-matching precision is required.

## Related Concepts

- [[concepts/ai-agents/agentic-workflows-hub.md|Agentic Workflows Hub]]
- [[concepts/software-development/software-development-hub.md|Software Development Hub]]
- [[concepts/llm-models/llm-models-hub.md|LLM Models Hub]]
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation Benchmarks Hub]]
