# Plan — Vancouver Round 2 implementation kit and first-card correction

> **Status: plan only, not executed.** Written 29 July 2026. Working document in Czech.
> Describes the intended scope, verification steps and git workflow for the work that would land
> in `docs/vancouver/`. Nothing in this document is a commitment made to any third party, and no
> part of it has been sent to the consultation core team.

---

## Kontext

Vancouver Standard (Global Reporting Standard for AI Disclosure in Research; ISC, WCRIF, COPE, STM, GYA) má otevřené 2. konzultační kolo do **16. 10. 2026**; pak tým z odpovědí píše standard (publikace ~prosinec 2026). Politickou vrstvu obsadit nelze, ale koalice nemá — a nebude mít — datový formát, validátor, vazbu na otisk verze ani řešení nepublikovatelných logů, přesto si do kritérií napsala „machine-readable and machine-generatable". Tam RPC už funkční kód má.

Cílem je proto přijít s **hotovými artefakty, ne se slibem**: (1) opravit vlastní kartu, která dnes tvrdí `artifact_linked` u artefaktu bez otisku a bez možnosti vydání — dokud tam ta lež je, celý pitch je mrtvý; (2) dodat malý balík, který jim ušetří práci a dá se prokliknout; (3) dodat zprávu z použití — věc, kterou si sami vyrobit nemohou, protože nemají nikoho, kdo jejich 18 kategorií zkusil vyplnit.

Výstup: jedna branch v `github.com/JanNehyba/research-provenance-card` + draft PR. **Nic se neodesílá** (žádné e-maily, žádný merge do main, Pages se z branche nedeployují). Koncepty e-mailů se podle rozhodnutí autora nepíšou vůbec.

Repo je veřejné — po pushnutí je obsah branche viditelný.

---

## A. Oprava první karty (nejdřív, je to podmínka všeho ostatního)

**`registry/2026/rpc-2026-0001.json`**
- Odstranit celý blok `artifacts` (artefakt `log1` bez `sha256`, `access_status: on_request`, který nelze vydat). `artifacts` není ve schématu povinné.
- U tří činností (`credit:conceptualization`/ai1, `rpc:source_retrieval`/ai1, `credit:writing_original_draft`/ai1) odstranit `artifact_refs` a změnit `evidence_level` z `artifact_linked` na **`declared`**.
- Ke každé činnosti doplnit `description` (schéma pole má) — co konkrétně aktér dělal, aby snížení úrovně nebylo ztrátou informace.
- Aktualizovat `human_guarantor.assertion_timestamp` na čas opravy (UTC) — přeznačené tvrzení je nové tvrzení.
- **Neměnit** `paper.pdf_sha256` (rukopis se nemění) a nezakládat novou kartu se `supersedes`: registr je git, historie commitů *je* auditní log. Oprava proběhne v místě + záznam v CHANGELOGu.

**Důsledek na panelu (ověřit, je to smysl celé opravy):** `site/build.py` počítá `artifacts_linked` jako `bool(card["artifacts"]) or any(a["artifact_refs"])` → status **zhasne**. `version_bound` zůstává ON. Přegenerovat `site/out/` (`python site/build.py`) a commitnout — výstup je deterministický, diff bude čistý.

**Navázané textové úpravy**
- `CHANGELOG.md` → nová sekce `## 0.1.1` s položkou o opravě karty a o Vancouver balíku.
- `docs/vancouver/README.md` → v checklistu odškrtnout položku o kartě + jednou větou co se stalo.
- `docs/vancouver/round2-submission-en.md` a `-cs.md`, §6 bod (2) → doplnit půlvětu, že oprava je provedená a dohledatelná v historii repozitáře (tvrzení tím zůstane pravdivé a zesílí).

---

## B. Implementation kit — `docs/vancouver/kit/`

### 1. `vs-taxonomy-round2.json` — jejich taxonomie jako datový soubor
Nejcennější a nejmenší položka. Obsah:
- `provenance` blok: zdroj (`WCRI2026FT_PrepReadingRound2_v45.pdf`), verze dokumentu (v4.5, 8. 7. 2026), datum stažení (2026-07-29), výslovně **„unofficial rendering of a proposal under public consultation"**, nabídka převzetí, kontakt.
- `rights`: názvy kategorií jsou **citované z konzultačního dokumentu** (práva u iniciativy, na požádání odstraníme/relicencujeme); struktura, identifikátory a naše poznámky CC BY 4.0. Nepředstírat, že licencujeme jejich obsah.
- 18 kategorií: `number`, `label` (verbatim), `suggested_id` (slug, např. `vs:literature-search`, bez pořadových čísel — viz P1 v podnětu), `definition: null` **(definice si nevymýšlíme — jejich PDF říká, že definice teprve doplní)**, `parent` u 5/6/7, `implementer_note` (naše, jasně odlišené).
- `proposed_additions`: 3 kategorie (`vs:orchestration`, `vs:ai-verification`, `vs:output-selection`) s odůvodněním.
- `deprecation_policy` pole demonstrující, jak má živý slovník vypadat (`deprecated`, `replaced_by`).

Držet konzistentní s už hotovým `docs/vancouver/taxonomy-crosswalk-v0.1.json` (stejné slugy, stejné poznámky).

### 2. `vs-disclosure-draft.schema.json` — malé schéma deklarace
JSON Schema Draft 2020-12 (stejný dialekt jako `schema/rpc-v0.1.schema.json`), záměrně **menší než RPC**, jen z jejich pojmů + jedna osa navíc:
- `work` (title, version, `pdf_sha256` volitelné), `guarantor` (name, orcid, timestamp), `disclosures[]`, `null_declaration`, `responsibility_statement`.
- Řádek `disclosures[]` = `task` (id z taxonomie) · `actor` (`kind`: ai|human, provider, model_family, `model_version_or_snapshot`, interface, orcid) · `verification` (uzavřený enum ze slotu 3 v odpovědi 5C: `not_checked`, `read_through`, `sampled`, `recomputed`, `cross_checked_primary_sources`, `checked_by_named_third_party`, `independently_reproduced`) · `trace` (`type`, `uri_or_pid`, `sha256`, `access_status` enum vč. `not_retained`, `restriction_reason`, volitelný `curation` objekt = dvouotiskové pravidlo) · `not_verified` (povinný krátký text).
- Každá property nese anotaci `"x-origin": "round2-proposal" | "implementer-proposal"` — aby bylo na první pohled vidět, co je jejich a co náš návrh. (Neznámá klíčová slova validátory ignorují.)
- Podmínka `if access_status != public then required restriction_reason` — stejný vzor jako v RPC schématu.

### 3. Validátor — **žádný nový kód**
`tools/validate.py` už bere `--schema`, takže balík validuje existující nástroj:
```
python tools/validate.py "docs/vancouver/kit/examples/example-disclosure.json" \
  --schema docs/vancouver/kit/vs-disclosure-draft.schema.json
```
Tohle je zároveň lepší argument („náš validátor je nezávislý na slovníku") než duplikát skriptu. Příkaz zdokumentovat v `kit/README.md`.

### 4. Vyplněný příklad + z něj vygenerované prohlášení
- `examples/example-disclosure.json` — **reálný** záznam k anglickému rukopisu, přeložený do jejich 18 kategorií, s poctivými hodnotami po opravě karty (převážně `read_through`, žádná třetí strana, log nepublikován → `access_status: not_retained`/`restricted` s důvodem).
- `examples/example-disclosure-broken.json` — chybí `verification`, pro demonstraci a test (vzor `schema/examples/broken/`).
- `tools/render_vs_statement.py` — malý renderer; znovupoužije `render_template()` z `tools/generate_disclosure.py` (`from generate_disclosure import render_template` funguje, protože nástroje se spouštějí jako skripty z rootu) a vyrobí lidsky čitelné prohlášení do článku.
- `tools/templates/vs_statement.txt` — šablona ve stylu existujících `elsevier.txt` / `springer.txt`.
- `examples/example-statement.md` — **commitnutý vygenerovaný výstup**, aby čtenář viděl obojí bez spouštění: stejná data → tabulka pro stroj i odstavec pro čtenáře. To je přesně ta ukázka k jejich otázce 2 (umístění).

### 5. `implementation-report.md` — dvě stránky, vlajková položka
Struktura: co jsme udělali (vyplnili jejich 18 kategorií na skutečném rukopisu) → **co chybí** (5 mezer v RPC, které jsme doplnili; 3 chybějící kategorie; 3 nejasnosti/překryvy) → **co se rozbilo** (zpětné doplnění provenience je o řády dražší než průběžný záznam; surové logy nejsou publikovatelný artefakt → dvouotiskové pravidlo) → **co jsme kvůli tomu změnili u sebe** (snížení vlastních úrovní důkazu, s odkazem na commit) → co z toho plyne pro standard (P1–P9 zkráceně, odkaz na podnět).

### 6. `kit/README.md`
Co balík je, tři příkazy k okamžitému vyzkoušení, výslovné disclaimery (neoficiální; návrh v konzultaci; nejde o konkurenční standard), licenční/rights nota, odkaz na podnět a crosswalk.

---

## C. Testy a CI

- `tests/test_vs_kit.py` — vzorem je `tests/test_schema.py` (fixture s `Draft202012Validator`, `load_json`):
  1. `example-disclosure.json` validuje proti kit schématu;
  2. `example-disclosure-broken.json` selže;
  3. `vs-taxonomy-round2.json` se parsuje, má 18 kategorií, unikátní `suggested_id`, žádnou vymyšlenou `definition`;
  4. smoke test rendereru přes `subprocess` (stejně, jak ho pouští CI) + kontrola, že výstup odpovídá commitnutému `example-statement.md`.
- `.github/workflows/validate.yml` — přidat krok „Validate Vancouver kit example" s příkazem z B.3, za existující validaci registru. Existující kroky nechat beze změny.

## D. Ostatní dokumenty

- root `README.md` — jedna odrážka o kitu pro vznikající standard s odkazem na `docs/vancouver/`.
- `docs/vancouver/README.md` — index nových souborů + aktualizovaný checklist.

**Záměrně se teď nedělá:** role v0.2 ve `spec/roles.md` a `schema/` (GOVERNANCE vyžaduje verzovací poznámky — samostatný krok); běh `refcheck.py` nad bibliografií (chybí zdroj referencí s DOI); Zenodo/DOI; jakékoli e-maily; merge do main.

---

## Verifikace

Vše z rootu repozitáře, s interpretem, který má `jsonschema` (v repu je `requirements.txt`, v `/Users/jannehyba/AICREDIT/.venv` existuje venv — ověřit `python -c "import jsonschema"` a případně `pip install -r requirements.txt`).

1. `pytest` → projdou existující + nové testy.
2. `python tools/validate.py "registry/**/*.json"` → `OK` (opravená karta je validní).
3. `python tools/validate.py "docs/vancouver/kit/examples/example-disclosure.json" --schema docs/vancouver/kit/vs-disclosure-draft.schema.json` → `OK`, exit 0.
4. Totéž na `example-disclosure-broken.json` → `ERROR`, exit 1 (ověřuje, že schéma opravdu něco vynucuje).
5. `python tools/render_vs_statement.py docs/vancouver/kit/examples/example-disclosure.json tools/templates/vs_statement.txt` → výstup **bajtově shodný** s commitnutým `example-statement.md`.
6. `python site/build.py` → v `site/out/cards/rpc-2026-0001.html` je `artifacts_linked` = **OFF**, `version_bound` = ON.
7. `python -c "import json,glob; [json.load(open(p)) for p in glob.glob('docs/vancouver/**/*.json', recursive=True)]"` → všechny nové JSONy se parsují.

## Git

Branch `vancouver/round2-kit`, commity v tomto pořadí (aby historie sama vyprávěla ten příběh):

1. `fix(registry): drop unbacked artifact claim from first card` — karta + `site/out` + CHANGELOG.
2. `docs(vancouver): add round 2 consultation submission and taxonomy crosswalk` — soubory v `docs/vancouver/`.
3. `feat(vancouver): add round 2 implementation kit` — taxonomie, schéma, příklady, renderer, šablona.
4. `docs(vancouver): add implementation report` — dvoustránková zpráva + `kit/README.md`.
5. `test,ci: validate Vancouver kit example` — testy + krok v CI + root README.

Pak `git push -u origin vancouver/round2-kit` a `gh pr create --draft` (PR spustí CI podle `validate.yml`, které běží na `pull_request`).
