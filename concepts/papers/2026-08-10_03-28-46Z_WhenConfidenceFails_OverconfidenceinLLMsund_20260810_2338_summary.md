# Summary: 2026-08-10_03-28-46Z_WhenConfidenceFails_OverconfidenceinLLMsunderUncer.md
Saved: 2026-08-10 23:38
Source: 2026-08-10_03-28-46Z_WhenConfidenceFails_OverconfidenceinLLMsunderUncer.md
Model: None

---

## Summary  
The authors investigate why large language models (LLMs) often give high‑confidence answers that are incorrect when clinical information is ambiguous or absent. They introduce a systematic evaluation framework on the MedMCQA dataset, manipulating prompts to create linguistic uncertainty and removing correct options to force abstention. The study measures both accuracy and confidence using calibration metrics such as the calibration gap, Expected Calibration Error (ECE), and Unsafe Confident Error Rate (UCER). Their analysis reveals a persistent mismatch between model performance and its expressed confidence, especially under clinically relevant information loss.  

## Key Contributions  
- Finding 1: LLMs exhibit a systematic failure mode where accuracy drops with increasing uncertainty yet confidence remains high, leading to unsafe confident errors.  
- Finding 2: Model confidence is largely insensitive to the loss of correct answer options, causing models to hallucinate high‑confidence responses when they should abstain.  
- Finding 3: There is significant variation across LLMs in their ability to correctly recognize missing information and produce low‑confidence abstentions versus persistent overconfident hallucinations.  

## Methodology  
The authors adopt a two‑pronged experimental design on the MedMCQA dataset, which contains medical multiple‑choice questions. First, they embed linguistic uncertainty cues into prompts to simulate ambiguous clinical contexts, thereby measuring how model confidence changes when input is vague. Second, they create an answer removal condition where the correct option is deleted, forcing the model to detect insufficient information and abstain rather than guess. For each question, the team records both the predicted answer and its confidence score, then computes calibration metrics: the calibration gap (difference between predicted probability and observed accuracy), Expected Calibration Error (average absolute difference between predicted probabilities and empirical frequencies), and Unsafe Confident Error Rate (proportion of high‑confidence predictions that are incorrect). This dual‑setting approach captures both ambiguous input and explicit information loss, providing a comprehensive view of model reliability under uncertainty.  

## Results  
Across 500 medical questions, the authors observe that accuracy declines as prompt ambiguity increases or correct answers are removed, yet confidence scores remain relatively stable or even increase in some cases. The calibration gap widens significantly (average ≈ 0.28), indicating a strong misalignment between predicted and observed performance. ECE is also elevated (≈ 0.15), confirming that high‑confidence predictions are disproportionately wrong. UCER rises sharply when the correct answer is absent, reaching up to 30 % for certain models, showing a dangerous propensity to produce unsafe confident hallucinations. Moreover, model behavior varies: some LLMs correctly abstain with low confidence (UCER < 5 %), while others persistently generate high‑confidence wrong answers even when the correct option is missing.  

## Significance  
These findings expose critical limitations in the epistemic reliability of current LLMs for clinical decision support, where misplaced confidence can lead to harmful patient outcomes. By quantifying unsafe confident errors and demonstrating that models often ignore clinically meaningful uncertainty cues, the study underscores the necessity of uncertainty‑aware evaluation protocols before deploying AI tools in high‑stakes healthcare environments. The results also highlight a need for model architectures or post‑processing mechanisms that can reliably detect information gaps and reduce overconfidence.  

## Related Concepts  
uncertainty, confidence calibration, safe AI, medical question answering, abstention, hallucination, calibration gap, Expected Calibration Error (ECE), Unsafe Confident Error Rate (UCER)
