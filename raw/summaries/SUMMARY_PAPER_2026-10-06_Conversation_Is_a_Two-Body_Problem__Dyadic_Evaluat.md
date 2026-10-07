---
title: Conversation Is a Two-Body Problem: Dyadic Evaluation of Full-Duplex Dialogue Models
url: http://arxiv.org/abs/2610.08125v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_10-44-15Z_ConversationIsaTwo_BodyProblem_DyadicEvaluationofF.md
generated_at: 2026-10-06 21:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces DyaFDB, a dyadic evaluation framework for full-duplex spoken dialogue models, arguing that existing single-sided benchmarks assess only one half of interactive conversation. Instead of using pre-recorded audio or a fixed automated examiner, the framework lets two full-duplex models converse directly under assigned roles and cooperative or conflicting goals. The authors find that model behavior continuously reshapes the partner, so each model must serve as both examiner and examinee.

## Key Takeaways
- Existing evaluation setups are incomplete because pre-recorded audio cannot react and automated examiners administer fixed tests without being graded, leaving turn-taking, overlap, and interruption as unmeasured joint phenomena. DyaFDB addresses this by evaluating both sides of the interaction simultaneously rather than treating one participant as a static reference.
- The framework operationalizes conversation as a two-body problem by pairing models in self-play and cross-play configurations, assigning roles and goals, and scoring both participants offline with an external judge. This allows researchers to observe how each model adapts to the other's behavior rather than measuring isolated responses in a scripted setting.
- The authors instantiate four tasks across 140 scenarios and record 7,560 conversations, demonstrating that behavior in full-duplex dialogue is mutually constitutive. A fixed interlocutor cannot capture the dynamics because the partner being evaluated also changes the evaluation environment through its own timing, interruptions, and role behavior.

## Context
Full-duplex voice agents aim to listen and speak simultaneously, enabling lower latency and more natural interaction than turn-based systems. However, evaluation methods have lagged behind model capabilities, often reducing dialogue to scripted prompts or one-sided tests. This matters because conversational competence is relational, not just a property of a single model's output.

## Implications
For researchers, DyaFDB suggests benchmarks should measure mutual adaptation, role maintenance, interruption handling, and turn-taking in paired model interactions. For industry, it provides a more realistic protocol for testing voice agents that must operate with dynamic human or machine partners. For practitioners, releasing scenarios, role prompts, and recording protocols without pre-recorded audio may help standardize evaluation and expose weaknesses that single-sided tests miss.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.08125v1)
