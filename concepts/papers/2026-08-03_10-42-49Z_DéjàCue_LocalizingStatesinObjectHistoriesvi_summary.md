# Summary: 2026-08-03_10-42-49Z_DéjàCue_LocalizingStatesinObjectHistoriesviaVocabu.md
Saved: 2026-08-04 00:30
Source: 2026-08-03_10-42-49Z_DéjàCue_LocalizingStatesinObjectHistoriesviaVocabu.md
Model: None

---

## Summary  
The paper tackles the problem of locating precise temporal intervals in object histories where multiple state descriptions are provided, which can be ambiguous because shared visual frames obscure evidence for a particular state. It proposes **Déjà Cue**, a training‑free framework that converts alternative state descriptions into a vocabulary‑relative coordinate system based on their centroids and scans frozen visual representations to retrieve the correct interval. The method improves accuracy without retraining the object encoder, demonstrating strong gains on standard datasets. This work advances multimodal state tracking by offering an object‑specific, query‑time coordinate framework.

## Key Contributions  
- [Finding 1] A formulation of identity‑conditioned state‑moment retrieval that uses alternative state descriptions as relative coordinates to disambiguate intervals.  
- [Finding 2] An end‑to‑end training‑free vocabulary‑relative coordinate system derived from centroid subtraction and frame calibration.  
- [Finding 3] Empirical improvements: R@1 at tIoU 0.5 rises from 10.3 % to 20.5 %, while Top‑1 tIoU increases from 16.0 % to 21.5 %.

## Methodology  
The authors treat each alternative state description as a vector in a vocabulary space, compute its centroid relative to the others, and subtract this baseline to obtain vocabulary‑relative coordinates for every frame. These coordinates are then used with a frozen object encoder that evaluates multiple temporal windows across contiguous visible runs, allowing the system to scan candidate intervals without additional training.

## Results  
Experiments on 78 VOST histories show that fixing the temporal scan while varying only the query reference nearly doubles R@1 at tIoU 0.5 (from 10.3 % to 20.5 %) and lifts Top‑1 tIoU from 16.0 % to 21.5 %. Candidate‑rank analyses confirm that vocabulary‑relative queries rank higher within the same candidate set, indicating a clear benefit of the relative coordinate approach.

## Significance  
Déjà Cue provides an object‑specific, query‑time coordinate system derived from state descriptions, enabling more accurate and efficient retrieval of temporal intervals in frozen visual representations. This contribution advances research on multimodal state tracking by delivering strong performance gains without requiring retraining or additional data.

## Related Concepts  
- identity‑conditioned retrieval  
- vocabulary‑relative coordinates  
- centroid subtraction  
- frozen encoder  
- tIoU (temporal IoU)  
- VOST dataset
