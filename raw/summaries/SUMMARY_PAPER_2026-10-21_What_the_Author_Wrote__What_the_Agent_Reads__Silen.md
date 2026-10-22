---
title: What the Author Wrote, What the Agent Reads: Silent Cue Loss in Enterprise Document Ingestion
url: http://arxiv.org/abs/2610.30026v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-21_16-51-25Z_WhattheAuthorWrote_WhattheAgentReads_SilentCueLoss.md
generated_at: 2026-10-21 23:06
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper demonstrates that mainstream enterprise document ingestion pipelines (such as docling and plain-text extraction) silently discard the visual formatting cues—specifically text highlighting and colour—that authors use to signal which requirements are mandatory. The authors construct a benchmark from 76 real policy documents scored against OOXML metadata and show that formatting-blind ingestion collapses requirement-recovery performance from a micro F1 of 0.690 down to 0.150 or 0.075, producing agents that are confidently wrong rather than transparently incomplete.

## Key Takeaways
- The performance gap is not a model-reasoning failure but an ingestion failure: across six answering models (five Claude tiers and GPT-5.6), the same degradation appears, proving the bottleneck is the converter layer that strips formatting before the agent ever sees the text. Docling's false-positive rate on unflagged requirements is four times the authors' deterministic matcher, showing agents hallucinate obligations when cues vanish.
- A span-level leave-one-out analysis localises the damage to exactly two cues—highlight (+0.302 F1) and colour (+0.262 F1), both Holm-adjusted at p < 1e-4—while bold, italic, monospace, and strikethrough contribute essentially nothing (within ±0.003 of zero). Colour is the cue no mainstream converter preserves and no parsing benchmark evaluates, yet 32.8% of 6,460 sampled documents carry a deliberate colour or highlight, with 10.3% marking an obligation.
- A pre-registered intervention test shows that explicitly typing the cue into the agent's prompt adds +0.085 F1 beyond merely preserving the formatting in the pipeline (Holm-adjusted p = 0.049), and labels are validated against rendered page images through an independent visual modality (inter-rater kappa = 0.72), bounding what pure wording can achieve at AUC 0.664.

## Context
As enterprise AI agents move from chat demos into compliance, policy enforcement, and ticket-filing workflows, the ingestion layer that converts Word files, PDFs, and OOXML documents into token sequences becomes the critical trust boundary. Prior work on document understanding benchmarks has focused on layout parsing or table extraction, but this paper isolates a previously unmeasured failure mode: the semantic meaning encoded in how text *looks* rather than what it *says*. By scoring against the file's own OOXML properties with a deterministic matcher and no LLM judge, the authors sidestep the circularity of model-evaluating-model and expose a gap that existing parsing benchmarks are structurally blind to.

## Implications
For agent builders and enterprise platform teams, the practical finding is that reliability is won or lost at ingestion, not at the reasoning or prompting stage, and the fix is cheap and measurable: preserve highlight and colour metadata through the converter, or inject explicit cue annotations into the agent's context window. For the broader field, the paper argues that document-understanding benchmarks must score colour and highlight preservation as first-class metrics, and that enterprise deployments should audit their ingestion pipelines for silent cue loss before attributing errors to model capability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30026v1)
