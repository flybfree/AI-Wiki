---
title: Position, Role or Label? A Controlled Study of Instruction Conflicts in LLM Agents
url: http://arxiv.org/abs/2610.33201v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-23_18-48-27Z_Position_RoleorLabel_AControlledStudyofInstruction.md
generated_at: 2026-10-26 20:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how LLM agents resolve conflicting instructions arriving from multiple sources such as system prompts, user messages, tool outputs, and saved memory. The authors construct a controlled benchmark called WhoWins containing 1,080 code-scored scenarios across five task types, then evaluate 14 open-weight models ranging from 0.6B to 122B parameters across nearly 1.9 million scored replies. The central finding is that instruction position within a single message dominates conflict resolution far more than the nominal source hierarchy, and that labeling a message as a user instruction can override its structural placement in the system or developer slot.

## Key Takeaways
- Position within a single message is the dominant factor in instruction conflict resolution: the first of two conflicting lines wins between 72.42% and 94.66% of the time inside one message, while across separate messages the advantage drops to 22.95%–62.65%, showing that intra-message ordering is far more decisive than inter-message ordering.
- The nominal instruction hierarchy (system > developer > user) does not hold in practice: a policy placed first in the system or developer message loses most conflicts with later lines in every Qwen model, and in tool and file-write tasks it wins less often than the identical text delivered as a labelled user message across every model and thinking mode tested.
- Models almost never acknowledge or hedge when they encounter conflicting instructions: by the authors' keyword-pattern detection, at most 2.92% of decided pair replies flag or hedge the conflict, meaning agents silently pick a winner without surfacing the ambiguity to the operator.

## Context
Instruction-hierarchy benchmarks in the LLM-agent literature typically treat a source's position, role, and label as a single bundled variable, making it impossible to isolate which factor actually drives conflict resolution. This paper is significant because it is the first controlled study that decouples delivery position, role assignment, and explicit labeling across a large model sweep, revealing that the community's assumed hierarchy is largely an artifact of how instructions are formatted rather than a genuine architectural guarantee. The scale of the evaluation—14 models, 1.9 million replies, held-out validation—sets a new methodological bar for instruction-following robustness research.

## Implications
For practitioners building agentic pipelines, these findings mean that simply placing a policy in the system or developer slot provides no reliable guarantee of compliance; the ordering of lines within a message and the explicit label attached to a message are stronger levers for controlling agent behavior. Industry teams deploying multi-source agent systems should treat instruction placement as a first-class engineering concern, audit for silent conflict resolution, and consider adding explicit conflict-flagging mechanisms since current models almost never surface ambiguity on their own.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33201v1)
