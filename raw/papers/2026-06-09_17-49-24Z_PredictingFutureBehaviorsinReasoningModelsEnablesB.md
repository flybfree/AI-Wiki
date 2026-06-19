---

title: Predicting Future Behaviors in Reasoning Models Enables Better Steering
published: "2026-06-09T17:49:24Z"
authors: Evgenii Kortukov, Piotr Komorowski, Florian Klein, Paula Engl, Gabriele Sarti, Seong Joon Oh, Sebastian Lapuschkin, Wojciech Samek
url: http://arxiv.org/abs/2606.11172v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Predicting Future Behaviors in Reasoning Models Enables Better Steering



**Source**: [Original Paper](http://arxiv.org/abs/2606.11172v1)
## Abstract
Deployed large reasoning models (LRMs) often behave unexpectedly. Test-time steering controls LRM outputs by intervening on their hidden representations, but it can degrade output quality. We argue that prior steering work implicitly relies on internal features that detect behavior in already generated text. We show that these detection features are poor predictors of future behavioral outcomes, and thus not the natural intervention target. Instead, we train activation probes to predict future behavior likelihoods from intermediate reasoning steps. These probes predict the most likely behavior with 64%-91% accuracy, revealing a separate type of internal prediction features. Building on these prediction features, we introduce a text-level steering method, Future Probe Controlled Generation. FPCG samples multiple candidate sentences and chooses the best one according to a probe predicting the future behavior likelihood. This enables steering with almost no output quality degradation. FPCG also enables steering in several evaluations where activation steering fails. These results show that distinguishing detection and prediction features enables a more nuanced approach to controlling LRM behaviors.

## Metadata
- **Published**: 2026-06-09T17:49:24Z
- **Authors**: Evgenii Kortukov, Piotr Komorowski, Florian Klein, Paula Engl, Gabriele Sarti, Seong Joon Oh, Sebastian Lapuschkin, Wojciech Samek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.11172v1)