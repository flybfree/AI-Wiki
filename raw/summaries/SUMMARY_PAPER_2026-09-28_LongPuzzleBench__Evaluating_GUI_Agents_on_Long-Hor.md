---
title: LongPuzzleBench: Evaluating GUI Agents on Long-Horizon Visual Puzzles
url: http://arxiv.org/abs/2609.34769v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_09-49-25Z_LongPuzzleBench_EvaluatingGUIAgentsonLong_HorizonV.md
generated_at: 2026-09-28 22:53
model: qwen3.6-35b-a3b
---

## Summary
LongPuzzleBench introduces a benchmark comprising 114 levels across six puzzle games to evaluate GUI agents on long-horizon visual reasoning using native GUI actions. The study reveals that while current agents handle short objectives well, their performance degrades sharply on longer boards where early moves can create unannounced dead ends, exposing a fundamental inability to maintain multi-step coherence under delayed feedback constraints.

## Key Takeaways
- LongPuzzleBench features persistent boards and hidden failure states requiring over a thousand human actions for complex objectives; seven of ten general-purpose agents fail on anything harder than Medium difficulty, and none complete the "Bolt Unscrew Hard" objective despite humans solving it effortlessly.
- Code Execution CUA fails to close the performance gap because its scores conflate visual problem-solving with algorithmic search, indicating that current methods do not genuinely improve long-horizon GUI navigation capabilities.
- Controlled diagnostics identify a core limitation: agents evaluate moves based on immediate visible progress rather than the future options they preserve, and this flaw persists even when rules, state hints, or failure memory mechanisms are introduced.

## Context
Existing benchmarks for computer use and game play rarely test whether agents can sustain coherent plans across long chains of coupled decisions where early actions constrain later possibilities. This work addresses a critical gap by providing a rigorous evaluation framework that directly measures an agent's ability to reason about delayed consequences and maintain solvability over extended interaction sequences in dynamic interfaces.

## Implications
The results indicate that advancing GUI agents requires shifting focus from reactive progress optimization to strategies that explicitly value future optionality and state preservation. Developers must address the tendency of current models to make locally optimal moves that lead to global dead ends, suggesting a need for new training objectives or architectural changes that incorporate forward-looking reasoning about long-term solvability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34769v1)
