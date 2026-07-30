# Summary: 2026-07-29_09-13-00Z_AIGen_AutomatingAIBillofMaterialsGenerationThrough.md
Saved: 2026-07-29 20:31
Source: 2026-07-29_09-13-00Z_AIGen_AutomatingAIBillofMaterialsGenerationThrough.md
Model: None

---

## Summary  
The paper introduces AIGen, a modular tool that automatically generates AI Bills of Materials (AIBoMs) in SPDX 3.0 format for end‑to‑end AI systems. By integrating mining heuristics with large language models within the MLflow MLOps framework, AIGen can extract and catalog all constituent artifacts—datasets, model weights, training pipelines, and runtime dependencies—without manual intervention. The system is extensible via a plugin interface that lets practitioners add domain‑specific collectors for frameworks such as Hugging Face, PyTorch, or TensorFlow. This hybrid approach enables compliance with regulatory standards like the EU AI Act, NIST AI Risk Management Framework, and ISO/IEC 42001 while providing a reusable foundation for transparent AI supply‑chain governance.

## Key Contributions  
- [Finding 1] AIGen produces machine‑readable, interoperable inventories of AI system components that conform to the SPDX 3.0 AI profile.  
- [Finding 2] The tool combines mining heuristics with a large language model to automate BoM generation and fill the SPDX fields automatically.  
- [Finding 3] A plug‑in architecture allows seamless extension for heterogeneous frameworks without altering core code, supporting extensibility across the AI ecosystem.

## Methodology  
AIGen operates on top of MLflow’s MLOps platform, where a mining phase extracts metadata from model artifacts and training scripts using heuristic rules. The extracted data is then fed to a fine‑tuned language model that generates SPDX 3.0 compliant BoM text, ensuring consistency with the AI profile schema. Practitioners can add custom collector plugins to capture framework‑specific information (e.g., Hugging Face datasets) without touching the main generator logic.

## Results  
The authors demonstrate AIGen on ten representative projects spanning Hugging Face, PyTorch, and TensorFlow pipelines. The generated BoMs are fully compliant with SPDX 3.0 AI profiles and pass automated validation scripts that check required fields such as `ai:artifact`, `ai:version`, and `ai:license`. Compliance checks against the EU AI Act and NIST frameworks confirm that AIGen can produce documentation suitable for regulatory audits.

## Significance  
By automating BoM generation, AIGen reduces human error in AI system documentation, accelerates audit preparation, and supports responsible AI development. Its extensible design encourages broader adoption across research labs and industry, fostering transparency and accountability throughout the AI supply chain.

## Related Concepts  
- SPDX 3.0 AI profile (standard for AI BoMs)  
- MLOps framework (MLflow)  
- Large Language Models (LLM mining & generation)  
- AI Bill of Materials (AIBoM)  
- EU AI Act, NIST AI Risk Management Framework, ISO/IEC 42001 (regulatory compliance)
