# Analýza mezery: co literatura modeluje a co projekt tvrdil

Napsáno 2026-09-27 z `data/lit/dimensions.json`,
`data/lit/eight-components-map.json` a `data/lit/schemes.jsonl`. Každé číslo
v tomhle dokumentu se dá v těch souborech přepočítat.

Český překlad souboru `gap-analysis.md`. Přeložený je text, ne data: názvy
kanonických dimenzí (`accountability-for-the-work` a podobně) a doslovné labely
ze zdrojů zůstávají v angličtině, protože jsou to citace a identifikátory, ne
próza. Překlad je vlastní, není publikovaný.

Tenhle dokument odpovídá na RQ5 protokolu, která byla postavená jako
falzifikační test tvrzení, které projekt dělá. Protokol říká: pokud se ukáže,
že tři složky, o kterých projekt tvrdí, že je nikdo nemodeluje, modelované jsou,
zapíše se to a přepíše se tvrzení projektu, ne nález. Jedna z těch tří
modelovaná je. To tvrzení se níže odvolává.

---

## 1. Co rešerše našla

**429 kategoriálních schémat** ze **400 prací**, s **1703 ověřenými řádky
dimenzí**. (Extrakce vyrobila 475 identifikátorů. Agent, který pracuje po
jednom balíčku, nemůže vědět, že v jiném balíčku bylo totéž schéma, takže CRediT
přišlo pod třinácti jmény. 429 je sloučený počet a ten se má uvádět.) Každý
řádek nese citát ze svého zdroje a každý citát ověřil skript proti stažené
předloze. **1502 doslovných labelů** se slučuje do **193 kanonických dimenzí**,
které postavilo zdola jedenáct agentů, kteří si navzájem neviděli do práce, a
pak se to jednou zkonsolidovalo.

Nejsilnější doklad, že ten slovník není artefakt jednoho promptu: sedm z devíti
hlavních dávek otevřeného kódování pracovalo na nepřekrývajících se částech a
dalo téže ose totéž jméno, **extent of AI involvement**. Je to zároveň největší
dimenze, stojí za ní 81 doslovných labelů.

**Dvě ze 193 dimenzí jsou artefakty měření, ne osy**, a každý počet, kterým se
argumentuje, je má vyloučit. `scheme-own-category-inventory` (31 labelů) sbírá
labely, které pojmenovávají vlastní nejvyšší úroveň nějakého schématu, ne
vlastnost přiznání. `generic-study-methodology-reporting` (31 labelů) sbírá
běžné sekce reportovacích guidelinů (Title, Abstract, Methods), které se tam
dostaly proto, že několik guidelinů pro AI je rozšířením těch obecných. Obojí
existuje proto, že extrakce běžela po jednotlivých pracích a tohle vědět
nemohla.

---

## 2. Osm složek proti literatuře

| Složka | Labelů | Dimenzí | Verdikt |
|---|---:|---:|---|
| 2. Podíl AI | 83 | 2 | široce modelováno |
| 3. Co udělal člověk | 74 | 4 | široce modelováno |
| 4. Ručení | 56 | 2 | **široce modelováno, tvrzení se odvolává** |
| 1. Role AI | 55 | 3 | široce modelováno |
| 8. Umístění | 52 | 3 | široce modelováno |
| 5. Jistota | 15 | 4 | slabě, a přesunuto na stroj |
| 7. Očekávání od příjemce | 6 | 4 | modelováno jen v návrhu systémů |
| 6. Stav výstupu | 2 | 1 | **nemodelováno** |

Pět z osmi je dobře doloženo. Ty tři, které projekt vypíchl, nejsou jeden nález,
ale tři různé.

### 4. Ručení: tvrzení bylo špatné

`accountability-for-the-work` nese 23 doslovných labelů a ptá se na přesně tu
otázku, kterou má projekt: kdo odpovídá za hotovou práci, kdo dává finální
schválení, kdo zůstává odpovědný za obsah, kterého se dotkla AI. Přidejte
`authorship-criteria` (33 labelů) a je to jedna z nejlépe doložených složek
v celé rešerši. **Tvrzení projektu, že ručení nikdo nemodeluje, musí pryč.**

Co z něj zůstalo, je užší a zajímavější. Když si těch 23 labelů přečtete, všechny
mluví o tom, **kdo**: author accountability, clinician accountability, final
approval, responsibility allocation statement, liability-responsibility chain,
principle of allocation. Ani jeden z nich není **stupňovaný nárok toho, kdo
podepisuje**. Nikde v literatuře není zaznamenaný rozdíl mezi „ručím za všechno"
a „ručím za fakta, formulace je modelu". Ručení se modeluje jako identita a jako
rozdělení odpovědnosti mezi strany, nikdy jako částečný nebo vymezený nárok,
který podepisující dělá o svém vlastním textu. To je skutečná mezera a dá se
vyslovit v jedné větě, což o původním tvrzení neplatilo.

### 6. Stav výstupu: chybí opravdu

Nic ze 193 dimenzí nezaznamenává, jestli to, co se předává, je koncept, pracovní
verze, nebo hotová věc. `maturity-level-of-the-thing-described` je nejblíž a jeho
dva labely jsou „maturity level ml" a „maturity tier", což popisuje, jak daleko
se dostal nějaký navržený rámec, ne v jakém stavu je text.
`integration-depth-of-ai-content` zaznamenává, kolik úprav výstup AI dostal, což
je zase podíl stroje, ne prohlášení o tom, co se předává.

Tohle je jediná z osmi složek, kterou literatura nemá vůbec, a ta absence není
z nedostatku hledání: 429 schémat, mezi nimi dobrá desítka pojmenovaných
reportovacích guidelinů s desítkami položek.

### 7. Očekávání od příjemce: existuje, ale nikdy jako pole přiznání

Dotýkají se toho čtyři dimenze a mají mezi sebou šest labelů: jestli čtenář
rozumí, jakou roli měla AI, co systém uživateli zobrazí, jestli se dá výstup
rozporovat, jestli jsou nabídnuty alternativy. Všechny pocházejí z prací
o návrhu systémů a z HCI a všechny jsou vlastností **rozhraní**, ne polem,
ve kterém autor říká, co se po čtenáři s tím textem žádá.

Poctivá podoba toho tvrzení tedy není „nikdo to nemodeluje", ale „modeluje se to
jako to, co dělá systém, nikdy jako to, co říká pisatel". Jako pole přiznání
chybí.

### 5. Jistota: je tam, ale míří jinam

Patnáct labelů ve čtyřech dimenzích a tři ze čtyř jsou o stroji, ne o člověku:
jistota, kterou systém vykazuje, kalibrační statistiky, varování, která zobrazí
rozhraní. Jen `limitations-and-validity-boundaries-disclosed` (8 labelů) je
autor, který říká, co jeho vlastní přiznání nepokrývá. Ta osa existuje. Verze,
kde člověk říká, jak je si jistý textem, který podepisuje, skoro ne.

---

## 3. Co to mění pro projekt

1. **Odvolat tvrzení o ručení** všude, kde je, včetně `docs/zadani.md` a všeho,
   co z něj vychází. Nahradit ho tím užším nálezem: ručení se modeluje jako
   identita a rozdělení odpovědnosti, ne jako stupňovaný nárok podepisujícího.
2. **Dvě ze tří zůstávají, v ostřejší podobě.** Stav výstupu chybí. Očekávání od
   příjemce existuje jen jako vlastnost systému. Obojí vyplývá z toho, že se
   přiznání bere jako výpověď adresovaná někomu, což je goffmanovské rámování
   projektu. To rámování má teď pod sebou data, ne tvrzení.
3. **Kódovací kniha se má stavět z crosswalku, ne z osmi složek.** Pět z osmi
   sedí na dimenzích, za kterými stojí 50 až 83 labelů. Kniha, která to ignoruje,
   zahazuje vlastní slovník oboru. Tři slabé v ní zůstanou jako vlastní přínos
   projektu, výslovně označené, a kniha zaznamená, které složky přišly
   z literatury a které ne.
4. **Ten inventář je sám přínos.** Nikdo tahle schémata nesebral a nesrovnal
   jejich dimenze napříč obory. Teď je to soubor, s citátem za každým řádkem.

---

## 4. Co tahle analýza říct nemůže

- **Nemůže říct, že dimenze chybí v literatuře, jen že chybí v tomhle korpusu.**
  Šedá literatura se systematicky neprohledávala, takže instrukce vydavatelů pro
  autory, citační normy a univerzitní politiky jsou zastoupené jen tam, kde na ně
  ukázala nějaká prohledaná práce.
- **Nemůže dimenze seřadit podle důležitosti.** Počet labelů měří, kolik schémat
  tu osu pojmenovalo, což je doloženost, ne významnost. Dimenze se dvěma labely
  může být důležitější než ta s osmdesáti.
- **Mapování osmi složek na slovník je interpretace**, udělaná přečtením 193
  glos. Vědomě jsem ji nedelegoval, protože agent, který má najít v datech
  schéma projektu, má každý důvod ho najít. Kdo s konkrétním mapováním
  nesouhlasí, může si ho zkontrolovat: `eight-components-map.json` jmenuje každou
  dimenzi, kterou počítá.
- **Dva záznamy vypadly kvůli jazyku** až po extrakci, nizozemská zpráva o C2PA
  a portugalský formulář o střetu zájmů. Pravidlo protokolu o angličtině a
  češtině je vylučuje a screeneři je propustili. Dotýká se to osmi řádků.

---

## 5. Lingvistická vrstva: „ručí" za co?

Tenhle oddíl vznikl z otázky, kterou první čtyři neodpovídaly. Když AI napíše
„Jan Nehyba za to ručí", **chybí tam předmět**. Za co ručí? Co to slovo vůbec
znamená? Jaká další slovesa se v té pozici objevují? A jak se ten úsek jmenuje?

Oddíly 1 až 4 o tom nic neříkají, protože popisují **osy**, kterými schémata
přiznání klasifikují, ne **výpovědi**, které lidé skutečně píšou. To je jiná
vrstva. Tady je, co k ní v datech je.

### 5.1 Předmět u „ručí" je v reálných formulacích téměř vždy celý artefakt

Ve korpusu 38 skutečných formulací (anglicky, vědecké články a softwarové
projekty) se predikát ručení objevuje **jen v 5 z 38 položek**. A ve všech pěti
je předmět vyplněný:

| Kolikrát | Předmět |
|---:|---|
| 2 | for the content of the publication |
| 1 | for the content of the submitted manuscript |
| 1 | for the final publication |
| 1 | for the final content |

Všech pět je šablona vydavatele. **Volné formulace ten nárok nedělají vůbec**,
místo prázdného předmětu ho prostě vynechají. Předmět je tedy vždy **celek**
(obsah publikace, finální verze), nikdy část. Nikde není „ručím za fakta" nebo
„ručím za závěry, ne za formulace".

Ta věta, která vás vyprovokovala, „za to ručí", je tedy ještě slabší než šablona:
šablona alespoň pojmenuje, co je předmětem, i když hrubě.

### 5.2 Co udělal člověk: v reálných datech dvě slovesa

Inventář sloves, kterými se v těch 38 formulacích popisuje lidský úkon:

| Kolikrát | Sloveso |
|---:|---|
| 6 | reviewed |
| 4 | edited |

To je všechno. Obojí pochází z jedné šablonové formulace „the authors reviewed
and edited the content as needed". Žádné „read", „verified", „checked",
„recalculated". V tomhle malém korpusu existuje jen jeden úkon, a je to úkon
šablony.

### 5.3 Schémata nabízejí bohatší inventář, ale předmět v něm není proměnná

Schémata předepisují víc. Nejdelší pojmenovaný výčet je „the verification ladder"
ze schématu F(AI)²R, sedm příček:

`unverified` → `needs-research` → `reference-resolved` → `ai-confirmed` →
`source-vendored` → `human-confirmed` → `human-read`

Jiná schémata nabízejí `source check / recalculation / re-analysis`, nebo
`accept / modify / reject`, nebo stupnici `E0 no revision / E1 automated review
only / E2 partial human review / E3 full human review / E4 multi-stage or
independent validation`.

Ale u samotného ručení je to jinak. Když se prohlédne, co ve schématech stojí
jako **hodnoty** dimenze ručení, rozpadá se to na čtyři úplně různé věci, které
se všechny jmenují stejně:

1. **Kdo** ručí: `developer / vendor / hospital / clinician` (řetěz stran)
2. **Jestli** je to řečeno: `Yes / No / No explicit statement`, `required / not required`
3. **Jaký druh** odpovědnosti to je: `causal / moral / legal` (Bleher a Braun)
4. **Co ten člověk musí udělat**: `No responsibility stated / Human remains accountable /
   Must explain-justify the work / Must review-test-validate before submit` (TRACE)

**Ani jeden z těch výčtů nevyplňuje předmět.** Nikde ve 429 schématech není
„ručím za X" jako pole, kde by se X dalo vybrat. To je přesně ta mezera
z oddílu 2, ale teď vyslovená jako věta o jazyce: **ručení je ve schématech buď
identita, nebo binární příznak, nebo typologie práva, nebo povinnost. Nikdy
predikát s doplnitelným předmětem.**

### 5.4 Jak se ten úsek jmenuje

Nejednotně. Ve schématech nese nejčastěji jméno `accountability` nebo
`responsibility`, u vydavatelů „responsibility statement", v konzultaci
k Vancouverskému standardu „attestation".

Pojmenované inventáře variant jsou dva a jsou ve skutečnosti o různých věcech:

- **attestation → review → audit → replication** (Vancouver, session 4.B): stupňuje
  sílu úkonu ověření.
- **the verification ladder**, sedm příček výše (F(AI)²R): stupňuje, co po tom
  úkonu zůstane dohledatelné.

Pro to, co se stupňuje u vašeho příkladu, tedy **rozsah nároku samotného**, žádné
pojmenování v datech není.

### 5.5 Co na tuhle otázku nemám

Tohle je třeba říct rovnou, protože z 5.1 a 5.2 by se dala vyčíst čísla, která
nesnesou váhu:

- **Korpus má 38 položek, jen anglicky, a jen dva žánry.** Na lingvistické
  tvrzení je to málo. Ta čísla ukazují metodu a naznačují tvar, netvrdí nic
  o populaci.
- **Česky nemám nic.** Váš příklad je česky, a čeština v korpusu není zastoupená
  ani jednou položkou. O tom, jak se „ručí" chová v českých formulacích, tahle
  data neříkají nic.
- **Data nejsou kódovaná na predikátové úrovni.** Extrakce zaznamenávala, jakou
  dimenzi schéma nabízí, ne jaký slovesný akt formulace provádí. Na to, co chcete,
  je potřeba jiné kódování: u každé formulace podmět, predikát, předmět, rozsah
  nároku, a jestli je předmět vyplněný, prázdný deiktický („za to"), nebo chybí.
  To je práce na korpusu, ne na schématech.

**Co by to vyžadovalo:** dotáhnout korpus (ten běží ve druhém vlákně, zatím 38 ze
300 položek, česká část zatím nulová) a postavit kódovací knihu na predikátové
struktuře vedle osmi složek. Tohle je myslím ten vlastní výzkumný krok, a
rešerše k němu dala jednu užitečnou věc: ukázala, že ve 429 schématech ta
struktura chybí, takže se nedá vypůjčit a je potřeba ji postavit.
