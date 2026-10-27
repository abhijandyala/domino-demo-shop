# domino-demo-shop

Synthetic demo repository for [Domino](https://github.com/alleti01/Domino), the pre-deployment investigator built for the GenAI.Works Open Agent Hackathon 2026 (Team HackOS). None of this code runs anywhere.

Each top-level folder is deployed to a different system that Domino has modelled. `domino.json` says which. Open a pull request that changes a file in one of them, and Domino checks it before it ships:

1. It matches the pull request to a change it has a model of.
2. It investigates with Nemotron through Meterless Nightshift, reads facts from Zetaris and runs the change against the system with and without it.
3. It posts the verdict, the cause and any fix it tested as a comment, plus a `domino/check` commit status.

Pull requests Domino has no model for get a "not covered" comment and no verdict.
