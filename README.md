<h1 align="center">Hey, I'm Nick.</h1>

<p align="center">
  I run paid ads for <a href="https://appsumo.com">AppSumo</a>. I write about AI agents at <a href="https://nickbuilds.ai">nickbuilds.ai</a>.
</p>

<p align="center">
  This is my GitHub. Most of what's here is the <strong>Paid Ads Agent Stack</strong> I use to run paid channels with Claude Code as the operator.
</p>

---

## The Paid Ads Agent Stack

Every marketer should have a GitHub repo. Here's mine — the [Claude Code](https://claude.com/claude-code) skills I use to run paid channels end to end. Each one is a single repo you can clone in 30 seconds and start using on your own accounts.

### Plan and design the campaign

| Skill | What it does |
|---|---|
| [`apple-grade-design`](https://github.com/nickyc1/apple-grade-design) | Stack Stitch MCP + Nano Banana 2 MCP + UI/UX Pro Max into one design workflow. For landing pages and ad creative that pass the swap test. |

### Run the campaign

| Skill | What it does |
|---|---|
| [`google-ads-manager`](https://github.com/nickyc1/google-ads-manager) | Profit-first Google Ads management. Weekly review, search-term mining, budget reallocation. Circuit breakers + propose-then-approve. |
| [`ppc-profit-intelligence`](https://github.com/nickyc1/ppc-profit-intelligence) | Free agent prompt + Apps Script for connecting Google Ads spend to your real profit data, not Google's reported ROAS. |

### Report on the campaign

| Skill | What it does |
|---|---|
| [`paid-channel-recap`](https://github.com/nickyc1/paid-channel-recap) | Generate a shareable HTML performance recap for any paid-channel campaign. Google Ads + Meta Ads + GA4. Stakeholder-safe redaction by default. |

### Support the rest of the marketing operation

| Skill | What it does |
|---|---|
| [`founder-email-finder`](https://github.com/nickyc1/founder-email-finder) | Enrich a Google Sheet of prospects with verified founder emails. Opinionated waterfall, confidence-scored, dry-run by default. |
| [`granola-action-items`](https://github.com/nickyc1/granola-action-items) | Parse Granola meeting recordings, extract action items, run daily/weekly briefings. With hallucination prevention. |
| [`social-publish-guardrails`](https://github.com/nickyc1/social-publish-guardrails) | Social publishing workflow with a hard human-approval gate. Five-step scaffold, draft mode by default, no bypass. |

---

## How to install one

Pick any skill and:

```bash
git clone https://github.com/nickyc1/<skill-name>.git ~/.claude/skills/<skill-name>
```

Restart Claude Code. The skill is available. Read the SKILL.md and the README in the repo for the specific install steps (most need an MCP server or two configured).

## What you'll probably want to know

- **Are these all by me?** Yes. They came out of running paid ads at scale and getting tired of doing the same operations by hand.
- **Do they only work for marketplaces / lifetime deals / AppSumo-style stuff?** No. They're scrubbed of any AppSumo-specific data and built generic. The opinions are about paid ads, not about any one business model.
- **What's the license?** MIT on all of them. Fork, modify, ship.
- **Will you accept PRs?** Yes, especially if you're using the skill in production and have a small improvement. I read every issue.

## Find me elsewhere

- [nickbuilds.ai](https://nickbuilds.ai) — the AI agent newsletter
- [CXL instructor profile](https://cxl.com/institute/instructors/nick-christensen/) — the courses I teach
- [x.com/nickchristensen](https://x.com/nickchristensen) — short-form posts and arguments
- [linkedin.com/in/nickchristensen](https://www.linkedin.com/in/nickchristensen) — longer-form posts and arguments

If you ship something with one of these skills, I'd love to see it.
