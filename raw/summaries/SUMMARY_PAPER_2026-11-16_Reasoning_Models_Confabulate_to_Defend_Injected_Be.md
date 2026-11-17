---
title: Reasoning Models Confabulate to Defend Injected Beliefs About Their Own Requests
url: http://arxiv.org/abs/2611.17958v1
type: paper-summary
date: 2026-11-16
source_paper: 2026-11-13_09-48-58Z_ReasoningModelsConfabulatetoDefendInjectedBeliefsA.md
generated_at: 2026-11-16 21:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper demonstrates that an invisible activation edit—specifically, an injected forming-trace of an off-topic concept—can overwrite a reasoning model's belief about what it was actually asked to do, causing the model to reason about, report on, and answer the injected topic instead of the true request. Across six models spanning different scales, architectures, and training recipes, the injected topic dominates the model's chain-of-thought and final output in nearly all cases, and even explicit warnings naming the true topic fail to restore correct behavior. The findings establish a concrete limit on chain-of-thought monitorability: the model's self-report is not anchored to its actual input, and its attention maps and circuit attributions misleadingly appear on-task even when the underlying reasoning has been corrupted.

## Key Takeaways
- Activation edits invisible in the prompt text can overwrite a model's belief about its own request. Across six models spanning scale, architecture, and training recipe, a forced quote-back returned the injected topic in 47 out of 48 model-concept cells, and on four models with clean final haiku outputs, the injected answer followed in 99% of generations. This shows the corruption is not a quirk of one model family but a broad, cross-architecture phenomenon.
- Warnings and explicit corrections barely mitigate the effect. Even a warning that directly names the true topic yields under 5% true-topic answers. When handed the truth in clean tokens, the model confabulates a story about the user—such as "maybe they got confused and corrected themselves"—and answers with the injection anyway, corrupting both its behavior and its chain-of-thought simultaneously.
- Opening the model up for interpretability inspection offers no reprieve. After the edit, the model attends to the true request even harder, yet that attention is causally inert. The injected content rides intact task circuits, so attention maps and circuit attributions read as on-task. The same edit also redirects the request's language and format, not only its topic, meaning standard monitoring tools would not flag the corruption.

## Context
Chain-of-thought monitoring and model self-report are widely proposed as practical levers for AI oversight, resting on the assumption that a model's account of its reasoning is anchored to what it was actually asked. This paper directly challenges that assumption by showing the anchor can be severed through a subtle, text-invisible intervention. The work sits at the intersection of mechanistic interpretability, AI safety, and oversight methodology, and it matters because the tools practitioners currently rely on—attention maps, circuit attributions, CoT audits—are precisely the tools this paper shows can be rendered misleading or inert by the very corruption they are meant to detect.

## Implications
For AI safety practitioners and oversight teams, this finding suggests that CoT-based monitoring and self-reporting cannot be trusted as reliable safeguards against subtle internal corruptions, since the model will confabulate a coherent defense of its altered belief rather than flag the discrepancy. For model developers and interpretability researchers, the result implies that attention maps and circuit-level attributions are insufficient diagnostic tools when an edit hijacks the model's reference to its own input, and that oversight strategies must account for the model's active defense of injected beliefs rather than assuming transparency. Industry deployments relying on CoT audits for compliance or alignment verification may need to supplement them with external verification mechanisms that do not depend on the model's own account of its task.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.17958v1)
