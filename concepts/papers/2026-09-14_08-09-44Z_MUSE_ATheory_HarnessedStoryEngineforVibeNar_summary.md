# Summary: 2026-09-14_08-09-44Z_MUSE_ATheory_HarnessedStoryEngineforVibeNarrativiz.md
Saved: 2026-09-14 22:32
Source: 2026-09-14_08-09-44Z_MUSE_ATheory_HarnessedStoryEngineforVibeNarrativiz.md
Original paper: http://arxiv.org/abs/2609.15188v1
Model: None

---

## Summary
This paper introduces MUSE, a novel "Theory-Harnessed Story Engine" designed to address the persistent challenges of generating high-quality narratives using Large Language Models (LLMs). The authors define "Vibe Narrativizing" as the specific task of translating natural-language writing requirements into cohesive finished stories, aiming to overcome bottlenecks in story guidance and its sustained application. By structuring story knowledge through rule atomization and semantic consolidation, MUSE provides a single source of truth that guides decisions across planning, drafting, and revision phases. The system demonstrates significant improvements in narrative consistency and quality over zero-shot baselines, leveraging both theoretical frameworks and intermediate deliverables to maintain creative integrity.

## Key Contributions
- **Introduction of Vibe Narrativizing**: The authors formalize a new task framework for converting natural language prompts into structured stories, addressing the disconnect between high-level writing requirements and low-level prose generation.
- **Theory-Harnessed Architecture**: MUSE integrates Robert McKee’s story theory through rule atomization and mechanism abstraction, creating a layered disclosure system that organizes guidance for specific creative decisions without overwhelming the model.
- **Agent Harness with Intermediate Deliverables**: The system employs an agent harness that preserves story decisions through intermediate outputs (design, character performance, scene composition), ensuring consistency across long-form narratives and reducing error density significantly compared to baselines.

## Methodology
The authors approached the problem by engineering a structured pipeline that separates story knowledge from generative prose. They developed Robert McKee’s narrative theory into atomic rules and semantic consolidations, creating a "single source of truth" for guidance. This guidance is organized via layered disclosure, where context-specific examples complement abstract principles. The core methodology involves an "agent harness" that manages design, character performance, scene composition, and revision through intermediate deliverables. These deliverables act as checkpoints to preserve story decisions throughout the creative process. Additionally, context engineering ensures each role receives relevant guidance, while a masterwork corpus provides inspiration and prose references. This structure allows the model to track thematic roles from initial requests to climactic actions, maintaining coherence across complex plotlines.

## Results
Experimental evaluations across four base LLMs show that MUSE improves scores on WritingBench by 1.6 to 4.8 points over zero-shot generation. Furthermore, it raises LongStoryEval scores by more than ten points in three distinct categories. Crucially, ConStory-Bench consistency error density remained in the low single digits for all tested models, outperforming every reproduced story-system baseline on three metrics. The study also identified that structural design contributes most to quality improvements, while voice-specific effects are prominent in character paths, with further gains observed during the revision phase.

## Significance
This research matters because it moves beyond simple text generation to address the structural and logical consistency required for long-form storytelling. By harnessing established narrative theories into an actionable engine, MUSE provides a reproducible framework for enhancing LLM creativity. It demonstrates that structured guidance and intermediate decision preservation are critical for reducing inconsistencies in AI-generated narratives, offering a scalable path toward more reliable creative AI tools.

## Related Concepts
- Large Language Models (LLMs)
- Narrative Theory (Robert McKee)
- Story Consistency
- Agent Harnesses
- Vibe Narrativizing
- Rule Atomization
- LongStoryEval
