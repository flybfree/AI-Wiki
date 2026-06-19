---
title: "2026 06 12 17 59 57Z Gazeheads Howvlmslookatwhattheydescribe Summary"
date: 2026-06-12
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-12_17-59-57Z_GazeHeads_HowVLMsLookatWhatTheyDescribe.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-06-14 22:01
Source: 2026-06-12_17-59-57Z_GazeHeads_HowVLMsLookatWhatTheyDescribe.md
Model: None

---


## Summary  
The paper investigates how vision‑language models generate captions and discovers a specific attention‑head mechanism called “gaze heads” that track the image region currently being described. By analyzing a few forward passes on comic strips, the authors identify these heads as a small subset (<9 % of all heads) whose attention correlates strongly with the tokens they are describing. The key finding is that intervening only on these gaze heads can steer the model’s output to any chosen panel with high accuracy, while random or full‑head interventions either fail or destroy generation. This reveals an interpretable internal structure for multimodal reasoning that can be manipulated at inference time without retraining.

## Key Contributions  
- [Finding 1] Gaze heads are a small set of attention heads (<9 % of total) whose output correlates with the image region being described.  
- [Finding 2] Applying an attention mask to only these gaze heads redirects generation to a chosen comic panel at ~83.1 % accuracy, whereas random or all‑head masks fail or destroy output.  
- [Finding 3] The mechanism works across model sizes (2B–32B parameters) and VLM architectures, and can be used for continuous control during generation.

## Methodology  
The authors first created a controlled testbed of comic strips where narrative order is spatially aligned with image tokens. They performed a limited number of forward passes to record attention head outputs, then computed correlation scores between each head’s activation pattern and the visual token it attends to. Heads with high correlation were labeled “gaze heads.” To verify their role, they inserted attention masks: (i) top‑100 gaze heads redirected generation to a specific panel at 83.1 % accuracy; (ii) random heads left output unchanged; (iii) masking all heads eliminated generation entirely. The same mask strategy was applied to natural COCO images and to continuous captioning, where switching the target mid‑generation caused the model to wrap up the current description within a few tokens.

## Results  
- Gaze heads were identified with simple correlation analysis from just a few forward passes.  
- Attention masking on gaze heads achieved 83.1 % accuracy in redirecting answers to any panel, while random masks had negligible effect and full‑head masking destroyed generation.  
- The same intervention works for continuous control: changing the gaze target mid‑generation triggers a rapid switch to the new region within three–four tokens.  
- Experiments across model sizes (2B to 32B parameters) and VLM architectures confirm the robustness of gaze heads, though frozen‑encoder families show no comparable head set.

## Significance  
This work demonstrates that deep multimodal models possess interpretable internal levers—gaze heads—that can be exploited for inference‑time steering without any retraining. By exposing these mechanisms, it advances AI interpretability and opens practical pathways for controllable generation, enabling users to direct model behavior precisely through attention manipulation.

## Related Concepts  
- Vision‑language models (VLMs)  
- Attention heads in transformer architectures  
- Interference cancellation via attention masking  
- Model interpretability and internal mechanism discovery  
- Prompt engineering using internal representations
