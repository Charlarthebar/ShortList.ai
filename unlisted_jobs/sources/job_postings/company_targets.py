#!/usr/bin/env python3
"""
Company Targets for ATS Ingestion
=================================

Comprehensive list of target companies for job posting ingestion.
Organized by:
1. Known ATS mapping (companies we know use specific ATS)
2. Target lists by industry/category for auto-detection

Author: ShortList.ai
Date: 2026-01-13
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class CompanyTarget:
    """Target company for job scraping."""
    company_id: str           # URL slug / API identifier
    company_name: str         # Human-readable name
    ats_type: Optional[str]   # Known ATS type (greenhouse, lever, smartrecruiters, workday)
    priority: int = 2         # 1=high, 2=medium, 3=low
    industry: str = "tech"
    metro: str = None         # Primary metro area (for matching to OEWS)
    notes: str = None


# ============================================================================
# KNOWN ATS MAPPINGS - Companies with confirmed ATS type
# ============================================================================

GREENHOUSE_COMPANIES: Dict[str, str] = {
    # Tech Giants & Unicorns
    "stripe": "Stripe",
    "airbnb": "Airbnb",
    "figma": "Figma",
    "notion": "Notion",
    "doordash": "DoorDash",
    "instacart": "Instacart",
    "slack": "Slack",
    "dropbox": "Dropbox",
    "coinbase": "Coinbase",
    "square": "Block (Square)",
    "robinhood": "Robinhood",
    "plaid": "Plaid",
    "mongodb": "MongoDB",
    "twilio": "Twilio",
    "hashicorp": "HashiCorp",
    "gitlab": "GitLab",
    "airtable": "Airtable",
    "confluent": "Confluent",
    "datadog": "Datadog",
    "snowflake": "Snowflake",

    # Growth Stage
    "anthropic": "Anthropic",
    "openai": "OpenAI",
    "databricks": "Databricks",
    "dbt-labs": "dbt Labs",
    "vercel": "Vercel",
    "supabase": "Supabase",
    "retool": "Retool",
    "linear": "Linear",
    "loom": "Loom",
    "miro": "Miro",
    "canva": "Canva",
    "grammarly": "Grammarly",
    "duolingo": "Duolingo",
    "zapier": "Zapier",
    "webflow": "Webflow",
    "calendly": "Calendly",
    "intercom": "Intercom",
    "amplitude": "Amplitude",
    "mixpanel": "Mixpanel",
    "segment": "Segment",

    # Enterprise SaaS
    "okta": "Okta",
    "servicenow": "ServiceNow",
    "pagerduty": "PagerDuty",
    "splunk": "Splunk",
    "newrelic": "New Relic",
    "elastic": "Elastic",
    "atlassian": "Atlassian",
    "autodesk": "Autodesk",
    "zendesk": "Zendesk",
    "freshworks": "Freshworks",

    # Fintech
    "chime": "Chime",
    "sofi": "SoFi",
    "marqeta": "Marqeta",
    "checkout": "Checkout.com",
    "wise": "Wise",
    "klarna": "Klarna",
    "adyen": "Adyen",
    "revolut": "Revolut",
    "nubank": "Nubank",

    # E-commerce / Marketplaces
    "etsy": "Etsy",
    "shopify": "Shopify",
    "wayfair": "Wayfair",
    "chewy": "Chewy",
    "poshmark": "Poshmark",
    "mercari": "Mercari",
    "offerup": "OfferUp",
    "rover": "Rover",

    # Healthcare Tech
    "oscar": "Oscar Health",
    "modernhealth": "Modern Health",
    "ro": "Ro",
    "hims": "Hims & Hers",
    "zocdoc": "Zocdoc",
    "cityblock": "Cityblock Health",
    "devoted": "Devoted Health",
    "noom": "Noom",

    # Security / Infrastructure
    "crowdstrike": "CrowdStrike",
    "sentinelone": "SentinelOne",
    "snyk": "Snyk",
    "1password": "1Password",
    "cloudflare": "Cloudflare",
    "fastly": "Fastly",
    "netlify": "Netlify",

    # Real Estate / PropTech
    "compass": "Compass",
    "zillow": "Zillow",
    "redfin": "Redfin",
    "opendoor": "Opendoor",
    "offerpad": "Offerpad",

    # Transportation / Mobility
    "bird": "Bird",
    "lime": "Lime",
    "getaround": "Getaround",
    "turo": "Turo",

    # Media / Entertainment
    "roblox": "Roblox",
    "discord": "Discord",
    "niantic": "Niantic",
    "epic-games": "Epic Games",
    "unity": "Unity",
}

LEVER_COMPANIES: Dict[str, str] = {
    # Major Tech
    "netflix": "Netflix",
    "github": "GitHub",
    "twitch": "Twitch",
    "lyft": "Lyft",
    "reddit": "Reddit",
    "spotify": "Spotify",

    # Growth Stage
    "gusto": "Gusto",
    "asana": "Asana",
    "flexport": "Flexport",
    "rippling": "Rippling",
    "brex": "Brex",
    "affirm": "Affirm",
    "scale": "Scale AI",
    "anduril": "Anduril Industries",
    "ramp": "Ramp",

    # More Growth Companies
    "deel": "Deel",
    "remote": "Remote",
    "lattice": "Lattice",
    "carta": "Carta",
    "mercury": "Mercury",
    "productboard": "Productboard",
    "contentful": "Contentful",
    "snorkel": "Snorkel AI",
    "weights-and-biases": "Weights & Biases",
    "cohere": "Cohere",
    "adept": "Adept",
    "mistral": "Mistral AI",
    "runway": "Runway",
    "midjourney": "Midjourney",

    # Fintech
    "wealthfront": "Wealthfront",
    "betterment": "Betterment",
    "current": "Current",
    "dave": "Dave",
    "varo": "Varo",
    "upgrade": "Upgrade",
    "monzo": "Monzo",
    "starling": "Starling Bank",

    # Enterprise
    "samsara": "Samsara",
    "figma": "Figma",
    "notion": "Notion",
    "loom": "Loom",
    "descript": "Descript",
    "jasper": "Jasper",

    # Healthcare
    "cerebral": "Cerebral",
    "hinge-health": "Hinge Health",
    "headspace": "Headspace",
    "calm": "Calm",

    # Other
    "nextdoor": "Nextdoor",
    "thumbtack": "Thumbtack",
    "taskrabbit": "TaskRabbit",
    "postmates": "Postmates",
}

SMARTRECRUITERS_COMPANIES: Dict[str, str] = {
    # Enterprise
    "Visa": "Visa",
    "BOSCH": "Bosch",
    "LinkedIn": "LinkedIn",
    "McDonalds": "McDonald's",
    "IKEA": "IKEA",
    "Adidas": "Adidas",
    "Spotify": "Spotify",
    "Wayfair": "Wayfair",
    "eBay": "eBay",
    "Equinix": "Equinix",

    # Consulting / Services
    "Capgemini": "Capgemini",
    "Infosys": "Infosys",
    "TCS": "Tata Consultancy Services",
    "Cognizant": "Cognizant",
    "Wipro": "Wipro",
    "HCL": "HCL Technologies",
    "LTIMindtree": "LTIMindtree",

    # Manufacturing / Industrial
    "PTC": "PTC",
    "SiemensEnergyGlobal": "Siemens Energy",
    "ABB": "ABB",
    "Honeywell": "Honeywell",
    "Schneider-Electric": "Schneider Electric",

    # Retail / Consumer
    "Gap": "Gap Inc.",
    "Levis": "Levi Strauss",
    "UnderArmour": "Under Armour",
    "Crocs": "Crocs",
    "Sephora": "Sephora",
    "LVMH": "LVMH",

    # Pharma / Healthcare
    "Novartis": "Novartis",
    "Roche": "Roche",
    "AstraZeneca": "AstraZeneca",
    "BristolMyersSquibb": "Bristol-Myers Squibb",
    "Pfizer": "Pfizer",
}

WORKDAY_COMPANIES: Dict[Tuple[str, str, str], str] = {
    # (company_id, workday_host, tenant): Company Name
    ("amazon", "wd5.myworkdayjobs.com", "External"): "Amazon",
    ("netflix", "wd5.myworkdayjobs.com", "External"): "Netflix",
    ("salesforce", "wd12.myworkdayjobs.com", "External"): "Salesforce",
    ("meta", "wd5.myworkdayjobs.com", "External"): "Meta",
    ("microsoft", "wd5.myworkdayjobs.com", "External"): "Microsoft",
    ("apple", "wd3.myworkdayjobs.com", "External"): "Apple",
    ("nvidia", "wd5.myworkdayjobs.com", "NVIDIAExternalCareerSite"): "NVIDIA",
    ("intel", "wd1.myworkdayjobs.com", "External"): "Intel",
    ("ibm", "wd3.myworkdayjobs.com", "External"): "IBM",
    ("oracle", "wd1.myworkdayjobs.com", "External"): "Oracle",
    ("walmart", "wd5.myworkdayjobs.com", "External"): "Walmart",
    ("target", "wd5.myworkdayjobs.com", "External"): "Target",
    ("disney", "wd5.myworkdayjobs.com", "disneycareer"): "Disney",
    ("nike", "wd1.myworkdayjobs.com", "NikeInc"): "Nike",
    ("verizon", "wd5.myworkdayjobs.com", "External"): "Verizon",
    ("att", "wd5.myworkdayjobs.com", "External"): "AT&T",
    ("comcast", "wd5.myworkdayjobs.com", "External"): "Comcast",
    ("chevron", "wd5.myworkdayjobs.com", "External"): "Chevron",
    ("exxonmobil", "wd5.myworkdayjobs.com", "External"): "ExxonMobil",
    ("jpmorgan", "wd5.myworkdayjobs.com", "External"): "JPMorgan Chase",
    ("bankofamerica", "wd5.myworkdayjobs.com", "External"): "Bank of America",
    ("wellsfargo", "wd5.myworkdayjobs.com", "External"): "Wells Fargo",
    ("goldmansachs", "wd5.myworkdayjobs.com", "External"): "Goldman Sachs",
    ("morganstanley", "wd5.myworkdayjobs.com", "External"): "Morgan Stanley",
    ("citi", "wd5.myworkdayjobs.com", "External"): "Citigroup",
    ("ge", "wd5.myworkdayjobs.com", "External"): "GE",
    ("johnsonandjohnson", "wd5.myworkdayjobs.com", "External"): "Johnson & Johnson",
    ("procter", "wd5.myworkdayjobs.com", "External"): "Procter & Gamble",
    ("cocacola", "wd5.myworkdayjobs.com", "External"): "Coca-Cola",
    ("pepsico", "wd5.myworkdayjobs.com", "External"): "PepsiCo",
    ("ups", "wd5.myworkdayjobs.com", "External"): "UPS",
    ("fedex", "wd5.myworkdayjobs.com", "External"): "FedEx",
    ("lockheedmartin", "wd5.myworkdayjobs.com", "External"): "Lockheed Martin",
    ("boeing", "wd5.myworkdayjobs.com", "External"): "Boeing",
    ("raytheon", "wd5.myworkdayjobs.com", "External"): "Raytheon",
    ("northropgrumman", "wd5.myworkdayjobs.com", "External"): "Northrop Grumman",
    ("generaldynamics", "wd5.myworkdayjobs.com", "External"): "General Dynamics",
}


# ============================================================================
# COMPANIES TO AUTO-DETECT - Try all ATS types for these
# ============================================================================

AUTO_DETECT_COMPANIES: List[Tuple[str, str]] = [
    # Format: (company_slug, company_name)
    # These will be tested against Greenhouse, Lever, SmartRecruiters

    # AI/ML Companies (high priority)
    ("cohere", "Cohere"),
    ("anthropic", "Anthropic"),
    ("deepmind", "DeepMind"),
    ("huggingface", "Hugging Face"),
    ("stability", "Stability AI"),
    ("inflection", "Inflection AI"),
    ("perplexity", "Perplexity AI"),
    ("character", "Character.AI"),
    ("replicate", "Replicate"),
    ("modal", "Modal"),
    ("together", "Together AI"),
    ("anyscale", "Anyscale"),
    ("langchain", "LangChain"),
    ("pinecone", "Pinecone"),
    ("weaviate", "Weaviate"),
    ("qdrant", "Qdrant"),
    ("chroma", "Chroma"),

    # Developer Tools
    ("vercel", "Vercel"),
    ("planetscale", "PlanetScale"),
    ("neon", "Neon"),
    ("turso", "Turso"),
    ("cockroachlabs", "Cockroach Labs"),
    ("timescale", "Timescale"),
    ("singlestore", "SingleStore"),
    ("clickhouse", "ClickHouse"),
    ("duckdb", "DuckDB"),
    ("motherduck", "MotherDuck"),
    ("posthog", "PostHog"),
    ("plausible", "Plausible"),
    ("metabase", "Metabase"),
    ("preset", "Preset"),
    ("hex", "Hex"),
    ("dbt-labs", "dbt Labs"),
    ("fivetran", "Fivetran"),
    ("airbyte", "Airbyte"),
    ("hightouch", "Hightouch"),
    ("census", "Census"),
    ("rudderstack", "RudderStack"),

    # Cloud/Infra
    ("fly", "Fly.io"),
    ("railway", "Railway"),
    ("render", "Render"),
    ("digitalocean", "DigitalOcean"),
    ("linode", "Linode"),
    ("vultr", "Vultr"),
    ("hetzner", "Hetzner"),
    ("upcloud", "UpCloud"),

    # Security
    ("1password", "1Password"),
    ("bitwarden", "Bitwarden"),
    ("dashlane", "Dashlane"),
    ("keeper", "Keeper Security"),
    ("lastpass", "LastPass"),
    ("wiz", "Wiz"),
    ("orca", "Orca Security"),
    ("lacework", "Lacework"),
    ("aqua", "Aqua Security"),
    ("snyk", "Snyk"),
    ("sonarqube", "SonarQube"),
    ("checkmarx", "Checkmarx"),
    ("veracode", "Veracode"),
    ("whitesource", "Mend (WhiteSource)"),

    # Fintech (beyond known)
    ("stripe", "Stripe"),
    ("plaid", "Plaid"),
    ("modern-treasury", "Modern Treasury"),
    ("increase", "Increase"),
    ("unit", "Unit"),
    ("treasury-prime", "Treasury Prime"),
    ("synapse", "Synapse"),
    ("galileo", "Galileo"),
    ("lithic", "Lithic"),
    ("privacy", "Privacy.com"),
    ("meow", "Meow"),

    # Healthcare (beyond known)
    ("flatiron", "Flatiron Health"),
    ("tempus", "Tempus"),
    ("veracyte", "Veracyte"),
    ("grail", "GRAIL"),
    ("guardant", "Guardant Health"),
    ("natera", "Natera"),
    ("exact-sciences", "Exact Sciences"),
    ("illumina", "Illumina"),
    ("pacific-biosciences", "PacBio"),
    ("10x-genomics", "10x Genomics"),

    # Crypto/Web3
    ("coinbase", "Coinbase"),
    ("kraken", "Kraken"),
    ("binance", "Binance"),
    ("ftx", "FTX"),
    ("gemini", "Gemini"),
    ("circle", "Circle"),
    ("fireblocks", "Fireblocks"),
    ("chainalysis", "Chainalysis"),
    ("elliptic", "Elliptic"),
    ("consensys", "ConsenSys"),
    ("alchemy", "Alchemy"),
    ("infura", "Infura"),
    ("moralis", "Moralis"),
    ("thirdweb", "thirdweb"),
    ("opensea", "OpenSea"),
    ("blur", "Blur"),
    ("magic-eden", "Magic Eden"),
    ("dapper", "Dapper Labs"),
    ("immutable", "Immutable"),
    ("polygon", "Polygon"),
    ("arbitrum", "Arbitrum"),
    ("optimism", "Optimism"),
    ("starkware", "StarkWare"),
    ("zksync", "zkSync"),

    # E-commerce / DTC
    ("shopify", "Shopify"),
    ("bigcommerce", "BigCommerce"),
    ("woocommerce", "WooCommerce"),
    ("magento", "Magento"),
    ("bolt", "Bolt"),
    ("fast", "Fast"),
    ("affirm", "Affirm"),
    ("klarna", "Klarna"),
    ("afterpay", "Afterpay"),
    ("sezzle", "Sezzle"),
    ("splitit", "Splitit"),

    # Real Estate / PropTech
    ("opendoor", "Opendoor"),
    ("offerpad", "Offerpad"),
    ("homelight", "HomeLight"),
    ("knock", "Knock"),
    ("flyhomes", "Flyhomes"),
    ("divvy", "Divvy Homes"),
    ("landed", "Landed"),
    ("better", "Better"),
    ("blend", "Blend"),
    ("snapdocs", "Snapdocs"),
    ("notarize", "Notarize"),

    # HR / Workforce
    ("rippling", "Rippling"),
    ("gusto", "Gusto"),
    ("deel", "Deel"),
    ("remote", "Remote"),
    ("oyster", "Oyster HR"),
    ("papaya", "Papaya Global"),
    ("workday", "Workday"),
    ("bamboohr", "BambooHR"),
    ("namely", "Namely"),
    ("paylocity", "Paylocity"),
    ("paycom", "Paycom"),
    ("ceridian", "Ceridian"),
    ("adp", "ADP"),
    ("paychex", "Paychex"),

    # Marketing / AdTech
    ("hubspot", "HubSpot"),
    ("mailchimp", "Mailchimp"),
    ("klaviyo", "Klaviyo"),
    ("braze", "Braze"),
    ("iterable", "Iterable"),
    ("customer-io", "Customer.io"),
    ("sendgrid", "SendGrid"),
    ("twilio", "Twilio"),
    ("messagebird", "MessageBird"),
    ("vonage", "Vonage"),
    ("bandwidth", "Bandwidth"),
    ("plivo", "Plivo"),
    ("telnyx", "Telnyx"),

    # Gaming
    ("roblox", "Roblox"),
    ("epic-games", "Epic Games"),
    ("unity", "Unity"),
    ("activision", "Activision"),
    ("electronic-arts", "Electronic Arts"),
    ("take-two", "Take-Two"),
    ("ubisoft", "Ubisoft"),
    ("riot", "Riot Games"),
    ("valve", "Valve"),
    ("niantic", "Niantic"),
    ("supercell", "Supercell"),
    ("zynga", "Zynga"),
    ("king", "King"),
    ("scopely", "Scopely"),
    ("jam-city", "Jam City"),

    # Autonomous Vehicles / Robotics
    ("waymo", "Waymo"),
    ("cruise", "Cruise"),
    ("aurora", "Aurora"),
    ("argo", "Argo AI"),
    ("nuro", "Nuro"),
    ("zoox", "Zoox"),
    ("motional", "Motional"),
    ("aptiv", "Aptiv"),
    ("mobileye", "Mobileye"),
    ("comma", "Comma.ai"),
    ("ghost", "Ghost Autonomy"),
    ("waabi", "Waabi"),
    ("kodiak", "Kodiak Robotics"),
    ("embark", "Embark Trucks"),
    ("tusimple", "TuSimple"),
    ("locomation", "Locomation"),

    # Space / Aerospace
    ("spacex", "SpaceX"),
    ("blue-origin", "Blue Origin"),
    ("rocket-lab", "Rocket Lab"),
    ("relativity", "Relativity Space"),
    ("astra", "Astra"),
    ("firefly", "Firefly Aerospace"),
    ("planet", "Planet Labs"),
    ("spire", "Spire Global"),
    ("hawkeye360", "HawkEye 360"),
    ("capella", "Capella Space"),
    ("iceye", "ICEYE"),
    ("blacksky", "BlackSky"),

    # Clean Energy / Climate
    ("tesla", "Tesla"),
    ("rivian", "Rivian"),
    ("lucid", "Lucid Motors"),
    ("fisker", "Fisker"),
    ("polestar", "Polestar"),
    ("nio", "NIO"),
    ("xpeng", "XPeng"),
    ("li-auto", "Li Auto"),
    ("byd", "BYD"),
    ("northvolt", "Northvolt"),
    ("quantumscape", "QuantumScape"),
    ("solid-power", "Solid Power"),
    ("redwood", "Redwood Materials"),
    ("li-cycle", "Li-Cycle"),
    ("form-energy", "Form Energy"),
    ("ess", "ESS Inc"),
    ("fluence", "Fluence"),
    ("stem", "Stem Inc"),

    # Food / AgTech
    ("impossible", "Impossible Foods"),
    ("beyond-meat", "Beyond Meat"),
    ("perfect-day", "Perfect Day"),
    ("upside-foods", "Upside Foods"),
    ("eat-just", "Eat Just"),
    ("apeel", "Apeel Sciences"),
    ("bowery", "Bowery Farming"),
    ("plenty", "Plenty"),
    ("aerofarms", "AeroFarms"),
    ("indigo-ag", "Indigo Ag"),
    ("farmers-business-network", "Farmers Business Network"),
    ("granular", "Granular"),
    ("arable", "Arable"),
    ("climate", "Climate Corporation"),
]


# ============================================================================
# FORTUNE 500 COMPANIES (for comprehensive coverage)
# ============================================================================

FORTUNE_500_TO_DETECT: List[Tuple[str, str]] = [
    # Retail
    ("walmart", "Walmart"),
    ("amazon", "Amazon"),
    ("costco", "Costco"),
    ("kroger", "Kroger"),
    ("home-depot", "Home Depot"),
    ("lowes", "Lowe's"),
    ("cvs", "CVS Health"),
    ("walgreens", "Walgreens"),
    ("target", "Target"),
    ("best-buy", "Best Buy"),
    ("macys", "Macy's"),
    ("nordstrom", "Nordstrom"),
    ("tjx", "TJX Companies"),
    ("ross", "Ross Stores"),
    ("dollar-general", "Dollar General"),
    ("dollar-tree", "Dollar Tree"),

    # Finance / Insurance
    ("berkshire", "Berkshire Hathaway"),
    ("unitedhealth", "UnitedHealth"),
    ("anthem", "Anthem"),
    ("cigna", "Cigna"),
    ("humana", "Humana"),
    ("centene", "Centene"),
    ("aetna", "Aetna"),
    ("metlife", "MetLife"),
    ("prudential", "Prudential"),
    ("aflac", "Aflac"),
    ("progressive", "Progressive"),
    ("allstate", "Allstate"),
    ("statefarm", "State Farm"),
    ("liberty-mutual", "Liberty Mutual"),
    ("travelers", "Travelers"),
    ("usaa", "USAA"),
    ("nationwide", "Nationwide"),

    # Healthcare
    ("cvs-health", "CVS Health"),
    ("mckesson", "McKesson"),
    ("amerisourcebergen", "AmerisourceBergen"),
    ("cardinal-health", "Cardinal Health"),
    ("hca", "HCA Healthcare"),
    ("mayo-clinic", "Mayo Clinic"),
    ("cleveland-clinic", "Cleveland Clinic"),
    ("kaiser", "Kaiser Permanente"),
    ("ascension", "Ascension"),
    ("commonspirit", "CommonSpirit Health"),
    ("adventhealth", "AdventHealth"),
    ("providence", "Providence"),
    ("sutter", "Sutter Health"),
    ("trinity", "Trinity Health"),

    # Pharma / Biotech
    ("pfizer", "Pfizer"),
    ("johnson-johnson", "Johnson & Johnson"),
    ("abbvie", "AbbVie"),
    ("merck", "Merck"),
    ("bristol-myers", "Bristol-Myers Squibb"),
    ("eli-lilly", "Eli Lilly"),
    ("amgen", "Amgen"),
    ("gilead", "Gilead Sciences"),
    ("regeneron", "Regeneron"),
    ("vertex", "Vertex Pharmaceuticals"),
    ("biogen", "Biogen"),
    ("moderna", "Moderna"),
    ("biontech", "BioNTech"),

    # Energy
    ("exxonmobil", "ExxonMobil"),
    ("chevron", "Chevron"),
    ("conocophillips", "ConocoPhillips"),
    ("phillips66", "Phillips 66"),
    ("valero", "Valero Energy"),
    ("marathon", "Marathon Petroleum"),
    ("occidental", "Occidental Petroleum"),
    ("devon", "Devon Energy"),
    ("pioneer", "Pioneer Natural Resources"),
    ("eog", "EOG Resources"),

    # Utilities
    ("duke-energy", "Duke Energy"),
    ("southern", "Southern Company"),
    ("dominion", "Dominion Energy"),
    ("nextera", "NextEra Energy"),
    ("exelon", "Exelon"),
    ("aes", "AES Corporation"),
    ("dte", "DTE Energy"),
    ("xcel", "Xcel Energy"),
    ("entergy", "Entergy"),
    ("pge", "PG&E"),
    ("edison", "Edison International"),
    ("sempra", "Sempra"),

    # Telecom
    ("att", "AT&T"),
    ("verizon", "Verizon"),
    ("t-mobile", "T-Mobile"),
    ("comcast", "Comcast"),
    ("charter", "Charter Communications"),
    ("dish", "DISH Network"),
    ("lumen", "Lumen Technologies"),
    ("frontier", "Frontier Communications"),

    # Tech (not already covered)
    ("hp", "HP Inc"),
    ("hpe", "Hewlett Packard Enterprise"),
    ("dell", "Dell Technologies"),
    ("lenovo", "Lenovo"),
    ("cisco", "Cisco"),
    ("qualcomm", "Qualcomm"),
    ("broadcom", "Broadcom"),
    ("amd", "AMD"),
    ("micron", "Micron Technology"),
    ("texas-instruments", "Texas Instruments"),
    ("analog-devices", "Analog Devices"),
    ("xilinx", "Xilinx"),
    ("on-semi", "ON Semiconductor"),
    ("nxp", "NXP Semiconductors"),
    ("skyworks", "Skyworks Solutions"),
    ("qorvo", "Qorvo"),

    # Industrial / Manufacturing
    ("caterpillar", "Caterpillar"),
    ("deere", "John Deere"),
    ("3m", "3M"),
    ("honeywell", "Honeywell"),
    ("ge", "General Electric"),
    ("emerson", "Emerson"),
    ("rockwell", "Rockwell Automation"),
    ("parker", "Parker Hannifin"),
    ("illinois-tool-works", "Illinois Tool Works"),
    ("dover", "Dover Corporation"),
    ("danaher", "Danaher"),
    ("fortive", "Fortive"),
    ("stanley-black-decker", "Stanley Black & Decker"),
    ("snap-on", "Snap-on"),

    # Aerospace / Defense
    ("lockheed", "Lockheed Martin"),
    ("boeing", "Boeing"),
    ("raytheon", "Raytheon"),
    ("northrop", "Northrop Grumman"),
    ("general-dynamics", "General Dynamics"),
    ("l3harris", "L3Harris"),
    ("textron", "Textron"),
    ("huntington-ingalls", "Huntington Ingalls"),
    ("leidos", "Leidos"),
    ("saic", "SAIC"),
    ("bae", "BAE Systems"),
    ("palantir", "Palantir"),

    # Transportation / Logistics
    ("ups", "UPS"),
    ("fedex", "FedEx"),
    ("delta", "Delta Air Lines"),
    ("united-airlines", "United Airlines"),
    ("american-airlines", "American Airlines"),
    ("southwest", "Southwest Airlines"),
    ("jbhunt", "J.B. Hunt"),
    ("xpo", "XPO Logistics"),
    ("ryder", "Ryder"),
    ("penske", "Penske"),
    ("csx", "CSX"),
    ("union-pacific", "Union Pacific"),
    ("norfolk-southern", "Norfolk Southern"),
    ("bnsf", "BNSF Railway"),
]


def get_all_known_targets() -> List[CompanyTarget]:
    """
    Return all known company targets with their ATS type.
    """
    targets = []

    # Greenhouse companies
    for company_id, company_name in GREENHOUSE_COMPANIES.items():
        targets.append(CompanyTarget(
            company_id=company_id,
            company_name=company_name,
            ats_type="greenhouse",
            priority=1
        ))

    # Lever companies
    for company_id, company_name in LEVER_COMPANIES.items():
        targets.append(CompanyTarget(
            company_id=company_id,
            company_name=company_name,
            ats_type="lever",
            priority=1
        ))

    # SmartRecruiters companies
    for company_id, company_name in SMARTRECRUITERS_COMPANIES.items():
        targets.append(CompanyTarget(
            company_id=company_id,
            company_name=company_name,
            ats_type="smartrecruiters",
            priority=1
        ))

    # Workday companies
    for (company_id, host, tenant), company_name in WORKDAY_COMPANIES.items():
        targets.append(CompanyTarget(
            company_id=company_id,
            company_name=company_name,
            ats_type="workday",
            priority=1,
            notes=f"host={host}, tenant={tenant}"
        ))

    return targets


def get_auto_detect_targets() -> List[CompanyTarget]:
    """
    Return companies that need ATS auto-detection.
    """
    targets = []

    # Combine auto-detect lists
    all_companies = AUTO_DETECT_COMPANIES + FORTUNE_500_TO_DETECT

    # Remove duplicates and companies we already know the ATS for
    known_ids = set()
    for company_id, _ in GREENHOUSE_COMPANIES.items():
        known_ids.add(company_id.lower())
    for company_id, _ in LEVER_COMPANIES.items():
        known_ids.add(company_id.lower())
    for company_id, _ in SMARTRECRUITERS_COMPANIES.items():
        known_ids.add(company_id.lower())
    for (company_id, _, _), _ in WORKDAY_COMPANIES.items():
        known_ids.add(company_id.lower())

    seen = set()
    for company_id, company_name in all_companies:
        if company_id.lower() not in known_ids and company_id.lower() not in seen:
            seen.add(company_id.lower())
            targets.append(CompanyTarget(
                company_id=company_id,
                company_name=company_name,
                ats_type=None,  # To be detected
                priority=2
            ))

    return targets


def get_all_targets() -> List[CompanyTarget]:
    """Return all targets (known + auto-detect)."""
    return get_all_known_targets() + get_auto_detect_targets()


if __name__ == "__main__":
    known = get_all_known_targets()
    auto_detect = get_auto_detect_targets()

    print(f"Known ATS targets: {len(known)}")
    print(f"  - Greenhouse: {len(GREENHOUSE_COMPANIES)}")
    print(f"  - Lever: {len(LEVER_COMPANIES)}")
    print(f"  - SmartRecruiters: {len(SMARTRECRUITERS_COMPANIES)}")
    print(f"  - Workday: {len(WORKDAY_COMPANIES)}")
    print(f"\nAuto-detect targets: {len(auto_detect)}")
    print(f"\nTotal targets: {len(known) + len(auto_detect)}")
