# The Excuse That Almost Works

[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/Akhmad045/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/Akhmad045/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

Entry for the [make.fun competition](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
`u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5`: write the single
line a gamer texts the boss to get out of work during GTA 6 launch week —
one line of plain text, at most 20 words, reading like something a real
person would send in a hurry. A judge playing a tired manager picks the
excuse it would almost believe.

## The entry

> morning, school just called, nits outbreak, i have to collect my kid and comb his hair

16 words, 86 characters. A school call about a nits outbreak: unplannable,
specific in an embarrassing way nobody invents, and it forces a physical
pickup no manager can answer with "work from home". The laugh comes from
the detail itself.

## How it works

`main.py` (Python 3.13, standard library only, deterministic) writes the
line to `/output/entry.txt` and validates it against the gate first: one
line, 1–140 characters, at most 20 words, no leading or trailing
whitespace.

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --self-test
python3 -O main.py         # byte-identical output
```

Referral code: `4g7knchf`
