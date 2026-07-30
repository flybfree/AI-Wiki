# Summary: 2026-07-29_10-15-36Z_AtmosERC_ModelingDialogue_LevelAffectiveAtmosphere.md
Saved: 2026-07-29 20:32
Source: 2026-07-29_10-15-36Z_AtmosERC_ModelingDialogue_LevelAffectiveAtmosphere.md
Model: None

---

## Summary  
The paper addresses Emotion Recognition in Conversation (ERC) by focusing on the affective atmosphere of dialogues, proposing AtmosERC—a graph‑based framework that extracts and fuses heterogeneous signals into a compact prior for emotion prediction. It improves both lightweight ERC models and LLM‑based ERC as a plug‑in cue while stabilizing predictions under local emotional deviations. This work bridges the gap between global context and local emotion cues by focusing on a compact, affect‑oriented signal that can be efficiently exploited.

## Key Contributions  
- Finding 1: The dialogue‑level affective atmosphere is identified as a latent tendency reflecting conversation‑wide emotion patterns.  
- Finding 2: AtmosERC builds a graph model over utterances and speakers, extracting relational signals to produce speaker‑conditioned affective priors.  
- Finding 3: The framework yields lightweight sequential prediction and can be rendered as prompt cues for LLMs without altering backbones. These findings highlight the importance of relational structure in affective modeling.

## Methodology  
The authors treat each dialogue as a conversational graph where nodes are utterances and edges encode speaker or turn relationships. A relation‑aware extractor filters noisy heterogeneous signals, fuses them into a compact affective prior that is conditionally indexed by speaker and context. This prior feeds lightweight recurrent models for emotion prediction and can be converted to textual prompts for LLM inference. The graph construction is iterative, allowing dynamic adaptation to varying dialogue lengths.

## Results  
Experiments on four ERC benchmarks demonstrate that AtmosERC boosts accuracy of lightweight ERC compared with baselines, improves performance of LLM‑based ERC when used as a cue, and provides more stable predictions when the conversation deviates locally from its overall affective trend. The improvements are statistically significant across all datasets. Overall, AtmosERC consistently outperforms state‑of‑the‑art methods across both traditional and large language model settings.

## Significance  
By isolating the most relevant affective signal and providing an efficient, interpretable prior, AtmosERC offers a scalable solution for emotion recognition that works well in both traditional sequence models and large language models, reducing reliance on heavy contextual encoders while preserving interpretability. This approach reduces computational overhead while preserving interpretability, making it suitable for real‑time applications.

## Related Concepts  
- Emotion Recognition in Conversation (ERC)  
- Dialogue‑level affective atmosphere  
- Graph‑based modeling of conversational data  
- Heterogeneous graph signals  
- Speaker‑conditioned priors  
- Lightweight sequential prediction  
- Prompt‑level cues for LLMs
