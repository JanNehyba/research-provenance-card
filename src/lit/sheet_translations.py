"""Czech renderings of the value strings shown on page 2.

The English stays on the page because it is a verbatim quotation, checked by
script against the retrieved text. These are my own translations, added so the
page is readable; anything not in this table falls back to the English, which is
visible on the sheet as an untranslated word rather than hidden.
"""

CZ_VAL = {
    # AI Usage (task list)
    "Permission to use AI": "povolení použít AI",
    "Role in research design": "role při návrhu výzkumu",
    "Language editing": "jazyková úprava",
    "Manuscript drafting": "psaní rukopisu",
    "Idea generation": "generování nápadů",
    "Image or graphic creation": "tvorba obrázků a grafiky",
    "Data generation": "generování dat",
    "Data collection": "sběr dat",
    # tool names stay as they are
    "ChatGPT": "ChatGPT", "Otter": "Otter", "Editage": "Editage",
    "Claude": "Claude", "Curie": "Curie", "ASReview": "ASReview",
    "Negative AI Disclosure": "přiznání, že se AI nepoužila",
    "Unspecified": "neuvedeno",
    # Type of task
    "Core layer task": "úkol jádrové vrstvy",
    "Conception and design": "koncepce a návrh",
    "Drafting article": "psaní článku",
    "Middle layer task": "úkol střední vrstvy",
    "Assisting in the study design*": "pomoc při návrhu studie*",
    "Assisting in drafting article*": "pomoc při psaní článku*",
    "Collecting data": "sběr dat",
    "Conducting experiments": "provádění experimentů",
    # Tasks AI tools assisted with
    "improve the quality of writing": "zlepšit kvalitu psaní",
    "translation": "překlad",
    "generating data and output": "generování dat a výstupů",
    "literature searches": "hledání literatury",
    "analyzing or collecting data": "analýza nebo sběr dat",
    "image processing": "zpracování obrázků",
    "code writing": "psaní kódu",
    "managing references": "správa citací",
    # the verification ladder
    "unverified": "neověřeno",
    "needs-research": "je potřeba dohledat",
    "reference-resolved": "odkaz rozřešen",
    "ai-confirmed": "potvrzeno AI",
    "source-vendored": "doloženo zdrojem",
    "human-confirmed": "potvrdil člověk",
    "human-read": "člověk to četl",
    # liability chain
    "developer": "vývojář", "vendor": "dodavatel",
    "hospital": "nemocnice", "clinician": "lékař",
    # pre-use gates
    "task scoping": "vymezení úkolu",
    "plan-before-execution": "plán před provedením",
    "task decomposition": "rozložení úkolu",
    "auditable computation": "auditovatelný výpočet",
    "mandatory output verification": "povinné ověření výstupu",
    "data isolation": "izolace dat",
    "AI-use disclosure": "přiznání použití AI",
    # Section
    "Title": "název", "Abstract": "abstrakt", "Keywords": "klíčová slova",
    "Introduction": "úvod", "Method": "metody", "Data": "data",
    "Segmentation": "segmentace", "Pre-processing": "předzpracování",
    "Results": "výsledky", "Discussion": "diskuse",
    # CRediT
    "Conceptualization": "koncepce",
    "Data curation": "správa dat",
    "Formal analysis": "formální analýza",
    "Funding acquisition": "získání financí",
    "Investigation": "provedení výzkumu",
    "Methodology": "metodika",
    "Project administration": "administrace projektu",
    "Resources": "zdroje a materiál",
    "Software": "software", "Supervision": "dohled",
    "Validation": "validace", "Visualization": "vizualizace",
    # presence of a disclosure
    "disclosure": "přiznání",
    "verification": "ověření",
    "human oversight": "lidský dohled",
    "authorship": "autorství",
    "confidentiality": "důvěrnost",
    "accountability": "odpovědnost",
    # common extras
    "Yes": "ano", "No": "ne", "N/A": "neuvedeno",
    "minimal": "minimální", "slight": "nepatrná", "moderate": "střední",
    "substantial": "podstatná", "extensive": "rozsáhlá", "full": "úplná",
    "accept": "přijmout", "reject": "zamítnout",
    "modify (light)": "lehce upravit", "modify (substantial)": "podstatně upravit",
}
