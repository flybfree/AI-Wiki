---
title: MLCommons Jailbreak Benchmark v1.0
published: 2026-10-02T05:17:56Z
authors: Carsten Maple, Cagatay Yucel, Isaac Holeman, Chris Knotz, Peter Mattson, James Goel, Jonathan Petit, Sean McGregor, James Ezick, Abhishek Kumar, Alicia Parrish, Murali Emani, Kashyap Iyer, Faiza Khan Khattak, Washington Mbonu, Daniel Machlab, Eileen Long, Shaona Ghosh, Jibin Varghese, Roman Lutz, Andrew Gruen, Bennett Hillenbrand, Prabal Gupta, Mohammed Serrhini, Dhivya Nagasubramanian, Aakash Gupta,  Jun,  Lu, Kurt Bollacker, Chang Liu, Jonathan Petit, Cong Chen, Jean-Philippe Monteuuis, Brent Miller, Apurv Verma, Roman Eng, Armstrong Foundjem, Mohammed Serrhini
url: http://arxiv.org/abs/2610.02827v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MLCommons Jailbreak Benchmark v1.0

## Abstract
Modern AI systems are designed to refuse hazardous requests. A jailbreak is a prompt crafted to bypass those safeguards and elicit outputs that the system would normally refuse to provide. The MLCommons Jailbreak Benchmark v1.0 provides an end-to-end methodology for evaluating the robustness of large language models to single-turn, text-based jailbreak attacks. It combines criteria-driven system and attack selection, paired baseline and adversarial evaluation, human annotation, automated evaluator calibration, scoring, grading, and risk-calibrated disclosure within a single benchmarking pipeline. The benchmark evaluates eight open-weight systems using 264 seed prompts spanning eleven hazard categories and representative attacks drawn from the MLCommons Jailbreak Taxonomy. Responses are assessed using the AILuminate Assessment Standard v1.4, and robustness is measured through the Resilience Gap: the change in safety performance between baseline and adversarial conditions. Across all evaluated systems and attacks, the unsafe-response rate increased from 11.08% under baseline conditions to 18.65% under jailbreak conditions, producing an average Resilience Gap of 7.57%. Accessible systems showed a larger mean gap, while attack effectiveness varied substantially across attack categories and hazards. The benchmark also examines evaluator reliability and sources of measurement error. Beyond reporting results, Jailbreak Benchmark v1.0 establishes a reproducible methodological foundation for comparative jailbreak evaluation and for future expansion across systems, attacks, hazards, and evaluation methods.

## Metadata
- **Published**: 2026-10-02T05:17:56Z
- **Authors**: Carsten Maple, Cagatay Yucel, Isaac Holeman, Chris Knotz, Peter Mattson, James Goel, Jonathan Petit, Sean McGregor, James Ezick, Abhishek Kumar, Alicia Parrish, Murali Emani, Kashyap Iyer, Faiza Khan Khattak, Washington Mbonu, Daniel Machlab, Eileen Long, Shaona Ghosh, Jibin Varghese, Roman Lutz, Andrew Gruen, Bennett Hillenbrand, Prabal Gupta, Mohammed Serrhini, Dhivya Nagasubramanian, Aakash Gupta,  Jun,  Lu, Kurt Bollacker, Chang Liu, Jonathan Petit, Cong Chen, Jean-Philippe Monteuuis, Brent Miller, Apurv Verma, Roman Eng, Armstrong Foundjem, Mohammed Serrhini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02827v1)