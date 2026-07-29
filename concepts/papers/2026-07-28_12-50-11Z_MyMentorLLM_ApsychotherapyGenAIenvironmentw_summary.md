# Summary: 2026-07-28_12-50-11Z_MyMentorLLM_ApsychotherapyGenAIenvironmentwithmult.md
Saved: 2026-07-28 22:49
Source: 2026-07-28_12-50-11Z_MyMentorLLM_ApsychotherapyGenAIenvironmentwithmult.md
Model: None

---

## Summary  
The paper introduces MyMentorLLM, a multimodal voice‑text simulation environment that generates 2,100 complete Cognitive Behavioural Therapy training sessions for trainees to practice delivering CBT interventions. It links DSM‑5‑TR‑grounded patients with disorders such as major depression, generalized anxiety disorder and borderline personality disorder to therapists‑in‑training and expert supervisors, enabling deliberate practice. The study evaluates how well LLMs can simulate patient emotional profiles, therapist competence, and supervisor feedback, producing a benchmark for scalable psychotherapy training.  

## Key Contributions  
- Finding 1: MyMentorLLM creates a large‑scale, multimodal simulation library of CBT sessions that can be reused across multiple trainees and experts.  
- Finding 2: Most LLMs overestimate trainee competence while native speech‑to‑speech models produce supervision feedback closest to human expert ratings.  
- Finding 3: Supervisor feedback improves diagnostic accuracy in simulated therapists for five out of seven LLM supervisors, and larger model sizes correlate with higher symptom identification performance.  

## Methodology  
The authors built MyMentorLLM by first constructing a corpus of 2,100 CBT sessions using GPT‑4 to generate patient dialogues that reflect DSM‑5‑TR diagnostic criteria. Each session includes a therapist‑in‑training (human) and an expert supervisor (another human). The system records emotional dynamics, therapeutic techniques, and diagnostic predictions, which are then analyzed for fidelity and competence.  

## Results  
Analysis of 2,100 sessions revealed that simulated patients displayed disorder‑congruent emotional profiles that trainees mirrored authentically. Expert supervision varied: five LLM supervisors gave feedback that led to correct diagnoses in simulated therapists, whereas two others overestimated competence. Symptom identification accuracy rose with model size, suggesting larger models capture richer patient narratives.  

## Significance  
This work demonstrates that AI‑driven simulation can scale psychotherapy training without sacrificing fidelity, offering a practical solution for therapist education and supervision bottlenecks.  

## Related Concepts  
CBT, deliberate practice, multimodal voice‑text interaction, DSM‑5‑TR, generative AI (LLMs), supervisor feedback, diagnostic accuracy, patient empathy simulation.
