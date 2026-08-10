---
title: Do Audio Language Models Use Paralinguistic Evidence? Counterfactual Audits for Response Evaluation
published: 2026-08-07T02:24:12Z
authors: Kevin Miller, Arjun Chandra, Venkatesh Saligrama
url: http://arxiv.org/abs/2608.06718v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Audio Language Models Use Paralinguistic Evidence? Counterfactual Audits for Response Evaluation

## Abstract
Audio-language models (ALMs) are increasingly used as judges for speech-to-speech systems, but a judge that receives audio may not actually use paralinguistic evidence. We introduce counterfactual audits for paralinguistic response evaluation. Each audit item holds the transcript fixed while varying affect, prosody, or the timing of an affective shift, forcing a valid judge to track the audio cue rather than lexical content or response style. We evaluate ALM judges using a native one-context judgment protocol and a contrastive recoverability control, then further decompose each item into its constituent perception and response-mapping skills. This yields useful diagnostic states that identify different sources of judge failures. Across Gemini, GPT, and open audio models, we find that contrastive success often overstates native judge reliability, and that similar aggregate accuracies can hide different failure modes. These results suggest that ALM judges should not be evaluated by accuracy alone, instead requiring thorough behavioral audits before deployment.

## Metadata
- **Published**: 2026-08-07T02:24:12Z
- **Authors**: Kevin Miller, Arjun Chandra, Venkatesh Saligrama
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06718v1)