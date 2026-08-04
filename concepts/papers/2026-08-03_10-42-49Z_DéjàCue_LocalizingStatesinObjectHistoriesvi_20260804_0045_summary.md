# Summary: 2026-08-03_10-42-49Z_DéjàCue_LocalizingStatesinObjectHistoriesviaVocabu.md
Saved: 2026-08-04 00:45
Source: 2026-08-03_10-42-49Z_DéjàCue_LocalizingStatesinObjectHistoriesviaVocabu.md
Model: None

---

## Summary  
The paper addresses a core challenge in visual object tracking: distinguishing between different states of an object (e.g., empty vs. filled) when only the visual history is available, as absolute image‑text similarity cannot resolve temporal intervals. To overcome this, the authors propose **Déjà Cue**, a training‑free framework that converts alternative state descriptions into a vocabulary‑relative coordinate system. By subtracting a shared centroid and scanning multiple durations within contiguous visible frames with a frozen encoder, the method localizes each described state to its exact interval in the history. The approach treats related state descriptions as an object‑specific query‑time reference, enabling precise retrieval without additional training.

## Key Contributions  
- [Finding 1] Introduces a training‑free framework that uses vocabulary‑relative coordinates derived from centroid subtraction of alternative state descriptions.  
- [Finding 2] Shows that fixing the temporal scan while varying only the query reference can double R@1 at tIoU 0.5, improving it from 10.3 % to 20.5 %.  
- [Finding 3] Demonstrates that candidate‑rank analyses reveal vocabulary‑relative queries consistently rank higher within the same candidate set than absolute similarity scores.

## Methodology  
The authors treat each state description as a vector in a fixed embedding space and compute its centroid across all frames where it is observed. The centroid serves as an object‑specific reference point; subtracting this from any query vector yields a relative coordinate that indicates how far the query deviates from the shared history. A frozen vision encoder processes the visual history once, generating a temporal map of visible frames. The system then scans contiguous runs of these frames, evaluating the relative scores to locate intervals where each described state holds. Because the encoder is not updated during inference, the method is fully training‑free and can be applied directly to any object‑history dataset.

## Results  
On 78 VOST (Video Object Tracking) histories, with the temporal scan held constant and only the query reference altered, the model’s R@1 at tIoU 0.5 rises from 10.3 % to 20.5 %, a near‑doubling improvement. Correspondingly, Top‑1 tIoU increases from 16.0 % to 21.5 %. Candidate‑rank analysis confirms that queries based on vocabulary‑relative coordinates outperform absolute similarity scores in ranking the correct intervals, highlighting the effectiveness of the relative coordinate system.

## Significance  
Déjà Cue provides a novel way to read frozen visual representations by treating related state descriptions as an object‑specific, query‑time coordinate system. This enables more accurate and faster state‑moment retrieval without retraining models on each dataset, which is valuable for real‑world applications where model updates are costly or impossible.

## Related Concepts  
- Object tracking  
- State‑moment retrieval  
- Vocabulary‑relative coordinates  
- Centroid subtraction  
- Frozen encoder  
- Temporal scanning  
- Candidate ranking
