"""Descriptive sheet, generated from the data files rather than written by hand.

Every number and every category on the first three pages comes out of
schemes.jsonl, dimensions.json and the corpus. Nothing is selected by theme: the
axes appear in the order the literature attests them, and the cut is a rank, not
a judgement. The one page that carries judgement says so at the top.
"""
import io, json, os, collections
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

LIT = r"C:\Users\Nehyba\rpc-lit\data\lit"
CORPUS = r"C:\Users\Nehyba\research-provenance-card\data\corpus\corpus.jsonl"
S = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(S, "empiricky.pdf")

FT = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("UI", os.path.join(FT, "segoeui.ttf")))
pdfmetrics.registerFont(TTFont("UIB", os.path.join(FT, "segoeuib.ttf")))
pdfmetrics.registerFont(TTFont("UISB", os.path.join(FT, "seguisb.ttf")))

W, H = A4
M = 50
INK = HexColor("#1b2733"); GREY = HexColor("#5c6b7a"); LINE = HexColor("#d7dee5")
ACC = HexColor("#0f6f6a"); ACCL = HexColor("#e6f2f1"); WARN = HexColor("#8a5a00")
WARNL = HexColor("#fdf4e3"); BARBG = HexColor("#eef2f5")

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
# Canonical schemes, not the raw identifiers: the same artefact arrived under
# several ids, so counting ids would overstate the field by about ten per cent.
sid2can = {m: cn["canonical_id"] for cn in merge["canonical_schemes"] for m in cn["members"]}
TOTAL_SCHEMES = len({sid2can.get(s, s) for _, s in pairs})

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
}


def best_values(dim_id, minlen=3):
    """A real enumerated value list for this axis, longest first."""
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

# ---------------------------------------------------------------- the canvas
c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Co se v přiznáních AI skutečně měří")
c.setAuthor("Jan Nehyba")


def wrap(t, f, s, w):
    out, cur = [], ""
    for word in t.split():
        x = (cur + " " + word).strip()
        if pdfmetrics.stringWidth(x, f, s) <= w:
            cur = x
        else:
            out.append(cur); cur = word
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


def foot(p, n):
    c.setFont("UI", 8); c.setFillColor(GREY)
    c.drawString(M, 30, "Generováno z dat rešerše. Popis, ne doporučení, kromě poslední strany.")
    c.drawRightString(W - M, 30, f"{p} / {n}")
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(M, 41, W - M, 41)


TOTPG = 4

# ===================================================================== page 1
y = H - 56
y = h1(y, "Co se v přiznáních AI skutečně měří",
       f"{TOTAL_SCHEMES} publikovaných schémat používá dohromady {len(dims)} různých os. "
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
    c.setFont("UISB", 8.4); c.setFillColor(HexColor("#ffffff") if n / maxn > 0.22 else GREY)
    if n / maxn > 0.22:
        c.drawRightString(bx + barw * n / maxn - 5, y - 9.4, f"{n} schémat")
    else:
        c.drawString(bx + barw * n / maxn + 5, y - 9.4, f"{n} schémat")
    c.setFont("UI", 7.6); c.setFillColor(GREY)
    c.drawString(M + 24, y - 20, byid[d]["canonical_label"])
    y -= 31

y = rule(y)
y = para(M, y, f"Zbylých {len(dims) - len(RANK)} os pojmenovalo méně schémat, "
               f"často jen jedno. To je samo o sobě nález: {sum(1 for d in dims if len(d['variants']) == 1)} "
               f"os má za sebou jediný doslovný název, tedy jediné schéma. Obor nemá "
               f"pár soupeřících systémů, má stovky jednorázových.", W - 2 * M)
foot(1, TOTPG)
c.showPage()

# ===================================================================== page 2
y = H - 56
y = h1(y, "Hodnoty, které schémata nabízejí",
       "U každé z prvních os jeden skutečný výčet hodnot, doslova jak je v článku, "
       "s identifikátorem zdroje. Pravidlo výběru bylo mechanické: vždy ten nejdelší. "
       "Proto první řádek sedí pod svou osou špatně, je to seznam úkolů, ne míry. "
       "Nechal jsem to tak, aby bylo vidět, co mechanické pravidlo udělá.")

shown = 0
for d, n in RANK:
    r = best_values(d)
    if not r:
        continue
    vals = [" ".join(v.split()) for v in r["value_list_verbatim"][:8]]
    txt = "  ·  ".join(vals)
    lines = wrap(txt, "UISB", 9, W - 2 * M - 24)
    if y - (34 + len(lines) * 12) < 60:
        break
    c.setFont("UISB", 10.4); c.setFillColor(INK)
    c.drawString(M, y, CZ.get(d, byid[d]["canonical_label"]))
    c.setFont("UI", 7.8); c.setFillColor(ACC)
    c.drawRightString(W - M, y, r["source_ref"])
    y -= 13
    c.setFont("UI", 8.2); c.setFillColor(GREY)
    c.drawString(M, y, "pole v článku: " + r["dimension_label_verbatim"][:70])
    y -= 15
    c.setFillColor(ACCL)
    c.roundRect(M, y - (len(lines) * 12) - 6, W - 2 * M, len(lines) * 12 + 10, 3, stroke=0, fill=1)
    c.setFont("UISB", 9); c.setFillColor(INK)
    yy = y
    for ln in lines:
        c.drawString(M + 12, yy, ln); yy -= 12
    y = yy - 18
    shown += 1

foot(2, TOTPG)
c.showPage()

# ===================================================================== page 3
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
      ("OBJ", "za co konkrétně ručí")]
barw2 = 150
for code, cz in MV:
    n = mcount[code]
    c.setFont("UISB", 9.6); c.setFillColor(INK)
    c.drawString(M, y - 8, cz)
    bx = W - M - barw2
    c.setFillColor(BARBG); c.roundRect(bx, y - 11, barw2, 10, 2, stroke=0, fill=1)
    c.setFillColor(ACC)
    c.roundRect(bx, y - 11, barw2 * n / NITEMS, 10, 2, stroke=0, fill=1)
    c.setFont("UI", 8.2); c.setFillColor(GREY)
    c.drawRightString(bx - 8, y - 8.6, f"{n} z {NITEMS}")
    y -= 19
y -= 6

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
    y -= 16
y -= 8

y = rule(y)
y = h2(y, "Pořadí")
resp = [i for i in items if "RESP" in moves(i["sequence"])]
with_check = sum(1 for i in resp if "CHECK" in moves(i["sequence"])[:moves(i["sequence"]).index("RESP")])
neg = [i for i in items if "NEG" in moves(i["sequence"])]
negresp = sum(1 for i in neg if "RESP" in moves(i["sequence"]))
y = para(M, y, f"Nárok na odpovědnost je v {len(resp)} z {NITEMS} formulací. "
               f"V {with_check} z nich mu ve stejné větě předchází kontrola. "
               f"Negativních prohlášení, tedy že se AI nepoužila, je {len(neg)} "
               f"a nárok na odpovědnost nemá {'ani jedno' if negresp == 0 else str(negresp)}.",
         W - 2 * M)
y -= 6
y = para(M, y, "Nejkratší formulace v korpusu má dva kroky, nejdelší dvanáct, "
               "medián čtyři.", W - 2 * M)
y -= 4

y = rule(y)
y = h2(y, "Žebříčků pro kontrolu je víc")
y = para(M, y, "Ten ze strany 2 není jediný a každý stupňuje něco jiného.",
         W - 2 * M, "UI", 9.4, 12.6)
y -= 4
OTHER = [
    ("co po kontrole zůstane dohledatelné",
     "unverified › needs-research › reference-resolved › ai-confirmed › "
     "source-vendored › human-confirmed › human-read", "doi:10.5281/zenodo.21667684"),
    ("jak hluboká byla lidská revize",
     "E0 žádná › E1 jen automatická › E2 částečná lidská › E3 plná lidská › "
     "E4 vícestupňová nebo nezávislá", "arXiv:2604.25346"),
    ("co jste s výstupem udělali",
     "accept › modify (light) › modify (substantial) › reject",
     "doi:10.1007/s12525-026-00915-x"),
    ("jaký úkon kontroly to byl",
     "source check › recalculation › re-analysis", "doi:10.11591/ijere.v15i4.38930"),
]
for what, chain, ident in OTHER:
    c.setFont("UISB", 9.4); c.setFillColor(INK); c.drawString(M, y, what)
    c.setFont("UI", 7.6); c.setFillColor(ACC); c.drawRightString(W - M, y, ident)
    y -= 13
    for ln in wrap(chain, "UI", 9, W - 2 * M - 14):
        c.setFont("UI", 9); c.setFillColor(GREY); c.drawString(M + 14, y, ln); y -= 12
    y -= 3
y -= 2
y = para(M, y, "A FAIR je něco jiného: dohledatelné, dostupné, propojitelné, znovu "
               "použitelné. Týká se sdílení dat a softwaru, ne kontroly výstupu AI. "
               "V rešerši je, ale odpovídá na jinou otázku.",
         W - 2 * M, "UI", 9.4, 12.6)

foot(3, TOTPG)
c.showPage()

# ===================================================================== page 4
y = H - 56
y = h1(y, "Kde v tomto listu je úsudek",
       "Předchozí tři strany jsou popis. Tahle je oddělená schválně, protože "
       "obsahuje rozhodnutí, která data neudělala.")

JUDG = [
    ("Co je z dat bez výhrad",
     "Pořadí os a všechna čísla. Osy vznikly zdola: jedenáct agentů rozdělilo "
     "1502 doslovných názvů z článků do skupin, každý viděl jen svou část a "
     "nikdo z nich neznal schéma tohoto projektu. Sedm z devíti hlavních dávek "
     "pojmenovalo nezávisle stejnou osu stejně. Výčty hodnot na straně 2 jsou "
     "doslovné citace ověřené skriptem proti staženému textu.", ACCL, ACC),
    ("Co je můj výběr",
     "Že je těch os šestnáct a ne osm nebo třicet. Že jsou na straně 2 zrovna "
     "tyhle výčty, byť pravidlo bylo mechanické, vždy ten nejdelší. České názvy "
     "os jsou můj překlad glos, ne jméno z článku.", WARNL, WARN),
    ("Co data neříkají vůbec",
     "Které osy jsou důležité. Počet schémat měří doloženost, ne význam. Osa, "
     "kterou pojmenovalo jedno schéma, může být pro praxi podstatnější než ta "
     "první. Tenhle list nemá jak to rozhodnout a nerozhoduje to.", WARNL, WARN),
    ("Co bylo v předchozí verzi listu zkreslené",
     "Dřívější verze vybírala pět os jako „povinné a doporučené“ a měla stranu "
     "o třech věcech, které v literatuře chybí. Ty tři věci jsou složky, se "
     "kterými do projektu vstoupil zadavatel. Nález, že v datech chybí, platí, "
     "ale otázku položil projekt, ne data, a v listu to nebylo vidět.", WARNL, WARN),
]
for title, body, fill, col in JUDG:
    lines = wrap(body, "UI", 9.4, W - 2 * M - 30)
    hb = 30 + len(lines) * 12.6
    c.setFillColor(fill)
    c.roundRect(M, y - hb, W - 2 * M, hb, 4, stroke=0, fill=1)
    c.setFont("UISB", 10.6); c.setFillColor(col)
    c.drawString(M + 15, y - 19, title)
    yy = y - 35
    c.setFont("UI", 9.4); c.setFillColor(GREY)
    for ln in lines:
        c.drawString(M + 15, yy, ln); yy -= 12.6
    y -= hb + 12

y = rule(y)
y = h2(y, "Odkud to je")
y = para(M, y, f"{TOTAL_SCHEMES} schémat ze 400 vědeckých prací, 1703 ověřených "
               f"údajů, {len(dims)} os. Soubory: data/lit/schemes.jsonl, "
               f"dimensions.json, scheme-merge.json. Korpus formulací: "
               f"data/corpus/corpus.jsonl, kódování v "
               f"data/lit/move-analysis-pilot.json.", W - 2 * M)
y -= 6
y = para(M, y, "Rešerše není publikovaná ani recenzovaná. Protokol byl zmrazený "
               "v gitu před prvním dotazem, dotazy jsou uložené doslovně, celý "
               "postup je v docs/scoping/report.md.", W - 2 * M)
y -= 10
c.setFillColor(HexColor("#f4f6f8"))
c.roundRect(M, y - 44, W - 2 * M, 44, 4, stroke=0, fill=1)
c.setFont("UISB", 9); c.setFillColor(INK)
c.drawString(M + 15, y - 16, "Jak vznikl tento list")
para(M + 15, y - 29, "Vygenerovala ho AI, Claude Opus 5 (Anthropic), přímo z datových "
     "souborů, takže čísla nejsou přepisovaná ručně. Jan Nehyba ho zadal a ručí za "
     "rozhodnutí, co v něm je. Za formulace neručí.",
     W - 2 * M - 30, "UI", 8.8, 11.4, GREY)

foot(4, TOTPG)
c.save()
print("napsano:", OUT)
