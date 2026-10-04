# EOR Scope: statutory employer costs by country

Publisher: EOR Scope, published by Trésor Kaya EI (Les Créavores), France
Licence: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
Methodology: https://eorscope.com/methodology/
Calculator: https://eorscope.com/eor-cost-calculator/ (total monthly cost, 1 to 50 employees)
Country pages: https://eorscope.com/employer-of-record/
Export date: 2026-10-04
Source commit: 3261ce39a898

**Cost comparison, not legal or tax advice.** Figures are an illustrative model of statutory employer charges; check with a local adviser before hiring.

## Files

| File | Rows | Content |
|---|---|---|
| `country_contributions.csv` | 542 | One row per employer contribution or statutory extra, with rate, base, floor/ceiling, source URL and date |
| `country_summary.csv` | 76 | One row per country: employer cost in % and USD per month at the example salary |
| `country_assumptions.csv` | 108 | One row per declared assumption: the case each country's lines and total are priced for |
| `datapackage.json` | | Frictionless Data Package descriptor (field types and descriptions) |

`employer_cost_pct` is produced by the same engine that prints the figure on eorscope.com (statutory contributions plus the statutory extras flagged `in_total`, at the example salary; EOR fees excluded). `employer_cost_pct_printed` is the figure as the site prints it (one decimal, half away from zero: 22.25 prints 22.3). Countries flagged `total_declared_floor` publish an "at least" figure, not a total. Under `total_declared_ceiling` the modelled contribution base is the highest the law allows; costs listed with `in_total=false` come on top.

Lines with `base = basic` apply to `basic_share_of_gross` × gross (`country_summary.csv`). `base_factor` multiplies gross into the statutory base before the floor and the ceiling apply (Mexico: the integrated contribution base includes the aguinaldo and the vacation premium). Each total holds for the case described in `country_assumptions.csv`.

`employer_cost_pct` is not a social-security contribution rate. It adds statutory contributions, compulsory payments to private funds and statutory pay supplements (13th month, holiday pay, accrued severance), so it is not comparable with OECD Taxing Wages employer rates.

The `notes` columns reproduce the site's prose and may refer to "this page".

## Country pages

Each country of `country_summary.csv` is printed on one page of eorscope.com, with its contribution lines and their sources:

| ISO | Country | Page |
|---|---|---|
| AE | United Arab Emirates | https://eorscope.com/employer-of-record/uae/ |
| AL | Albania | https://eorscope.com/employer-of-record/albania/ |
| AM | Armenia | https://eorscope.com/employer-of-record/armenia/ |
| AR | Argentina | https://eorscope.com/employer-of-record/argentina/ |
| AT | Austria | https://eorscope.com/employer-of-record/austria/ |
| AU | Australia | https://eorscope.com/employer-of-record/australia/ |
| AZ | Azerbaijan | https://eorscope.com/employer-of-record/azerbaijan/ |
| BD | Bangladesh | https://eorscope.com/employer-of-record/bangladesh/ |
| BE | Belgium | https://eorscope.com/employer-of-record/belgium/ |
| BG | Bulgaria | https://eorscope.com/employer-of-record/bulgaria/ |
| BR | Brazil | https://eorscope.com/employer-of-record/brazil/ |
| CA | Canada | https://eorscope.com/employer-of-record/canada/ |
| CH | Switzerland | https://eorscope.com/employer-of-record/switzerland/ |
| CL | Chile | https://eorscope.com/employer-of-record/chile/ |
| CN | China | https://eorscope.com/employer-of-record/china/ |
| CO | Colombia | https://eorscope.com/employer-of-record/colombia/ |
| CR | Costa Rica | https://eorscope.com/employer-of-record/costa-rica/ |
| CZ | Czech Republic | https://eorscope.com/employer-of-record/czech-republic/ |
| DE | Germany | https://eorscope.com/employer-of-record/germany/ |
| DK | Denmark | https://eorscope.com/employer-of-record/denmark/ |
| DO | Dominican Republic | https://eorscope.com/employer-of-record/dominican-republic/ |
| EC | Ecuador | https://eorscope.com/employer-of-record/ecuador/ |
| EE | Estonia | https://eorscope.com/employer-of-record/estonia/ |
| EG | Egypt | https://eorscope.com/employer-of-record/egypt/ |
| ES | Spain | https://eorscope.com/employer-of-record/spain/ |
| FI | Finland | https://eorscope.com/employer-of-record/finland/ |
| FR | France | https://eorscope.com/employer-of-record/france/ |
| GB | United Kingdom | https://eorscope.com/employer-of-record/uk/ |
| GE | Georgia | https://eorscope.com/employer-of-record/georgia/ |
| GH | Ghana | https://eorscope.com/employer-of-record/ghana/ |
| GR | Greece | https://eorscope.com/employer-of-record/greece/ |
| HK | Hong Kong | https://eorscope.com/employer-of-record/hong-kong/ |
| HR | Croatia | https://eorscope.com/employer-of-record/croatia/ |
| HU | Hungary | https://eorscope.com/employer-of-record/hungary/ |
| ID | Indonesia | https://eorscope.com/employer-of-record/indonesia/ |
| IE | Ireland | https://eorscope.com/employer-of-record/ireland/ |
| IL | Israel | https://eorscope.com/employer-of-record/israel/ |
| IN | India | https://eorscope.com/employer-of-record/india/ |
| IT | Italy | https://eorscope.com/employer-of-record/italy/ |
| JO | Jordan | https://eorscope.com/employer-of-record/jordan/ |
| JP | Japan | https://eorscope.com/employer-of-record/japan/ |
| KE | Kenya | https://eorscope.com/employer-of-record/kenya/ |
| KR | South Korea | https://eorscope.com/employer-of-record/south-korea/ |
| KZ | Kazakhstan | https://eorscope.com/employer-of-record/kazakhstan/ |
| LK | Sri Lanka | https://eorscope.com/employer-of-record/sri-lanka/ |
| LT | Lithuania | https://eorscope.com/employer-of-record/lithuania/ |
| LV | Latvia | https://eorscope.com/employer-of-record/latvia/ |
| MA | Morocco | https://eorscope.com/employer-of-record/morocco/ |
| MM | Myanmar | https://eorscope.com/employer-of-record/myanmar/ |
| MT | Malta | https://eorscope.com/employer-of-record/malta/ |
| MX | Mexico | https://eorscope.com/employer-of-record/mexico/ |
| MY | Malaysia | https://eorscope.com/employer-of-record/malaysia/ |
| NG | Nigeria | https://eorscope.com/employer-of-record/nigeria/ |
| NL | Netherlands | https://eorscope.com/employer-of-record/netherlands/ |
| NO | Norway | https://eorscope.com/employer-of-record/norway/ |
| NZ | New Zealand | https://eorscope.com/employer-of-record/new-zealand/ |
| PE | Peru | https://eorscope.com/employer-of-record/peru/ |
| PH | Philippines | https://eorscope.com/employer-of-record/philippines/ |
| PK | Pakistan | https://eorscope.com/employer-of-record/pakistan/ |
| PL | Poland | https://eorscope.com/employer-of-record/poland/ |
| PT | Portugal | https://eorscope.com/employer-of-record/portugal/ |
| QA | Qatar | https://eorscope.com/employer-of-record/qatar/ |
| RO | Romania | https://eorscope.com/employer-of-record/romania/ |
| RS | Serbia | https://eorscope.com/employer-of-record/serbia/ |
| SA | Saudi Arabia | https://eorscope.com/employer-of-record/saudi-arabia/ |
| SE | Sweden | https://eorscope.com/employer-of-record/sweden/ |
| SG | Singapore | https://eorscope.com/employer-of-record/singapore/ |
| SK | Slovakia | https://eorscope.com/employer-of-record/slovakia/ |
| TH | Thailand | https://eorscope.com/employer-of-record/thailand/ |
| TR | Turkey | https://eorscope.com/employer-of-record/turkey/ |
| TW | Taiwan | https://eorscope.com/employer-of-record/taiwan/ |
| UA | Ukraine | https://eorscope.com/employer-of-record/ukraine/ |
| US | United States | https://eorscope.com/employer-of-record/united-states/ |
| UY | Uruguay | https://eorscope.com/employer-of-record/uruguay/ |
| VN | Vietnam | https://eorscope.com/employer-of-record/vietnam/ |
| ZA | South Africa | https://eorscope.com/employer-of-record/south-africa/ |

## Columns

### `country_contributions.csv`

| Column | Type | Description |
|---|---|---|
| `iso` | string | ISO 3166-1 alpha-2 country code |
| `country` | string | Country name |
| `currency` | string | ISO 4217 local currency |
| `line_type` | string | contribution (employer charge or compulsory payment computed by rate, base, floor and ceiling) or statutory_extra (13th month, bonus, leave pay...) |
| `line_id` | string | Line identifier, unique within the country and line type |
| `line_name` | string | Line name as published |
| `rate` | number | Contribution: employer rate as a decimal (0.12 = 12%). Empty for statutory extras |
| `base` | string | Contribution base: gross / basic (share of gross) / flat (fixed amount) / band (slice of gross between floor and cap) |
| `base_factor` | number | Contribution: multiplier from gross to the statutory base, applied before floor and cap (1 = gross itself; Mexico's SBC integrates aguinaldo and vacation premium). Empty for flat lines and statutory extras |
| `base_floor_annual_local` | number | Yearly floor on the contribution base, local currency |
| `base_cap_annual_local` | number | Yearly ceiling on the contribution base, local currency |
| `flat_annual_local` | number | Fixed yearly amount when base = flat, local currency |
| `min_gross_annual_local` | number | Line applies only when annual gross is at least this, local currency |
| `max_gross_annual_local` | number | Line applies only when annual gross is at most this, local currency |
| `extra_kind` | string | Statutory extra: percent (of gross per year) / months (extra salary months) / days (paid days) |
| `extra_value` | number | Statutory extra value in the unit given by extra_kind |
| `secondary_source` | boolean | The line rests, in whole or in part, on a non-official source (declared in the notes, or the source URL is a commercial page, a private legal portal or a firm's publication) |
| `thirteenth_month` | boolean | The country mandates a 13th-month salary |
| `total_declared_floor` | boolean | The country's employer cost is declared a floor (at least), not a total |
| `total_declared_ceiling` | boolean | The modelled contribution base is the highest the law allows; costs listed with in_total=false come on top |
| `in_total` | boolean | The line is included in the employer cost total |
| `applies` | string | Condition in plain words |
| `notes` | string | Notes |
| `source_name` | string | Source name |
| `source_url` | string | Source URL |
| `source_checked_at` | date | Date the source was read |

### `country_summary.csv`

| Column | Type | Description |
|---|---|---|
| `iso` | string | ISO 3166-1 alpha-2 country code |
| `country` | string | Country name |
| `region` | string | Region |
| `currency` | string | ISO 4217 local currency |
| `example_salary_usd` | integer | Illustrative gross annual salary in USD (an example, not a median) |
| `example_role` | string | Illustrative role |
| `example_place` | string | State, province or city the lines are priced for, when not national |
| `basic_share_of_gross` | number | Share of gross taken as basic pay by the lines with base = basic (empty when the country has none) |
| `employer_cost_pct` | number | Statutory employer cost as a percent of gross at the example salary (EOR Scope engine), 4 decimals |
| `employer_cost_pct_printed` | number | The same percent as printed on eorscope.com (1 decimal, half away from zero) |
| `total_declared_floor` | boolean | The employer cost is declared a floor (at least), not a total |
| `total_declared_ceiling` | boolean | The modelled contribution base is the highest the law allows; costs listed with in_total=false come on top |
| `employer_cost_usd_month` | number | Statutory employer cost per month in USD at the example salary |
| `total_excludes` | string | A cost the total leaves out |
| `fx_local_per_usd` | number | Local currency units per 1 USD used for the conversion |
| `fx_date` | date | Date of the exchange rate used (empty for USD) |
| `last_reviewed` | date | Date the country data was last verified |

### `country_assumptions.csv`

| Column | Type | Description |
|---|---|---|
| `iso` | string | ISO 3166-1 alpha-2 country code |
| `id` | string | Assumption identifier, unique within the country |
| `label` | string | Assumption as published |
| `value` | number | Value the engine or the prose relies on (a share, a rate, a threshold, or 1 for a stated case) |
| `notes` | string | Notes |

## Suggested citation

EOR Scope (2026). *EOR Scope: statutory employer costs by country* (export 2026-10-04). EOR Scope, published by Trésor Kaya EI (Les Créavores), France. Licensed under CC BY 4.0. https://eorscope.com/methodology/
