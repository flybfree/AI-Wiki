---

title: Failed Reasoning Traces Tell You What Is Fixable (But Not by Reading Them)
published: "2026-06-03T17:50:26Z"
authors: Nizar Islah, Istabrak Abbes, Irina Rish, Sarath Chandar, Eilif B. Muller
url: http://arxiv.org/abs/2606.05145v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Failed Reasoning Traces Tell You What Is Fixable (But Not by Reading Them)



**Source**: [Original Paper](http://arxiv.org/abs/2606.05145v1)
## Abstract
When post-trained language models fail on reasoning problems, the common test-time-scaling response is to spend more compute on additional attempts, and the failed traces play no further role. We argue this discards a crucial signal; some failures come from unlucky sampling, where more rollouts help, while others are structural and resist resampling regardless of budget. We propose that failed traces encode recoverability structure: the inference-time signature of which test-time interventions can rescue a given failure. Three problem-level trajectory features, derived from the structure of available interventions, recover this structure from the distributional signature of failed rollouts, not their text. They cluster failures into stable regimes, characterize the failure topography of different post-training methods ($84.3{\pm}4.3\%$ accuracy, $+20\%$ over a majority-class baseline), and support a training-free routing rule that lifts rescue by $+12.2\%$ on the deployment-relevant Steerable-Hard subset (failures where retry is insufficient and a bounded intervention is reachable). The features and the routing rule transfer across two cross-family probes. The same three features thus convert failed traces from discarded data into a diagnostic object, supporting test-time routing and post-training analysis without training-time or weight-space access.

## Metadata
- **Published**: 2026-06-03T17:50:26Z
- **Authors**: Nizar Islah, Istabrak Abbes, Irina Rish, Sarath Chandar, Eilif B. Muller
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.05145v1)