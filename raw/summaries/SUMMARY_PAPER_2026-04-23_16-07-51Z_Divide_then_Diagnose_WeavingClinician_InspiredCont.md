---

title: "Divide-then-Diagnose: Weaving Clinician-Inspired Contexts for Ultra-Long Capsule Endoscopy Videos"
url: http://arxiv.org/abs/2604.21814v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-04-23_16-07-51Z_Divide_then_Diagnose_WeavingClinician_InspiredCont.md
generated_at: "2026-06-11 10:26"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces VideoCAP, a dataset of 240 full‑length capsule endoscopy videos annotated for diagnosis‑driven video summarization, and proposes DiCE, a clinician‑inspired framework that extracts key evidence frames and builds coherent diagnostic contexts. Experiments demonstrate that DiCE outperforms existing methods by producing concise, reliable summaries that capture sparse but clinically relevant events.

## Key Takeaways
- The dataset VideoCAP provides realistic supervision for both frame extraction and diagnosis, addressing the scarcity of diagnostically relevant events in ultra‑long CE videos.
- DiCE’s three‑stage pipeline—candidate screening, context weaving, and evidence converging—mirrors human reading workflows to organize sparse lesions into coherent diagnostic narratives.
- The framework consistently improves video summarization quality by reducing redundancy and handling motion blur, debris, and viewpoint changes that degrade individual frame detection.

## Context
Capsule endoscopy generates terabytes of visual data where only a few frames contain meaningful pathology. Current AI methods focus on per‑frame classification, neglecting the need for coherent video summaries. This work bridges that gap by integrating diagnostic reasoning into video summarization tasks, aligning with broader efforts to make long‑form medical imaging more interpretable.

## Implications
Clinicians can rely on DiCE’s concise summaries for faster decision making and reduced review burden. The approach also offers a template for other ultra‑long medical video domains where sparse events must be highlighted in contextually meaningful clips.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2604.21814v1)
