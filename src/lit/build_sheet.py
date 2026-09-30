"""The sheet, rewritten after the author read it and could not use it.

Four things he was right about. The six block names and their prose were
compressed glosses of English canonical labels, written to fit the box rather
than to be read cold. The one-sentence example did not say which part of it was
which block. The cut after six axes has no support in the data: the only real
break in the ranking is between the first axis and the second. And FAIR on the
ladder page was the wrong FAIR; the one that matters here is F(AI)2R, which is
the same deposit the verification ladder already came from.

Added with this pass: the sentence taken apart span by span, paired bars for the
two genres instead of a number table, and a crosswalk saying why the moves of an
utterance and the axes of a scheme are two different cuts.
"""
import io, json, os, sys, collections
from .sheet_translations import CZ_VAL
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

LIT = r"C:\Users\Nehyba\rpc-lit\data\lit"
CORPUS = r"C:\Users\Nehyba\research-provenance-card\data\corpus\corpus.jsonl"
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "docs", "scoping", "priznani-ai-list.pdf")

FT = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("UI", os.path.join(FT, "segoeui.ttf")))
pdfmetrics.registerFont(TTFont("UIB", os.path.join(FT, "segoeuib.ttf")))
pdfmetrics.registerFont(TTFont("UISB", os.path.join(FT, "seguisb.ttf")))

W, H = A4
M = 50
INK = HexColor("#1b2733"); GREY = HexColor("#5c6b7a"); LINE = HexColor("#d7dee5")
ACC = HexColor("#0f6f6a"); ACCL = HexColor("#e6f2f1")
WARN = HexColor("#8a5a00"); WARNL = HexColor("#fdf4e3")
BAD = HexColor("#a8342a"); BADL = HexColor("#fbeceb")
GOOD = HexColor("#2a7a45"); GOODL = HexColor("#eaf4ec")
BARBG = HexColor("#eef2f5"); PALE = HexColor("#f4f6f8"); WHITE = HexColor("#ffffff")
SW = HexColor("#b06a2c"); SWL = HexColor("#fbeedd")

TOTPG = 9
P_BLOKY, P_VETA, P_HODNOTY, P_ZEBRICKY, P_KORPUS, P_KROKY, P_USUDEK = 2, 3, 4, 5, 6, 7, 8

# ------------------------------------------------------------------ the data
norm = lambda s: " ".join(s.lower().replace("_", " ").split())
dims = json.load(io.open(f"{LIT}/dimensions.json", encoding="utf-8"))["dimensions"]
byid = {d["canonical_id"]: d for d in dims}
l2d = {norm(v): d["canonical_id"] for d in dims for v in d["variants"]}
rows = [json.loads(l) for l in io.open(f"{LIT}/schemes.jsonl", encoding="utf-8") if l.strip()]
merge = json.load(io.open(f"{LIT}/scheme-merge.json", encoding="utf-8"))
oos = {r["scheme_id"] for r in merge["out_of_scope"]}
ART = {"scheme-own-category-inventory", "generic-study-methodology-reporting"}

pairs = set()
for r in rows:
    d = l2d.get(norm(r["dimension_label_verbatim"]))
    if not d or d in ART or r["scheme_id"] in oos:
        continue
    pairs.add((d, r["scheme_id"]))
schemes_per_dim = collections.Counter(d for d, _ in pairs)
FULLRANK = schemes_per_dim.most_common()
RANK = FULLRANK[:16]
sid2can = {m: cn["canonical_id"] for cn in merge["canonical_schemes"] for m in cn["members"]}
ALL_SCHEMES = len(merge["canonical_schemes"])
TOTAL_SCHEMES = len({sid2can.get(s, s) for _, s in pairs})
NROWS = len(rows)

CZ = {
    "extent-of-ai-involvement": "Kolik z textu je od stroje",
    "ai-tool-identity-and-version": "Jaký nástroj a jaká verze",
    "contribution-role-taxonomy": "Kdo z lidí co dělal",
    "verification-of-ai-output": "Co se na výstupu ověřilo",
    "task-or-function-of-ai-use": "Jakou práci nástroj udělal",
    "accountability-for-the-work": "Kdo za výsledek ručí",
    "permitted-and-prohibited-ai-use": "Co je dovolené a co zakázané",
    "location-of-the-disclosure": "Kde přiznání v textu stojí",
    "authorship-criteria": "Kdo se smí podepsat jako autor",
    "presence-of-a-disclosure": "Jestli přiznání vůbec je",
    "stage-of-the-process-where-ai-was-used": "V jaké fázi práce se nástroj použil",
    "strength-of-the-disclosure-mandate": "Jak silně se přiznání vyžaduje",
    "traceability-of-output-to-its-sources": "Jestli jde výstup dohledat ke zdrojům",
    "purpose-or-reason-for-ai-use": "Proč se nástroj použil",
    "transparency-as-a-virtue": "Transparentnost jako hodnota, ne jako pole",
    "prompts-and-inputs-disclosed": "Jaké prompty a vstupy se přiznaly",
}
PRIKLAD = {
    "extent-of-ai-involvement": "„jen korektura“ – „většina textu“ – „celý text“",
    "ai-tool-identity-and-version": "„Claude Opus 5“ – „ChatGPT GPT-5.5“ – „Grammarly“",
    "contribution-role-taxonomy": "„sběr dat“ – „analýza“ – „psaní“ – „revize“",
    "task-or-function-of-ai-use": "„překlad“ – „jazyková úprava“ – „obrázek“ – „kód“",
    "verification-of-ai-output": "„nezkontrolováno“ – „přečetl jsem to“ – „ověřil proti zdroji“",
    "accountability-for-the-work": "„autor“ – „vydavatel“ – „dodavatel nástroje“",
    "permitted-and-prohibited-ai-use": "„dovoleno“ – „dovoleno, když to přiznáte“ – „zakázáno“",
    "location-of-the-disclosure": "„v metodice“ – „v poděkování“ – „pod čarou“",
    "authorship-criteria": "„podstatně přispěl“ – „schválil finální verzi“",
    "presence-of-a-disclosure": "„je tam“ – „není“ – „neuvedeno“",
    "stage-of-the-process-where-ai-was-used": "„při rešerši“ – „při psaní“ – „při revizi“",
    "strength-of-the-disclosure-mandate": "„povinné“ – „doporučené“ – „dobrovolné“ – „neřeší se“",
    "purpose-or-reason-for-ai-use": "„nejsem rodilý mluvčí“ – „ušetřit čas“ – „zlepšit čtivost“",
    "transparency-as-a-virtue": "„pracujeme transparentně“, bez pole, které by se dalo vyplnit",
    "prompts-and-inputs-disclosed": "„prompty jsou v příloze“ – „vložil jsem tam svoje poznámky“",
    "traceability-of-output-to-its-sources": "„log promptů“ – „odkaz na zdroj u každého tvrzení“",
}

# Šest bloků. Název je otázka, na kterou v přiznání odpovídáte. Věta pod ním
# říká, co tam má stát. Dvojice špatně/lépe je konkrétní příklad. Text je můj,
# čísla nejsou.
# Pět bloků v pořadí, ve kterém tyto části stojí ve skutečných formulacích.
# Pořadí je z korpusu, ne z mého úsudku: rozsah před nástrojem 6:1, nástroj před
# prací 13:0, práce před kontrolou 4:0, kontrola před ručením 4:0. Průměrná
# pozice ve větě 0.11, 0.69, 0.75, 0.80, 0.87, tedy schody. Počáteční písmena
# anglických názvů v tomto pořadí dávají STAIR.
# Šestá osa, role lidí, do věty nepatří a je vyřízená na straně 3.
BLOKY = [
    ("S", "Scope", "extent-of-ai-involvement",
     "Kolik z toho je od stroje?",
     "Podíl, nebo jmenovitě ta část. Jde o množství, ne o druh práce. Tohle je "
     "osa, kterou žádá nejvíc schémat ze všech.",
     "Text vznikl s pomocí AI.", "Zhruba polovina textu."),
    ("T", "Tool", "ai-tool-identity-and-version",
     "Která AI a jaká verze?",
     "Přesný název i verze. Samotné „AI“ za rok neřekne nikomu nic, protože "
     "modely se mění a jmenují se pořád stejně.",
     "Použil jsem AI.", "Claude Opus 5 (Anthropic)."),
    ("A", "Action", "task-or-function-of-ai-use",
     "Jakou práci udělal?",
     "Sloveso a předmět. Druh práce, ne míra pomoci. „Pomohl“ není druh práce.",
     "AI mi s tím pomohla.", "Napsal první koncept."),
    ("I", "Inspection", "verification-of-ai-output",
     "Co jsem ověřil?",
     f"Konkrétní úkon, který by někdo mohl zopakovat. „Zkontroloval jsem to“ se "
     f"ověřit nedá, protože neříká co. Hotové stupnice jsou na straně {P_ZEBRICKY}.",
     "Vše jsem zkontroloval.",
     "Každou citaci jsem porovnal s originálem."),
    ("R", "Responsibility", "accountability-for-the-work",
     "Za co ručím?",
     f"Ne kdo ručí, ale za co. Schémata se ptají jen na to první. Pole „za co“ "
     f"nemá ani jedno z nich, takže druhou půlku si musíte dopsat sami. Není to "
     f"totéž co ověření o řádek výš; proč, je na straně {P_ZEBRICKY}.",
     "Autor za to ručí.", "Ručím za fakta a závěry, ne za formulace."),
]

# Barvy bloků, aby se daly poznat ve větě na další straně.
BCOL = [HexColor(x) for x in ("#0f6f6a", "#2f5f9e", "#6a4a8a", "#4a7a34", "#a1710f", "#a8342a")]
BTINT = [HexColor(x) for x in ("#cde7e2", "#d6e4f4", "#e8dff1", "#ddeed1", "#fae8c6", "#f6dbd8")]
MISS = HexColor("#6b7280"); MISSL = HexColor("#eceef1")


def best_values(dim_id, minlen=3):
    cand = [r for r in rows
            if l2d.get(norm(r["dimension_label_verbatim"])) == dim_id
            and r["scheme_id"] not in oos and len(r["value_list_verbatim"]) >= minlen]
    cand.sort(key=lambda r: -len(r["value_list_verbatim"]))
    return cand[0] if cand else None


corpus = [json.loads(l) for l in io.open(CORPUS, encoding="utf-8") if l.strip()]
coding = json.load(io.open(f"{LIT}/move-analysis-pilot.json", encoding="utf-8"))
items = [i for i in coding["items"]
         if "not a disclosure" not in i.get("flag", "") and "meta:" not in i.get("flag", "")]
moves = lambda seq: [m for m in seq.replace("|", " ").split() if m]
mcount = collections.Counter(m for i in items for m in set(moves(i["sequence"])))
NITEMS = len(items)
art = [i for i in items if i["genre"] == "article"]
sw = [i for i in items if i["genre"] == "software_project"]
gc = lambda grp, code: sum(1 for i in grp if code in moves(i["sequence"]))
resp = [i for i in items if "RESP" in moves(i["sequence"])]
with_check = sum(1 for i in resp
                 if "CHECK" in moves(i["sequence"])[:moves(i["sequence"]).index("RESP")])
nobj = sum(1 for i in items if "OBJ" in moves(i["sequence"]))
neg = [i for i in items if "NEG" in moves(i["sequence"])]
negresp = sum(1 for i in neg if "RESP" in moves(i["sequence"]))
n_state = len({r["scheme_id"] for r in rows
               if l2d.get(norm(r["dimension_label_verbatim"])) in
               ("maturity-level-of-the-thing-described", "third-party-handoff-readiness")
               and r["scheme_id"] not in oos})

# ---------------------------------------------------------------- the canvas
c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Přiznání AI: co se měří a jak ho napsat")
c.setAuthor("Jan Nehyba")
c.setSubject(f"Praktický list z rešerše {ALL_SCHEMES} publikovaných schémat")


def wrap(t, f, s, w):
    out, cur = [], ""
    for word in t.split():
        x = (cur + " " + word).strip()
        if pdfmetrics.stringWidth(x, f, s) <= w:
            cur = x
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def para(x, y, t, w, f="UI", s=10.2, lead=14.2, col=GREY):
    c.setFont(f, s); c.setFillColor(col)
    for ln in wrap(t, f, s, w):
        c.drawString(x, y, ln); y -= lead
    return y


def h1(y, t, sub=None):
    c.setFont("UIB", 24); c.setFillColor(INK); c.drawString(M, y, t); y -= 19
    if sub:
        y = para(M, y, sub, W - 2 * M, "UI", 10.4, 14.2)
    c.setStrokeColor(ACC); c.setLineWidth(2.6); c.line(M, y - 5, M + 60, y - 5)
    return y - 26


def h2(y, t):
    c.setFont("UISB", 13.4); c.setFillColor(ACC); c.drawString(M, y, t.upper())
    return y - 21


def rule(y):
    c.setStrokeColor(LINE); c.setLineWidth(0.7); c.line(M, y, W - M, y); return y - 20


def foot(p, tag="Popis z dat"):
    c.setFont("UI", 8); c.setFillColor(GREY)
    c.drawString(M, 30, f"Přiznání AI, list z rešerše {ALL_SCHEMES} schémat. {tag}.")
    c.drawRightString(W - M, 30, f"{p} / {TOTPG}")
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(M, 41, W - M, 41)


def dot(x, y, n, col, r=7.2, fs=7.6):
    """The small numbered disc that ties a sentence span to its block."""
    c.setFillColor(col); c.circle(x, y, r, stroke=0, fill=1)
    c.setFont("UIB", fs); c.setFillColor(WHITE)
    c.drawCentredString(x, y - fs * 0.35, n)


def marked(y, segs, fs=10.2, lead=26, lab_gap=11, width=None, x0=None):
    """Draw a sentence whose spans carry a code label above them."""
    x0 = M + 10 if x0 is None else x0
    x1 = (W - M - 10) if width is None else x0 + width
    lines, line, cx = [], [], x0
    for si, (text, code) in enumerate(segs):
        code = (code, si)
        for wd in text.split():
            wdw = pdfmetrics.stringWidth(wd, "UI", fs)
            spw = pdfmetrics.stringWidth(" ", "UI", fs)
            if line and cx + spw + wdw > x1:
                lines.append(line); line = []; cx = x0
            if line:
                cx += spw
            line.append((wd, code, cx, wdw))
            cx += wdw
    if line:
        lines.append(line)
    ty = y - 14
    prev = "__none__"
    for ln in lines:
        k = 0
        while k < len(ln):
            j = k
            while j + 1 < len(ln) and ln[j + 1][1] == ln[k][1]:
                j += 1
            code, si = ln[k][1]
            a = ln[k][2] - 3
            b = ln[j][2] + ln[j][3] + 3
            c.setFillColor(ACCL if si % 2 == 0 else PALE)
            c.roundRect(a, ty - 4, b - a, fs + 6, 2, stroke=0, fill=1)
            c.setFillColor(HexColor("#b7cecb")); c.rect(a, ty - 4, b - a, 1.6, stroke=0, fill=1)
            if not (k == 0 and ln[k][1] == prev):
                c.setFont("UIB", 6.4); c.setFillColor(WARN)
                c.drawString(a + 1, ty + fs + lab_gap - 8, code)
            if j == len(ln) - 1:
                prev = ln[k][1]
            k = j + 1
        c.setFont("UI", fs); c.setFillColor(INK)
        for wd, code, x, wdw in ln:
            c.drawString(x, ty, wd)
        ty -= lead
    return ty + lead - 14


# ===================================================================== page 1
y = H - 56
y = h1(y, "Co se v přiznáních AI skutečně měří",
       f"Rešerše našla {ALL_SCHEMES} publikovaných schémat, {TOTAL_SCHEMES} z nich "
       f"pojmenovává aspoň jednu osu. Dohromady jich používají {len(dims)}. "
       f"Tady je šestnáct nejčastějších, seřazených podle toho, kolik schémat "
       f"každou pojmenovalo. Pořadí je z dat, není vybrané podle tématu.")

y = h2(y, "Šestnáct nejčastějších os")
maxn = RANK[0][1]
barw = 190
for i, (d, n) in enumerate(RANK, 1):
    c.setFont("UI", 9); c.setFillColor(GREY)
    c.drawRightString(M + 16, y - 9, str(i) + ".")
    c.setFont("UISB", 10); c.setFillColor(INK)
    c.drawString(M + 24, y - 9, CZ.get(d, byid[d]["canonical_label"]))
    bx = W - M - barw
    c.setFillColor(BARBG); c.roundRect(bx, y - 12, barw, 11, 2, stroke=0, fill=1)
    c.setFillColor(ACC if i <= 6 else HexColor("#8fb8b5"))
    c.roundRect(bx, y - 12, barw * n / maxn, 11, 2, stroke=0, fill=1)
    inside = barw * n / maxn > 62
    c.setFont("UISB", 8.4); c.setFillColor(WHITE if inside else GREY)
    if inside:
        c.drawRightString(bx + barw * n / maxn - 5, y - 9.4, f"{n} schémat")
    else:
        c.drawString(bx + barw * n / maxn + 5, y - 9.4, f"{n} schémat")
    c.setFont("UI", 8.2); c.setFillColor(HexColor("#6f7f8d"))
    c.drawString(M + 24, y - 19.5, PRIKLAD.get(d, byid[d]["canonical_label"]))
    if i == 1:
        c.setStrokeColor(HexColor("#b9c6d0")); c.setLineWidth(0.8); c.setDash(3, 2)
        c.line(M, y - 26, W - M, y - 26); c.setDash()
        c.setFont("UI", 7.6); c.setFillColor(HexColor("#8b9aa6"))
        c.drawString(M + 24, y - 33, "jediný výrazný zlom v žebříčku: 74 → 46")
        y -= 11
    y -= 29.6

y = rule(y)
y = para(M, y, f"Zbylých {len(dims) - len(RANK)} os pojmenovalo méně schémat, "
               f"často jen jedno. To je samo o sobě nález: {sum(1 for d in dims if len(d['variants']) == 1)} "
               f"os má za sebou jediný doslovný název, tedy jediné schéma. Obor nemá "
               f"pár soupeřících systémů, má stovky jednorázových.", W - 2 * M)
y -= 6
y = rule(y)
y = h2(y, "Kde se žebříček na další straně uřízne")
nxt = FULLRANK[6:9]
y = para(M, y, "Po šesté ose. V datech pro to opora není: jediný výrazný zlom je "
               "hned na začátku, 74 proti 46. Od druhé osy dolů žebříček klesá "
               "plynule, rozestupy jsou 3, 2, 0, 5, 3, 5. Řez je můj. Hned za "
               "hranou stojí: " +
         "  ·  ".join(f"{j}. {CZ.get(d, byid[d]['canonical_label'])} ({n})"
                      for j, (d, n) in enumerate(nxt, 7)) + ".",
         W - 2 * M, "UI", 9.4, 12.6)
foot(1)
c.showPage()

# ===================================================================== page 2
y = H - 56
y = h1(y, "STAIR: pět otázek v pořadí, v jakém se píšou",
       "Pět otázek, na které přiznání odpovídá, v pořadí, ve kterém je lidé "
       "opravdu píšou. Čtyřikrát se ptáme „co“ a jednou „která“, a to není "
       "náhoda: odpovědí je vždycky předmět.")

bh0 = 54
c.setFillColor(ACCL)
c.roundRect(M, y - bh0, W - 2 * M, bh0, 5, stroke=0, fill=1)
c.setFillColor(ACC); c.rect(M, y - bh0, 3.6, bh0, stroke=0, fill=1)
c.setFont("UISB", 9.2); c.setFillColor(ACC)
c.drawString(M + 18, y - 17, "PRAVIDLO, KTERÉ NAHRAZUJE VŠECHNA OSTATNÍ")
c.setFont("UIB", 14); c.setFillColor(INK)
c.drawString(M + 18, y - 35, "Ke každému slovesu doplňte předmět.")
c.setFont("UI", 8.8); c.setFillColor(GREY)
c.drawString(M + 18, y - 47, "„AI pomohla“ s čím  ·  „zkontroloval jsem to“ co  "
                             "·  „ručím za to“ za co. Jedna vada, ne tři.")
y = y - bh0 - 14

colw = W - 2 * M
for i, (letter, eng, d, name, what, bad, good) in enumerate(BLOKY):
    n = schemes_per_dim[d]
    lw = wrap(what, "UI", 9.4, colw - 58)
    exw = (colw - 58 - 14) / 2
    lb = wrap(bad, "UI", 9.2, exw - 20)
    lg = wrap(good, "UI", 9.2, exw - 20)
    exh = 16 + max(len(lb), len(lg)) * 11.8
    hb = 34 + len(lw) * 12 + exh + 7
    c.setFillColor(PALE); c.roundRect(M, y - hb, colw, hb, 4, stroke=0, fill=1)
    c.setFillColor(BCOL[i]); c.rect(M, y - hb, 3.4, hb, stroke=0, fill=1)
    dot(M + 26, y - 20, letter, BCOL[i], 9.4, 10.6)
    c.setFont("UISB", 9); c.setFillColor(BCOL[i])
    c.drawString(M + 44, y - 24, eng.upper())
    ew = pdfmetrics.stringWidth(eng.upper(), "UISB", 9) + 11
    c.setFont("UISB", 11.6); c.setFillColor(INK)
    c.drawString(M + 44 + ew, y - 24, name)
    c.setFont("UISB", 8.6); c.setFillColor(BCOL[i])
    c.drawRightString(W - M - 14, y - 24, f"{n} schémat")
    yy = y - 40
    c.setFont("UI", 9.4); c.setFillColor(GREY)
    for ln in lw:
        c.drawString(M + 44, yy, ln); yy -= 12
    yy -= 6
    ex_y = yy
    c.setFillColor(BADL); c.roundRect(M + 44, ex_y - exh + 14, exw, exh, 3, stroke=0, fill=1)
    c.setFillColor(GOODL); c.roundRect(M + 58 + exw, ex_y - exh + 14, exw, exh, 3, stroke=0, fill=1)
    c.setFont("UISB", 7.6); c.setFillColor(BAD)
    c.drawString(M + 54, ex_y + 2, "MÍSTO")
    c.setFillColor(GOOD); c.drawString(M + 68 + exw, ex_y + 2, "RADĚJI")
    c.setFont("UI", 9.2); c.setFillColor(INK)
    t = ex_y - 11
    for ln in lb:
        c.drawString(M + 54, t, ln); t -= 11.8
    t = ex_y - 11
    for ln in lg:
        c.drawString(M + 68 + exw, t, ln); t -= 11.8
    y -= hb + 5

y -= 2
y = rule(y)
c.setFillColor(MISSL)
c.roundRect(M, y - 34, W - 2 * M, 34, 3, stroke=0, fill=1)
dot(M + 22, y - 17, "+", MISS, 8.4, 10)
c.setFont("UISB", 9.6); c.setFillColor(INK)
c.drawString(M + 38, y - 13, "Šestá osa do věty nepatří: kdo z lidí co dělal "
             f"({schemes_per_dim['contribution-role-taxonomy']} schémat)")
c.setFont("UI", 8.8); c.setFillColor(GREY)
c.drawString(M + 38, y - 26, "Patří do seznamu přispěvatelů vedle jmen autorů. "
             f"Proč, je na straně {P_VETA}.")
y -= 46
y = para(M, y, "Pořadí písmen není vymyšlené kvůli slovu, je to naopak. V korpusu "
               "stojí rozsah před nástrojem 6:1, nástroj před prací 13:0, práce před "
               "kontrolou 4:0, kontrola před ručením 4:0. Průměrná pozice ve větě "
               "stoupá 0,11 → 0,69 → 0,75 → 0,80 → 0,87. Jsou to schody a ručení "
               "je nahoře, ne na začátku. Pořadí podle počtu schémat je jiné a je "
               "na straně 1.", W - 2 * M, "UI", 9.2, 12.4)

foot(P_BLOKY, "Pořadí z korpusu, texty moje")
c.showPage()

# ===================================================================== page 3
y = H - 56
y = h1(y, "Ta věta rozebraná po částech",
       "Věta v pořadí STAIR. Barva a písmeno říkají, který úsek je která otázka.")

SEG = [
    ("Zhruba polovina textu", 0),
    ("je od Claude Opus 5:", 1),
    ("napsal první koncept.", 2),
    ("Každou citaci jsem porovnal s originálem.", 3),
    ("Ručím", 4),
    ("za fakta a závěry, ne za formulace.", None),
]
LET = ["S", "T", "A", "I", "R"]

FS, LEAD = 12.8, 34
xa, xb = M + 8, W - M - 8
lines, line, cx = [], [], xa
for text, tag in SEG:
    for wd in text.split():
        wdw = pdfmetrics.stringWidth(wd, "UISB", FS)
        spw = pdfmetrics.stringWidth(" ", "UISB", FS)
        if line and cx + spw + wdw > xb:
            lines.append(line); line = []; cx = xa
        if line:
            cx += spw
        line.append((wd, tag, cx, wdw))
        cx += wdw
if line:
    lines.append(line)

boxh = len(lines) * LEAD + 26
c.setFillColor(WHITE); c.setStrokeColor(LINE); c.setLineWidth(0.8)
c.roundRect(M, y - boxh, W - 2 * M, boxh, 5, stroke=1, fill=1)
ty = y - 28
prev_tag = "__none__"
for ln in lines:
    k = 0
    while k < len(ln):
        j = k
        while j + 1 < len(ln) and ln[j + 1][1] == ln[k][1]:
            j += 1
        tag = ln[k][1]
        x0 = ln[k][2] - 3.5
        x1 = ln[j][2] + ln[j][3] + 3.5
        tint = BTINT[tag] if tag is not None else MISSL
        col = BCOL[tag] if tag is not None else MISS
        c.setFillColor(tint)
        c.roundRect(x0, ty - 6, x1 - x0, FS + 8, 3, stroke=0, fill=1)
        c.setFillColor(col); c.rect(x0, ty - 6, x1 - x0, 2.2, stroke=0, fill=1)
        if not (k == 0 and tag == prev_tag):
            dot(x0 + 1, ty + FS + 4, LET[tag] if tag is not None else "?", col, 6.4, 7.6)
        if j == len(ln) - 1:
            prev_tag = tag
        k = j + 1
    c.setFont("UISB", FS); c.setFillColor(INK)
    for wd, tag, x, wdw in ln:
        c.drawString(x, ty, wd)
    ty -= LEAD
y -= boxh + 18

y = h2(y, "Legenda")
LEG = [(0, "Zhruba polovina textu", "Scope · Kolik z toho je od stroje?"),
       (1, "je od Claude Opus 5", "Tool · Která AI a jaká verze?"),
       (2, "napsal první koncept", "Action · Jakou práci udělal?"),
       (3, "Každou citaci jsem porovnal", "Inspection · Co jsem ověřil?"),
       (4, "Ručím", "Responsibility · zatím jen sloveso"),
       (None, "za fakta a závěry, ne za formulace", "předmět, který schémata nemají")]
for tag, span, what in LEG:
    col = BCOL[tag] if tag is not None else MISS
    dot(M + 8, y - 4, LET[tag] if tag is not None else "?", col, 7.4, 8.6)
    c.setFont("UISB", 9.6); c.setFillColor(INK)
    c.drawString(M + 24, y - 7.6, "„" + span + "“")
    c.setFont("UI", 9.6); c.setFillColor(GREY)
    c.drawString(M + 300, y - 7.6, what)
    y -= 18
y -= 6

c.setFillColor(MISSL)
c.roundRect(M, y - 44, W - 2 * M, 44, 4, stroke=0, fill=1)
dot(M + 22, y - 20, "?", MISS, 8.6, 9)
c.setFont("UISB", 9.6); c.setFillColor(INK)
c.drawString(M + 40, y - 17, "Poslední úsek je pole, které v žádném z 429 schémat není")
para(M + 40, y - 31, f"„Kdo ručí“ řeší {schemes_per_dim['accountability-for-the-work']} "
     f"schémat. „Za co“ neřeší žádné. Tu půlku věty si píšete sami a nemáte se "
     f"o co opřít.", W - 2 * M - 56, "UI", 8.8, 11.4, GREY)
y -= 64

c.setFillColor(MISSL)
c.roundRect(M, y - 40, W - 2 * M, 40, 4, stroke=0, fill=1)
dot(M + 22, y - 18, "+", MISS, 8.6, 10)
c.setFont("UISB", 9.6); c.setFillColor(INK)
c.drawString(M + 40, y - 15, "Šestá osa ve větě není, a to schválně")
para(M + 40, y - 28, "„Kdo z lidí co dělal“ se do jedné věty nevejde. Patří do "
     "seznamu přispěvatelů vedle jmen autorů, ne do přiznání o nástroji.",
     W - 2 * M - 56, "UI", 8.8, 11.4, GREY)
y -= 54

y = rule(y)
y = h2(y, "Pět otázek nad hotovým textem")
for q in ["Je tam jméno nástroje a verze, ne jen „AI“?",
          "Je tam, co přesně udělal, ne že „pomohl“?",
          "Je tam, co jste ověřili vy, ne jen že jste ověřili?",
          "Ručíte za něco konkrétního, ne „za to“?",
          "Je z toho poznat, jestli je to koncept, nebo finál?"]:
    c.setStrokeColor(ACC); c.setLineWidth(1)
    c.rect(M + 2, y - 9.6, 10.4, 10.4, stroke=1, fill=0)
    c.setFont("UI", 10.2); c.setFillColor(INK)
    c.drawString(M + 24, y - 9, q)
    y -= 17.5
y -= 2
y = para(M, y, "Druhá, třetí a čtvrtá otázka jsou tatáž otázka: má to sloveso "
               "předmět?", W - 2 * M, "UI", 9.2, 12.4)
y -= 8
y = rule(y)
y = h2(y, "Na pořadí záleží")
cw3 = (W - 2 * M - 2 * 26) / 3
bx3 = M
for i2, (t3, s3) in enumerate([("Použili jsme X", "co a čím"),
                               ("Ověřili jsme Y", "co jste udělali vy"),
                               ("Ručíme za Z", "a za co konkrétně")]):
    c.setFillColor(ACCL if i2 < 2 else GOODL)
    c.roundRect(bx3, y - 46, cw3, 46, 4, stroke=0, fill=1)
    c.setFont("UISB", 10.6); c.setFillColor(INK)
    c.drawCentredString(bx3 + cw3 / 2, y - 20, t3)
    c.setFont("UI", 8.8); c.setFillColor(GREY)
    c.drawCentredString(bx3 + cw3 / 2, y - 34, s3)
    if i2 < 2:
        c.setFont("UIB", 15); c.setFillColor(ACC)
        c.drawCentredString(bx3 + cw3 + 13, y - 27, "→")
    bx3 += cw3 + 26
y -= 64
y = para(M, y, f"Ve skutečných formulacích není nárok na odpovědnost samostatná věta. "
               f"Je jich {len(resp)} z {NITEMS} a ve {with_check} z nich mu ve stejné "
               f"větě předchází kontrola. Odpovědnost, před kterou nic není, vypadá "
               f"jako fráze, protože obvykle je.", W - 2 * M, "UI", 9.6, 13)
y -= 6
y = para(M, y, f"A obráceně: kdo nic nepřiznal, neručí. Ani jedno z {len(neg)} "
               f"prohlášení typu „AI jsme nepoužili“ nedodává, že za text někdo ručí. "
               f"Ten závazek se přebírá za to, co udělal stroj.", W - 2 * M, "UI", 9.6, 13)
foot(P_VETA, "Věta je můj návrh, bloky z dat")
c.showPage()

# ===================================================================== page 4
y = H - 56
y = h1(y, "Hodnoty, které schémata nabízejí",
       "U každé osy jeden skutečný výčet hodnot, doslova jak je v článku, "
       "s identifikátorem zdroje. Pravidlo výběru bylo mechanické: vždy ten nejdelší. "
       "Proto první řádek sedí pod svou osou špatně, je to seznam úkolů, ne měr. "
       "Nechal jsem to tak, aby bylo vidět, co mechanické pravidlo udělá. "
       "Šedý řádek pod každým výčtem je můj překlad, ne citace.")

for d, n in RANK:
    r = best_values(d)
    if not r:
        continue
    vals = [" ".join(v.split()) for v in r["value_list_verbatim"][:8]]
    lines2 = wrap("  ·  ".join(vals), "UISB", 9, W - 2 * M - 24)
    czvals = [CZ_VAL.get(v, v) for v in vals]
    czlines = wrap("  ·  ".join(czvals), "UI", 8.6, W - 2 * M - 24)
    if y - (48 + len(lines2) * 12 + len(czlines) * 11) < 60:
        break
    c.setFont("UISB", 10.4); c.setFillColor(INK)
    c.drawString(M, y, CZ.get(d, byid[d]["canonical_label"]))
    c.setFont("UI", 7.8); c.setFillColor(ACC)
    c.drawRightString(W - M, y, r["source_ref"])
    y -= 13
    c.setFont("UI", 8.2); c.setFillColor(GREY)
    c.drawString(M, y, "pole v článku: " + r["dimension_label_verbatim"][:70])
    y -= 15
    boxh = len(lines2) * 12 + len(czlines) * 11 + 16
    c.setFillColor(ACCL)
    c.roundRect(M, y - boxh + 12, W - 2 * M, boxh, 3, stroke=0, fill=1)
    c.setFont("UISB", 9); c.setFillColor(INK)
    yy = y
    for ln in lines2:
        c.drawString(M + 12, yy, ln); yy -= 12
    yy -= 2
    c.setFont("UI", 8.6); c.setFillColor(GREY)
    for ln in czlines:
        c.drawString(M + 12, yy, ln); yy -= 11
    y = yy - 16
foot(P_HODNOTY)
c.showPage()

# ===================================================================== page 5
y = H - 56
y = h1(y, "Žebříčky, ze kterých si můžete vybrat",
       "Když nechcete vymýšlet vlastní stupnici. Je jich víc, protože každý "
       "stupňuje něco jiného. Vyberte ten, který odpovídá na vaši otázku.")

LAD = [
    ("Co po kontrole zůstane dohledatelné", "F(AI)²R, arXiv:2607.25637",
     ["unverified", "needs-research", "reference-resolved", "ai-confirmed",
      "source-vendored", "human-confirmed", "human-read"],
     ["neověřeno", "nutno dohledat", "odkaz rozřešen", "potvrzeno AI",
      "doloženo zdrojem", "potvrdil člověk", "člověk to četl"],
     "Sedm příček. Neptá se, jak pečlivě jste kontrolovali, ale co by po vás mohl "
     "ověřit někdo další."),
    ("Jak hluboká byla lidská revize", "arXiv:2604.25346",
     ["E0", "E1", "E2", "E3", "E4"],
     ["žádná revize", "jen automatická", "částečná lidská", "plná lidská",
      "vícestupňová nebo nezávislá"],
     "Pět příček z facetového modelu. Tohle je ta stupnice, kterou většina lidí "
     "hledá, když chce říct „zkontroloval jsem to“ přesněji."),
    ("Co jste s výstupem udělali", "doi:10.1007/s12525-026-00915-x",
     ["accept", "modify (light)", "modify (substantial)", "reject"],
     ["přijmout", "lehce upravit", "podstatně upravit", "zamítnout"],
     "Čtyři možnosti, použitelné u každého výstupu zvlášť."),
    ("Jaký úkon kontroly to byl", "doi:10.11591/ijere.v15i4.38930",
     ["source check", "recalculation", "re-analysis"],
     ["kontrola zdroje", "přepočet", "nová analýza"],
     "Tři úkony. Nejjednodušší náhrada za prázdné „zkontroloval jsem to“."),
]
for title, ident, terms, cz, note in LAD:
    c.setFont("UISB", 11); c.setFillColor(INK); c.drawString(M, y, title)
    c.setFont("UI", 8); c.setFillColor(ACC); c.drawRightString(W - M, y, ident)
    y -= 18
    n = len(terms); gap = 10
    cwid = (W - 2 * M - (n - 1) * gap) / n
    fs = 8.2 if n > 5 else 9.2
    while any(pdfmetrics.stringWidth(t, "UISB", fs) > cwid - 6 for t in terms) and fs > 5.8:
        fs -= 0.2
    fs2 = fs - 0.6
    while any(pdfmetrics.stringWidth(t, "UI", fs2) > cwid - 6 for t in cz) and fs2 > 5.4:
        fs2 -= 0.2
    bx = M
    for i, (t, g) in enumerate(zip(terms, cz)):
        c.setFillColor(ACCL if i < n - 1 else GOODL)
        c.roundRect(bx, y - 30, cwid, 30, 3, stroke=0, fill=1)
        c.setFont("UISB", fs); c.setFillColor(INK)
        c.drawCentredString(bx + cwid / 2, y - 13, t)
        c.setFont("UI", fs2); c.setFillColor(GREY)
        c.drawCentredString(bx + cwid / 2, y - 24, g)
        if i < n - 1:
            c.setFont("UIB", 9); c.setFillColor(ACC)
            c.drawCentredString(bx + cwid + gap / 2, y - 18, "›")
        bx += cwid + gap
    y -= 38
    y = para(M, y, note, W - 2 * M, "UI", 8.8, 11.6)
    y -= 10

y = rule(y)
y = h2(y, "Dvě zkratky, které se snadno spletou")
TWO = [
    ("F(AI)²R", "arXiv:2607.25637 · doi:10.5281/zenodo.21667684",
     "„Who Did What, and Who Checked?“ Přesně ta otázka, o které je tenhle "
     "list. Do rešerše z něj vstoupily čtyři osy: třídy aktérů, činností a entit, "
     "a ten sedmistupňový žebříček nahoře.", ACCL, ACC),
    ("FAIR", "bez vztahu k předchozímu",
     "Findable, Accessible, Interoperable, Reusable. O sdílení dat a softwaru: "
     "identifikátor, licence, formát, metadata. Odpovídá na jinou otázku, jestli "
     "s tou věcí může pracovat někdo další, ne jestli ji někdo zkontroloval.",
     PALE, GREY),
]
for name, ident, body, fill, col in TWO:
    lb = wrap(body, "UI", 9, W - 2 * M - 30)
    hb = 30 + len(lb) * 11.8
    c.setFillColor(fill); c.roundRect(M, y - hb, W - 2 * M, hb, 4, stroke=0, fill=1)
    c.setFont("UISB", 11.4); c.setFillColor(col if col != GREY else INK)
    c.drawString(M + 15, y - 19, name)
    c.setFont("UI", 7.8); c.setFillColor(col)
    c.drawRightString(W - M - 15, y - 19, ident)
    yy = y - 34
    c.setFont("UI", 9); c.setFillColor(GREY)
    for ln in lb:
        c.drawString(M + 15, yy, ln); yy -= 11.8
    y -= hb + 10
y -= 4
y = rule(y)
y = h2(y, "Ověření a ručení nejsou totéž")
y = para(M, y, "Ověření je zpráva o tom, co jste udělal: skutek, dá se doložit. "
               "Ručení je závazek: vyzkouší se, až když se něco pokazí. Kontrolu "
               "jde zopakovat, ručení jen vymáhat. A rozcházejí se na obě strany.",
         W - 2 * M, "UI", 9.4, 12.6)
y -= 10

cw5 = (W - 2 * M - 14) / 2
PAIR5 = [
    ("OVĚŘIL, ALE NERUČÍ", GOODL, GOOD,
     "„Přečetl jsem celý text a opravil, co jsem našel. Za čísla v tabulce 3 "
     "ale neručím, statistiku dělal někdo jiný.“",
     "Kontrola proběhla, závazek je užší. Poctivé a běžné."),
    ("RUČÍ, ALE NEOVĚŘIL", BADL, BAD,
     "„AI-assisted language editing was used to improve the readability of this "
     "manuscript; the authors take full responsibility for the final content.“",
     f"Z korpusu, doslova. Jedna z {len(resp)}: nárok na odpovědnost, před "
     f"kterým nestojí žádná kontrola."),
]
hb5 = 0
for _, _, _, ex, note in PAIR5:
    hb5 = max(hb5, 30 + len(wrap(ex, "UISB", 8.8, cw5 - 26)) * 11.6
              + len(wrap(note, "UI", 8.4, cw5 - 26)) * 10.8 + 8)
bx5 = M
for title, fill, col, ex, note in PAIR5:
    c.setFillColor(fill); c.roundRect(bx5, y - hb5, cw5, hb5, 4, stroke=0, fill=1)
    c.setFont("UISB", 8.4); c.setFillColor(col)
    c.drawString(bx5 + 13, y - 15, title)
    yy = y - 30
    c.setFont("UISB", 8.8); c.setFillColor(INK)
    for ln in wrap(ex, "UISB", 8.8, cw5 - 26):
        c.drawString(bx5 + 13, yy, ln); yy -= 11.6
    yy -= 5
    c.setFont("UI", 8.4); c.setFillColor(GREY)
    for ln in wrap(note, "UI", 8.4, cw5 - 26):
        c.drawString(bx5 + 13, yy, ln); yy -= 10.8
    bx5 += cw5 + 14
y -= hb5 + 8
y = para(M, y, "A rozsah bývá jiný. Ověřil jsem citace, ručím za závěry. Nejsou to "
               "dvě jména pro jednu množinu.", W - 2 * M, "UI", 9.4, 12.6)

foot(P_ZEBRICKY)
c.showPage()

# ===================================================================== page 6
y = H - 56
y = h1(y, "Jak to lidé skutečně píšou",
       f"{len(corpus)} formulací sebraných z otevřeného webu, z toho {NITEMS} "
       f"použitelných. Jen anglicky, jen vědecké články a softwarové projekty. "
       f"Pilot, ne vzorek.")

y = h2(y, "Které části se ve formulaci objeví")
MV = [("USE", "že se nástroj použil"), ("TOOL", "který nástroj"),
      ("PURPOSE", "k čemu"), ("ACTOR", "kdo ho použil"),
      ("FRAME", "kdy nebo kde v práci"), ("HEAD", "nadpis pojmenující akt"),
      ("NEG", "že se nic nepoužilo"), ("SCOPE", "jak velká část"),
      ("CHECK", "že to někdo zkontroloval"), ("RESP", "že za to někdo ručí"),
      ("OBJ", "za co ručí")]
barw2 = 150
for code, cz in MV:
    n = mcount[code]
    c.setFont("UISB", 9.6); c.setFillColor(INK); c.drawString(M, y - 8, cz)
    bx = W - M - barw2
    c.setFillColor(BARBG); c.roundRect(bx, y - 11, barw2, 10, 2, stroke=0, fill=1)
    c.setFillColor(ACC); c.roundRect(bx, y - 11, barw2 * n / NITEMS, 10, 2, stroke=0, fill=1)
    c.setFont("UI", 8.2); c.setFillColor(GREY)
    c.drawRightString(bx - 8, y - 8.6, f"{n} z {NITEMS}")
    y -= 17
y -= 4

y = rule(y)
y = h2(y, "Články a software to píšou jinak")
c.setFillColor(ACC); c.roundRect(M, y - 1, 9, 9, 2, stroke=0, fill=1)
c.setFont("UI", 8.6); c.setFillColor(GREY)
c.drawString(M + 14, y + 1.4, f"vědecké články ({len(art)})")
c.setFillColor(SW); c.roundRect(M + 122, y - 1, 9, 9, 2, stroke=0, fill=1)
c.drawString(M + 136, y + 1.4, f"softwarové projekty ({len(sw)})")
y -= 20

GB = [("ACTOR", "kdo ho použil"), ("FRAME", "kdy nebo kde v práci"),
      ("PURPOSE", "k čemu"), ("SCOPE", "jak velká část"),
      ("CHECK", "že se kontrolovalo"), ("RESP", "že za to někdo ručí"),
      ("HEAD", "nadpis pojmenující akt"), ("TOOL", "který nástroj")]
lab_w, gbw = 165, 232
for code, cz in GB:
    na, ns = gc(art, code), gc(sw, code)
    sa, ss = na / len(art), ns / len(sw)
    c.setFont("UISB", 9.4); c.setFillColor(INK)
    c.drawString(M, y - 12, cz)
    bx = M + lab_w
    for share, cnt, tot, col, off in ((sa, na, len(art), ACC, 0), (ss, ns, len(sw), SW, 11)):
        c.setFillColor(BARBG); c.roundRect(bx, y - 9 - off, gbw, 9, 2, stroke=0, fill=1)
        if share > 0:
            c.setFillColor(col)
            c.roundRect(bx, y - 9 - off, max(gbw * share, 2.4), 9, 2, stroke=0, fill=1)
        c.setFont("UISB", 7.8); c.setFillColor(col)
        c.drawString(bx + gbw + 7, y - 6.8 - off, f"{cnt} z {tot}")
        c.setFont("UI", 7.8); c.setFillColor(HexColor("#94a3ad"))
        c.drawRightString(W - M, y - 6.8 - off, f"{round(share * 100)} %")
    y -= 29
y -= 2

y = rule(y)
y = h2(y, "Co z těch grafů plyne")
y = para(M, y, f"Podmět. Články napíšou, kdo nástroj použil, ve {gc(art, 'ACTOR')} "
               f"z {len(art)} případů, software v {gc(sw, 'ACTOR')} ze {len(sw)}. "
               f"Software mluví o nástroji, ne o člověku.", W - 2 * M, "UI", 9.6, 13)
y -= 6
y = para(M, y, f"Rozsah je obráceně. Software kvantifikuje podíl v {gc(sw, 'SCOPE')} "
               f"ze {len(sw)} případů („most of the code“), články v {gc(art, 'SCOPE')} "
               f"z {len(art)}. Žánry se neliší mírou pečlivosti, liší se tím, co "
               f"považují za zajímavé říct.", W - 2 * M, "UI", 9.6, 13)
y -= 6
y = para(M, y, f"Odpovědnost je jen v článcích, {gc(art, 'RESP')} z {len(art)}, "
               f"v softwaru {gc(sw, 'RESP')} ze {len(sw)}. A i tam je to většinou "
               f"věta z vydavatelské šablony.", W - 2 * M, "UI", 9.6, 13)
foot(P_KORPUS)
c.showPage()

# ===================================================================== page 7
y = H - 56
y = h1(y, "Proč jsou tohle jiné kategorie než ty osy",
       "Jsou to dva různé řezy a oba vznikly zdola, ale z jiného materiálu. "
       "Osy z toho, co obor navrhuje měřit. Kroky z toho, co lidé opravdu napíšou.")

TWOCUT = [
    ("Osy", f"{len(dims)} kategorií", "paradigmatický řez",
     f"Z {NROWS} doslovných názvů polí ve {TOTAL_SCHEMES} schématech, roztříděných "
     f"jedenácti agenty, z nichž každý viděl jen svou část. Otázka: co všechno se "
     f"dá o použití AI zaznamenat? Inventář kolonek formuláře.", ACCL, ACC),
    ("Kroky", f"{len(coding['move_inventory'])} kategorií", "syntagmatický řez",
     f"Z přečtení {NITEMS} skutečných formulací, jedna po druhé. Otázka: z čeho se "
     f"skládá ta věta? Inventář dílů výpovědi, které jdou za sebou a mají pořadí.",
     WARNL, WARN),
]
for name, cnt, kind, body, fill, col in TWOCUT:
    lb = wrap(body, "UI", 9.2, W - 2 * M - 30)
    hb = 32 + len(lb) * 12
    c.setFillColor(fill); c.roundRect(M, y - hb, W - 2 * M, hb, 4, stroke=0, fill=1)
    c.setFont("UISB", 12.4); c.setFillColor(col); c.drawString(M + 15, y - 20, name)
    c.setFont("UI", 9); c.setFillColor(GREY)
    c.drawString(M + 15 + pdfmetrics.stringWidth(name, "UISB", 12.4) + 10, y - 20,
                 f"{cnt}  ·  {kind}")
    yy = y - 36
    c.setFont("UI", 9.2); c.setFillColor(GREY)
    for ln in lb:
        c.drawString(M + 15, yy, ln); yy -= 12
    y -= hb + 10

y -= 10
y = h2(y, "Kde se potkávají")
c.setFont("UISB", 8.4); c.setFillColor(GREY)
c.drawString(M + 10, y, "KROK VE VĚTĚ")
c.drawString(M + 250, y, "ODPOVÍDAJÍCÍ OSA")
y -= 14
PAIR = [("TOOL", "který nástroj", "Jaký nástroj a jaká verze"),
        ("SCOPE", "jak velká část", "Kolik z textu je od stroje"),
        ("PURPOSE", "k čemu", "Proč se nástroj použil"),
        ("CHECK", "že se kontrolovalo", "Co se na výstupu ověřilo"),
        ("RESP", "že za to někdo ručí", "Kdo za výsledek ručí"),
        ("FRAME", "kdy nebo kde v práci", "V jaké fázi práce se nástroj použil")]
for code, cz, osa in PAIR:
    c.setFillColor(PALE); c.roundRect(M, y - 16, W - 2 * M, 16, 2, stroke=0, fill=1)
    c.setFont("UISB", 8); c.setFillColor(WARN); c.drawString(M + 10, y - 11.6, code)
    c.setFont("UI", 9.2); c.setFillColor(INK)
    c.drawString(M + 48, y - 12, cz)
    c.setFont("UIB", 9); c.setFillColor(HexColor("#b9c6d0")); c.drawString(M + 232, y - 12, "→")
    c.setFont("UI", 9.2); c.setFillColor(ACC); c.drawString(M + 250, y - 11.6, osa)
    y -= 18.5
y -= 6

NOPAIR = [
    ("Kroky, které žádnou osu nemají",
     "HEAD nadpis nad přiznáním · LINK spojka „po použití tohoto nástroje“ · "
     "ACTOR kdo nástroj obsluhoval · NEG prohlášení, že se nic nepoužilo. "
     "To jsou věci věty, ne měření. Schéma se neptá, jestli má odstavec nadpis.",
     WARNL, WARN),
    ("Osy, které žádný krok nemají",
     "Kde přiznání v textu stojí · kdo se smí podepsat jako autor · jak silně se "
     "přiznání vyžaduje · co je dovolené a co zakázané. To jsou pravidla o "
     "přiznání, ne jeho obsah. Do věty se nedostanou, protože věta je už jejich "
     "výsledek.", ACCL, ACC),
]
for t, b, fill, col in NOPAIR:
    lb = wrap(b, "UI", 9, W - 2 * M - 28)
    hb = 26 + len(lb) * 11.6
    c.setFillColor(fill); c.roundRect(M, y - hb, W - 2 * M, hb, 4, stroke=0, fill=1)
    c.setFont("UISB", 9.8); c.setFillColor(col); c.drawString(M + 14, y - 17, t)
    yy = y - 32
    c.setFont("UI", 9); c.setFillColor(GREY)
    for ln in lb:
        c.drawString(M + 14, yy, ln); yy -= 11.6
    y -= hb + 9

y -= 6
y = para(M, y, "Spárování v tabulce je moje. Vzniklo tak, že jsem se u každého "
               "kroku podíval, jestli se na totéž ptá některá osa. Automaticky "
               "počítané to není.", W - 2 * M, "UI", 8.8, 11.6)

y -= 12
y = rule(y)
y = h2(y, "Jak vypadá zakódovaná formulace")
y = para(M, y, "Nejčastější šablona z vědeckých článků, doslova a se štítky kroků.",
         W - 2 * M, "UI", 9.4, 12.6)
y -= 12
SEG7 = [
    ("Declaration of generative AI and AI-assisted technologies in the writing process.", "HEAD"),
    ("During the preparation of this work,", "FRAME"),
    ("the authors", "ACTOR"),
    ("used", "USE"),
    ("Grammarly (Grammarly Inc)", "TOOL"),
    ("to check for grammar, spelling, and clarity.", "PURPOSE"),
    ("After using this tool/service,", "LINK"),
    ("the authors", "ACTOR"),
    ("reviewed and edited the content as needed", "CHECK"),
    ("and take full responsibility", "RESP"),
    ("for the content of the publication.", "OBJ"),
]
y = marked(y, SEG7)
y -= 16
y = para(M, y, "Pořadí je ten záznam. Kolonka takový záznam nevytvoří, protože "
               "pořadí nemá. Proto jsou to dva různé řezy.",
         W - 2 * M, "UI", 9.4, 12.6)
foot(P_KROKY, "Dva řezy z dat, párování moje")
c.showPage()

# ===================================================================== page 8
y = H - 56
y = h1(y, "Příklady, mezera a kde v listu je úsudek",
       "Tahle strana není popis dat. Jsou na ní doporučení a rozhodnutí, která "
       "data neudělala. Oddělená je schválně.")

y = h2(y, "Slabé a lepší")
colw2 = (W - 2 * M - 16) / 2
EX = [
    ("Tento text vznikl s pomocí AI.",
     "První koncept napsal Claude (Opus 5). Text jsem přepsal a fakta ověřil proti zdrojům.",
     "Chybí nástroj, co udělal, i co jste udělali vy."),
    ("Autor za to ručí.",
     "Ručím za fakta a za závěry. Formulace jsou z části modelu.",
     "„Za to“ nemá předmět. Ručení bez předmětu se nedá ověřit ani vyvrátit."),
    ("AI byla použita ke zlepšení čtivosti.",
     "Použil jsem Grammarly na pravopis a interpunkci. Nic dalšího.",
     f"Trpný rod maže, kdo to udělal. V článcích je podmět v {gc(art, 'ACTOR')} "
     f"z {len(art)} případů, v softwaru v {gc(sw, 'ACTOR')} ze {len(sw)}."),
]
for bad, good, why in EX:
    lb = wrap(bad, "UI", 9.6, colw2 - 26)
    lg = wrap(good, "UI", 9.6, colw2 - 26)
    lw = wrap(why, "UI", 8.8, W - 2 * M - 20)
    hbox = 30 + max(len(lb), len(lg)) * 12.6
    c.setFillColor(BADL); c.roundRect(M, y - hbox, colw2, hbox, 4, stroke=0, fill=1)
    c.setFillColor(GOODL); c.roundRect(M + colw2 + 16, y - hbox, colw2, hbox, 4, stroke=0, fill=1)
    c.setFont("UISB", 8.4); c.setFillColor(BAD); c.drawString(M + 13, y - 15, "SLABÉ")
    c.setFillColor(GOOD); c.drawString(M + colw2 + 29, y - 15, "LEPŠÍ")
    c.setFont("UI", 9.6); c.setFillColor(INK)
    yy = y - 31
    for ln in lb:
        c.drawString(M + 13, yy, ln); yy -= 12.6
    yy = y - 31
    for ln in lg:
        c.drawString(M + colw2 + 29, yy, ln); yy -= 12.6
    y -= hbox + 7
    c.setFont("UI", 8.8); c.setFillColor(GREY)
    for ln in lw:
        c.drawString(M + 12, y, ln); y -= 11.4
    y -= 8

y = rule(y)
y = h2(y, "Tři věci, které v datech chybí")
y = para(M, y, "Tuhle otázku položil projekt, ne data. Data se neptala, co chybí; "
               "ptal jsem se já, se třemi hotovými složkami v ruce. Že v nich chybí, "
               "platí a je ověřitelné. Že jsou to zrovna tyhle tři, je volba projektu.",
         W - 2 * M, "UI", 9.2, 12.4)
y -= 8
THREE = [
    ("V jakém stavu ten text je", "„pracovní verze, ne finál“ – „surový výstup“",
     f"{n_state} schémata mají stupeň zralosti, ale zralosti systému nebo rubriky. "
     f"O tom, jestli předáváte koncept, nebo hotovou věc, není nic."),
    ("Co se po čtenáři žádá", "„jen na vědomí“ – „ověř čísla v tabulce 2“",
     "Existuje, ale jen jako vlastnost rozhraní, ne jako věta autora."),
    ("Za co přesně ručíte", "„ručím za fakta, ne za formulace“",
     f"{schemes_per_dim['accountability-for-the-work']} schémat řeší KDO ručí; pole "
     f"ZA CO nenabízí žádné. V korpusu předmět je, ale vždy jen „celá publikace“."),
]
for t, ex, why in THREE:
    lw = wrap(why, "UI", 8.8, W - 2 * M - 250)
    hb = 20 + max(2, len(lw)) * 11.6
    c.setFillColor(WARNL); c.roundRect(M, y - hb, W - 2 * M, hb, 3, stroke=0, fill=1)
    c.setFont("UISB", 9.8); c.setFillColor(INK); c.drawString(M + 14, y - 16, t)
    c.setFont("UISB", 8.8); c.setFillColor(WARN); c.drawString(M + 14, y - 28, ex)
    yy = y - 16
    c.setFont("UI", 8.8); c.setFillColor(GREY)
    for ln in lw:
        c.drawString(M + 250, yy, ln); yy -= 11.6
    y -= hb + 5

y -= 2
y = rule(y)
y = h2(y, "Co je z dat a co ode mě")
JUDG = [
    ("Z dat bez výhrad", "Pořadí os a všechna čísla. Osy vznikly zdola: jedenáct "
     "agentů rozdělilo 1502 doslovných názvů z článků do skupin, nikdo z nich neznal "
     f"schéma tohoto projektu. Výčty na straně {P_HODNOTY} jsou doslovné citace "
     "ověřené skriptem proti staženému textu.", ACCL, ACC),
    ("Ode mě", f"Řez po šesté ose: v datech pro něj opora není. České názvy os a "
     f"příklady u nich. Texty v šesti blocích a obě dvojice příkladů. Věta na "
     f"straně {P_VETA} a její rozdělení na úseky. Párování kroků a os na straně "
     f"{P_KROKY}. Výběr těch tří chybějících věcí. Data neříkají, které osy jsou "
     f"důležité: počet schémat měří doloženost, ne význam.", WARNL, WARN),
]
for title, body, fill, col in JUDG:
    lines3 = wrap(body, "UI", 9, W - 2 * M - 28)
    hb = 26 + len(lines3) * 11.8
    c.setFillColor(fill); c.roundRect(M, y - hb, W - 2 * M, hb, 4, stroke=0, fill=1)
    c.setFont("UISB", 10); c.setFillColor(col); c.drawString(M + 14, y - 17, title)
    yy = y - 32
    c.setFont("UI", 9); c.setFillColor(GREY)
    for ln in lines3:
        c.drawString(M + 14, yy, ln); yy -= 11.8
    y -= hb + 6
foot(P_USUDEK, "Doporučení a úsudek")
c.showPage()

# ===================================================================== page 9
y = H - 56
y = h1(y, "Zdroje",
       "Každé číslo v tomto listu se dá dohledat. Nahoře schémata, která stojí za "
       "přečtení, dole soubory, ze kterých čísla pocházejí.")

SRC = [
    ("F(AI)²R: Who Did What, and Who Checked?", "arXiv:2607.25637",
     "Verifiable AI Provenance as an Executable Skill. Sedmistupňový žebříček "
     f"ověření na straně {P_ZEBRICKY}, plus třídy aktérů, činností a entit. "
     "Data a software: doi:10.5281/zenodo.21667684."),
    ("Xexéo, A Faceted Proposal for Transparent Attribution", "arXiv:2604.25346",
     "Šest facet, u každé stupnice. Generation od G0 „fully human-authored“ po G5. "
     "Nejpodrobnější hotová stupnice v datech."),
    ("AI Assessment Scale (AIAS)", "doi:10.14742/ajet.9434",
     "Pět úrovní od „NO AI“ po „AI Exploration“. Nejrozšířenější ve výuce. Míchá "
     "dvě osy dohromady, druh práce a její rozsah."),
    ("CRediT Contributor Roles Taxonomy", "doi:10.1038/s41467-023-37039-1",
     "Čtrnáct rolí, kdo co na práci dělal. Není o AI, ale je to nejcitovanější "
     "schéma v celé rešerši a stojí za třetím blokem. Existuje i český překlad "
     "rolí, doi:10.31222/osf.io/2rp7s_v2."),
    ("TRACE", "doi:10.48550/arxiv.2608.03329",
     "Čtyři hodnoty odpovědnosti: žádná uvedena, člověk zůstává odpovědný, musí to "
     "zdůvodnit, musí to před odesláním ověřit."),
    ("GiriMedicolegal", "doi:10.5281/zenodo.22784876",
     "Řetěz odpovědnosti vývojář, dodavatel, nemocnice, klinik. Příklad ručení jako "
     "identity, ne jako rozsahu."),
    ("CANGARU", "arXiv:2307.08974",
     "Guideline pro přiznávání AI v akademickém psaní, tři seznamy: co nedělat, co "
     "přiznat, co reportovat."),
    ("GAIDeT, Generative AI Delegation Taxonomy", "doi:10.1080/08989621.2025.2544331",
     "Taxonomie delegovaných úkolů. Použitelná, když potřebujete pojmenovat, co "
     "přesně nástroj dělal."),
    ("TRIPOD+AI a CONSORT-AI", "doi:10.1136/bmj-2023-078378",
     "Reportovací guideliny pro studie s AI. Pokud píšete vědecký text, tohle po "
     "vás nejspíš bude chtít časopis."),
    ("C2PA, Content Credentials", "doi:10.48550/arxiv.2405.12336",
     "Podepsaný záznam připojený k souboru. Pro obrázky a video relevantnější než "
     "pro text."),
    ("DAISY", "arXiv:2604.02760",
     "Šest činností přiznání krát čtyřstupňová škála podpory AI, plus hodnocení "
     "úplnosti hotového přiznání."),
]
for num, (name, ident, what) in enumerate(SRC, 1):
    lw = wrap(what, "UI", 8.4, W - 2 * M - 36)
    c.setFont("UISB", 8.6); c.setFillColor(ACC)
    c.drawString(M, y - 9, "[" + str(num) + "]")
    c.setFont("UISB", 9.4); c.setFillColor(INK)
    c.drawString(M + 30, y - 9, name)
    c.setFont("UI", 8); c.setFillColor(ACC)
    c.drawRightString(W - M, y - 9, ident)
    yy = y - 21
    c.setFont("UI", 8.4); c.setFillColor(GREY)
    for ln in lw:
        c.drawString(M + 30, yy, ln); yy -= 10.6
    y = yy - 2

y = rule(y)
y = h2(y, "Odkud jsou čísla")
DATA = [
    ("[D]", f"{TOTAL_SCHEMES} schémat ze 400 prací, {NROWS} údajů, {len(dims)} os",
     "data/lit/schemes.jsonl, dimensions.json, scheme-merge.json. Každý řádek nese "
     "doslovný citát a identifikátor zdroje; skript ověřil, že citát je doslovný "
     "podřetězec staženého textu. Neověřené řádky se do souboru nedostaly."),
    ("[K]", f"{NITEMS} skutečných formulací, strany {P_KORPUS} až {P_USUDEK}",
     "data/corpus/corpus.jsonl, kódování skladby v data/lit/move-analysis-pilot.json. "
     "Jen anglicky, jen články a software. Česky zatím není sebráno nic, takže "
     "o chování českých formulací tento list neříká nic."),
]
for tag, what, where in DATA:
    lw = wrap(where, "UI", 8.4, W - 2 * M - 40)
    c.setFont("UISB", 8.6); c.setFillColor(ACC); c.drawString(M, y - 9, tag)
    c.setFont("UISB", 9.2); c.setFillColor(INK); c.drawString(M + 34, y - 9, what)
    yy = y - 21
    c.setFont("UI", 8.4); c.setFillColor(GREY)
    for ln in lw:
        c.drawString(M + 34, yy, ln); yy -= 10.6
    y = yy - 4

y = rule(y)
c.setFillColor(PALE)
c.roundRect(M, y - 58, W - 2 * M, 58, 4, stroke=0, fill=1)
c.setFont("UISB", 9.2); c.setFillColor(ACC)
c.drawString(M + 16, y - 18, "JAK VZNIKL TENTO LIST")
para(M + 16, y - 33, "Vygenerovala ho AI, Claude Opus 5 (Anthropic), přímo z datových "
     f"souborů, takže čísla na stranách 1 až {P_KORPUS} nejsou přepisovaná ručně. "
     f"Jan Nehyba zadal, co v něm je, a ručí za výběr a za doporučení na straně "
     f"{P_USUDEK}. Za formulace neručí. Rešerše není publikovaná ani recenzovaná, "
     f"postup je v docs/scoping/report.md.",
     W - 2 * M - 32, "UI", 8.8, 11.4, GREY)

foot(TOTPG)
c.save()
print("napsano:", OUT)
