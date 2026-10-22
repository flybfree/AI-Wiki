---
title: Asking What a Director Sees Can Change What Vision-Language Models Choose
url: http://arxiv.org/abs/2610.29318v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-21_07-21-08Z_AskingWhataDirectorSeesCanChangeWhatVision_Languag.md
generated_at: 2026-10-21 21:25
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper challenges a widely held assumption in theory-of-mind evaluation of vision-language models: that first asking a model to report what another person sees will not alter the model's subsequent action. Through a rendered Director Task in which a partition hides the largest block from a director, the authors demonstrate that inserting a perspective-reporting question before the action prompt dramatically shifts model behavior, causing models to choose the hidden block far more often despite correctly reporting the director's viewpoint. The authors provide a paired-prompt baseline design that any perspective-taking benchmark can adopt to control for this confound.

## Key Takeaways
- The common evaluation design—ask the model to report a person's perspective, then score its action—rests on the unexamined assumption that the report question leaves the action unchanged. The authors show this assumption is false: adding the perspective question raises the share of replies choosing the hidden block by 12 to 88 percentage points across six GPT models and by 17 percentage points on Qwen3.8-27B, even though the models correctly identify which blocks the director can see.
- Reasoning traces and prompt rewordings reveal the mechanism: the perspective question shifts how the model interprets the subsequent request, redirecting it from the director's viewpoint toward the model's own privileged viewpoint. This reframing effect means the model's "action" is no longer a clean measure of whether it can use the reported perspective.
- When the prompt explicitly states what the director knows and refers to—rather than eliciting a report first—fewer than 1% of replies pair a correct perspective report with a hidden-block choice, confirming that the confound is introduced by the elicitation step itself. The authors deliver a paired-prompt baseline that differs only in the presence of the perspective question, offering a reusable control for any perspective-taking benchmark.

## Context
Theory-of-mind evaluation has become a standard component of assessing vision-language models, with benchmarks routinely probing whether models can infer what another agent sees, knows, or intends. The dominant evaluation pattern—elicit a perspective report, then score the model's action—has been adopted across multiple benchmark suites without scrutiny of whether the elicitation step contaminates the action being measured. This paper sits at the intersection of model evaluation methodology and cognitive science, exposing a methodological blind spot that could inflate apparent failures of perspective integration in VLMs and mislead researchers about the true capabilities of these systems.

## Implications
For researchers building and evaluating perspective-taking benchmarks, this finding demands that every evaluation which elicits a report before scoring an action must include a matched baseline without the elicitation question, or risk attributing a prompt-framing artifact to a genuine failure of perspective integration. For practitioners deploying VLMs in multi-agent or human-AI interaction settings, the result warns that the way a question is structured can silently redirect a model's reasoning away from the user's intended perspective, with practical consequences for safety, alignment, and user trust. The paired-prompt design the authors provide offers a concrete, adoptable control that can be integrated into existing benchmark pipelines with minimal overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.29318v1)
