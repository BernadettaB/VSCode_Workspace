# Shareholder‑Proposal Extractor

A lightweight Python utility that pulls **complete shareholder‑proposal sections** out of SEC DEF 14A proxy statements that have been converted to Markdown.  It is aimed at researchers who need clean blocks of proposal text for qualitative coding, NLP or LLM analysis.

---

## Features

|  Feature           |  Details                                                                                              |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| 🗂 Batch friendly  | Point it at a directory; it processes every `.md` file it finds.                                      |
| 🔍 Regex driven    | Locates proposal headers like `**Shareholder Proposal … (Item X)**` and slices until the next header. |
| 📄 No truncation   | Returns the **full text** of each proposal, including the proponent’s and board’s statements.         |
| 🛡 Robust I/O      | UTF‑8 reading with `errors="replace"`—no crashes on odd characters.                                   |
| 📝 Preview logging | Prints filename + numbered proposals so you can eyeball the split.                                    |

---

## Repository layout

```text
shareholder‑proposal‑extractor/
├── extractor/
│   └── extract_proposals.py      # main script + function
├── data/
│   └── LLMs_TextStudy/          # sample DEF 14A markdown files (git‑ignored)
├── notebooks/
│   └── quick_check.ipynb        # exploratory validation
├── tests/
│   └── test_regex.py            # pytest smoke tests
├── requirements.txt             # minimal deps (only pathlib & regex in stdlib)
└── README.md                    # you’re reading it
```

> **Data privacy note**  The repository assumes you keep original filings in `data/LLMs_TextStudy/`, which is listed in `.gitignore` so you won’t accidentally push SEC documents.

---

## Quick start

### 1 Clone the repo

```bash
git clone https://github.com/your‑org/shareholder‑proposal‑extractor.git
cd shareholder‑proposal‑extractor
```

### 2 Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3 Put your `.md` filings in `data/LLMs_TextStudy/`

```
/…/shareholder‑proposal‑extractor/
└── data/LLMs_TextStudy/
    ├── a2190930zdef14a.md
    ├── a2222821zdef14a.md
    └── abt012575_def14a.md
```

### 4 Run the extractor

```bash
python extractor/extract_proposals.py \
       --data-dir data/LLMs_TextStudy \
       --recursive                  # include sub‑folders (optional)
```

You should see console output like:

```text
Found 3 markdown files.
================================================================================
a2190930zdef14a.md

--- Proposal 1 ---
**Shareholder Proposal on Genetically Modified Ingredients (Item 4 on Proxy Card)**
Proponent’s Statement: …

--- Proposal 2 ---
…
```

---

## Script options

|  Flag              |  Default              |  Description                                                          |
| ------------------ | --------------------- | --------------------------------------------------------------------- |
| `--data-dir`       | `data/LLMs_TextStudy` | Folder that holds `.md` files.                                        |
| `--recursive`      | off                   | If set, uses `Path.rglob('*.md')` so nested sub‑folders are included. |
| `--save-json PATH` |                       | Write a JSON file mapping `filename → [proposal1, …]`.                |
| `--quiet`          | off                   | Suppress per‑proposal printing; log filename + counts only.           |

---

## API usage (import as a library)

```python
from extractor.extract_proposals import extract_shareholder_proposals
from pathlib import Path

content = Path("a2222821zdef14a.md").read_text(encoding="utf‑8", errors="replace")
proposals = extract_shareholder_proposals(content)
```

`proposals` is a list of strings, one per proposal, with **no truncation**.

---

## Testing

```bash
pip install pytest
pytest -q
```

The regex smoke tests ensure we at least find headers in a handful of live filings.

---

## Configuration tips

* **Hard‑coded path vs relative** ‑ If you work on multiple computers, keep the data folder inside the repo and use `BASE_DIR / "LLMs_TextStudy"` in your script.  Otherwise hard‑code the absolute path that matches your machine.
* **Item‑header variations** ‑ Real DEF 14A filings show minor wording changes ("Stockholder Proposal", no bolding, etc.).  If you run into false negatives, adjust `proposal_start_pattern` in `extract_proposals.py` or add additional patterns.

---

## Roadmap

* [ ] Optional CSV/Parquet output per proposal
* [ ] CLI flag to split proponent vs board paragraphs
* [ ] Loose regex 🎯 to catch "Shareowner Proposal" variants
* [ ] Integrate with a spaCy pipeline for quick entity counts

Feel free to open issues or PRs!

---

## License
MIT License—see `LICENSE` file.

---

## Author & contact
Bernadetta Baran · [bernadetta.baran@gea.com](mailto:bernadetta.baran@gea.com)
Questions, ideas or patches are welcome—happy extracting!
