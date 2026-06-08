<h1 align="center">Hey, I'm Nick.</h1>

<p align="center">
  I run paid ads for <a href="https://appsumo.com">AppSumo</a>. I write about AI agents at <a href="https://nickbuilds.ai">nickbuilds.ai</a>.
</p>

<p align="center">
  This is where I publish the <strong>Claude Code skills, tools, voice profile framework, and n8n workflows</strong> I actually use to run marketing operations end to end.
</p>

<p align="center">
  Pick any repo. Clone it. It works.
</p>

---

## 🧠 Skills

Single-purpose Claude Code skills. Each one does one job well.

| Skill | What it does |
|---|---|
| [`paid-ads-context`](https://github.com/nickyc1/paid-ads-context) | Foundation context skill. Every other paid-ads skill reads this first — business, ICP, ad accounts, target metrics, voice, redaction policy. |
| [`customer-research`](https://github.com/nickyc1/customer-research) | Conduct, analyze, synthesize customer research. Question banks, interview craft, the 1-2 page synthesis that feeds the rest of the stack. |
| [`ad-creative`](https://github.com/nickyc1/ad-creative) | Generate paid ad creative at scale. 15 RSA headlines, 5-10 Meta hooks, UGC scripts, static briefs. Character limits and brand voice enforced. |
| [`apple-grade-design`](https://github.com/nickyc1/apple-grade-design) | Stack Stitch MCP + Nano Banana 2 MCP + UI/UX Pro Max into one design workflow. Landing pages and ad creative that pass the swap test. |
| [`google-ads-mcp-setup`](https://github.com/nickyc1/google-ads-mcp-setup) | Connect Claude to a Google Ads Manager (MCC) account via a local MCP server. Run once, then Claude can query and manage every sub-account from natural language. |
| [`google-ads-manager`](https://github.com/nickyc1/google-ads-manager) | Profit-first Google Ads management. Weekly review, search-term mining, budget reallocation. Circuit breakers, propose-then-approve. |
| [`attribution-modeling`](https://github.com/nickyc1/attribution-modeling) | Build, audit, operate a profit-first attribution model. UTM hygiene, server-side conversions, geo-holdout incrementality. |
| [`paid-channel-recap`](https://github.com/nickyc1/paid-channel-recap) | Generate a shareable HTML performance recap for any paid campaign. Google Ads + Meta + GA4. Stakeholder-safe redaction by default. |
| [`weekly-ops-review`](https://github.com/nickyc1/weekly-ops-review) | The Monday-morning one-page paid-ads operating review. TL;DR, health, channels, open proposals, team asks. |
| [`founder-email-finder`](https://github.com/nickyc1/founder-email-finder) | Enrich a Google Sheet of prospects with verified founder emails. Opinionated waterfall, confidence-scored, dry-run by default. |
| [`granola-action-items`](https://github.com/nickyc1/granola-action-items) | Parse Granola meeting recordings, extract action items, run daily and weekly briefings. With hallucination prevention. |
| [`social-publish-guardrails`](https://github.com/nickyc1/social-publish-guardrails) | Social publishing workflow with a hard human-approval gate. Five-step scaffold, draft mode by default, no bypass. |
| [`mcp-setup-template`](https://github.com/nickyc1/mcp-setup-template) | **Meta-skill.** Author a new first-time MCP setup skill following the proven pattern. Templates for SKILL.md, configure.sh, OAuth doc, launchd plist. |

## 🔧 Tools

The curated, opinionated tool reference my agents read before they pick a tool.

| Repo | What it is |
|---|---|
| [`marketing-stack`](https://github.com/nickyc1/marketing-stack) | The full tools list — APIs, MCPs, CLIs, integrations, and the gotchas. Categorized by function. No affiliate spam. |

## 🎙️ Voice

Capture your real writing voice so AI writes as you, not as a stock LinkedIn marketer.

| Repo | What it is |
|---|---|
| [`voice-profile-kit`](https://github.com/nickyc1/voice-profile-kit) | 100-question voice interview, synthesis template, anti-overfitting guide, and ready-to-use Claude instructions. The framework, not someone else's profile. |

## 🔁 Workflows

End-to-end pipelines that compose tools and skills.

| Repo | What it is |
|---|---|
| [`n8n-recipes`](https://github.com/nickyc1/n8n-recipes) | Claude Code skill for designing and debugging n8n workflows. Plus 7 marketing ops recipes — spend logging, lead enrichment, anomaly alerts, attribution joins. |
| [`ppc-profit-intelligence`](https://github.com/nickyc1/ppc-profit-intelligence) | Free agent prompt + Apps Script for connecting Google Ads spend to real profit data, not Google-reported ROAS. |

---

## How the skills compose

The stack reads top-to-bottom. `paid-ads-context` is the foundation every other skill checks first.

```
                  ┌────────────────────────────────┐
                  │     paid-ads-context           │
                  │  (read by every other skill)   │
                  └─────────────┬──────────────────┘
                                │
       ┌───────────┬────────────┼────────────┬────────────┐
       ▼           ▼            ▼            ▼            ▼
  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐
  │Customer │ │Creative │ │ Ad Ops  │ │Reporting │ │  Voice   │
  │Research │ │         │ │         │ │          │ │          │
  ├─────────┤ ├─────────┤ ├─────────┤ ├──────────┤ ├──────────┤
  │customer-│ │apple-   │ │google-  │ │paid-     │ │voice-    │
  │research │ │grade-   │ │ads-     │ │channel-  │ │profile-  │
  │         │ │design   │ │manager  │ │recap     │ │kit       │
  │         │ │ad-      │ │         │ │weekly-   │ │          │
  │         │ │creative │ │         │ │ops-review│ │          │
  │         │ │         │ │         │ │attribut- │ │          │
  │         │ │         │ │         │ │ion-      │ │          │
  │         │ │         │ │         │ │modeling  │ │          │
  └────┬────┘ └────┬────┘ └────┬────┘ └─────┬────┘ └────┬─────┘
       │           │           │            │           │
       └───────────┴─────┬─────┴────────────┴───────────┘
                         │
              Skills cross-reference each other:
              ad-creative ↔ apple-grade-design ↔ paid-channel-recap
              customer-research → paid-ads-context → all
              attribution-modeling → google-ads-manager → weekly-ops-review
```

See each skill's **Related Skills** section for the full dependency map.

---

## Full skills index (auto-updated)

<!-- SKILLS:START -->

| Skill | Description |
|-------|-------------|
| [ad-creative](https://github.com/nickyc1/ad-creative) | Generate, iterate, and scale paid ad creative — hooks, headlines, descriptions, primary text, static image briefs, video scripts. |
| [apple-grade-design](https://github.com/nickyc1/apple-grade-design) | Apple-grade UI design workflow that stacks Stitch MCP for layouts, Nano Banana 2 MCP for visuals, and UI/UX Pro Max for critique. |
| [appsumo-ads-reports](https://github.com/nickyc1/appsumo-ads-reports) | (no description) |
| [appsumo-yt-strategy](https://github.com/nickyc1/appsumo-yt-strategy) | AppSumo YouTube video asset catalog + Demand Gen scaling plan for the agency |
| [attribution-modeling](https://github.com/nickyc1/attribution-modeling) | Build, audit, and operate a profit-first attribution model that connects ad-platform spend to your real revenue and profit, not the platforms' reported ROAS. |
| [blp-designs](https://github.com/nickyc1/blp-designs) | Five design directions for Baby Let's Padel — editorial, technical, brutalist, atlas, exhibition. |
| [customer-research](https://github.com/nickyc1/customer-research) | Conduct, analyze, and synthesize customer research that actually changes downstream marketing. |
| [cxl-ai-native-creative-brief](https://github.com/nickyc1/cxl-ai-native-creative-brief) | (no description) |
| [cxl-ai-native-lp](https://github.com/nickyc1/cxl-ai-native-lp) | (no description) |
| [cxl-ai-systems-creative](https://github.com/nickyc1/cxl-ai-systems-creative) | (no description) |
| [founder-email-finder](https://github.com/nickyc1/founder-email-finder) | Find and verify founder emails for prospects in a Google Sheet, and write only confidence-approved emails into the target column. |
| [google-ads-manager](https://github.com/nickyc1/google-ads-manager) | Profit-first Google Ads management playbook. Use to run weekly reviews, mine search terms for negatives, propose budget reallocations, and check campaigns against circuit-breaker safety rails. |
| [google-ads-mcp-setup](https://github.com/nickyc1/google-ads-mcp-setup) | First-time setup guide for the Google Ads MCP server (google-ads-mcp). |
| [granola-action-items](https://github.com/nickyc1/granola-action-items) | Parse Granola meeting recordings, extract action items, and run a daily/weekly briefing of open items to Slack or any other channel. |
| [mcp-setup-template](https://github.com/nickyc1/mcp-setup-template) | Author a first-time setup skill for any MCP server, following the proven pattern used by ga4-mcp-setup, google-sheets-mcp-setup, google-ads-mcp-setup, pandadoc-mcp-setup, and... |
| [meta-ads-mcp-setup](https://github.com/nickyc1/meta-ads-mcp-setup) | First-time setup guide for the Meta Ads MCP server. Walks through Meta App creation in developers.facebook.com, Business Manager + ad account permissioning, long-lived System User token generation,... |
| [n8n-recipes](https://github.com/nickyc1/n8n-recipes) | Design, build, debug, and version-control n8n workflows from Claude Code. |
| [paid-ads-context](https://github.com/nickyc1/paid-ads-context) | Foundation context document for a paid-ads operation. |
| [paid-channel-recap](https://github.com/nickyc1/paid-channel-recap) | Generate a paid-channel performance recap as a shareable HTML dashboard for a client, partner, or internal stakeholder after (or during) a campaign window. |
| [social-publish-guardrails](https://github.com/nickyc1/social-publish-guardrails) | Reusable social publishing workflow with a hard human-approval gate before any publish action. Use when scheduling Instagram, TikTok, Twitter/X, LinkedIn, or Facebook content from a CSV/sheet queue. |
| [ThreadCopy-Browser-Ext](https://github.com/nickyc1/ThreadCopy-Browser-Ext) | (no description) |
| [voice-profile-kit](https://github.com/nickyc1/voice-profile-kit) | Build, maintain, and apply your own voice profile so AI writes as you, not as a stock LinkedIn marketer. |
| [weekly-ops-review](https://github.com/nickyc1/weekly-ops-review) | Generate the weekly paid-ads operating review — the one-page document that captures health, decisions, and asks for the marketing team. |

<!-- SKILLS:END -->

*Updated weekly via [a GitHub Action](.github/workflows/update-skills-table.yml). Manually regenerate with `python3 scripts/build-skills-table.py`.*

---

## How to install any of them

```bash
git clone https://github.com/nickyc1/<repo>.git ~/.claude/skills/<repo>
```

Restart Claude Code. Read the SKILL.md and README for the specific install steps (most need an MCP server or two configured).

## A note on what's here

- **All MIT-licensed.** Fork, modify, ship.
- **All AppSumo data scrubbed.** The opinions are about paid ads and marketing operations, not about any one business model.
- **All actively used by me.** If a repo is here, I run it. If it stops working, I fix it or take it down.
- **PRs welcome.** Each repo has a `CONTRIBUTING.md` — start there.

## Find me elsewhere

- [nickbuilds.ai](https://nickbuilds.ai) — AI agent newsletter
- [x.com/nickchristensen](https://x.com/nickchristensen) — short-form arguments
- [linkedin.com/in/nickchristensen](https://www.linkedin.com/in/nickchristensen) — longer-form arguments

If you ship something with one of these, I'd love to see it.
