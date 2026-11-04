# Summary: 2026-10-30_19-17-20Z_WhenAIAgentsActonOurBehalf_ATaxonomyofHuman_AgentI.md
Saved: 2026-11-02 21:49
Source: 2026-10-30_19-17-20Z_WhenAIAgentsActonOurBehalf_ATaxonomyofHuman_AgentI.md
Model: None

---

## Summary
This paper investigates the specific forms of failure that occur when AI agents act autonomously on behalf of human users, particularly in contexts involving code execution, UI manipulation, and transactions. By analyzing 695 documented incidents from public repositories, the authors develop a bottom-up taxonomy of 12 distinct failure modes categorized across three interaction stages adapted from Amershi et al.’s guidelines. The study highlights that the nature of these failures is heavily influenced by the level of agent autonomy fixed at deployment, demonstrating that identical models can exhibit different failure patterns depending on how much work is completed between user involvement points. Ultimately, the paper argues for the necessity of intermediate control mechanisms between full delegation and full manual work to mitigate these risks.

## Key Contributions
- **Development of a 12-Mode Failure Taxonomy:** The authors systematically identify and categorize 12 specific failure modes in human-agent interactions, organized by interaction stages rather than just technical errors. This provides a structured framework for understanding how agents fail when acting on behalf of users.
- **Analysis of Autonomy’s Impact on Failure Forms:** The study demonstrates that rising autonomy fundamentally changes the *form* each failure takes, even if the underlying model and task remain constant. It establishes that user recourse is constrained by the deployment configuration, specifically the gaps between points of user involvement.
- **Identification of Gaps in Current Evaluation Methods:** The paper reveals a critical disconnect between existing incident records/agent benchmarks and actual human-agent interaction failures. Current evaluation methods fail to capture the nuanced interactional contexts where these specific failures occur, highlighting a blind spot in current AI safety and usability assessments.

## Methodology
The authors employed a qualitative, bottom-up coding approach to analyze 695 documented incidents sourced from two public repositories. These incidents involved AI agents performing tasks such as writing code, manipulating user interfaces, or executing transactions. The research framework was adapted from Amershi et al.’s guidelines for human-AI interaction, dividing the analysis into three distinct interaction stages. Each incident was coded to identify specific failure modes and, crucially, the level of autonomy present at the time of failure. This method allowed the researchers to correlate specific failure types with varying degrees of agent independence and user involvement points, providing a granular view of how deployment configurations influence failure outcomes.

## Results
The analysis revealed that all 12 identified failure modes appear across both low and high autonomy settings, but their manifestations shift significantly as autonomy increases. A key finding is that the "property fixed at deployment"—specifically, how much work an agent completes between user checkpoints—dictates what a person can do when an agent fails. Consequently, the same model on the same task can fail differently depending on these configuration choices. The results show that current benchmarks and incident records do not adequately capture the interactional dynamics where these failures occur, suggesting that standard performance metrics are insufficient for assessing real-world human-agent safety and usability.

## Significance
This research is significant because it shifts the focus from purely technical model errors to the *interactional* context of AI agent deployment. It underscores that safety and reliability in agentic systems cannot be assessed solely by model capability but must account for the structural design of user involvement. By providing a concrete taxonomy, the paper offers practitioners and researchers a tool to diagnose and mitigate specific interaction failures. It calls for new evaluation frameworks that capture human-agent dynamics and advocates for designing intermediate control mechanisms, bridging the gap between full automation and manual oversight to enhance user safety and agency.

## Related Concepts
- Human-Agent Interaction (HAI)
- AI Agent Autonomy
- Failure Taxonomy
- Human-AI Interaction Guidelines (Amershi et al.)
- Deployment Configuration
- User Control and Oversight
- Agentic Systems Safety

## Original research paper

[Canonical original paper: https://arxiv.org/abs/2611.00291v1]
