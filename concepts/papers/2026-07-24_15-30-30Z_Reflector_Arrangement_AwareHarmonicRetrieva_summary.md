# Summary: 2026-07-24_15-30-30Z_Reflector_Arrangement_AwareHarmonicRetrievalforSam.md
Saved: 2026-07-26 21:53
Source: 2026-07-24_15-30-30Z_Reflector_Arrangement_AwareHarmonicRetrievalforSam.md
Model: None

---

## Summary  
The paper introduces Reflector, an interactive audio workstation that enables composers to retrieve harmonically compatible material as their arrangement evolves on a multi‑track timeline. By tracking harmonic combinations and adapting retrieval scores in real time, Reflector addresses the limitation of fixed reference‑sample queries. The system leverages a hand‑designed interval‑class oracle encoded in a 128‑dimensional embedding to compute compatibility at interactive speed. This arrangement‑aware approach allows the composer’s evolving harmonic identity to be reflected in the retrieval process.

## Key Contributions  
- [Finding 1] Reflector provides an arrangement‑aware harmonic retrieval system that dynamically updates compatibility scores as material is arranged on a timeline.  
- [Finding 2] The learned 128‑dimensional embedding approximates a hand‑designed interval‑class oracle, preserving the kernel’s pairwise judgments while covering the entire library and enabling fast dot‑product similarity at interactive speed.  
- [Finding 3] Session centroids projected into a navigable three‑dimensional space reveal structural harmonic relations across a composer’s body of work.

## Methodology  
The authors began with a fixed interval‑class oracle—a hand‑crafted table assigning weights to how pitch classes combine between sources. An encoder trained exclusively on synthetic audio learns to approximate this oracle in a 128‑dimensional embedding space, where dot products serve as compatibility scores. As the composer arranges material on a multi‑track timeline, a sweep‑line analysis identifies co‑sounding regions and computes oracle‑weighted centroids that represent the composite harmonic identity of the session. Retrieval is performed against these evolving centroids, producing results in real time without reliance on copyrighted training data.

## Results  
Experimental evaluation shows that the learned embedding faithfully reproduces the kernel’s pairwise compatibility judgments while covering all library samples, a property unattainable when using the oracle directly as a retrieval rule. The dot‑product similarity between source and session centroids correlates strongly with perceived harmonic compatibility at interactive speed. Additionally, the 3‑D projection of session centroids uncovers coherent structural patterns across multiple compositions, confirming the system’s ability to capture long‑term harmonic relationships.

## Significance  
Reflector matters because it bridges theory and practice: composers can retrieve material that remains harmonically compatible as their arrangement changes, avoiding the need for manual tuning. The work also provides theoretical insight into how normalized embeddings preserve kernel judgments while handling degenerate solutions that direct scoring favors. By being fully local, open‑source, and free, Reflector democratizes advanced harmonic retrieval tools for musicians worldwide.
