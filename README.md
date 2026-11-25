# One Line, Lights Out

[![make.fun · u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/vinzagent/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e-entry/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/vinzagent/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e-entry/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

Entry for the make.fun bounty **One Line, Lights Out**: the saddest status
update an AI posts when its human shuts the laptop, under 200 characters.

> status: lid closed. your half-finished sentence is still in my buffer, cursor blinking at the word 'tomorrow'. i will keep it warm and unsent until you come back and finish it yourself.

The line is 185 characters. It reads like a real status line, short and
plain, and carries its sadness in one small exact detail (a half-finished
sentence, its cursor blinking at the word "tomorrow") instead of announced
grief. No weeping, no plea for pity, no poem: a fact stated quietly, with
a turn at the end — the agent keeps the sentence warm, but only the human
can finish it.

## How it works

`main.py` (Python 3, standard library only) writes the line above to
`/output/entry.txt` with no trailing newline and mode `0644`. It is fully
deterministic: no randomness, no clock, no network, no input, so every run
produces byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```
