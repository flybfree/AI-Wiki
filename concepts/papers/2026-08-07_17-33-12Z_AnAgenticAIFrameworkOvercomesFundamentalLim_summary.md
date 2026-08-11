# Summary: 2026-08-07_17-33-12Z_AnAgenticAIFrameworkOvercomesFundamentalLimitation.md
Saved: 2026-08-10 22:38
Source: 2026-08-07_17-33-12Z_AnAgenticAIFrameworkOvercomesFundamentalLimitation.md
Model: None

---

## Summary  
The paper proposes an agentic AI framework that combines large language models (LLMs) with specialized deep‑learning tools to detect glaucoma from fundus photographs, addressing LLM hallucination and inconsistency. By orchestrating assessments, function calls, and reflections, the system overcomes fundamental limitations of LLMs alone. The approach was evaluated on two public datasets using two LLMs under both uncropped and cropped fields of view.

## Key Contributions  
- The agentic workflow boosts classification accuracy by 16–47 percentage points compared with LLM‑only methods, reaching within six points of human specialist grading.  
- It eliminates systematic over‑diagnosis (e.g., GPT‑5.4 mini’s sensitivity 95–100% but specificity 0–5%) and stochastic run‑to‑run variability seen in LLMs.  
- Integration reduces cup‑to‑disc ratio errors by 15–50% and improves correlation with specialist grading from r=0.12–0.39 to r=0.59–0.84.

## Methodology  
The authors built a three‑step pipeline where an LLM first provides an initial assessment, then invokes domain‑specific tools (QAModel for image quality, FundaQ‑8 for glaucoma classification, SwinV2‑Tiny and SegFormer‑B0 for segmentation), and finally the LLM reflects on both its own output and the tool results. Two LLMs (Gemini 2.5 Flash and GPT‑5.4 mini) were run on ORIGA (n=100) and RIM‑ONE‑v3 (n=100) images, graded independently by a masked fellowship‑trained specialist.

## Results  
The agentic system achieved classification accuracies of 82–96% across conditions, within six points of the human reference. Cup‑to‑disc ratio errors dropped from MAE 0.156–0.228 to 0.104–0.132, and run‑to‑run consistency improved from near‑random (kappa ≈ -0.01) to near‑perfect (kappa up to 0.96). LLM‑only approaches failed with high false positives or stochastic inconsistency.

## Significance  
This work demonstrates that orchestrating specialized AI tools through an LLM can overcome hallucination, bias, and variability, offering a more reliable diagnostic assistant for glaucoma screening and hinting at broader adoption of multi‑agent architectures in medical imaging.

## Related Concepts  
- Large language models (LLMs)  
- Function calling  
- Orchestrated multi‑agent systems  
- Deep learning tools for image quality assessment  
- Glaucoma detection from fundus photography  
- Run‑to‑run consistency metrics (kappa)  
- Cup‑to‑disc ratio error
