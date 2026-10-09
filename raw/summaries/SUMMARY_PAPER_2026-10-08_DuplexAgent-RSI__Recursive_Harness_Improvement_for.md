---
title: DuplexAgent-RSI: Recursive Harness Improvement for Full-Duplex Voice Agent Collaboration
url: http://arxiv.org/abs/2610.11299v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_06-06-42Z_DuplexAgent_RSI_RecursiveHarnessImprovementforFull.md
generated_at: 2026-10-08 21:05
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
DuplexAgent-RSI presents a full-duplex voice agent collaboration system that combines continuous conversational interaction with asynchronous delegation of complex reasoning, search, and coding tasks through a modular harness of six editable components. The paper introduces a recursive self-improvement loop (Duplex-Harness-RSI) that automatically diagnoses collaboration failures from interaction traces and proposes targeted module repairs, demonstrating that this structured improvement process yields stronger spoken-knowledge and tool-execution performance than both the initial harness and unstructured repeated editing.

## Key Takeaways
- The core architectural insight is that a full-duplex voice model (supporting continuous listening and speaking) and a coding agent (capable of extended planning and execution) serve fundamentally different roles in a conversation, and bridging them requires an explicit coordination harness handling task acceptance, progress tracking, cancellation, replacement, and result delivery. DuplexAgent decomposes this coordination into six editable modules rather than relying on coupled heuristics, making each component independently diagnosable and improvable.
- The recursive self-improvement loop uses a simulator to generate timed test conversations, run the system, and produce failure traces that pinpoint which collaboration modules need repair. An Exam Planner selects the next tests based on observed weaknesses and a repair archive, while a Harness Editor proposes targeted module changes. This means the same reasoning LLMs and coding agents that serve the user also drive the system's own coordination improvement, creating a closed feedback loop.
- Experimental results across intelligence, agentic, and duplex benchmarks show DuplexAgent achieves stronger spoken-knowledge and executable-tool scores than compared delegated systems while maintaining strong interruption response. A harness ablation confirms that the modular, verifiable improvement loop with its diagnosis and repair archive outperforms both the initial harness and repeated editing that lacks structured diagnosis, validating that systematic evidence-driven revision is essential for harness quality.

## Context
This work sits at the intersection of full-duplex speech interaction research and agentic AI systems, addressing a practical convergence problem: voice assistants are increasingly expected to handle both fluid conversation and complex multi-step tasks, yet the underlying models for these two functions have incompatible interface assumptions. The modular harness approach and recursive self-improvement methodology connect to broader trends in self-improving AI systems, automated evaluation, and tool-augmented language models, offering a concrete blueprint for how coordination infrastructure can be treated as a first-class, improvable component rather than a fixed engineering artifact.

## Implications
For practitioners building voice-based assistants, this paper demonstrates that coordination logic between conversational and agentic capabilities can be systematically audited and improved through automated testing and targeted revision, reducing reliance on brittle hand-tuned heuristics. For the broader AI field, the recursive harness improvement loop suggests a general pattern for self-improving multi-agent systems: decompose coordination into verifiable modules, generate diagnostic traces, and use the same reasoning capabilities that serve end users to iteratively refine the system's own architecture. This approach could inform the design of future voice platforms, customer-service agents, and interactive coding assistants where responsiveness and task depth must coexist.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11299v1)
