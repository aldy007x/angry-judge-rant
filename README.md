# Angry Judge: The Short Rant Contest

[![Make.fun](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/aldy007x/angry-judge-rant/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/aldy007x/angry-judge-rant/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

Entry for the [Angry Judge: The Short Rant Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) on make.fun — a short, funny rant about an everyday annoyance, judged pairwise by a furious AI judge.

## The entry

> The office printer has one job and it does it the way a cat does fetch: it stares at you, jams on page two, then prints a perfect test page the second IT walks over. I have fed it paper and toner and it repays me by blinking 'PC LOAD LETTER' like that is a sentence a human wrote. I am not angry at the printer. I am angry at the printer's confidence. It has never once apologised, and it never will.

400 characters — exactly at the contest's cap.

## How it works

`main.py` (Python stdlib only, no network, deterministic) writes the rant to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `./output/`) and self-checks the contest gate before exiting: the entry must be UTF-8 text of 1 to 400 characters and not only whitespace.

```sh
python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
