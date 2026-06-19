---

title: "Gaze Heads: How VLMs Look at What They Describe"
published: "2026-06-12T17:59:57Z"
authors: Rohit Gandikota, David Bau
url: http://arxiv.org/abs/2606.14703v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Gaze Heads: How VLMs Look at What They Describe



**Source**: [Original Paper](http://arxiv.org/abs/2606.14703v1)
## Abstract
How a vision-language model internally solves the task of describing an image is far from obvious. We find that the model develops a specific mechanism for this: a small set of attention heads in its language-model backbone, which we call gaze heads, whose attention tracks the image region the model is currently describing. We find them with a simple correlation score from a few forward passes, using comic strips as a controlled testbed where narrative order is laid out spatially. These gaze heads do not just track the image tokens being described: redirecting their attention to a chosen region forces the VLM to describe that region instead. A single attention-mask intervention on the top-100 gaze heads, fewer than 9% of all heads, steers the model's answer to any chosen comic panel at 83.1% accuracy, while the same intervention on random heads fails to redirect the answer, and intervening on all heads destroys generation. The same lever also extends to continuous control: switching the gaze target mid-generation makes the model wrap up its current panel description and move to the new one within a few tokens. Beyond comics, the same intervention redirects answers to chosen regions in natural COCO images. The mechanism further recurs across model sizes from 2B to 32B parameters and across other VLM architectures, although some frozen-encoder families show no comparable head set. More broadly, this shows that targeted edits identified through mechanistic analysis can serve as practical inference-time levers for steering multimodal model behavior, without any retraining. Our code, interactive demo, and datasets are available at https://gaze.baulab.info/

## Metadata
- **Published**: 2026-06-12T17:59:57Z
- **Authors**: Rohit Gandikota, David Bau
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.14703v1)