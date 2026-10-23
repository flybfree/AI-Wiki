---
title: Feedback That Backfires in Games: Do LLM Players Repeat the Move They Just Watched Fail?
url: http://arxiv.org/abs/2610.30205v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-21_12-29-30Z_FeedbackThatBackfiresinGames_DoLLMPlayersRepeatthe.md
generated_at: 2026-10-22 22:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether recording a failed move in an LLM agent's transcript actually helps the model avoid repeating that mistake in game-playing tasks. Across eight instruction-tuned models ranging from 135M to 1.7B parameters tested on Sokoban, Connect Four, and Othello, the authors find the opposite of the intended effect: the failure record makes the model more likely to repeat the failed action, yielding a negative corrective gain of −1.38 nats per token. The backfire is driven by the surface string of the move appearing in the transcript, and it affects illegal moves but not legal-but-losing moves, revealing a narrow and counterintuitive failure mode in how small language models process in-context feedback.

## Key Takeaways
- The failure record backfires through the move's surface form: when the exact failed move string appears in the transcript, the model's log-probability for that move barely depends on how likely it was before the record (slope 0.18), meaning the model essentially "locks in" the error. Moves the model would not have played become more likely, and greedy decoding begins producing them, while moves the model was about to play become less likely yet are still repeated 38% of the time under greedy decoding.
- The backfire is format- and training-stage-dependent. Along the OLMo 2 1B post-training ladder, the inversion is present in the base model and largely removed at the DPO stage, suggesting that preference-tuning partially mitigates the problem. RAGEN's default models also invert in RAGEN's own Sokoban format before any reinforcement learning is applied. Crucially, a description of the failure that omits the move string preserves the model's original preference, isolating the surface-form token as the causal mechanism.
- Common harness mitigations fail. A "do not repeat" instruction has no measurable effect, a clean retry (removing the failed turn entirely) is the worst harness option, and a decoder-level ban on exact repeats stops verbatim repetition but does not prevent the model from producing other illegal moves. This means naive prompt engineering and decoding constraints are insufficient fixes.

## Context
This work sits at the intersection of LLM agent design, in-context learning, and small-model behavior in structured decision tasks. As LLM agents are increasingly deployed in tool-calling pipelines, coding assistants, and game-playing benchmarks, the standard harness pattern of appending a failed action and its error message to the transcript is nearly universal. Prior work in tool calling had already hinted that this pattern can backfire for small models, but the mechanism and its generalization to game environments—where failures can be illegal moves or legal-but-suboptimal moves—had not been rigorously tested. By using fixed probe items built by perturbing a correct move and verifying outcomes exactly, the paper provides a controlled, reproducible measurement (run in float32 on a free Colab GPU) that isolates the causal role of the move string in the transcript.

## Implications
For practitioners building LLM agent harnesses, the findings challenge the near-universal assumption that showing a model its mistake and asking it to try again is beneficial. The results suggest that harness designers should avoid including the exact failed action string in the transcript and instead describe failures abstractly, or rely on preference-tuning stages like DPO to suppress the inversion. For the broader field, the paper highlights that small instruction-tuned models remain vulnerable to surface-form anchoring in multi-turn interactions, a concern that extends beyond games to any agentic system where tool calls or actions are echoed back after failure. It also underscores that decoder-level constraints and explicit "do not repeat" instructions are inadequate safeguards, pointing toward the need for architectural or training-level solutions rather than prompt-level patches.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30205v1)
