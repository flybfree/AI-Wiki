---
title: Sanzaru: Benchmarking Protocol Formation under Epistemic & Communication Asymmetry
url: http://arxiv.org/abs/2610.15163v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-10_20-25-34Z_Sanzaru_BenchmarkingProtocolFormationunderEpistemi.md
generated_at: 2026-10-13 21:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SANZARU is a benchmark that tests whether language models capable of solving tasks individually can coordinate as a team when each member has restricted access to information and communication channels. Drawing on cooperative bomb-defusal puzzles adapted from BOMBANANA!, the benchmark assigns three agents distinct sensory or communicative disabilities—one cannot hear, one cannot speak, and one cannot see—and evaluates their ability to form shared protocols to complete 120 puzzle instances spanning seven coordination families. Across 1512 episodes with seven models, the overall team success rate is 49%, and trace analysis reveals that roughly 60% of team failures stem from communication breakdowns rather than task reasoning errors.

## Key Takeaways
- Individual model competence does not guarantee team success: even models scoring well on solo tasks achieve team success rates as low as 20% when information and action authority are asymmetrically distributed among agents, highlighting a critical gap between solo reasoning and collaborative coordination.
- Teams spontaneously invent heterogeneous communication protocols ranging from simple gesture codes to Morse code and full manual encodings, demonstrating that language models can bootstrap ad hoc coordination languages, but these emergent protocols are fragile and often incompatible with teammates' actual capabilities.
- Approximately 60% of the 771 recorded team losses are directly attributable to communication failures, and agents frequently attempt to use channels (such as speaking or seeing) that are explicitly unavailable to their teammates despite clear role instructions, indicating a persistent failure of perspective-taking and theory-of-mind reasoning during multi-agent cooperation.

## Context
This work sits at the intersection of multi-agent systems, embodied communication, and theory-of-mind evaluation in large language models. While prior benchmarks such as BOMBANANA! and various cooperative game suites test coordination under symmetric information, SANZARU introduces deliberate epistemic and communicative asymmetry to probe whether models can adapt their communication strategies to teammates' actual perceptual and expressive limitations. The benchmark thus extends the evaluation frontier from "can a model reason?" to "can a model reason about what its partner can and cannot perceive or express?"

## Implications
For practitioners building multi-agent LLM pipelines in robotics, human-AI collaboration, or distributed decision-making, SANZARU demonstrates that simply assigning roles in a prompt is insufficient; models must be explicitly trained or prompted to model their teammates' channel constraints, or teams will default to communication modes that exclude critical partners. For the broader AI research community, the finding that 60% of failures are communication-attributable rather than reasoning-attributable suggests that future multi-agent benchmarks and training objectives should prioritize perspective-taking and channel-aware protocol design as first-class evaluation targets, not secondary considerations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.15163v1)
