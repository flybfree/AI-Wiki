---
title: CounselPlex: A Stressor-Aware Full-Duplex Counseling Model
url: http://arxiv.org/abs/2610.32702v1
type: paper-summary
date: 2026-10-25
source_paper: 2026-10-23_14-26-22Z_CounselPlex_AStressor_AwareFull_DuplexCounselingMo.md
generated_at: 2026-10-25 21:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
CounselPlex addresses a critical failure mode in full-duplex speech models used for counseling, termed "Stressor Blindness," where models fixate on the most recent utterance and lose track of the seeker's underlying problem. The proposed framework introduces two novel operations—updating a short stressor state during seeker silence and injecting it into <PAD> positions while listening—alongside a training augmentation technique called RoPE Position Shift Augmentation (RPSA). LLM-judge evaluations demonstrate that CounselPlex achieves improved counseling quality and stronger stressor grounding compared to strong baselines.

## Key Takeaways
- Stressor Blindness is identified as a fundamental failure mode in full-duplex counseling models: because these systems prioritize the latest utterance for responsiveness, they progressively lose awareness of the seeker's core problem over the course of a conversation, undermining therapeutic effectiveness. CounselPlex counters this by maintaining and updating a compact "stressor state" during periods of seeker silence, ensuring the model retains a persistent representation of the underlying issue rather than treating each turn as isolated.
- The framework injects the stressor state into <PAD> token positions during the listening phase, effectively embedding therapeutic context into the model's internal representation without disrupting the natural full-duplex flow of listening and speaking simultaneously. This mechanism allows the model to ground its responses in the seeker's actual problem rather than merely reacting to surface-level conversational content.
- RoPE Position Shift Augmentation (RPSA) is a training-time technique that broadens the positional encoding coverage of the model, enabling it to handle longer conversational turn depths more effectively. This augmentation improves performance in extended counseling sessions where the model must track context across many turns, a scenario where standard positional encodings degrade.

## Context
Full-duplex speech models represent a frontier in conversational AI, enabling simultaneous listening and speaking to achieve natural, low-latency interaction. While these models have shown promise in general dialogue tasks, their application to counseling introduces unique challenges because therapeutic conversations require sustained attention to a user's underlying emotional or psychological problem across many turns. CounselPlex bridges the gap between the technical capabilities of full-duplex architectures and the domain-specific demands of mental health support, addressing a failure mode that prior work had not formally characterized or mitigated.

## Implications
For practitioners in AI-assisted mental health services, CounselPlex offers a concrete architectural strategy for building counseling systems that remain therapeutically grounded over extended sessions, which is essential for trust and clinical effectiveness. For the broader full-duplex speech model community, the identification of Stressor Blindness and the introduction of RPSA provide transferable insights into how positional encoding and internal state management can be adapted for any domain requiring long-horizon contextual awareness, potentially informing future work in tutoring, negotiation, and other multi-turn advisory interactions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.32702v1)
