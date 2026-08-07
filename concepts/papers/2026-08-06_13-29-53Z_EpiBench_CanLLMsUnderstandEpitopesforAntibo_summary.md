# Summary: 2026-08-06_13-29-53Z_EpiBench_CanLLMsUnderstandEpitopesforAntibodyDrugD.md
Saved: 2026-08-06 20:44
Source: 2026-08-06_13-29-53Z_EpiBench_CanLLMsUnderstandEpitopesforAntibodyDrugD.md
Model: None

---

## Summary  
The paper proposes EpiBench, a benchmark to evaluate whether large language models can reason about epitopes in antibody‑antigen interactions. It introduces a closed‑book, sequence‑only test with 1,609 curated samples covering discovery, identification, binning, functional assessment and escape analysis. LLM performance is measured across nine models using stratified sampling and explicit reasoning baselines. The study reveals partial success but highlights limitations in grounding, long‑context localization and biological reasoning.  

## Key Contributions  
- EpiBench provides a closed‑book, sequence‑only benchmark for epitope reasoning that integrates structural contacts, functional assays and deep mutational scanning.  
- It evaluates nine general‑purpose LLMs across five connected tasks with controlled sampling to mitigate shortcut artifacts.  
- The analysis identifies three failure modes: poor antigen grounding, limited residue localization in long contexts, and lack of biologically grounded reasoning.  

## Methodology  
The authors constructed EpiBench by curating 1,609 samples that link antibody sequences to known epitope regions derived from high‑resolution structural data, functional B‑cell assays, and escape mutation profiles. Tasks include targetable region discovery, antibody‑conditioned epitope identification, epitope binning, functional assessment, and escape assessment. Evaluation uses stratified sampling by antigen length, task type, and model, with baselines that either ignore sequence (random) or use explicit reasoning modules; performance is scored automatically via predefined criteria.  

## Results  
Across tasks, models like GPT‑4 and Claude captured some epitope signals but performed poorly on long‑context localization and escape prediction. The average accuracy on functional assessment was 58 %, dropping to 31 % when antigen length exceeded 200 residues. Failure analyses showed that LLMs often rely on superficial pattern matching rather than true sequence grounding.  

## Significance  
EpiBench offers a standardized diagnostic for LLM performance in epitope‑centric drug discovery, guiding developers toward better sequence modeling and reasoning capabilities. By exposing systematic weaknesses, it helps prioritize improvements such as longer context windows or domain‑specific fine‑tuning.  

## Related Concepts  
- Epitope: the antigenic region recognized by an antibody.  
- Large language model (LLM): a neural network trained on massive text corpora for natural language tasks.  
- Antibody drug discovery: developing monoclonal antibodies to treat diseases.  
- Deep mutational scanning: measuring functional impact of point mutations.
