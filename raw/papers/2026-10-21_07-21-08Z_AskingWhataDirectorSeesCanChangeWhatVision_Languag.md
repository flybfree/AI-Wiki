---
title: Asking What a Director Sees Can Change What Vision-Language Models Choose
published: 2026-10-21T07:21:08Z
authors: Jiaxuan Guo, Xingyu Ren, Kejia Zhang, Jingxin Yang, Youran Sun, Haizhao Yang
url: http://arxiv.org/abs/2610.29318v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Asking What a Director Sees Can Change What Vision-Language Models Choose

## Abstract
Vision-language models are now routinely tested on theory of mind: whether they can work out what another person sees, knows, and means. A common design asks the model to report that perspective and then to act for the person, and reads a correct report beside a wrong action as a failure to use the perspective. That reading rests on a quiet assumption: that asking for the report leaves the action unchanged. We show that it does not. In a rendered Director Task, a partition hides the largest block from a director who asks for "the largest block". Asking first which blocks the director can see raises the share of replies that choose this hidden block by 12 to 88 percentage points on six GPT models and by 17 on Qwen3.8-27B, even though the models mostly report correctly which blocks the director sees. Reasoning traces and prompt rewordings suggest why: the question shifts how the request is read, from the director's view toward the model's own. When the prompt states what the director knows and refers to, fewer than 1% of replies pair a correct report with a hidden-block choice. Any evaluation that elicits a perspective report before the action it scores needs a baseline without the question, and we deliver one: paired prompts that differ only in that question, a design any perspective-taking benchmark can adopt.

## Metadata
- **Published**: 2026-10-21T07:21:08Z
- **Authors**: Jiaxuan Guo, Xingyu Ren, Kejia Zhang, Jingxin Yang, Youran Sun, Haizhao Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.29318v1)