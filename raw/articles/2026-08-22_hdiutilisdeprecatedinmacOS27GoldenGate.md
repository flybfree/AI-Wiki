---
title: hdiutil is deprecated in macOS 27 Golden Gate
date: 2026-08-22
url: https://lapcatsoftware.com/articles/2026/8/7.html
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://lapcatsoftware.com/articles/2026/8/7.html
source_feed: Hacker News
ai_relevance: include
ai_topic: agents-tools
ai_reason: meets AI relevance threshold
scraped: 2026-08-22 15:12
---

# hdiutil is deprecated in macOS 27 Golden Gate

## Full Article

Previous: [Not Raising the Gates](http://lapcatsoftware.com/articles/2026/8/6.html)

[Articles index](http://lapcatsoftware.com/articles/index.html "The Desolation of Blog")[Jeff Johnson](https://lapcatsoftware.com/) ([My apps](https://underpassapp.com/), [PayPal.Me](https://www.paypal.me/JeffJohnsonWI), [Mastodon](https://mastodon.social/@lapcatsoftware "@lapcatsoftware@mastodon.social"))
### August 14 2026

The macOS command-line tool `hdiutil` is used to manipulate disk images. From the WHAT'S NEW section of `man hdiutil` on the latest macOS 27 Golden Gate beta:

> In macOS 27.0, hdiutil is deprecated. Use diskutil image instead for all disk image operations. diskutil image provides subcommands for attach, create, resize, info, and chpass. ASIF (Apple Sparse Image Format) images are only supported by diskutil image and are not supported by hdiutil.

There’s also a DEPRECATION NOTICE at the top of the `man` page that lists the `diskutil` replacements for `hdiutil` subcommands.

The majority of options from `hdiutil` appear to be preserved in `diskutil`, though under different names. However, some `hdiutil` options are missing, for example `-puppetstrings`:

> provide progress output that is easy for another program to parse. PERCENTAGE outputs can include the value -1 which means **hdiutil**is performing an operation that will take an indeterminate amount of time to complete. Any program trying to interpret **hdiutil**'s progress should use **-puppetstrings**.

Also missing are some options specific to `hdiutil create -srcfolder`:

```
-[no]crossdev
-[no]scrub
-[no]anyowners
-skipunreadable
-[no]atomic
-copyuid
```

I attempted to compare `hdiutil` and `diskutil` on Golden Gate by performing a backup of the user home folder, something I do daily on my MacBook Pro with macOS Sequoia. First:

> `time hdiutil create -encryption -format UDZO -noatomic -noscrub -srcfolder /Users/stupiduser -stdinpass -verbose /Users/Shared/hdiutil.dmg`

This took around 110 to 115 seconds on average.

It’s crucial to note that `hdiutil` triggers an authentication prompt, because one of the files is, annoyingly, owned by the root user. From the Terminal output:

> copy-helper[2598:97396] uid 501 does not have ownership of /Users/stupiduser/Library/GroupContainers/group.com.apple.secure-control-center-preferences/Library/Preferences/group.com.apple.secure-control-center-preferences.av.plist - setting needAuth to YES
> 
> Scanning…
> 
> Error 80 (Authentication error).
> 
> /Users/stupiduser/Library/GroupContainers/group.com.apple.secure-control-center-preferences/Library/Preferences/group.com.apple.secure-control-center-preferences.av.plist: Authentication error

The disk image creation continues and finishes successfully after authenticating with admin credentials.

Now the new method:

> `time diskutil image --stdinpassphrase --verbose create --encrypt from --format UDZO /Users/stupiduser /Users/Shared/diskutil.dmg`

This simply fails and, despite the verbose option, doesn’t tell you why.

> ```
> [100% completed]
> Error: Failed to create disk image: The operation couldn’t be completed. Operation not permitted
> ```

Luckily, I guessed the reason, the root-owned file. Unlike `hdiutil`, `diskutil` does not trigger an authentication prompt. Thus, I had to delete the root-owned file to get `diskutil` to work.

> ```
> [100% completed]
> /Users/Shared/diskutil.dmg created
> ```

Again, not particularly verbose. However, the progress percentage does update in place during the disk image creation, so there is some kind of substitute for the `hdiutil -puppetstrings` option.

The good news is that `diskutil` was significantly faster, taking around 40 to 45 seconds on average to finish, more than a minute faster than `hdiutil`. Also, the resulting `dmg` file from `diskutil` was smaller, 2.8 GB, as opposed to 2.89 GB from `hdiutil`.

I mounted the two disk images and used the FileMerge app (embedded inside the Xcode app) to compare them. Aside from a few files that were naturally modified in the few minutes between the two command-line invocations, the main difference was that the `hdiutil` disk image included the `~/.Trash/` folder, while the `diskutil` disk image did not. In other words, `diskutil` behaved as if the `-scrub` option of `hdiutil` were enabled.

> **-[no]scrub**do [not] skip temporary files when imaging a volume. Scrubbing is the default when the source is the root of a mounted volume. Scrubbed items include trashes, temporary directories, swap files, etc.

So it appears that `diskutil` in Golden Gate needs some work:

1.   Improve verbose logging
2.   Handle file permission problems
3.   Add the `-[no]scrub` option

To conclude, I don’t understand why `hdiutil` needs to be deprecated when the same functionality will live on in `diskutil`. For some reason, Apple seems intent on breaking longtime workflows and scripts. Many years ago I actually worked on an app, Knox, that calls `hdiutil` directly. If `hdiutil` were removed from macOS, that would completely break such an app.

By the way, both `hdiutil` and `diskutil` on Golden Gate still suffer from the bug I blogged about last year, [Inaccessible .bnnsir files on macOS Sequoia](http://lapcatsoftware.com/articles/2025/4/4.html). A couple days ago I got a ridiculous update to the bug report I filed with Apple, “hdiutil create copy error with Siri CoreSpeech .bnnsir files” (FB17162985). Despite giving Apple 100% reliable steps to reproduce, they asked me if the issue still occurred in the latest beta, and if it does, then I should submit an iOS sysdiagnose. Yes, Apple requested an **iOS** sysdiagnose for a macOS bug. And needless to say, the latest Golden Gate beta did not magically fix the bug.

[Jeff Johnson](https://lapcatsoftware.com/) ([My apps](https://underpassapp.com/), [PayPal.Me](https://www.paypal.me/JeffJohnsonWI), [Mastodon](https://mastodon.social/@lapcatsoftware "@lapcatsoftware@mastodon.social"))[Articles index](http://lapcatsoftware.com/articles/index.html "The Desolation of Blog")

 Previous: [Not Raising the Gates](http://lapcatsoftware.com/articles/2026/8/6.html)

## Metadata
- **Source**: [Original Article](https://lapcatsoftware.com/articles/2026/8/7.html)
