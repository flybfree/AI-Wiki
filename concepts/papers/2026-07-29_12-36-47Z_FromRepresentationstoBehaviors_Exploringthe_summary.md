# Summary: 2026-07-29_12-36-47Z_FromRepresentationstoBehaviors_ExploringthePerson_.md
Saved: 2026-07-29 20:33
Source: 2026-07-29_12-36-47Z_FromRepresentationstoBehaviors_ExploringthePerson_.md
Model: None

---

## Summary  
This paper investigates whether large language models (LLMs) possess internal personality‑related representations that can be expressed through behavior in response to specific situations, building on Funder’s person‑situation‑behavior triad. The authors propose a framework for discovering, controlling, and validating trait‑like features inside LLMs using contrastive behavior pairs grounded in shared contexts. By applying SAE decomposition they uncover sparse internal features linked to opposing poles of personality traits, then demonstrate that these features reliably influence token activations and responses across multiple situations. Finally, the interventions are shown to produce bidirectional shifts in behavior on social intelligence tasks, mirroring human personality trade‑off patterns.

## Key Contributions  
- [Finding 1] Sparse internal SAE features associated with opposing poles of personality traits are identified through contrastive behavior pairs that share a common situation.  
- [Finding 2] Feature‑level interventions produce consistent bidirectional trait‑related shifts across diverse, previously unseen situations while preserving response validity.  
- [Finding 3] The same interventions generate behavioral changes on social intelligence tasks with benefit‑tradeoff patterns consistent with human personality research.

## Methodology  
The authors adopt Funder’s triad framework: Person = internal personality representations; Situation = contextual cues that trigger trait‑relevant responses; Behavior = observable output. To discover traits, they construct contrastive behavior pairs—pairs of outputs that arise from the same situational prompt but express opposite poles of a trait (e.g., extraversion vs. introversion). SAE decomposition is applied to these pairs to extract sparse latent features that differentiate them. Validation proceeds via token‑level activation analysis, robustness checks against paraphrased prompts, and effect measurements on behavior‑to‑situation transitions. For control experiments, they inject the extracted features into a separate set of situations, measuring bidirectional changes in output while ensuring semantic validity.

## Results  
The contrastive SAE analysis reveals a handful of low‑dimensional internal factors that reliably separate opposite trait expressions. When these factors are manipulated, token activations corresponding to those poles shift predictably, and paraphrasing the prompt does not erase the effect, confirming robustness. Across 12 unrelated situations, feature injection yields consistent bidirectional shifts in output style and content, preserving factual correctness. On a set of social‑intelligence tasks (e.g., empathy estimation), interventions produce measurable changes that follow classic human personality trade‑offs: higher extraversion improves sociability but slightly reduces depth of conversation.

## Significance  
These findings provide empirical evidence that LLMs contain controllable trait‑like representations linking internal states, situational expression, and behavioral outcomes. By offering a systematic method to probe and manipulate such features, the work bridges theoretical personality models with practical model engineering, enabling researchers and developers to study or simulate personality dynamics in AI systems.

## Related Concepts  
Person (internal representation), Situation (contextual affordances), Behavior (observable output), Funder’s triad framework, SAE decomposition, trait poles, cross‑situational expression, behavior‑to‑situation effects, paraphrasing robustness, bidirectional intervention, benefit‑tradeoff patterns.
