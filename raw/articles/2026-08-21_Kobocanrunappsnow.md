---
title: Kobo can run apps now
date: 2026-08-21
url: https://bandarlabs.github.io/Cobalt/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://bandarlabs.github.io/Cobalt/
source_feed: Hacker News
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-08-21 14:16
---

# Kobo can run apps now

## Full Article

Your Kobo can run apps now.
Cobalt is an open-source application platform for Kobo e-readers: a launcher, a signed App Store, a Rust SDK, and a runtime that keeps every app in its own unprivileged process.
Install it once over USB. Every app after that installs, updates and removes on the reader itself, over Wi-Fi. A reboot returns to the stock Kobo reader.
Install on your Kobo
Read the source
[The Cobalt launcher on a Kobo Clara BW showing Settings, App Store, Terminal, AI Chat, Audiobooks, Components, Daily Brief, Feeds and Gutenbird]
The launcher on a Kobo Clara BW.
Not affiliated with Rakuten Kobo
[A Kobo Clara BW running Audiobook Studio, Gutenbird, Terminal, Hacker News, Sidekick and the App Store, then installing, playing, removing and reinstalling Sudoku over Wi-Fi]
Recorded on-device at 3× speed.
Watch as video.
Running on a Kobo.
Every app is a static ARM binary running as its own unprivileged process on stock hardware. The App Store installs, updates and removes them over Wi-Fi, with signatures verified before anything launches.
arXiv papers and coding agents, on the panel.
These are photographs of the device, not simulator captures. The arXiv app reads the HTML rendering arXiv publishes for every paper since December 2023: abstracts, sections, math and result tables, paginated for the panel.
[An arXiv preprint section titled 'A hard optimization problem and its relaxation' rendered on a Kobo Clara BW]
A preprint, page 8 of 54, on the panel.
[A results table from an arXiv paper comparing language models, rendered on a Kobo e-reader]
A results table from the same paper.
[Mathematical notation and a numbered algorithm from an arXiv paper on a Kobo e-reader]
Math notation and a numbered algorithm.
[Sidekick on a Kobo showing a question from Claude Code with three tappable answers and a 'Leave it for the terminal' button]
Sidekick showing a question from Claude Code, with tappable answers.
[Sidekick's watching screen on a Kobo, paired with a machine on the local network, showing the last answer sent]
Sidekick paired over the local network, waiting for the next question.
Apps
The apps.
Every screenshot below is a capture from a Kobo Clara BW. Store apps version independently of the platform; the rest ship with the platform install.
[Cobalt launcher app grid on e-ink]
Launcher
Opens installed apps and always keeps a route back to the Kobo reader.
[Cobalt App Store catalog listing installed and available apps]
App Store
Installs, updates, removes and reinstalls signed apps over Wi-Fi.
[Newest machine learning preprints listed in the arXiv app on a Kobo]
arXiv
Browses a subject's newest preprints and reads the full text on the panel.
[A complete 81-cell Sudoku game on a Kobo Clara BW]
Sudoku
Store-only by design: installing it proves delivery of an app the USB package never contained.
[The letter S filling the Kobo panel while the front light sends it in Morse]
Morse
Sends a typed message in Morse on the front light, one letter across the whole panel.
[An audiobook player with cover art, position and transport controls on e-ink]
Audiobook Studio
Researches, writes, narrates and plays an original audiobook.
[A shelf of book covers from an OPDS catalogue on a Kobo]
Gutenbird
Reads any OPDS library: Project Gutenberg, Standard Ebooks, Open Library, or yours.
[A ranked list of Hacker News stories on a Kobo e-reader]
Hacker News
Top, New, Ask and Show stories with complete comment threads.
[Subscribed feeds and articles in the Feeds app]
Feeds
Discovers a site's feed and presents its articles without the site's layout.
[A numbered daily news brief on e-ink]
Daily Brief
Collects the day's stories in the background while you use another app.
[An AI answer displayed as readable text on the Kobo panel]
AI Command Center
Asks a question and turns the answer into touch-friendly reading.
[A coding agent request with tappable responses in Sidekick]
Sidekick
Approve or deny requests from coding agents, away from the keyboard.
[A shell and touch keyboard on the Kobo display]
Terminal
A panel-native shell with keys that send input immediately.
[Cobalt typography and UI components on e-ink]
Components
The UI toolkit's controls, layouts, typography and states, on the panel.
[Battery status and hardware facts in Settings]
Settings
Connectivity, hardware, and platform updates, kept separate from Store.
[A persistent to-do list with completed items]
Todo
A persistent list with touch entry and completed-item states.
[A completed game of tic-tac-toe on e-ink]
Tic-tac-toe
Two players, partial refreshes for individual cells.
[The Kobo hall sensor responding to a magnet]
Magnet
Locates the hall sensor behind the bezel and reports its changes.
The SDK
An app is one Rust file.
Implement
KoboApp
, describe screens declaratively, and the runtime handles layout, e-ink refresh planning, Back navigation and lifecycle.
Apps don't open device resources; they ask. Network, storage, audio, frontlight and Wi-Fi are capability-gated, and a refusal comes back as a value the app can handle.
E-ink UI
Text, tiles, dialogs, keyboards, pagination, partial refresh planning
Simulators
Browser and runtime simulators with layout diagnostics
Async work
HTTPS, ranged downloads, cancellable tasks, scheduled wakes
State
Atomic per-app keyed storage
Shipping
Signed static ARMv7 binaries, published when an app PR merges
kobo new my-app
cd
my-app
kobo dev
Read the SDK docs
use
kobo_sdk::{
    ActionId, Context, KoboApp, ScreenBuilder,
};

#[derive(Default)]
struct
Hello { taps: u32 }
impl
KoboApp
for
Hello {
fn
on_start(&
mut
self
, ctx: &
mut
Context) {
self
.show(ctx);
    }
fn
on_action(
        &
mut
self
, ctx: &
mut
Context, a: ActionId,
    ) {
if
a == kobo_sdk::action_id(
"tap"
) {
self
.taps += 1;
        }
self
.show(ctx);
    }
}
impl
Hello {
fn
show(&
self
, ctx: &
mut
Context) {
let
screen = ScreenBuilder::new(
"hello"
)
            .top_bar(
"Hello"
)
            .heading(format!(
"{} taps"
,
self
.taps))
            .button(
"tap"
,
"Tap me"
)
            .build();
        ctx.set_screen(screen);
    }
}
fn
main() {
let
app = Hello::default();
let
_ = kobo_sdk::run(
"hello"
, app);
}
The Store
Signed packages, verified before launch.
Store reads a signed catalog from a fixed GitHub release. Each package holds one ARM executable and a signed canonical manifest. The runtime verifies the catalog, the package, the installed manifest and the binary before an app runs.
App releases are independent of platform releases: merging an app PR builds it for ARM, signs it, and updates the catalog. No Cobalt version bump, no reinstall. The app simply appears in Store.
The Cobalt platform itself also updates over Wi-Fi, through Settings, on a channel separate from the app catalog. The USB cable is only ever needed once.
Install and catalog transactions are recovery-safe; an interrupted update leaves the reader with the version it had.
Publish your own app →
[The Cobalt App Store installing an app over Wi-Fi on a Kobo Clara BW]
Sudoku arriving over Wi-Fi.
FIG. 1 CLARA BW N365
Install
Installing from source.
Charge a Kobo Clara BW (N365)
and connect it over USB. Other models are refused, not guessed at.
Run the setup:
git clone https://github.com/BandarLabs/Cobalt.git
cd
Cobalt
rustup target add armv7-unknown-linux-musleabihf
cargo run -p kobo-cli -- setup
Restart the reader
and open
Cobalt
from Kobo's menu.
Open Store.
Everything from here on arrives over Wi-Fi.
The complete walkthrough, including recovery steps, is in
docs/INSTALL.md
.
Contributing
Contribute an app.
App contributions are regular pull requests. If it runs on your device and the PR shows it running, it gets merged and published.
Build it.
Add the app as a workspace package under
apps/<app-id>/
and register it in
apps/catalog.json
.
Test it.
Add unit and layout tests, and run it in the browser and runtime simulators.
Run it on your own device.
A real Clara BW, not just the simulator.
Open a PR with a gif or photos of it running.
Once reviewed and merged, the publish workflow signs it and it appears in Store. No platform release needed.
Own a different Kobo model?
Porting
is welcome too; open an issue first so the device profile can be agreed. Full details in
docs/CONTRIBUTING_APPS.md
.
Safety
Device support and safety.
Cobalt does not replace Kobo's boot chain. Device writes are gated on an exact hardware and firmware match, and a reboot returns to the stock reader. The first installation does modify files on the user storage partition, and it is provided without warranty.
Only the Clara BW profile has been hardware-tested. Don't install on another model until it has a
reviewed, hardware-tested profile
. Cobalt is an independent project, not affiliated with Rakuten Kobo.

## Metadata
- **Source**: [Original Article](https://bandarlabs.github.io/Cobalt/)
