"""One sheet, replacing the two earlier ones.

The earlier pair split badly: a normative guide whose building blocks were my
own selection, and a descriptive sheet that was honest but not much use to
anybody writing a disclosure. This one keeps the practical parts and takes the
building blocks from the data's own ranking, including the axis I had skipped.

Every count on pages 1 to 4 is computed here from schemes.jsonl,
dimensions.json, scheme-merge.json and the corpus; nothing is transcribed.
Pages 5 and 6 carry advice and say so at the top; page 7 carries the sources.
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
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
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
BARBG = HexColor("#eef2f5"); PALE = HexColor("#f4f6f8")

TOTPG = 7

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
RANK = schemes_per_dim.most_common(16)
TOP6 = RANK[:6]
sid2can = {m: cn["canonical_id"] for cn in merge["canonical_schemes"] for m in cn["members"]}
# 429 canonical schemes were found; 416 of them name at least one of these axes.
# The rest are either out of scope or describe only their own inventory.
ALL_SCHEMES = len(merge["canonical_schemes"])
TOTAL_SCHEMES = len({sid2can.get(s, s) for _, s in pairs})
NROWS = len(rows)

CZ = {
    "extent-of-ai-involvement": "Jak velká část je od stroje",
    "ai-tool-identity-and-version": "Který nástroj a jaká verze",
    "contribution-role-taxonomy": "Jakou roli kdo na práci měl",
    "verification-of-ai-output": "Jestli a jak se výstup ověřoval",
    "task-or-function-of-ai-use": "Jakou práci nástroj dělal",
    "accountability-for-the-work": "Kdo za hotovou práci odpovídá",
    "permitted-and-prohibited-ai-use": "Co je dovolené a co zakázané",
    "location-of-the-disclosure": "Kde přiznání v textu stojí",
    "authorship-criteria": "Kdo se smí podepsat jako autor",
    "presence-of-a-disclosure": "Jestli přiznání vůbec je",
    "stage-of-the-process-where-ai-was-used": "V jaké fázi práce se nástroj použil",
    "strength-of-the-disclosure-mandate": "Jak silně se přiznání vyžaduje",
    "traceability-of-output-to-its-sources": "Jestli jde výstup dohledat ke zdrojům",
    "purpose-or-reason-for-ai-use": "Proč se nástroj vůbec použil",
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

# Co si pod tou osou představit, když ji máte sami vyplnit. Text je můj, čísla
# nejsou. Strana 6 to přiznává.
JAK = {
    "extent-of-ai-involvement":
        "Míra, ne druh práce. „AI psala“ neříká, jestli větu, nebo celý článek. "
        "Odhadněte podíl nebo jmenujte tu část: „první koncept kapitoly 3“.",
    "ai-tool-identity-and-version":
        "Jméno a verze, ne „AI“. Verze proto, že se modely mění a za půl roku by "
        "nikdo nevěděl, o čem mluvíte.",
    "contribution-role-taxonomy":
        "Kdo z lidí co dělal. Není to o AI, je to nejcitovanější schéma v celé "
        "rešerši a AI se do něj přidává jako další řádek, ne jako spoluautor.",
    "verification-of-ai-output":
        "Co jste udělali vy, ne že jste „to zkontrolovali“. Kontrola bez předmětu "
        "se nedá ověřit. Hotové žebříčky jsou na straně 4.",
    "task-or-function-of-ai-use":
        "Druh práce: překlad, jazyková úprava, analýza dat, hledání literatury, "
        "kód, obrázek. Ne „pomohl“ a ne „byl použit“.",
    "accountability-for-the-work":
        "Kdo za výsledek ručí. Pozor: 36 schémat řeší KDO, žádné nenabízí pole "
        "ZA CO. To je ta mezera na straně 6.",
}

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

# ---------------------------------------------------------------- the canvas
c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Přiznání AI: co se měří a jak ho napsat")
c.setAuthor("Jan Nehyba")
c.setSubject(f"Praktický list z rešerše {TOTAL_SCHEMES} publikovaných schémat")


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


# ===================================================================== page 1
y = H - 56
y = h1(y, "Co se v přiznáních AI skutečně měří",
       f"Rešerše našla {ALL_SCHEMES} publikovaných schémat, {TOTAL_SCHEMES} z nich "
       f"pojmenovává aspoň jednu osu. Dohromady jich používají {len(dims)}. "
       f"Tady je šestnáct nejčastějších, seřazených podle toho, kolik schémat "
       f"každou pojmenovalo. Pořadí je z dat, není vybrané podle tématu. "
       f"Prvních šest jsou stavební bloky na straně 2.")

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
    c.setFont("UISB", 8.4); c.setFillColor(HexColor("#ffffff") if inside else GREY)
    if inside:
        c.drawRightString(bx + barw * n / maxn - 5, y - 9.4, f"{n} schémat")
    else:
        c.drawString(bx + barw * n / maxn + 5, y - 9.4, f"{n} schémat")
    c.setFont("UI", 8.2); c.setFillColor(HexColor("#6f7f8d"))
    c.drawString(M + 24, y - 20, PRIKLAD.get(d, byid[d]["canonical_label"]))
    y -= 31

y = rule(y)
y = para(M, y, f"Zbylých {len(dims) - len(RANK)} os pojmenovalo méně schémat, "
               f"často jen jedno. To je samo o sobě nález: {sum(1 for d in dims if len(d['variants']) == 1)} "
               f"os má za sebou jediný doslovný název, tedy jediné schéma. Obor nemá "
               f"pár soupeřících systémů, má stovky jednorázových.", W - 2 * M)
foot(1)
c.showPage()

# ===================================================================== page 2
y = H - 56
y = h1(y, "Šest bloků, ze kterých se přiznání skládá",
       "Prvních šest os z předchozí strany, v tom samém pořadí. Nevybíral jsem je "
       "podle tématu, je to prostě těch šest, které pojmenovalo nejvíc schémat. "
       "Popis pod každou z nich je můj.")

for i, (d, n) in enumerate(TOP6, 1):
    body = JAK.get(d, "")
    lb = wrap(body, "UI", 9.6, W - 2 * M - 50)
    hb = 37 + len(lb) * 12.6
    c.setFillColor(PALE)
    c.roundRect(M, y - hb, W - 2 * M, hb, 4, stroke=0, fill=1)
    c.setFillColor(ACC)
    c.circle(M + 24, y - 21, 10.4, stroke=0, fill=1)
    c.setFont("UIB", 10.4); c.setFillColor(HexColor("#ffffff"))
    c.drawCentredString(M + 24, y - 24.6, str(i))
    c.setFont("UISB", 11.6); c.setFillColor(INK)
    c.drawString(M + 45, y - 25, CZ[d])
    c.setFont("UISB", 8.6); c.setFillColor(ACC)
    c.drawRightString(W - M - 14, y - 25, f"{n} schémat")
    c.setFont("UI", 8.6); c.setFillColor(HexColor("#6f7f8d"))
    c.drawString(M + 45, y - 38, PRIKLAD[d])
    yy = y - 52
    c.setFont("UI", 9.6); c.setFillColor(GREY)
    for ln in lb:
        c.drawString(M + 45, yy, ln); yy -= 12.8
    y -= hb + 6

y -= 1
c.setFillColor(ACCL)
c.roundRect(M, y - 52, W - 2 * M, 52, 4, stroke=0, fill=1)
c.setFillColor(ACC); c.rect(M, y - 52, 3.6, 52, stroke=0, fill=1)
c.setFont("UISB", 9.2); c.setFillColor(ACC)
c.drawString(M + 18, y - 18, "DOHROMADY, JAKO JEDNA VĚTA")
c.setFont("UISB", 11.4); c.setFillColor(INK)
c.drawString(M + 18, y - 36, "„První koncept kapitoly 3 napsal Claude (Opus 5). Fakta a citace")
c.drawString(M + 18, y - 50, "jsem ověřil proti zdrojům. Ručím za závěry, ne za formulace.“")
y -= 68
y = para(M, y, "Že takhle má přiznání vypadat, v datech není. Data říkají jen to, "
               "které osy schémata pojmenovávají nejčastěji. Věta výše je můj návrh, "
               "jak je poskládat.", W - 2 * M, "UI", 9.4, 12.6)
y -= 8

y = rule(y)
y = h2(y, "Pět otázek, než to pošlete")
for q in ["Je tam jméno nástroje a verze, ne jen „AI“?",
          "Je tam, co přesně udělal, ne že „pomohl“?",
          "Je tam, co jste zkontrolovali vy, ne jen že jste zkontrolovali?",
          "Ručíte za něco konkrétního, ne „za to“?",
          "Je z toho poznat, jestli je to koncept, nebo finál?"]:
    c.setStrokeColor(ACC); c.setLineWidth(1)
    c.rect(M + 2, y - 9.6, 10.4, 10.4, stroke=1, fill=0)
    c.setFont("UI", 10.2); c.setFillColor(INK)
    c.drawString(M + 24, y - 9, q)
    y -= 18.5
y -= 7
y = para(M, y, "Poslední otázka je jediná, na kterou vám v literatuře nikdo "
               "neporadí. Viz strana 6.", W - 2 * M, "UI", 9.2, 12.4)
foot(2, "Bloky z dat, popisy moje")
c.showPage()

# ===================================================================== page 3
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
    lines = wrap("  ·  ".join(vals), "UISB", 9, W - 2 * M - 24)
    czvals = [CZ_VAL.get(v, v) for v in vals]
    czlines = wrap("  ·  ".join(czvals), "UI", 8.6, W - 2 * M - 24)
    if y - (48 + len(lines) * 12 + len(czlines) * 11) < 60:
        break
    c.setFont("UISB", 10.4); c.setFillColor(INK)
    c.drawString(M, y, CZ.get(d, byid[d]["canonical_label"]))
    c.setFont("UI", 7.8); c.setFillColor(ACC)
    c.drawRightString(W - M, y, r["source_ref"])
    y -= 13
    c.setFont("UI", 8.2); c.setFillColor(GREY)
    c.drawString(M, y, "pole v článku: " + r["dimension_label_verbatim"][:70])
    y -= 15
    boxh = len(lines) * 12 + len(czlines) * 11 + 16
    c.setFillColor(ACCL)
    c.roundRect(M, y - boxh + 12, W - 2 * M, boxh, 3, stroke=0, fill=1)
    c.setFont("UISB", 9); c.setFillColor(INK)
    yy = y
    for ln in lines:
        c.drawString(M + 12, yy, ln); yy -= 12
    yy -= 2
    c.setFont("UI", 8.6); c.setFillColor(GREY)
    for ln in czlines:
        c.drawString(M + 12, yy, ln); yy -= 11
    y = yy - 16

foot(3)
c.showPage()

# ===================================================================== page 4
y = H - 56
y = h1(y, "Žebříčky, ze kterých si můžete vybrat",
       "Když nechcete vymýšlet vlastní stupnici. Je jich víc, protože každý "
       "stupňuje něco jiného. Vyberte ten, který odpovídá na vaši otázku.")

LAD = [
    ("Co po kontrole zůstane dohledatelné", "doi:10.5281/zenodo.21667684",
     ["unverified", "needs-research", "reference-resolved", "ai-confirmed",
      "source-vendored", "human-confirmed", "human-read"],
     ["neověřeno", "nutno dohledat", "odkaz rozřešen", "potvrzeno AI",
      "doloženo zdrojem", "potvrdil člověk", "člověk to četl"],
     "Sedm příček. Neptá se, jak pečlivě jste kontrolovali, ale co by po vás mohl "
     "zkontrolovat někdo další. Pořadí je autorovo."),
    ("Jak hluboká byla lidská revize", "arXiv:2604.25346",
     ["E0", "E1", "E2", "E3", "E4"],
     ["žádná revize", "jen automatická", "částečná lidská", "plná lidská",
      "vícestupňová nebo nezávislá"],
     "Pět příček z facetového modelu. Tohle je ta stupnice, kterou většina lidí "
     "hledá, když chce říct „zkontroloval jsem to“ přesněji."),
    ("Co jste s výstupem udělali", "doi:10.1007/s12525-026-00915-x",
     ["accept", "modify (light)", "modify (substantial)", "reject"],
     ["přijmout", "lehce upravit", "podstatně upravit", "zamítnout"],
     "Čtyři možnosti. Použitelné u každého jednotlivého výstupu zvlášť, ne za celý "
     "text najednou."),
    ("Jaký úkon kontroly to byl", "doi:10.11591/ijere.v15i4.38930",
     ["source check", "recalculation", "re-analysis"],
     ["kontrola zdroje", "přepočet", "nová analýza"],
     "Tři konkrétní úkony. Nejjednodušší způsob, jak nahradit prázdné „zkontroloval "
     "jsem to“ něčím ověřitelným."),
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
y = h2(y, "A FAIR? To je něco jiného")
y = para(M, y, "FAIR znamená Findable, Accessible, Interoperable, Reusable, tedy "
               "dohledatelné, dostupné, propojitelné a znovu použitelné. Je to "
               "o sdílení dat a softwaru, ne o kontrole výstupu AI.", W - 2 * M)
y -= 6
y = para(M, y, "V rešerši je zastoupené silně, čtrnáct os o vlastnostech artefaktu: "
               "trvalý identifikátor, licence, formát, metadata. Odpovídá ale na "
               "jinou otázku: jestli s tou věcí může někdo další pracovat, ne "
               "jestli jste ji zkontrolovali. Plést se to dá snadno, protože obojí "
               "se tváří jako transparentnost.", W - 2 * M)
foot(4)
c.showPage()

# ===================================================================== page 5
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
    y -= 18
y -= 2

y = rule(y)
y = h2(y, "Články a software to píšou jinak")
c.setFont("UISB", 9); c.setFillColor(GREY)
c.drawString(M + 250, y, "články"); c.drawString(M + 330, y, "software")
y -= 15
for code, cz in [("ACTOR", "kdo ho použil"), ("FRAME", "kdy nebo kde"),
                 ("PURPOSE", "k čemu"), ("SCOPE", "jak velká část"),
                 ("CHECK", "že se kontrolovalo"), ("RESP", "že za to někdo ručí")]:
    c.setFont("UI", 9.6); c.setFillColor(INK); c.drawString(M, y, cz)
    c.setFont("UISB", 9.6); c.setFillColor(ACC)
    c.drawString(M + 250, y, f"{gc(art, code)} z {len(art)}")
    c.drawString(M + 330, y, f"{gc(sw, code)} z {len(sw)}")
    y -= 15
y -= 2

y = rule(y)
y = h2(y, "Pořadí a co ten předmět ručení je")
y = para(M, y, f"Poslední dva řádky mají stejné číslo, a to je past. Předmět ručení "
               f"tam je, ale ve všech {nobj} případech je to celá publikace: „for the "
               f"content of the publication“, „for the final content“. Nezužuje nic. "
               f"Formulace, která by ručení omezila na část, v korpusu není.",
         W - 2 * M)
y -= 10
y = para(M, y, f"Nárok na odpovědnost je v {len(resp)} z {NITEMS} formulací. "
               f"V {with_check} z nich mu ve stejné větě předchází kontrola. "
               f"Negativních prohlášení, tedy že se AI nepoužila, je {len(neg)} "
               f"a nárok na odpovědnost nemá {'ani jedno' if negresp == 0 else str(negresp)}.",
         W - 2 * M)
y -= 10

y = rule(y)
y = h2(y, "Nejčastější šablona v článcích, přeložená")
c.setFillColor(PALE)
c.roundRect(M, y - 62, W - 2 * M, 62, 4, stroke=0, fill=1)
para(M + 16, y - 20, "„Při přípravě této práce autoři použili ChatGPT k jazykové "
     "úpravě. Po použití tohoto nástroje autoři obsah zkontrolovali a podle "
     "potřeby upravili a nesou plnou odpovědnost za obsah publikace.“ [12]",
     W - 2 * M - 32, "UI", 9.8, 13.4, INK)
y -= 74
y = para(M, y, "Má celý řetěz a spojkou je svázaný, proto se rozšířila. Pořád ale "
               "„podle potřeby“ neříká, co se kontrolovalo, a ručí se za celek.",
         W - 2 * M, "UI", 9.6, 13)
foot(5)
c.showPage()

# ===================================================================== page 6
y = H - 56
y = h1(y, "Příklady, mezera a kde v listu je úsudek",
       "Tahle strana není popis dat. Jsou na ní doporučení a rozhodnutí, která "
       "data neudělala. Oddělená je schválně.")

y = h2(y, "Slabé a lepší")
colw = (W - 2 * M - 16) / 2
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
    lb = wrap(bad, "UI", 9.6, colw - 26)
    lg = wrap(good, "UI", 9.6, colw - 26)
    lw = wrap(why, "UI", 8.8, W - 2 * M - 20)
    hbox = 30 + max(len(lb), len(lg)) * 12.6
    c.setFillColor(BADL); c.roundRect(M, y - hbox, colw, hbox, 4, stroke=0, fill=1)
    c.setFillColor(GOODL); c.roundRect(M + colw + 16, y - hbox, colw, hbox, 4, stroke=0, fill=1)
    c.setFont("UISB", 8.4); c.setFillColor(BAD); c.drawString(M + 13, y - 15, "SLABÉ")
    c.setFillColor(GOOD); c.drawString(M + colw + 29, y - 15, "LEPŠÍ")
    c.setFont("UI", 9.6); c.setFillColor(INK)
    yy = y - 31
    for ln in lb:
        c.drawString(M + 13, yy, ln); yy -= 12.6
    yy = y - 31
    for ln in lg:
        c.drawString(M + colw + 29, yy, ln); yy -= 12.6
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
n_state = len({r["scheme_id"] for r in rows
               if l2d.get(norm(r["dimension_label_verbatim"])) in
               ("maturity-level-of-the-thing-described", "third-party-handoff-readiness")
               and r["scheme_id"] not in oos})
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
for i, (t, ex, why) in enumerate(THREE, 1):
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

y -= 3
y = rule(y)
y = h2(y, "Co je z dat a co ode mě")
JUDG = [
    ("Z dat bez výhrad", "Pořadí os a všechna čísla. Osy vznikly zdola: jedenáct "
     "agentů rozdělilo 1502 doslovných názvů z článků do skupin, nikdo z nich neznal "
     "schéma tohoto projektu. Výčty na straně 3 jsou doslovné citace ověřené "
     "skriptem proti staženému textu.", ACCL, ACC),
    ("Ode mě", "Že je těch os šestnáct a ne osm nebo třicet. České názvy a příklady "
     "u os. Popisy na straně 2. Věta „dohromady“. Příklady slabé a lepší. Výběr "
     "těch tří chybějících věcí. Data neříkají, které osy jsou důležité: počet "
     "schémat měří doloženost, ne význam.", WARNL, WARN),
]
for title, body, fill, col in JUDG:
    lines = wrap(body, "UI", 9, W - 2 * M - 28)
    hb = 26 + len(lines) * 11.8
    c.setFillColor(fill); c.roundRect(M, y - hb, W - 2 * M, hb, 4, stroke=0, fill=1)
    c.setFont("UISB", 10); c.setFillColor(col); c.drawString(M + 14, y - 17, title)
    yy = y - 32
    c.setFont("UI", 9); c.setFillColor(GREY)
    for ln in lines:
        c.drawString(M + 14, yy, ln); yy -= 11.8
    y -= hb + 6
foot(6, "Doporučení a úsudek")
c.showPage()

# ===================================================================== page 7
y = H - 56
y = h1(y, "Zdroje",
       "Každé číslo v tomto listu se dá dohledat. Nahoře schémata, která stojí za "
       "přečtení, dole soubory, ze kterých čísla pocházejí.")

SRC = [
    ("Xexéo, A Faceted Proposal for Transparent Attribution", "arXiv:2604.25346",
     "Šest facet, u každé stupnice. Generation od G0 „fully human-authored“ po G5. "
     "Nejpodrobnější hotová stupnice v datech."),
    ("AI Assessment Scale (AIAS)", "doi:10.14742/ajet.9434",
     "Pět úrovní od „NO AI“ po „AI Exploration“. Nejrozšířenější ve výuce. Míchá "
     "dvě osy dohromady, druh práce a její rozsah."),
    ("CRediT Contributor Roles Taxonomy", "doi:10.1038/s41467-023-37039-1",
     "Čtrnáct rolí, kdo co na práci dělal. Není o AI, ale je to nejcitovanější "
     "schéma v celé rešerši a stojí za osou číslo 3."),
    ("aiprov, rozšíření PROV-O", "doi:10.5281/zenodo.21667684",
     "Sedmistupňový žebříček ověření od „unverified“ po „human-read“, strana 4."),
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
    ("[K]", f"{NITEMS} skutečných formulací, strany 5 a 6",
     "data/corpus/corpus.jsonl, kódování skladby v data/lit/move-analysis-pilot.json. "
     "Jen anglicky, jen články a software. Česky zatím není sebráno nic, takže "
     "o chování českých formulací tento list neříká nic."),
    ("[12]", "Šablona vydavatele, strana 5",
     "europepmc.org/article/PMC/PMC13471082, otevřený přístup. Totéž znění se "
     "v korpusu opakuje u více článků, je to šablona, ne formulace jednoho autora."),
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
     "souborů, takže čísla na stranách 1 až 5 nejsou přepisovaná ručně. Jan Nehyba "
     "zadal, co v něm je, a ručí za výběr a za doporučení na straně 6. Za formulace "
     "neručí. Rešerše není publikovaná ani recenzovaná, postup je v docs/scoping/report.md.",
     W - 2 * M - 32, "UI", 8.8, 11.4, GREY)

foot(7)
c.save()
print("napsano:", OUT)
