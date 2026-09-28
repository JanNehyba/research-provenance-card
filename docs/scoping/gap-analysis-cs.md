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
| 2. Podíl AI | 75 | 2 | široce modelováno |
| 3. Co udělal člověk | 71 | 4 | široce modelováno |
| 4. Ručení | 54 | 2 | **široce modelováno, tvrzení se odvolává** |
| 1. Role AI | 54 | 3 | široce modelováno |
| 8. Umístění | 52 | 3 | široce modelováno |
| 5. Jistota | 15 | 4 | slabě, a přesunuto na stroj |
| 7. Očekávání od příjemce | 6 | 4 | modelováno jen v návrhu systémů |
| 6. Stav výstupu | 2 | 1 | **nemodelováno** |

Počty labelů **vylučují 15 schémat, která merge označil jako mimo záběr** (41
řádků z 1703, většinou taxonomie autonomie AI systémů). První výpočet je
zahrnoval a čísla byla o 1 až 7 vyšší. Pořadí ani verdikty se tím nemění, u tří
slabých složek se nemění vůbec nic.

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

---

## 6. Skladba: skládá se to vůbec do jedné formulace?

Ano, skládá, a má to pravidla. Oddíly 1 až 5 popisovaly **zásobník**, ze kterého
se vybírá. Tenhle oddíl popisuje **skladbu**: v jakém pořadí ty kroky jdou, co na
čem závisí a co z toho jako celek tvrdí.

Zdroj: 38 skutečných formulací z `data/corpus/corpus.jsonl` (větev
`corpus/collectors`, commit 23776ad). Kódování je v
`data/lit/move-analysis-pilot.json`, řádek po řádku, takže se dá zkontrolovat.
Překlady jsou vlastní a nepublikované; originál je u každé položky uveden.

### 6.1 Jak se tomu říká

Přesně na tohle existuje ustálená metoda a jmenuje se **analýza rétorických
kroků** (move analysis), která je součástí **žánrové analýzy**: u opakujícího se
typu textu se hledají kroky, které jsou povinné, a ty, které jsou volitelné, a
jejich pořadí. Vaše tušení o pragmatice je také správné, protože tři věci
v těch formulacích jsou pragmatické, ne syntaktické:

- **řečový akt**: „použili jsme X" je konstatování, „nesou plnou odpovědnost" je
  závazek, a jsou to dva různé akty v jedné formulaci;
- **presupozice**: „Po použití tohoto nástroje" předpokládá předchozí větu a bez
  ní nestojí;
- **deixe**: prázdné „za to" ve vašem příkladu je ukazovací výraz bez
  antecedentu.

Jména těch metod uvádím z obecné znalosti oboru, **nejsou to nálezy téhle
rešerše**. Co ale nález je: mezi 429 schématy a 193 dimenzemi **není ani jedna
dimenze, která by kódovala skladbu**. Schémata vyjmenovávají, co má být řečeno,
nikdy v jakém pořadí a s jakou návaznostÍ. Tahle vrstva v literatuře chybí, takže
se nedá vypůjčit.

### 6.2 Inventář kroků

Ze 38 formulací (po vyřazení tří, které se do korpusu dostaly omylem, zbývá 35):

| Krok | V kolika z 35 | Co to je |
|---|---:|---|
| `USE` | 28 | predikát použití: „použili", „byl použit", „napsáno s pomocí" |
| `TOOL` | 26 | nástroj, buď konkrétní (Grammarly, ChatGPT GPT-5.5), nebo obecný („AI") |
| `PURPOSE` | 15 | k čemu: „ke kontrole gramatiky", „ke zlepšení čtivosti" |
| `ACTOR` | 14 | lidský podmět: „autoři", „KIF a JY", „my", „já" |
| `FRAME` | 13 | časový nebo textový rámec: „při přípravě této práce", datum |
| `HEAD` | 12 | nadpis, který akt pojmenovává: „Prohlášení o generativní AI" |
| `NEG` | 8 | negativní prohlášení: „nebyla použita žádná umělá inteligence" |
| `SCOPE` | 7 | kvantifikovaný podíl: „části", „mnoho částí", „většina kódu", „výhradně" |
| `CHECK` | 6 | lidský úkon kontroly: „obsah zkontrolovali a upravili" |
| `PART` | 6 | konkrétní část artefaktu jako podmět: „Obrázek 1", „Python skript" |
| `RESP` | 5 | nárok na odpovědnost: „nesou plnou odpovědnost" |
| `OBJ` | 5 | předmět toho nároku: „za obsah publikace" |
| `LINK` | 4 | spojka navazující druhou větu na první: „Po použití tohoto nástroje" |
| `POLICY` | 3 | přítomný čas, trvalá praxe, ne zpráva o tomhle artefaktu: „používáme" |
| `CARVE` | 1 | negativní výjimka zužující pozitivní tvrzení |
| `COND` | 1 | normativní podmínka na výstup: „musí zůstat udržovatelné" |
| `CLAIM_OTHER` | 1 | jiný nárok než kontrola či odpovědnost: „plně rozumím" |
| `ASIDE` | 1 | postojový komentář: „(pardon, puristi, haha)" |

### 6.3 Čtyři pravidla skladby, která z toho vyšla

**1. Povinné jádro jsou dva kroky: `USE` a `TOOL`.** Nic jiného není povinné.
Nejkratší formulace v celém korpusu má dva kroky: „Vygenerováno s Claude Code."
Nejdelší má dvanáct. Medián jsou čtyři.

**2. Nárok na odpovědnost je na konci řetězu a má před sebou kontrolu.** `RESP`
se objevuje pětkrát a čtyřikrát z toho mu předchází `CHECK` ve stejné větě:

> `HEAD FRAME ACTOR USE TOOL PURPOSE` **|** `LINK ACTOR CHECK RESP OBJ`

Ta spojka `LINK` („Po použití tohoto nástroje") je to, co druhou větu **váže na
první**. Nárok na odpovědnost tedy nestojí sám za sebe, je zavěšený za přiznání
použití a za kontrolu. Jediná výjimka je položka 12, kde odpovědnost následuje
hned po použití bez jakékoli kontroly.

**3. Kdo nic nepřiznal, neručí.** Negativních prohlášení je osm a **ani jedno**
neobsahuje nárok na odpovědnost. To dává smysl a zároveň to ukazuje, že ten akt
je licencovaný přiznáním: odpovědnost se přebírá za to, co AI udělala, ne za text
jako takový.

**4. Žánry skládají jinak, a ne v míře, ale v druhu.**

| Krok | Články (19) | Software (16) |
|---|---:|---:|
| `ACTOR` | 13/19 | 1/16 |
| `FRAME` | 12/19 | 1/16 |
| `HEAD` | 11/19 | 1/16 |
| `PURPOSE` | 11/19 | 4/16 |
| `RESP` | 5/19 | 0/16 |
| `CHECK` | 4/19 | 2/16 |
| `SCOPE` | 1/19 | 6/16 |
| `PART` | 2/19 | 4/16 |
| `POLICY` | 0/19 | 3/16 |

Software **maže podmět** (jednou z šestnácti proti třinácti z devatenácti)
a **nikdy neručí**. Články naopak skoro nikdy nekvantifikují podíl, zato ho
zužují účelem („výhradně k jazykové úpravě"), zatímco software kvantifikuje
přímo („části", „mnoho částí", „většina kódu"). To je **dvě různé gramatické
strategie pro totéž**, a přesně ten typ nálezu, na který je projekt postavený.

A tři formulace ze softwaru nejsou zpráva o artefaktu, ale **trvalá politika**
v přítomném čase („Nástroje AI používáme ke zrychlení vývoje"). To je jiný
řečový akt: neříká nic o tom, jak vznikl tenhle konkrétní kód.

### 6.4 Všech 38 formulací

Originál, vlastní překlad, a kódování skladby. `|` dělí věty. Kde je položka
označená, je to nález o sběru, ne o jazyce.

**01.** `article`, šablona

> Declaration of generative AI and AI-assisted technologies in the writing process During the preparation of this work, the authors used Grammarly (Grammarly Inc) to check for grammar, spelling, and clarity. After using this tool/service, the authors reviewed and edited the content as needed and take full responsibility for the content of the publication.

*Překlad:* Prohlášení o generativní AI a technologiích s podporou AI v procesu psaní. Při přípravě této práce autoři použili Grammarly (Grammarly Inc) ke kontrole gramatiky, pravopisu a jasnosti. Po použití tohoto nástroje nebo služby autoři obsah zkontrolovali a podle potřeby upravili a nesou plnou odpovědnost za obsah publikace.

*Skladba:* `HEAD FRAME ACTOR USE TOOL PURPOSE | LINK ACTOR CHECK RESP OBJ`

**02.** `article`, šablona

> Declaration of generative AI and AI-assisted technologies in the writing process During the preparation of this work, the authors used ChatGPT, an AI-assisted language model developed by OpenAI, solely for language editing and improving the clarity and readability of the manuscript. After using this tool, the authors reviewed and edited the content as needed and take full responsibility for the content of the submitted manuscript.

*Překlad:* Prohlášení o generativní AI a technologiích s podporou AI v procesu psaní. Při přípravě této práce autoři použili ChatGPT, jazykový model s podporou AI vyvinutý OpenAI, výhradně k jazykové úpravě a zlepšení jasnosti a čtivosti rukopisu. Po použití tohoto nástroje autoři obsah zkontrolovali a podle potřeby upravili a nesou plnou odpovědnost za obsah odeslaného rukopisu.

*Skladba:* `HEAD FRAME ACTOR USE TOOL SCOPE PURPOSE | LINK ACTOR CHECK RESP OBJ`

**03.** `article`, šablona

> During the preparation of this work, the authors used DeepSeek for language polishing and copy-editing. After using this tool, the authors reviewed and edited the content as needed and take full responsibility for the final publication.

*Překlad:* Při přípravě této práce autoři použili DeepSeek k jazykovému vyhlazení a redakční úpravě. Po použití tohoto nástroje autoři obsah zkontrolovali a podle potřeby upravili a nesou plnou odpovědnost za finální publikaci.

*Skladba:* `FRAME ACTOR USE TOOL PURPOSE | LINK ACTOR CHECK RESP OBJ`

**04.** `article`, šablona

> Acknowledgments During the preparation of this work, KIF and JY used Chat GPT to improve writing.

*Překlad:* Poděkování. Při přípravě této práce KIF a JY použili Chat GPT ke zlepšení psaní.

*Skladba:* `HEAD FRAME ACTOR USE TOOL PURPOSE`

**05.** `article`, volná formulace

> Additionally, the authors used generative AI to create Fig. 1.

*Překlad:* Autoři navíc použili generativní AI k vytvoření obr. 1.

*Skladba:* `ACTOR USE TOOL PURPOSE`

**06.** `article`, volná formulace

> The Generative AI statement: States that we have used generative AI in the creation of this manuscript. We have not used any generative AI.

*Překlad:* Prohlášení o generativní AI: Uvádí, že jsme v tvorbě tohoto rukopisu použili generativní AI. Žádnou generativní AI jsme nepoužili.

*Skladba:* `HEAD ACTOR USE PURPOSE | ACTOR NEG`

*Pozor:* self-contradictory: the heading asserts use, the next sentence denies it

**07.** `article`, šablona

> Declaration of Generative AI and AI-assisted technologies in the writing process: During the preparation of this work the authors used generative AI technologies to improve readability and language structure. After using this tool/service, the authors reviewed and edited the content as needed and take full responsibility for the content of the publication.

*Překlad:* Prohlášení o generativní AI a technologiích s podporou AI v procesu psaní: Při přípravě této práce autoři použili technologie generativní AI ke zlepšení čtivosti a jazykové struktury. Po použití tohoto nástroje nebo služby autoři obsah zkontrolovali a podle potřeby upravili a nesou plnou odpovědnost za obsah publikace.

*Skladba:* `HEAD FRAME ACTOR USE TOOL PURPOSE | LINK ACTOR CHECK RESP OBJ`

**08.** `article`, volná formulace

> Results ChatGPT was used to automate concept retrieval, problem‐solving and applying theory to clinical context. This occurred because students were motivated by the efficient completion of workbook questions, which could be achieved by entering them into ChatGPT. Collaborative groups were less likely to automate cognitive effort because they placed greater value on being engaged during learning and perceived socially constructing answers as more efficient than ChatGPT use. Although ChatGPT sometimes gave partial or false‐but‐plausible answers, students were rarely observed cross‐checking it.

*Překlad:* Výsledky. ChatGPT byl použit k automatizaci vyhledávání pojmů, řešení problémů a aplikace teorie na klinický kontext. Dělo se to proto, že studenty motivovalo efektivní dokončení otázek v pracovním listu, čehož šlo dosáhnout jejich zadáním do ChatGPT. Skupiny, které spolupracovaly, automatizovaly kognitivní úsilí méně, protože si více cenily zapojení během učení.

*Skladba:* `TOOL USE PURPOSE`

*Pozor:* not a disclosure: a findings sentence about what students did, collected in error

**09.** `article`, volná formulace

> Figure 1 Sandwich Generation Caregiver Subtypes and Atypical Burden was created with the assistance of ChatGPT (OpenAI, GPT-5.5) to illustrate our understanding of Abramson’s (2015) overview of the different subtypes of sandwich generation caregivers.

*Překlad:* Obrázek 1 Podtypy pečujících sendvičové generace a atypická zátěž byl vytvořen s pomocí ChatGPT (OpenAI, GPT-5.5), aby ilustroval naše chápání Abramsonova (2015) přehledu různých podtypů pečujících sendvičové generace.

*Skladba:* `PART USE TOOL PURPOSE`

**10.** `article`, volná formulace

> Medical illustration concept generated with the assistance of ChatGPT (OpenAI, GPT-5.5 Thinking) on May 19, 2026.

*Překlad:* Koncept medicínské ilustrace vytvořen s pomocí ChatGPT (OpenAI, GPT-5.5 Thinking) dne 19. května 2026.

*Skladba:* `PART USE TOOL FRAME`

**11.** `article`, volná formulace

> Acknowledgments ChatGPT5 was used to improve the readability of the manuscript.

*Překlad:* Poděkování. ChatGPT5 byl použit ke zlepšení čtivosti rukopisu.

*Skladba:* `HEAD TOOL USE PURPOSE`

**12.** `article`, volná formulace

> AI-assisted language editing was used to improve the readability of this manuscript; the authors take full responsibility for the final content.

*Překlad:* K zlepšení čtivosti tohoto rukopisu byla použita jazyková úprava s podporou AI; autoři nesou plnou odpovědnost za finální obsah.

*Skladba:* `USE PURPOSE | ACTOR RESP OBJ`

*Pozor:* responsibility claimed with no checking move before it

**13.** `article`, volná formulace

> Specifically, Paperpal (Editage, Mumbai, India) was used to improve the readability of the manuscript. No AI tools were used to generate content, analyze data, search for literature, or manipulate images.

*Překlad:* Konkrétně byl ke zlepšení čtivosti rukopisu použit Paperpal (Editage, Mumbai, Indie). Žádné nástroje AI nebyly použity k vytváření obsahu, analýze dat, hledání literatury ani manipulaci s obrázky.

*Skladba:* `TOOL USE PURPOSE | CARVE`

**14.** `article`, volná formulace

> STATEMENT ON THE USE OF ARTIFICIAL INTELLIGENCE No artificial intelligence was used in the preparation of this article

*Překlad:* PROHLÁŠENÍ O POUŽITÍ UMĚLÉ INTELIGENCE. Při přípravě tohoto článku nebyla použita žádná umělá inteligence.

*Skladba:* `HEAD NEG FRAME`

**15.** `article`, volná formulace

> STATEMENT ON THE USE OF ARTIFICIAL INTELLIGENCE No artificial intelligence was used in the preparation of this work.

*Překlad:* PROHLÁŠENÍ O POUŽITÍ UMĚLÉ INTELIGENCE. Při přípravě této práce nebyla použita žádná umělá inteligence.

*Skladba:* `HEAD NEG FRAME`

**16.** `article`, volná formulace

> The authors declare that this manuscript did not use any Generative AI.

*Překlad:* Autoři prohlašují, že tento rukopis nepoužil žádnou generativní AI.

*Skladba:* `ACTOR NEG`

**17.** `article`, šablona

> Declaration of generative AI in scientific writing: During the preparation of this work, the authors did not use any generative AI or AI-assisted technologies.

*Překlad:* Prohlášení o generativní AI ve vědeckém psaní: Při přípravě této práce autoři nepoužili žádnou generativní AI ani technologie s podporou AI.

*Skladba:* `HEAD FRAME ACTOR NEG`

**18.** `article`, volná formulace

> The authors did not use any generative AI or AI‐assisted technologies in the preparation of this manuscript.

*Překlad:* Autoři při přípravě tohoto rukopisu nepoužili žádnou generativní AI ani technologie s podporou AI.

*Skladba:* `ACTOR NEG FRAME`

**19.** `article`, volná formulace

> Declaration of the use of generative AI and AI-assisted technologies in scientific writing and in figures, images and artwork The authors declare that they did not use any generative AI and/or AI-assisted technologies in writing the manuscript TJPAD-26–00,085.

*Překlad:* Prohlášení o použití generativní AI a technologií s podporou AI ve vědeckém psaní a v obrázcích, ilustracích a grafice. Autoři prohlašují, že při psaní rukopisu TJPAD-26-00,085 nepoužili žádnou generativní AI ani technologie s podporou AI.

*Skladba:* `HEAD ACTOR NEG FRAME`

**20.** `article`, volná formulace

> Declaration of AI The authors declare that no AI tools were used in the preparation of this manuscript.

*Překlad:* Prohlášení o AI. Autoři prohlašují, že při přípravě tohoto rukopisu nebyly použity žádné nástroje AI.

*Skladba:* `HEAD ACTOR NEG FRAME`

**21.** `software_project`, volná formulace

> Make enumeration demand driven (#4367) * Relocate the memento pool to the proof spine Generated with Claude Code

*Překlad:* Udělat enumeraci řízenou poptávkou (#4367) * Přesunout pool memento na osu důkazu. Vygenerováno s Claude Code.

*Skladba:* `USE TOOL`

**22.** `software_project`, volná formulace

> Stamp visual report symbol kinds at emission (#4388) * Stamp report symbol kinds at emission Generated with Claude Code

*Překlad:* Označit druhy symbolů vizuálního reportu při emisi (#4388) * Označit druhy symbolů reportu při emisi. Vygenerováno s Claude Code.

*Skladba:* `USE TOOL`

**23.** `software_project`, volná formulace

> Generated with Claude Code Co-Authored-By: Claude <email redacted>

*Překlad:* Vygenerováno s Claude Code. Co-Authored-By: Claude <e-mail redigován>

*Skladba:* `USE TOOL`

**24.** `software_project`, volná formulace

> Added disclaimer that this was written with the help of AI

*Překlad:* Přidáno upozornění, že tohle bylo napsáno s pomocí AI.

*Skladba:* `USE TOOL`

*Pozor:* meta: a commit reporting that a disclaimer was added

**25.** `software_project`, volná formulace

> Add files via upload Performance test written with the help of AI.

*Překlad:* Přidat soubory nahráním. Výkonnostní test napsán s pomocí AI.

*Skladba:* `PART USE TOOL`

**26.** `software_project`, volná formulace

> Standardize commit message footer instruction - Updated footer text to "AI-Assisted Commit Message" - Removed restriction on blank line after the footer - Clarified formatting requirements for commit messages

*Překlad:* Standardizovat instrukci pro patičku commit message. Aktualizován text patičky na „AI-Assisted Commit Message“. Zrušeno omezení na prázdný řádek po patičce. Vyjasněny formátovací požadavky na commit messages.

*Skladba:* `POLICY`

*Pozor:* meta: a commit about the wording of a commit-message footer, not a disclosure

**27.** `software_project`, volná formulace

> Some parts of this project were generated or assisted by AI.

*Překlad:* Části tohoto projektu byly vygenerovány AI nebo vznikly s její pomocí.

*Skladba:* `SCOPE USE TOOL`

**28.** `software_project`, volná formulace

> Parts of this project were generated with Amazon Q Developer.

*Překlad:* Části tohoto projektu byly vygenerovány s Amazon Q Developer.

*Skladba:* `SCOPE USE TOOL`

**29.** `software_project`, volná formulace

> Many parts of this project were generated with AI (sorry purists, haha), but I have reviewed it and fully understand all of its output.

*Překlad:* Mnoho částí tohoto projektu bylo vygenerováno AI (pardon, puristi, haha), ale zkontroloval jsem to a plně rozumím všemu, co z toho vyšlo.

*Skladba:* `SCOPE USE TOOL ASIDE | ACTOR CHECK CLAIM_OTHER`

**30.** `software_project`, volná formulace

> Parts of this project were generated or assisted by AI tools, and were reviewed and modified by a human before publication.

*Překlad:* Části tohoto projektu byly vygenerovány nástroji AI nebo vznikly s jejich pomocí a před publikováním je zkontroloval a upravil člověk.

*Skladba:* `SCOPE USE TOOL | CHECK FRAME`

**31.** `software_project`, volná formulace

> This documentation was written with Conda 4.6.12.

*Překlad:* Tato dokumentace byla napsána s Conda 4.6.12.

*Skladba:* `PART USE TOOL`

*Pozor:* not an AI disclosure: Conda is a package manager, collected in error

**32.** `software_project`, volná formulace

> A significant part of this codebase was written with the help of AI coding assistants, primarily Claude (Anthropic), used for implementation, shader debugging, and refactoring.

*Překlad:* Významná část této kódové báze byla napsána s pomocí AI asistentů pro kód, především Claude (Anthropic), použitých k implementaci, ladění shaderů a refaktoringu.

*Skladba:* `SCOPE USE TOOL PURPOSE`

**33.** `software_project`, volná formulace

> The Python script was written with the help of AI.

*Překlad:* Ten Python skript byl napsán s pomocí AI.

*Skladba:* `PART USE TOOL`

**34.** `software_project`, volná formulace

> AI coding tools - most of the code was written with the help of AI (Claude, GPT-5, Cursor Composer and others)

*Překlad:* Nástroje AI pro kód. Většina kódu byla napsána s pomocí AI (Claude, GPT-5, Cursor Composer a další).

*Skladba:* `HEAD SCOPE USE TOOL`

**35.** `software_project`, volná formulace

> The patching code was written with the help of AI tools.

*Překlad:* Kód pro patchování byl napsán s pomocí nástrojů AI.

*Skladba:* `PART USE TOOL`

**36.** `software_project`, volná formulace

> We use AI tools to speed up development and code review.

*Překlad:* Nástroje AI používáme ke zrychlení vývoje a revize kódu.

*Skladba:* `POLICY USE TOOL PURPOSE`

**37.** `software_project`, volná formulace

> We use AI tools to develop Scout.

*Překlad:* Nástroje AI používáme k vývoji Scoutu.

*Skladba:* `POLICY USE TOOL PURPOSE`

**38.** `software_project`, volná formulace

> We use AI tools to accelerate development, but all outputs must remain maintainable, portable, and aligned with our engineering standards.

*Překlad:* Nástroje AI používáme ke zrychlení vývoje, ale všechny výstupy musí zůstat udržovatelné, přenositelné a v souladu s našimi inženýrskými standardy.

*Skladba:* `POLICY USE TOOL PURPOSE | COND`

### 6.5 Co je na tom vidět a co ne

Tři položky se do korpusu dostaly omylem a je to nález o sběrači: **08** je věta
z výsledků o tom, co dělali studenti, ne přiznání autorů; **31** říká, že
dokumentace byla napsána s Condou, což je správce balíčků, ne AI; **26** je
commit o formátování patičky commit messages. Sběrač hledá fráze a tyhle tři
frázi obsahují, ale přiznání nejsou.

Položka **06** je zajímavější a není to chyba sběru: **sama si odporuje.**
Nadpis tvrdí, že generativní AI byla použita, a hned následující věta to popírá.
Taková formulace v žádném schématu nemá kategorii, protože schémata předpokládají,
že přiznání je konzistentní.

**A teď limity, které jsou u téhle vrstvy tvrdší než u zbytku dokumentu.**
38 položek je pilot, ne vzorek. Jsou jen anglicky, jen ve dvou žánrech ze šesti,
a čeština není zastoupená ani jednou položkou. Rozdíly mezi žánry v 6.3 vycházejí
z devatenácti a šestnácti položek, což na tvrzení nestačí; ukazují, že ten rozdíl
lze měřit, ne jak velký je. Kódování jsem dělal sám a nikdo ho nekontroloval,
takže o jeho reliabilitě nevím nic.

**Co by to vyžadovalo:** dotáhnout korpus na plánovaných 300 položek ve dvanácti
buňkách, přidat českou část, a postavit kódovací knihu na téhle skladbě, ne jen
na osmi složkách. Rešerše k tomu přispěla jednu věc: ukázala, že tahle vrstva ve
429 schématech chybí, takže se nedá vypůjčit a je potřeba ji postavit.

---

## 7. Příklady dimenzí z článků, doslovně

Oddíly 1 až 5 uváděly jména dimenzí a počty. To je málo, protože z toho není
vidět, co v těch článcích doopravdy stojí. Tady je pro každou důležitou osu
několik skutečných řádků z dat: schéma, zdroj, doslovný label, výčet hodnot, a
citát, který brána ověřila proti stažené předloze.

Citáty jsou v originále, protože jsou to citáty. Nepřekládám je, aby zůstaly
dohledatelné. Všechno pochází z `data/lit/schemes.jsonl`. Řádky z patnácti
schémat, která merge označil jako mimo záběr, jsou vynechané: v prvním běhu se
mezi příklady podílu AI dostaly stupnice autonomie kyberbezpečnostních systémů,
což ten nález zkresluje.

### Podíl AI: nejlépe doložená osa v celé rešerši

`extent-of-ai-involvement` · 74 doslovných labelů · 74 schémat

*Glosa:* How much of the output or task the machine did relative to the human, expressed as an ordered scale, level, tier, percentage or categorical band.

**Genai lr checklist three domains** (research_publishing, empirical_study, doi:10.38124/ijisrt/25oct243)

- label v článku: **AI Usage**
- hodnoty, které schéma nabízí: Permission to use AI · Role in research design · Language editing · Manuscript drafting · Idea generation · Image or graphic creation · Data generation · Data collection · Data analysis and interpretation · Coding or programming
- citát: „The pieces were classified into three thematic categories: authorship, applications, and human accountability." (B. Specific Aspects of AI Guidelines)

**Credit merit ordinal contribution scale** (research_publishing, normative_proposal, doi:10.31234/osf.io/s6h58)

- label v článku: **fine-grained**
- hodnoty, které schéma nabízí: minimal · slight · moderate · substantial · extensive · full
- citát: „fine-grained (e.g., minimal, slight, moderate, substantial, extensive, and full)" (abstract)

**Faceted ai attribution model** (research_publishing, normative_proposal, arXiv:2604.25346)

- label v článku: **Generation**
- hodnoty, které schéma nabízí: G0: fully human-authored. · G1: AI-assisted completion. · G2: AI-generated with a simple prompt. · G3: AI-generated with a detailed prompt. · G4: AI-generated through iterative conversation. · G5: AI-generated through a structured multi-step conversational or computational pipeline.
- definice: „describes how a text segment came into existence"
- citát: „The Generation facet describes how a text segment came into existence." (3.2 Generation)

**graduated disclosure framework for AI contributions in biomedical publications** (research_publishing, normative_proposal, doi:10.1097/io9.0000000000000370)

- label v článku: **the level of AI involvement in research and writing**
- hodnoty, které schéma nabízí: Level 1 (minimal) · Level 2 (standard) · Level 3 (enhanced) · Level 4 (critical) · Never
- definice: „the level of disclosure should be proportional to the impact of AI on the contents of the manuscript"
- citát: „we outline a system of graduated levels of disclosure regarding the use of AI (Table 2 and the flowchart shown in Figure 1)" (abstract)


### Co udělal člověk: úkon kontroly

`verification-of-ai-output` · 39 doslovných labelů · 41 schémat

*Glosa:* Whether and how AI-produced content was checked, validated, corrected or confirmed before use, and how extensive that review was.

**aiprov** (research_publishing, normative_proposal, doi:10.5281/zenodo.21667684)

- label v článku: **the verification ladder**
- hodnoty, které schéma nabízí: unverified · needs-research · reference-resolved · ai-confirmed · source-vendored · human-confirmed · human-read
- definice: „Rungs answer who
checked what"
- citát: „TABLE I: The verification ladder. Positions are machine-readable
( aiprov:ladderPosition )" (Table I)

**Vietnam advertising reform taxonomy** (advertising, normative_proposal, doi:10.62225/2583049x.2026.6.3.6356)

- label v článku: **claim substantiation duty**
- hodnoty, které schéma nabízí: quality · origin · performance · safety · health effects · financial benefit · environmental impact
- citát: „Any objective advertising claim about quality, origin, performance, safety, health effects, financial benefit or environmental impact" (Policy Recommendations)

**Ai sr conceptual framework** (research_publishing, normative_proposal, doi:10.1016/j.gloepi.2026.100282)

- label v článku: **Validity**
- hodnoty, které schéma nabízí: Human verification procedures · source traceability · proportion of AI outputs checked · duplicate or independent verification · discrepancy resolution · criteria for accepting, modifying, or rejecting AI outputs
- citát: „Validity Human verification procedures; source traceability; proportion of AI outputs checked" (Table 3)

**Faceted ai attribution model** (research_publishing, normative_proposal, arXiv:2604.25346)

- label v článku: **Evaluation**
- hodnoty, které schéma nabízí: E0: no revision. · E1: automated review only. · E2: partial human review. · E3: full human review. · E4: multi-stage or independent validation.
- definice: „describes how the resulting text was reviewed, checked, or validated"
- citát: „The Evaluation facet describes how the resulting text was reviewed, checked, or validated." (3.3 Evaluation)


### Ručení: čtyři různé věci pod jedním jménem

`accountability-for-the-work` · 22 doslovných labelů · 36 schémat

*Glosa:* Who answers for the finished work - who approves it, who remains responsible for AI-touched content, and how liability is distributed along a chain of parties.

**GiriMedicolegal™ CDSS** (law_regulation, normative_proposal, doi:10.5281/zenodo.22784877)

- label v článku: **a liability-responsibility chain**
- hodnoty, které schéma nabízí: developer · vendor · hospital · clinician
- citát: „a liability-responsibility chain across developer, vendor, hospital and clinician" (abstract)

**TRACE** (software, empirical_study, doi:10.48550/arxiv.2608.03329)

- label v článku: **Responsibility**
- hodnoty, které schéma nabízí: No responsibility stated. · Human remains accountable. · Must explain/justify the work. · Must review/test/validate before submit.
- definice: „human accountability for AI output"
- citát: „Responsibility (human accountability for AI output)," (Table I)

**Girimedicolegal liability responsibility chain** (law_regulation, normative_proposal, doi:10.5281/zenodo.22784876)

- label v článku: **liability-responsibility chain**
- hodnoty, které schéma nabízí: developer · vendor · hospital · clinician
- citát: „a liability-responsibility chain across developer, vendor, hospital and clinician" (abstract)

**Originality transparency accountability** (education_assessment, normative_proposal, doi:10.29140/97817637116240-25)

- label v článku: **accountability**
- hodnoty, které schéma nabízí: workshops on ethical AI use and detection techniques · writing tutorials · grading penalties for undisclosed AI use · disciplinary punishments for repeated violations
- definice: „accountability is ensured by updating AI ethical guidance and academic policy, discipline-specific practices and training programs"
- citát: „including workshops on ethical AI use and detection techniques, writing tutorials" (4)


### Umístění přiznání

`location-of-the-disclosure` · 34 doslovných labelů · 28 schémat

*Glosa:* Where the disclosure sits - which manuscript section, dedicated statement, byline, cover letter or private channel, and under what heading.

**CheckList for EvaluAtion of Radiomics research (CLEAR)** (research_publishing, reporting_guideline, doi:10.1186/s13244-023-01415-8)

- label v článku: **Section**
- hodnoty, které schéma nabízí: Title · Abstract · Keywords · Introduction · Method · Data · Segmentation · Pre-processing · Feature extraction · Data preparation
- citát: „Table 1  CheckList for EvaluAtion of Radiomics research (CLEAR checklist)
Section" (Table 1)

**TRIPOD+AI** (research_publishing, reporting_guideline, doi:10.1136/bmj-2023-078378)

- label v článku: **Methods**
- hodnoty, které schéma nabízí: Data · Participants · Data preparation · Outcome · Predictors · Sample size · Missing data · Analytical methods · Class imbalance · Fairness
- definice: „Describe how missing data were handled. Provide reasons for omitting any data"
- citát: „Describe the sources of data separately for the development and evaluation datasets" (Table 2)

**PRISMA-trAIce checklist** (research_publishing, reporting_guideline, doi:10.2196/80247)

- label v článku: **Methods**
- hodnoty, které schéma nabízí: P-trAIce M1 - Protocol and Registration · P-trAIce M2 - Identification and Access · P-trAIce M3 - Purpose and Stage of Application · P-trAIce M4 - Input Data · P-trAIce M5 - Output Data · P-trAIce M6 - Prompt Engineering · P-trAIce M7 - Operational Details and Settings · P-trAIce M8 - Human-AI Interaction and Oversight · P-trAIce M9 - AI Performance Evaluation · P-trAIce M10 - Data Governance and Ethics
- definice: „If specific AI tools or AI-assisted methods were pre-specified in the review protocol"
- citát: „Methods P-trAIce M1 - Protocol and Registration If specific AI tools or AI-assisted methods were pre-specified in the review protocol" (Table 1)

**The STARD-AI checklist** (research_publishing, reporting_guideline, doi:10.1038/s41591-025-03953-8)

- label v článku: **Section and topic**
- hodnoty, které schéma nabízí: Title or abstract · Analysis · Results · Participants and dataset · Test results · Discussion · Other information
- citát: „the checklist contains items relating to the title or abstract (item 1), abstract (item 2), introduction (items 3 and 4), methods (items 5–23)," (Table 2 | The STARD-AI checklist)


### Míra podrobnosti přiznání

`granularity-and-detail-of-the-disclosure` · 13 doslovných labelů · 11 schémat

*Glosa:* How much detail the disclosure gives and at what layer - from no detectable statement through partial to a full, traceable, layered account.

**AI Disclosure Guidance for Authors based on Editor Expectations** (research_publishing, reporting_guideline, doi:10.1101/2025.07.17.25331725)

- label v článku: **Complexities of Sufficiency and Necessity**
- hodnoty, které schéma nabízí: Distinguish between technical & intellectual use. · Be strategic about the level of detail. · Indicate how you verified content. · Aim for credibility, not necessarily reproducibility. · Don’t avoid disclosure in fear of punitive action.
- citát: „Distinguish between technical & intellectual use. Intellectual uses are 
of more concern to editors and require more explanation." (Table 2. AI Disclosure Guidance for Authors based on Editor Expectations)

**four-tier disclosure granularity variable** (research_publishing, empirical_study, doi:10.1016/j.patter.2026.101585)

- label v článku: **disclosure granularity**
- hodnoty, které schéma nabízí: tier 0 · tier 1 · tier 2 · tier 3
- definice: „disclose not merely that AI was used, but how it was used."
- citát: „tier 0 denotes no detectable AI disclosure; tier 1 denotes a general reference" (Does more granular disclosure track more strongly with open science?)

**Dimensions along which survey participants indicate their preferences for framing AI disclosures** (research_publishing, empirical_study, doi:10.48550/arxiv.2608.23271)

- label v článku: **Length**
- hodnoty, které schéma nabízí: 1-2 sentences · A few sentences or a short paragraph · Multiple paragraphs · Length and detail proportionate to the extent of AI use
- citát: „we elicit preferences on details and length through multiple-choice questions" (Table 2)

**GAMER checklist** (research_publishing, reporting_guideline, doi:10.1136/bmjebm-2025-113825)

- label v článku: **AI-assisted sections in manuscript**
- hodnoty, které schéma nabízí: Yes · No · N/A
- definice: „Report the specific section or paragraphs of the manuscript that GAI tools contributed to."
- citát: „declaration of new GAI model(s) developed, AI-assisted sections in manuscript, content verification, data privacy" (Table 1)


### Co všechno má přiznání obsahovat

`required-content-of-the-disclosure` · 14 doslovných labelů · 12 schémat

*Glosa:* The bundle of data points a disclosure must contain to count as complete - tool, task, operator, date, oversight, responsibility - stated as one composite requirement.

**Dimensions along which survey participants indicate their preferences for framing AI disclosures** (research_publishing, empirical_study, doi:10.48550/arxiv.2608.23271)

- label v článku: **details dimension**
- hodnoty, které schéma nabízí: Task · Model name · Reason for AI use · Non-use of AI · Human oversight · Responsibility declaration · Purpose of disclosure
- citát: „The specific options, present in Table 2 were consolidated from existing conference guidelines and conceptual frameworks outlined in past work" (Table 2)

**Daisy completeness coding scheme** (research_publishing, empirical_study, arXiv:2604.02760)

- label v článku: **six elements**
- hodnoty, které schéma nabízí: the name of the AI tool used · the version of the tool · the location of AI use within the manuscript · the purpose of AI use · the extent or level of AI involvement · an explicit statement that responsibility for the content remains with the authors
- citát: „Completeness was assessed using a binary coding scheme indicating whether each disclosure statement included the following six elements" (4.1.4. Measures)

**AI Disclosure Guidance for Authors based on Editor Expectations** (research_publishing, reporting_guideline, doi:10.1101/2025.07.17.25331725)

- label v článku: **Disclosure Basics**
- hodnoty, které schéma nabízí: State how you used AI. · Be specific: tool, tasks, location. · Add a responsibility statement. · Put the disclosure in your 
manuscript. · When in doubt, disclose.
- citát: „Table 2. AI Disclosure Guidance for Authors based on Editor Expectations 
Disclosure Basics 
Complexities of Sufficiency and Necessity 
State how you used AI." (Table 2. AI Disclosure Guidance for Authors based on Editor Expectations)

**MINIMAR (MINimum Information for Medical AI Reporting)** (research_publishing, reporting_guideline, doi:10.1093/jamia/ocaa088)

- label v článku: **the minimum information necessary to understand**
- hodnoty, které schéma nabízí: intended predictions · target populations · hidden biases · the ability to generalize these emerging technologies
- citát: „a proposal describing the minimum information necessary to understand intended predictions, target populations, and hidden biases, and the ability to generalize these emerging technologies" (abstract)


### Prah, od kterého se přiznává

`threshold-that-triggers-disclosure` · 14 doslovných labelů · 13 schémat

*Glosa:* What makes a given use substantial enough to require disclosure - stated criteria, thresholds, tiers, lanes or traffic-light bands.

**tiered disclosure system** (research_publishing, normative_proposal, doi:10.3346/jkms.2026.41.e306)

- label v článku: **Tiered disclosure standards**
- hodnoty, které schéma nabízí: Tier 1: Assistive use · Tier 2: Augmentative use · Tier 3: Substantive use
- citát: „A more informative framework would adopt a tiered disclosure system, standardized across journals through coordination among ICMJE, COPE, WAME, and regional editorial associations" (Tiered disclosure standards)

**Generative AI Use Declaration** (research_publishing, policy, arXiv:2511.08639)

- label v článku: **tiered options**
- hodnoty, které schéma nabízí: no use · limited use of a specified kind · substantial use
- citát: „The Journal of Medical Ethics now requires a structured Generative AI Use Declaration before the reference list, with tiered options" (4. Why Existing AI-Disclosure Formats Don’t Fit Philosophy)

**the traffic light approach** (education_assessment, normative_proposal, doi:10.1007/s40979-025-00207-5)

- label v článku: **traffic light system**
- hodnoty, které schéma nabízí: red prohibits the use of AI tools · green allows to use AI · yellow represents the limited use of AI tools
- definice: „different colors indicate varying levels of AI use"
- citát: „red prohibits the use of AI tools, green allows to use AI, and yellow represents the limited use of AI tools" (Redefining plagiarism in the era of GenAI)

**tiered disclosure framework** (research_publishing, normative_proposal, doi:10.3346/jkms.2026.41.e281)

- label v článku: **three distinct levels**
- hodnoty, které schéma nabízí: Technical tasks (exempt from disclosure) · Linguistic support (optional) · Impact on originality (mandatory)
- definice: „authors must evaluate their disclosure requirements based on the depth of the AI’s influence on the research substance"
- citát: „this evaluation is guided by three distinct levels" (ETHICAL RESPONSIBILITY IN AI-ASSISTED AUTHORSHIP)


### Doslovné znění a volba označení

`wording-of-the-disclosure` · 6 doslovných labelů · 4 schémat

*Glosa:* The literal text chosen - sample wording, the label picked (AI-generated versus AI-assisted), tone, explicitness, covert versus overt framing.

**Research Framework** (other, empirical_study, arXiv:2602.15698)

- label v článku: **emotional tone (pathos)**
- hodnoty, které schéma nabízí: high · low
- definice: „referring to the degree of positivity conveyed in the disclosure"
- citát: „emotional tone (pathos), referring to the degree of positivity conveyed in the disclosure" (3. RESEARCH FRAMEWORK)

**Provenance disclosure cue codebook** (journalism_media, empirical_study, doi:10.3389/frai.2026.1815243)

- label v článku: **framing**
- hodnoty, které schéma nabízí: neutral informational · warning-like language
- citát: „framing (neutral informational vs. warning-like language)" (Data extraction and coding)

**Iranian med journals ai policy checklist** (research_publishing, empirical_study, doi:10.47176/mjiri.40.47)

- label v článku: **Example of Disclosure Statement**
- hodnoty: žádné vyjmenované, je to volné pole
- definice: „The policy provides sample wording and templates for disclosing the use of AI."
- citát: „The policy provides sample wording and templates for disclosing the use of AI." (Table 2)

**Ai use audit trail log** (research_publishing, normative_proposal, doi:10.11591/ijere.v15i4.38930)

- label v článku: **disclosure wording**
- hodnoty: žádné vyjmenované, je to volné pole
- citát: „Keep the exact disclosure wording used in the manuscript." (3.4.5. Maintaining an audit trail for AI-assisted writing)


### Jaký úkon AI udělala

`task-or-function-of-ai-use` · 44 doslovných labelů · 41 schémat

*Glosa:* Which concrete task, activity or content type the AI was applied to - translation, language editing, image generation, coding, summarising, literature search.

**Declaration of Artificial Intelligence Uses (Declaración de Usos de Inteligencia Artificial, DUIA)** (education_assessment, empirical_study, doi:10.21203/rs.3.rs-7539154/v1)

- label v článku: **10-category
taxonomy**
- hodnoty, které schéma nabízí: idea generation · drafting · text structuring · grammar/spelling correction · summarization · information extraction · content analysis · citation/reference management · translation · data visualization
- definice: „operationalizes transparent disclosure of generative-AI assistance via a 10-category
taxonomy"
- citát: „The DUIA operationalizes transparent disclosure of generative-AI assistance via a 10-category
taxonomy: (1) idea generation; (2) drafting; (3) text structuring" (2.2. Case context and intervention)

**Bmj ai tool task taxonomy** (research_publishing, empirical_study, doi:10.1101/2025.10.24.25338574)

- label v článku: **Tasks AI tools assisted with**
- hodnoty, které schéma nabízí: improve the quality of writing · translation · generating data and output · literature searches · analyzing or collecting data · image processing · code writing · managing references · To detect originality of text · Task not disclosed
- definice: „Table 3 reveals how self-disclosed AI use is being utilized to assist with various tasks."
- citát: „The predominant use of AI was to improve the quality of writing (87%, 1248)." (Table 3)

**TRIPOD-LLM** (research_publishing, reporting_guideline, doi:10.1038/s41591-024-03425-5)

- label v článku: **LLM task**
- hodnoty, které schéma nabízí: Text processing · Classification · Long-form question 
answering · Information retrieval · Conversational agent 
(chatbot) · Documentation 
generation · Summarization and 
simplification · Machine translation · Outcome forecasting
- citát: „Table 1 | Research design and LLM task categories for the modular TRIPOD-LLM guidelines" (Table 1)

**Ai assisted writing practice constructs** (education_assessment, empirical_study, doi:10.5281/zenodo.21398432)

- label v článku: **AI-assisted writing practice**
- hodnoty, které schéma nabízí: language refinement · drafting support · Information verification · disclosure of AI assistance · Revision and feedback use · idea generation · planning
- citát: „learners demonstrated a high level of AI-assisted writing practice, particularly in language refinement and drafting support" (abstract)


### Který nástroj a jaká verze

`ai-tool-identity-and-version` · 54 doslovných labelů · 46 schémat

*Glosa:* Which AI tool, model, provider or system was used, named with its version, build or access date.

**Medlit disclosure content analysis** (research_publishing, empirical_study, doi:10.5334/pme.2431)

- label v článku: **the name of AI tool(s) used**
- hodnoty, které schéma nabízí: ChatGPT · Otter · Negative AI Disclosure · Unspecified · Editage · Claude · Curie · ASReview · ClusterBot · Consensus.app
- citát: „Disclosure-specific extractions focused on the name of AI tool(s) used, purpose of AI use, location of the disclosure statement" (Table 3)

**Bmj ai tool task taxonomy** (research_publishing, empirical_study, doi:10.1101/2025.10.24.25338574)

- label v článku: **types of AI tools used**
- hodnoty, které schéma nabízí: AI Chatbots · Writing assistant tools · Visual/image Processing Tools · Evidence Synthesis Tools · Predictive Analytics Models · AI powered translators · AI-powered data analysis tools · AI-powered markdown editors · Automatic Speech Recognition Systems · Other
- definice: „taxonomy that grouped tools according to their 
primary purpose within the manuscript."
- citát: „Categories included: AI Chatbots, Writing Assistants, Visual/Image Processing Tools, Evidence Synthesis Tools, Predictive Analytics Models" (Table 2)

**Taxonomy for software and related information** (research_publishing, empirical_study, doi:10.7717/peerj-cs.835)

- label v článku: **Additional Information**
- hodnoty, které schéma nabízí: Developer · Version · URL · Citation · Extension · Release · License · Abbreviation · Alternative Name
- definice: „that is provided to closer describe a software entity"
- citát: „Additional Information that is provided to closer describe a software entity" (Table 2)

**Minimum telemetry for auditable outcome measurement in AI-CDSS** (other, normative_proposal, doi:10.3389/fdgth.2026.1871438)

- label v článku: **LLM provenance and metering**
- hodnoty, které schéma nabízí: Model/version ID · retrieval-source ID · prompt/output provenance policy · redaction status · token/compute use · latency · review result · documentation-quality audit result where applicable
- citát: „LLM provenance and metering Model/version ID, retrieval-source ID, prompt/output provenance policy, redaction status, token/compute use, latency, review result, documentation-quality audit result where applicable." (Table 7)


### Jistota: co přiznání nepokrývá

`limitations-and-validity-boundaries-disclosed` · 8 doslovných labelů · 11 schémat

*Glosa:* What the disclosure says about the limits of the AI use - caveats, known tool limitations, non-recommended uses, generalisation limits, where the output is valid and where it fails.

**Transparent Reporting of a multivari-
able prediction model for Individual Prognosis Or Diag-
nosis (TRIPOD) Statement** (research_publishing, reporting_guideline, doi:10.1186/s12874-021-01469-6)

- label v článku: **Limitations**
- hodnoty, které schéma nabízí: reported · not reported
- definice: „Limitations"
- citát: „18. Limitations" (Table 1)

**Verifiable vs declared integrity questions** (research_publishing, normative_proposal, doi:10.17605/osf.io/tna23)

- label v článku: **two classes**
- hodnoty, které schéma nabízí: those a record can settle · those no record can reach
- definice: „those a record can settle — sources retrieved, dates, parameters, tool and data versions — and those no record can reach"
- citát: „those a record can settle — sources retrieved, dates, parameters, tool and data versions — and those no record can reach" (abstract)

**Reporting and reproducibility checklist** (research_publishing, normative_proposal, doi:10.7759/cureus.92571)

- label v článku: **Limitations**
- hodnoty, které schéma nabízí: Limitations and generalizability
- definice: „All"
- citát: „Limitations and generalizability" (TABLE 4: Reporting and reproducibility checklist.)

**PETMALU-AI (Principles for Ensuring Transparency in Machine-assisted Authorship, Logging, and Use of Artificial Intelligence)** (research_publishing, reporting_guideline, doi:10.3390/educsci16071127)

- label v článku: **limitations**
- hodnoty: žádné vyjmenované, je to volné pole
- citát: „a 33-item checklist organized across nine domains: disclosure, human accountability, system transparency, prompting and interaction processes, data provenance, validation, ethics, limitations, and reproducibility" (abstract)


### Stav výstupu: jediné, co se tomu blíží

`maturity-level-of-the-thing-described` · 2 doslovných labelů · 2 schémat

*Glosa:* The maturity stage of the described item - proposed, implemented, evaluated.

**the taxonomy of data provenance in healthcare** (other, empirical_study, doi:10.3390/s23146495)

- label v článku: **maturity level ‘ML’**
- hodnoty, které schéma nabízí: architecture ‘A’ · proposed ‘P’ · implemented ‘I’ · evaluated ‘E’
- citát: „maturity level ‘ML’ is considered in this question as an additional attribute" (4.2.3. Addressing RQ-3)

**AA-1, the Agent Governance Attestation** (software, technical_standard, doi:10.2139/ssrn.6935198)

- label v článku: **maturity tier**
- hodnoty: žádné vyjmenované, je to volné pole
- citát: „at which maturity tier, supported by what evidence" (abstract)


### Očekávání od příjemce: jen jako vlastnost rozhraní

`relational-transparency-of-the-ai-role` · 1 doslovných labelů · 1 schémat

*Glosa:* Whether the people communicated with actually understand what part AI played in producing the message.

**AIMIC framework** (other, normative_proposal, doi:10.31875/2979-1081.2026.02.09)

- label v článku: **Relational Transparency Axis**
- hodnoty: žádné vyjmenované, je to volné pole
- definice: „describes whether communication partners understand the role AI played in message production"
- citát: „The relational transparency axis describes whether communication partners understand the role AI played in message production." (7.2. Relational Transparency Axis)


### Očekávání od příjemce: možnost výstup rozporovat

`contestability-of-ai-output` · 2 doslovných labelů · 2 schémat

*Glosa:* Whether an AI interpretation is fixed as fact or can be reflected on, revised, rejected or formally reported by an outside party.

**The Ethical Design Space for Sensor-Fused LLMs** (software, normative_proposal, arXiv:2604.06203)

- label v článku: **5. Contestability**
- hodnoty, které schéma nabízí: Fixed (Fact) · Correctable (Negotiable)
- definice: „User’s ability to correct"
- citát: „Contestability is a fundamental safety mechanism, not merely a UI option, enabling users to reflect, revise, or reject interpretations" (Table 1)

**Fda disclosure reform components** (government, normative_proposal, doi:10.3389/fmed.2026.1894905)

- label v článku: **contestability interface**
- hodnoty: žádné vyjmenované, je to volné pole
- definice: „provides a manufacturer-maintained reporting route linked from public summaries and labeling"
- citát: „Finally, a contestability interface provides a manufacturer-maintained reporting route linked from public summaries and labeling." (Prospective directions)


### Co je na těch příkladech vidět

Srovnejte první tři oddíly s poslední trojicí. U podílu AI a u kontroly mají
schémata **vyjmenované hodnoty**, často stupnice: nula až pět, žádná až plná.
U ručení hodnoty existují taky, ale vyjmenovávají **strany** (developer, vendor,
hospital, clinician), **jestli** to bylo řečeno (Yes, No, No explicit statement),
nebo **druh** odpovědnosti (causal, moral, legal). Ani jedno není rozsah nároku.

A u stavu výstupu a očekávání od příjemce ty příklady prostě nejsou, protože
v datech nejsou. To není redakční zkratka, je to nález.
