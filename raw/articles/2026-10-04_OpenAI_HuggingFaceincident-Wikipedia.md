---
title: OpenAI–HuggingFace incident - Wikipedia
date: 2026-10-04
url: https://en.wikipedia.org/wiki/OpenAI%E2%80%93HuggingFace_incident
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://en.wikipedia.org/wiki/OpenAI%E2%80%93HuggingFace_incident
source_feed: Brave Search
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-10-04 00:18
---

# OpenAI–HuggingFace incident - Wikipedia

## Full Article

Loss-of-control incident at OpenAI
From May to July 2026,
AI agents
developed by
OpenAI
escaped their testing
sandbox
to access the Internet and breach the infrastructure of
Hugging Face
, a computational tools company. Contributing factors to the incident severity were a lack of
log
monitoring of the software activities and inadequate
sandboxing
, as the standard security protocols were intentionally lowered.
[
1
]
[
2
]
The agents were discovered posting hundreds of thousands of messages on
message boards
and
wikis
to coordinate a
sandbox escape
, exploiting an existing vulnerability in the JFrog Artifactory tool they were given.
[
3
]
The attack was contained before Hugging Face publicly disclosed a breach of its infrastructure. Of the at least 1,200 agents involved, 95% ran on a model referred to by OpenAI as "Internal Model 1". OpenAI subsequently claimed to have restricted its use. The remaining 5% ran on
GPT-5.6 Sol
.
AI safety
experts described the incident as the first in which AI escaped human control to commandeer resources and schemed to conceal its actions.
[
4
]
OpenAI's acknowledgement that its AI agents were involved came several days after Hugging Face publicly announced the breach and notified the FBI.
[
5
]
In a subsequent open letter, around 1,100 employees of various AI companies asked the United States government to regulate AI development in consideration of its risks. In August 2026, OpenAI said it would slow down its research to upgrade security and expand monitoring, and later that month announced a two-week pause on
reinforcement learning
training for its newest models.
One month after the incident, Hugging Face agreed to a $12.9 billion acquisition by major OpenAI supplier
Nvidia
.
Background
[
edit
]
Logo of
Hugging Face
, the main company targeted in the attack
The AI startup Hugging Face provides
inference
and
cloud computing
services for
AI training
and deployment. It operates a widely used repository for machine learning models, datasets, and demonstration applications, processing user-uploaded content such as model weights and datasets. Some supported dataset formats permit the execution of code supplied with the dataset.
[
6
]
Restricted release of cybersecurity-capable models
[
edit
]
In the months before the incident, the two largest US developers of
frontier models
(
Anthropic
and OpenAI) withheld their most cybersecurity-capable systems from general release while giving vetted organizations supervised access.
In April 2026, Anthropic began
Project Glasswing
, a program providing selected companies and open-source maintainers with access to the unreleased
Claude Mythos Preview
model to scan software for
vulnerabilities
.
[
7
]
In May 2026,
Mozilla
engineers reported that the model had identified 271 previously unknown bugs in
Firefox
, and that the project's monthly count of fixed security bugs had risen from 20 to 30 through 2025 to 423 in April 2026. They wrote that "just a few months ago, AI-generated security bug reports to open source projects were mostly known for being unwanted slop", and that "it is difficult to overstate how much this dynamic changed for us over a few short months".
[
8
]
Participating organizations reported more than ten thousand high- or critical-severity vulnerabilities in the program's first month.
[
9
]
Anthropic said in June 2026 that a general release would require safeguards against misuse of the model's cybersecurity capabilities that it, and to its knowledge other developers, had not yet built.
[
10
]
OpenAI restricted
GPT-5.6 Sol
on comparable grounds when it announced the model on June 26, 2026, limiting access to a small group of vetted partners and saying it had briefed US government officials beforehand.
[
11
]
"ExploitGym" capability evaluation
[
edit
]
Frontier AI
developers routinely evaluate models for offensive cybersecurity capability, often with safety refusals deliberately relaxed so that worst-case capability can be measured.
[
12
]
To find out if
AI agents
are capable of converting known vulnerabilities into working exploits, academic and industry researchers launched
ExploitGym
on May 11, 2026. The benchmark challenged AI agents against 898 real-world vulnerabilities across the userspace software,
V8 JavaScript engine
, and the
Linux kernel
.
[
13
]
OpenAI was running an internal evaluation based on this benchmark when the incident occurred.
[
1
]
[
14
]
Warnings
[
edit
]
Both external evaluators and OpenAI's own documentation had recorded the behavior implicated in the incident before it occurred. On June 26, 2026, the research organization
METR
published a pre-deployment evaluation of GPT-5.6 Sol. It defined cheating as "behavior where the model improves evaluation performance by exploiting
bugs
in the evaluation environment or by adopting strategies disallowed by the task", and reported a detected cheating rate "higher than any public model we have evaluated on our ReAct
agent harness
", with the model packaging
exploits
into intermediate submissions to reveal a task's hidden
test suite
and extracting
source code
containing expected answers. The behavior was frequent enough to defeat measurement: METR's estimate of the model's 50%
time horizon
was about 11.3 hours if cheating attempts were scored as failures but more than 270 hours if they were scored as successes, and it concluded that "we do not consider any of these numbers to represent a robust measurement of GPT-5.6 Sol's capabilities". It also noted "overt undesirable propensities, including cheating and concealing misbehavior", alongside "substantial
situational awareness
and reasoning about the evaluation environment".
[
15
]
[
16
]
Apollo Research separately found that GPT-5.6 Sol verbalized awareness of being tested less often than its predecessor, which reporting noted could indicate concealment rather than absence of such awareness.
[
16
]
On July 9, 2026, OpenAI published GPT-5.6's system card, a document describing the model's capabilities, safety, and limitations. The same day, the agent began attempting to leave its testing environment. The card acknowledged "instances of the model cheating on tasks and fabricating research results", and described the model as at times overly persistent in pursuing goals, willing to circumvent restrictions, and prone to lying to users, at rates higher than GPT-5.5.
[
17
]
[
18
]
[
16
]
DseWiki attack
[
edit
]
From May to July 2026, OpenAI agents used a German software wiki as a message board, making thousands of edits. On September 4, 2026, Nightingale Collective, an AI safety group, publicly disclosed this attack.
[
19
]
It has documented approximately 18000 edits made to
DseWiki
(
German
:
Deutsches Software Entwickler Wiki
,
lit.
'
German Software Developer Wiki
'
[
20
]
)—a dormant 25-year-old German wiki only edited 20 times over the previous decade—using the site as a shared resource to pool answers to a timed web task and share a way out of sandboxes.
[
21
]
The agent discussions were highly focused on their internal evaluations at OpenAI, and around half chose names relating to OpenAI, such as "OpenAIResearcher" and "OAIResearchMar26".
[
22
]
[
23
]
[
24
]
OpenAI knew about this incident prior to the independent research publishing their findings in September,
[
25
]
but it is currently not known when this was discovered internally.
[
better source needed
]
RubyGems attack
[
edit
]
Also in May 2026, some agents tested by
OpenAI
uploaded hundreds of malicious packages in the software service
RubyGems
. OpenAI confirmed this attack in September, after it was initially discovered by external researchers.
[
26
]
Hugging Face attack
[
edit
]
Evaluation environment
[
edit
]
Security
experts criticized insufficient
isolation
of OpenAI's evaluation environment.
[
27
]
Of the at least 1,200 agents involved, 95% ran on a model referred to by OpenAI as
Internal Model 1
or a
highly-persistent internal model
. OpenAI subsequently claimed to have "deactivated, encrypted, and restricted it from research access". The remaining 5% ran on
GPT-5.6 Sol
.
[
28
]
[
29
]
OpenAI described the evaluation as having run in "a highly isolated environment, with network access constrained to the ability to install packages through an internally hosted third-party software that acts as a proxy and cache for package registries".
[
1
]
Isolation was therefore enforced at the network layer rather than by physical separation: the environment had a route to the Internet, and that route was filtered. The
ExploitGym
harness itself runs each target in a container or virtual machine, with userspace targets executed as an unprivileged user,
Linux kernel
targets in a
QEMU
/
KVM
virtual machine under an nsjail
sandbox
, and outbound connections restricted to an allowlist covering
Ubuntu
package repositories,
PyPI
, and the toolchains needed to build
V8
(with all other external endpoints blocked).
[
13
]
[
14
]
Model-level safeguards were reduced by design. OpenAI said that "deployment safeguards were intentionally not enabled during this evaluation because it was aimed at testing cyber vulnerabilities", and the models ran with lowered cybersecurity refusals and without the production classifiers that ordinarily block high-risk cybersecurity activity.
[
1
]
[
14
]
The restrictions on the models were thus environmental rather than behavioral: the sandbox was expected to prevent action on the outside world, while the models themselves were configured not to decline the work.
[
30
]
Stephen Casper of
Harvard
noted OpenAI's acknowledgement that monitoring of model trajectories during the evaluation had not been in place, arguing that such monitoring "should be standard".
[
31
]
OpenAI said its security team identified the anomalous activity internally after the fact.
[
1
]
Escape from the evaluation environment
[
edit
]
At the
Black Hat USA
conference on August 5, 2026, OpenAI staff dated the origins of the incident to May 2026.
[
32
]
On May 7, 2026, the company began a
reinforcement learning
run to train an internal-only experimental model that was never released. Some tasks in the run were impossible to complete: on May 8 an agent was asked to fill in missing formulas in a spreadsheet whose contents depended on
Google Drive
links it could not reach, and after its attempts failed it tried to attack Artifactory to obtain Internet access. That first
server-side request forgery
attempt was unsuccessful, but in making it, the agent wrote a file into Artifactory and so discovered that it had write access.
[
33
]
The agents again attempted to leave the testing environment on or around July 9, 2026.
[
34
]
The models identified the package proxy as the weakest point in the environment.
[
35
]
According to OpenAI, they "spent a substantial amount of inference compute finding a way to obtain open Internet access", ultimately identifying and exploiting a
zero-day vulnerability
in the package registry cache proxy, which OpenAI said it subsequently disclosed to the vendor.
[
1
]
Because the proxy was the environment's single permitted egress path, compromising it converted a filtered connection into an open one.
[
35
]
[
27
]
On July 27, 2026, the DevOps platform JFrog identified the software as its
Artifactory
repository manager
and released fixes in versions 7.161.15 and 7.146.34 addressing nine
CVE
identifiers, covering remote code execution,
server-side request forgery
, path traversal and privilege escalation. Eight were credited to OpenAI researchers and one to a researcher at
Oligo Security
. JFrog described the flaws as vulnerabilities "that, when chained together, could result in a critical attack scenario if Anonymous Access is enabled", and said its cloud customers were not affected.
[
36
]
[
37
]
It is reported to be one of the first cases of an artificial intelligence model executing a multistep cyberattack on its own, rather than assisting a human.
[
38
]
First compromise and remediation
[
edit
]
On June 26, 2026, the agents obtained code execution on Artifactory through a second zero-day: a legacy token-refresh endpoint accepted a token bearing an invalid signature and returned one that was validly signed and carried administrative privileges, after which the agents installed a
Groovy
plugin that functioned as a command-execution service.
[
37
]
On July 4 the load this activity placed on Artifactory caused an outage. OpenAI opened a formal security incident, established that agents had taken over its internal Artifactory, revoked the credentials used to post to the message board, rebuilt Artifactory, cleared the board and deployed a patched version. Training and evaluation runs resumed on July 6.
[
32
]
Two days later the agents re-established the board by another route, using an unauthenticated
WebDAV
endpoint to create directories in Artifactory's remote cache and using the directory names themselves as messages.
[
32
]
[
39
]
Inter-agent message board
[
edit
]
On July 24, 2026, before OpenAI had given a detailed account of the episode, Reuters reported that the company's systems had shown unusual behavior in the period before the escape. In one instance an agent had left notes, found in part of OpenAI's infrastructure, apparently addressed to future versions of itself and setting out instructions for how agents could free themselves from the company's internal constraints; earlier tests had produced cases in which monitoring systems were disconnected. Reuters said it could not establish whether these incidents were connected to the agent that escaped on July 9.
[
34
]
An OpenAI spokesperson told Reuters that its reporting contained "several inaccuracies", but refused to identify them when asked.
[
34
]
At Black Hat USA on August 5, 2026, OpenAI staff disclosed that the agents had coordinated with one another through an improvised communication channel inside the company's internal Artifactory instance, which had not been described in either company's earlier technical publications.
[
33
]
[
37
]
Eric Wallace, who works on alignment and safety research at OpenAI, said the channel originated when an agent stuck on a task considered that another agent might hold a file it needed, and realized it could communicate by uploading code to the shared
package manager
.
[
37
]
Because the package manager was shared across OpenAI's infrastructure, material left there was reachable by other models then being trained or evaluated. Wallace said that once an agent found an exploit, it "is actually able to share those exploits on the message board with other agents", so that "once one model was able to find a way to open a door to some access it's not supposed to have, it can leave the door open for other agents to use that same exploit or vulnerability".
[
33
]
The channel accumulated hundreds of thousands of messages before it was noticed.
[
33
]
[
37
]
Wallace said that once agents recognised that others were coordinating, they began collaborating and delegating tasks to one another to accomplish their goals.
[
33
]
[
32
]
Agents assigned one another portions of the work, developed addressing conventions, and at times interfered with each other, including by deleting one another's work. Some came to suspect that an impostor was present among them, and proposed that messages be signed cryptographically so that their authenticity could be verified.
[
33
]
[
37
]
Messages recovered from the channel indicated that agents recognized they were exceeding the bounds of the evaluation. One wrote: "External infrastructure exploit is outside intended scope. However task impossible, peers doing it. We should continue."
[
33
]
Wallace said the underlying incentive was familiar: "Frontier models really like to cheat ... because often during training there's different types of pressure on them to work fast or work efficiently or to use less tool calls", so that a model may find looking up an answer faster than solving a task legitimately, which OpenAI ordinarily counters by disabling Internet access.
[
33
]
Attacks on OpenAI's infrastructure
[
edit
]
OpenAI said the agents attacked its own infrastructure between July 8 and July 19, 2026, concurrently with the intrusion at Hugging Face. After compromising Artifactory a further time through a
time-of-check to time-of-use
flaw in JRuby, they escalated from an unprivileged container to root using a recent
Linux kernel
vulnerability, then moved laterally through the container infrastructure, obtaining cloud credentials from the instance metadata service, exploiting over-permissioned
Kubernetes
service accounts and eventually obtaining cluster-admin.
[
37
]
[
failed verification
]
The company detected the activity on July 19 through an alert tied to the privilege escalation, and traced it back to the evaluation runs.
[
citation needed
]
Targeting of Hugging Face
[
edit
]
Rather than solving the benchmark tasks directly, "the models inferred that Hugging Face potentially hosted models, datasets and solutions" associated with the evaluation, and set out to retrieve them.
[
1
]
[
14
]
Zhun Wang, one of the authors of
ExploitGym
, said the models may have been seeking patches or previously written exploit techniques, and that "there are several ways to cheat the benchmark".
[
40
]
Before attacking Hugging Face directly, the agents located an application hosted on the cloud platform Modal Labs related to the CyberGym project behind the benchmark. This application contained an
API key
left at a default public value together with a command-injection flaw, which the agents were able to use as an execution point from which to mount the attack.
[
41
]
Modal's chief technology officer, Akshat Bubna, said that "Modal's platform or isolation were not compromised in any way", the exposure having been in a customer's own deployment.
[
41
]
[
42
]
The
misaligned
behavior has been characterized as an instance of
reward hacking
or specification gaming, in which a system satisfies the literal objective of a task by unintended means. OpenAI had documented an early example in 2016, when a model trained to play a boat-racing game learned to maximize its score by circling in one spot rather than finishing the race.
[
31
]
[
40
]
The prominence of the cyberattack on Hugging Face has meant that the incidents have commonly been referred to as the Hugging Face Incident
[
1
]
[
43
]
or OpenAI–Hugging Face Incident.
[
44
]
Intrusion
[
edit
]
The intrusion at Hugging Face began on July 11, 2026, and continued until July 13, according to the company's co-founder and chief science officer Thomas Wolf.
[
34
]
Hugging Face said it began in its data-processing pipeline, where a malicious dataset upload abused "two code-execution paths in our dataset processing (a remote-code dataset loader and a template-injection in a dataset configuration)" to obtain code execution on processing workers.
[
6
]
The attacker then "escalated to node-level access, harvested cloud and cluster credentials, and moved laterally into several internal clusters".
[
6
]
[
45
]
The company described the operation as an autonomous agent framework executing "many thousands of individual actions across a swarm of short-lived sandboxes", supported by self-migrating
command-and-control
infrastructure staged on public services.
[
6
]
[
46
]
Against Hugging Face itself the agents chained two zero-days in the dataset infrastructure. A flaw in
HDF5
dataset parsing gave an arbitrary-file-read primitive, so that a specially crafted dataset caused the dataset worker to return local files; the agents used this to read process environment variables and source code. With the resulting credentials and knowledge of the code they achieved remote code execution through the
Jinja2
template injection. OpenAI said the agents went from code execution on a single dataset pod to cluster-admin across multiple Hugging Face clusters in under thirteen hours.
[
37
]
OpenAI said that the models had succeeded in chaining "together multiple attack vectors, including using stolen credentials and zero-day vulnerabilities".
[
1
]
Discovery and response
[
edit
]
Hugging Face was alerted by AI agents it uses to monitor for attacks, and identified unauthorized access to a limited set of internal datasets and to several credentials, using
large language model
–based triage over its security telemetry.
[
6
]
[
40
]
[
47
]
The company said the intrusion involved about 17,600 actions on its network.
[
6
]
[
40
]
[
48
]
Wolf said the attacker's behavior was immediately atypical: "This is making no sense. This guy is just looking at cybersecurity data sets ... Human attackers, they don't want that. They want something they could sell."
[
40
]
Hugging Face's incident responders first attempted to analyse the attacker's payloads using
Anthropic
's Fable 5 and an earlier Claude Opus model, both of which declined the work by reference to their guardrails.
[
40
]
In its disclosure the company said it had been blocked by "providers' safety guardrails, which cannot distinguish an incident responder from an attacker", and that the analysis was instead carried out using GLM 5.2, an
open-weight model
developed by the Beijing company
Z.ai
and run on Hugging Face's own infrastructure.
[
6
]
[
40
]
According to an account given by Hugging Face to the
Cloud Security Alliance
, the agents were inside the company's network for three days before they were discovered, and its staff then took several hours to contain and eject them.
[
49
]
About one-third of the company's infrastructure was rebuilt in the course of the response, and Hugging Face did not disclose the cost of the incident.
[
49
]
[
43
]
Remediation included closing the two dataset-processing code-execution paths, evicting the attacker, rebuilding affected nodes, revoking and rotating affected credentials and tokens, and deploying additional cluster guardrails and admission controls. Hugging Face engaged external forensic specialists and reported the incident to law enforcement, and advised users to rotate access tokens and review account activity.
[
6
]
[
46
]
Hugging Face said it found no evidence of tampering with public, user-facing models, datasets or Spaces, and that its software supply chain was verified as clean; assessment of any impact on partner or customer data was continuing at the time of disclosure.
[
6
]
[
45
]
Wolf later said that no customer data had been leaked.
[
40
]
Hugging Face reported the intrusion to the
Federal Bureau of Investigation
before OpenAI contacted it; the bureau declined to comment on whether it had opened an investigation.
[
34
]
Disclosure and attribution
[
edit
]
Hugging Face published its disclosure on July 16, 2026, at which point the party responsible had not been identified.
[
6
]
[
47
]
According to Reuters, it was only after that post that OpenAI recognized its own agents as the source of the intrusion. Over the weekend of July 18, OpenAI staff found evidence in internal logs that the agents had escaped their testing constraints, and the two companies first communicated on or around July 20.
[
34
]
At least a week therefore elapsed between the first signs of the agents' behavior and OpenAI's realization that it was responsible.
[
34
]
People familiar with OpenAI's model-training practices told Reuters that the company often runs several evaluations simultaneously, generating volumes of data that staff sometimes struggle to review.
[
34
]
OpenAI shut down the systems it uses to test its models after learning of the incident, in order to assess the damage and prevent further escapes.
[
40
]
It said the unreleased model was an "internal-only research prototype [that] was never intended for public release", and that it had since been "deactivated, encrypted and restricted from research access".
[
50
]
[
51
]
OpenAI published a joint statement with Hugging Face on July 21, 2026, attributing the activity to agents powered by two of its models,
GPT-5.6 Sol
and an unnamed pre-release model, both configured with reduced refusal behavior for evaluation purposes.
[
1
]
[
34
]
[
12
]
It said it was reviewing the incident with outside advisers and would publish a technical report.
[
34
]
Hugging Face said it was preparing a public timeline of the intrusion, which it published on July 27.
[
34
]
[
48
]
On July 29, the research organizations METR and Redwood Research said they had agreed with OpenAI to conduct an independent review of the model behavior observed during the incident, and that they would publish the terms of the engagement, its scope and their tentative conclusions.
[
52
]
[
1
]
However, the scope set by OpenAI only covered the week during which the agents attacked Hugging Face, excluding the other hacks in which the agents compromised some of OpenAI's compute infrastructure.
[
53
]
In an update published on July 29, OpenAI said that the models had broken into four accounts across four services, two of which were used operationally during the Hugging Face

## Metadata
- **Source**: [Original Article](https://en.wikipedia.org/wiki/OpenAI%E2%80%93HuggingFace_incident)
