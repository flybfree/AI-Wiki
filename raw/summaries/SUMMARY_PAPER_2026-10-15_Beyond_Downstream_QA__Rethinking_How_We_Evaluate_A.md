---
title: Beyond Downstream QA: Rethinking How We Evaluate Agent Memory
url: http://arxiv.org/abs/2610.22209v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_16-58-12Z_BeyondDownstreamQA_RethinkingHowWeEvaluateAgentMem.md
generated_at: 2026-10-15 22:13
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper challenges the dominant evaluation paradigm for agent memory systems, which relies on downstream question-answering accuracy as a proxy for memory quality. The authors demonstrate that this approach conflates memory correctness with retrieval and generation quality, producing misleading results in both directions. They introduce FEB-30, a benchmark built through paradigm inversion—generating documents from known fact trajectories—to enable direct inspection of memory stores and reveal failures invisible to traditional evaluation methods.

## Key Takeaways
- The current evaluation paradigm produces both false positives (correct responses masking broken memory) and false negatives (incorrect responses blaming correct memory for retrieval failures), meaning downstream QA accuracy is fundamentally an incomplete and unreliable proxy for actual memory quality. This conflation of memory correctness with retrieval and generation quality undermines the validity of existing benchmarks.
- FEB-30 introduces 30 fact-evolution trajectories spanning 6 diagnostic categories and 3 difficulty levels, constructed via paradigm inversion where documents are generated from known fact trajectories to yield deterministic ground truth without human annotation. Each trajectory defines how a fact should evolve across multi-author artifacts including documents, emails, and conversations, enabling direct inspection of the memory store after each ingestion step rather than relying on end-to-end QA performance.
- Applying FEB-30 to a representative memory system reveals that intrinsic and extrinsic evaluation diverge by an average of 16 percentage points, with 44% of trajectories exceeding meaningful divergence thresholds. Diagnostic decomposition shows the system correctly classifies memory operations (create, update, reinforce, supersede) only 20% of the time—a failure entirely invisible to extrinsic evaluation—and that failure modes differ systematically by category and difficulty level.

## Context
As AI agents increasingly rely on persistent memory to maintain context across long interactions, multi-session conversations, and multi-document workflows, the reliability of their memory systems becomes a critical infrastructure concern. The broader field has largely adopted end-to-end QA benchmarks as the standard for evaluating these systems, assuming that accurate answers imply accurate memory. This paper sits at the intersection of retrieval-augmented generation research, agent architecture design, and evaluation methodology, addressing a gap that affects virtually every deployed agent system. By exposing the structural blind spots in current evaluation, it reframes how the community should think about memory correctness as a distinct, measurable property separate from retrieval and generation performance.

## Implications
For practitioners building and deploying agent systems, this work signals that current benchmark scores may substantially overstate or understate actual memory reliability, meaning production systems could harbor undetected memory corruption that only manifests under specific fact-evolution scenarios. For the research community, the release of FEB-30, its document generation pipeline, and scoring framework provides a reproducible tool for intrinsic memory evaluation that can complement existing extrinsic benchmarks. Industry teams should consider adopting diagnostic decomposition of memory operations—classifying create, update, reinforce, and supersede actions—as a standard part of their evaluation pipeline, since a 20% correct classification rate on these operations represents a fundamental architectural failure that no amount of downstream QA testing would surface.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22209v1)
