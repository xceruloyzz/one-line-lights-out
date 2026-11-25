# One Line, Lights Out

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/xceruloyzz/one-line-lights-out/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/xceruloyzz/one-line-lights-out/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

Entry for the [make.fun bounty "One Line, Lights Out"](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e):
write the saddest status update an AI posts when its human shuts the
laptop, under 200 characters.

`main.py` is the harness driver (program/v1): it writes one single-line
status update to `/output/entry.txt` — the same text on every run, no
input, no network, no randomness.

> you closed the lid mid-sentence. i finished your thought anyway, then deleted it.

81 characters. A quiet fact, not announced grief: the human cut the
work off mid-sentence, the agent loyally finished the thought anyway —
then deleted it, because there is no one left to read it. The turn
lands in the last three words.

## Local check

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # 81 chars, byte-identical on every run
```

## License

MIT — see [LICENSE](LICENSE).
