---
title: Can We Read the Mind of an Audio LLM? A Verbalizable, Multilingual Middle-Layer Workspace
published: 2026-08-25T06:17:28Z
authors: Jiajun Fan, Jingyuan Li, Prashanth Gurunath Shivakumar, Qi Luo, Jia-Hong Huang, M. Maruf, Roger Ren, Yile Gu, Rahul Pandey, Ge Liu, Ivan Bulyko
url: http://arxiv.org/abs/2608.24958v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can We Read the Mind of an Audio LLM? A Verbalizable, Multilingual Middle-Layer Workspace

## Abstract
An audio language model is a black box in a specific way: we see what it says, never what it works out on the way there, and chain-of-thought monitoring helps only if the model writes its reasoning down. Reading a base Qwen3-Omni with a logit lens at the audio-token positions, we find that the answer to a spoken question becomes legible - in words - in the model's middle layers, before it emits any token. Five findings follow. (1) The readout carries concepts in neither the question, the options, nor the model's own transcription: on a clip whose verbatim transcription is empty garbling, it reconstructs Watergate and scandal, passes through the role president, and resolves to Nixon - a hidden multi-hop chain, read with no chain-of-thought. (2) The content is language-agnostic: one audio-inferred concept surfaces in several scripts at once, and 38% of top-1 readouts are Chinese on English inputs. (3) It is paralinguistic: given the same clip as audio and as the model's own emotion-free caption, the audio mind forms the sound source, speaker role, or affect that the caption discards, and answers correctly more often. (4) The audio-driven signal is absent at the input, turns on about a tenth of the way into the network, separates most cleanly from the text prior in the middle band (35-80% of depth), and activation patching shows it is causally used and committed before the last fifth of the layers. (5) Deleting single layers maps the pipeline: reading the sound in is localized to the entry layers and answer delivery to the output layer, while retrieval is distributed across the interior. Throughout, a waveform-swap control - identical text, only the sound changed - isolates the audio-driven signal from a prior over the printed options. This is a qualitative account of what an audio model works out before it speaks: the quantities are controls, not benchmark scores.

## Metadata
- **Published**: 2026-08-25T06:17:28Z
- **Authors**: Jiajun Fan, Jingyuan Li, Prashanth Gurunath Shivakumar, Qi Luo, Jia-Hong Huang, M. Maruf, Roger Ren, Yile Gu, Rahul Pandey, Ge Liu, Ivan Bulyko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24958v1)