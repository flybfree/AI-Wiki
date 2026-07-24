# Summary: 2026-07-18_04-37-20Z_TellTale_BlendingMulti_InstanceLoRATextEncodersand.md
Saved: 2026-07-24 00:01
Source: 2026-07-18_04-37-20Z_TellTale_BlendingMulti_InstanceLoRATextEncodersand.md
Model: None

---

## Summary  
TellTale is a text‑only method for recognizing ambivalence/hesitancy (A/H) in interview videos that relies solely on the transcript, not on video or audio cues. The approach blends two fine‑tuned multilingual LoRA encoders with a zero‑shot instruction LLM judge to generate three independent probability streams. These streams are merged via weighted averaging and a single decision threshold selected on participant‑grouped cross‑validated predictions. Compared with the official vision‑based baseline, TellTale achieves substantially higher macro‑F1 scores while requiring no video processing.

## Key Contributions  
- Multi‑instance LoRA adapters enable efficient per‑chunk scoring under video‑level supervision without full fine‑tuning.  
- A quantized 14B instruction LLM provides zero‑shot, high‑quality A/H ratings for each transcript chunk.  
- Weighted averaging of the three probability streams yields a robust decision with an optimal threshold.

## Methodology  
The authors fine‑tune multilingual‑e5‑large and mDeBERTa‑v3‑base using LoRA under multiple‑instance learning, where each transcript chunk is scored individually and pooled via smooth maximum pooling to produce the video label. A quantized 14B instruction LLM is prompted zero‑shot for per‑chunk A/H ratings. The three probability outputs are combined with weights derived from participant‑grouped cross‑validation.

## Results  
On the private test set of 152 videos, TellTale reaches a Macro‑F1 of 0.7364 and an average precision of 0.7940, significantly outperforming the official vision baseline’s Macro‑F1 of 0.2827. The improvement is attributed to the complementary strengths of the two encoders and the zero‑shot judge.

## Significance  
This work demonstrates that text‑only models can rival or exceed visual methods for a challenging A/H detection task, reducing reliance on expensive video processing pipelines and enabling scalable deployment across languages. It also shows how combining parameter‑efficient adapters with large language models can produce robust, interpretable decision streams.

## Related Concepts  
- Multi‑instance learning  
- LoRA (Low‑Rank Adaptation) adapters  
- Zero‑shot prompting  
- Instruction tuning  
- Smooth maximum pooling  
- Macro‑F1 and average precision metrics  
- Ambivalence/hesitancy recognition
