---
title: h1: A Taste of the Bitter Lesson in Automated Theorem Proving
url: http://arxiv.org/abs/2610.35962v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-25_11-07-24Z_h1_ATasteoftheBitterLessoninAutomatedTheoremProvin.md
generated_at: 2026-10-27 22:47
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether a simple agentic loop that scales test-time compute can match the complex, human-designed workflows currently used in formal theorem proving, echoing the "Bitter Lesson" from AI research. The authors introduce h1, a minimal harness that provides a language model with an efficient interface to Lean 4 and relies solely on verifier feedback and self-reflection, without imposing decomposition or search structures. h1 achieves state-of-the-art results across multiple benchmarks and demonstrates that a single attempt (pass@1) can often solve open formal problems, challenging the assumption that elaborate orchestration workflows are necessary.

## Key Takeaways
- A simple agentic loop (h1) with an efficient Lean 4 interface and verifier feedback achieves state-of-the-art results on PutnamBench, FATE-X, and FormalConjectures100-Solved, and settles eight open problems in FormalConjectures, matching or outperforming specialized workflows like Goedel-Architect and AlphaProof Nexus at matched model scales. This suggests that the gains attributed to complex workflows may largely be confounded by stronger models or additional compute rather than the workflow structure itself.
- The paper demonstrates that pass@1 (a single attempt) can often scale to solve open formal problems, which challenges the prevailing assumption that multi-step decomposition, planning, and orchestration of specialized provers are essential for progress in formal verification. This finding directly parallels the Bitter Lesson from general AI: simple scaling of compute and feedback loops tends to outperform hand-engineered architectures.
- Through ablations and matched-model comparisons with Claude Code and AxProverBase, the authors find that simplicity alone is insufficient; the efficiency of the Lean interface is the critical factor determining both computational cost and solve rate. The interface design, rather than the reasoning architecture, is what makes the difference between a working and a failing system.

## Context
This paper sits at the intersection of two major trends in AI: the scaling of chain-of-thought reasoning in frontier language models for informal mathematics, and the growing demand for formal verification to keep pace with AI-generated research mathematics. The broader field has increasingly invested in elaborate multi-agent workflows, proof decomposition pipelines, and specialized prover orchestration to handle formal theorem proving. By directly testing whether these workflows provide genuine architectural advantages or merely benefit from confounded compute and model strength, this work applies the Bitter Lesson framework to a domain where it has not yet been rigorously tested, raising fundamental questions about where research effort should be directed.

## Implications
For practitioners and researchers in formal verification and AI-assisted mathematics, this paper recommends a critical methodological shift: evaluate frontier models with efficient execution feedback interfaces before prescribing complex workflows, to avoid attributing gains to architecture when they may stem from compute or model capability. For industry, the findings suggest that investing in high-quality tool interfaces (such as efficient Lean 4 bindings) may yield greater returns than engineering elaborate multi-agent orchestration systems. This could reshape how organizations allocate resources in building AI systems for formal reasoning, prioritizing interface quality and test-time compute scaling over bespoke workflow design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35962v1)
