# EOR Scope: employer costs and EOR provider prices

Publisher: EOR Scope, published by Trésor Kaya EI (Les Créavores), France
Licence: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
Methodology: https://eorscope.com/methodology/
Export date: 2026-10-02
Source commit: 710c20b734e7

**Cost comparison, not legal or tax advice.** Figures are an illustrative model of statutory employer charges and published provider prices; check with the provider and a local adviser before hiring.

## Files

| File | Rows | Content |
|---|---|---|
| `country_contributions.csv` | 542 | One row per employer contribution or statutory extra, with rate, base, floor/ceiling, source URL and date |
| `country_summary.csv` | 76 | One row per country: employer cost in % and USD per month at the example salary |
| `country_assumptions.csv` | 108 | One row per declared assumption: the case each country's lines and total are priced for |
| `providers.csv` | 35 | One row per provider and plan: monthly and annual prices, billing, deposit, add-ons, exclusions, source URL and date |

`employer_cost_pct` is produced by the same engine that prints the figure on eorscope.com (statutory contributions plus the statutory extras flagged `in_total`, at the example salary; EOR fees excluded). `employer_cost_pct_printed` is the figure as the site prints it (one decimal, half away from zero: 22.25 prints 22.3). Countries flagged `total_declared_floor` publish an "at least" figure, not a total. Under `total_declared_ceiling` the modelled contribution base is the highest the law allows; costs listed with `in_total=false` come on top.

Lines with `base = basic` apply to `basic_share_of_gross` × gross (`country_summary.csv`). `base_factor` multiplies gross into the statutory base before the floor and the ceiling apply (Mexico: the integrated contribution base includes the aguinaldo and the vacation premium). Each total holds for the case described in `country_assumptions.csv`.

`employer_cost_pct` is not a social-security contribution rate. It adds statutory contributions, compulsory payments to private funds and statutory pay supplements (13th month, holiday pay, accrued severance), so it is not comparable with OECD Taxing Wages employer rates.

The `notes` columns reproduce the site's prose and may refer to "this page".

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
| `secondary_source` | boolean | The line rests, in whole or in part, on a non-official source (declared in the notes, or the source URL is a provider page, a private legal portal or a firm's publication) |
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

### `providers.csv`

| Column | Type | Description |
|---|---|---|
| `provider_id` | string | Provider identifier |
| `provider` | string | Provider name |
| `plan_id` | string | Plan identifier, unique within the provider |
| `plan` | string | Plan name |
| `scope` | string | eor / contractor / payroll / peo |
| `pricing_model` | string | list (public flat price) / from (public starting price) / quote (not published) |
| `price_usd_month` | number | Published price per person per month, USD |
| `annual_price_usd_month` | number | Price per person per month on annual billing, USD |
| `billing` | string | monthly / annual / either / unknown |
| `min_term_months` | integer | Minimum term in months |
| `deposit_policy` | string | Deposit policy as published |
| `fx_markup_pct` | number | Published FX markup, percent |
| `addons` | string | Add-ons, separated by ' / ' |
| `countries_excluded` | string | Countries tracked by EOR Scope that the provider does not cover (ISO codes, ';'-separated) |
| `notes` | string | Notes |
| `source_name` | string | Source name |
| `source_url` | string | Pricing page URL |
| `checked_at` | date | Date the price was read |

## Suggested citation

EOR Scope (2026). *EOR Scope: employer costs and EOR provider prices* (export 2026-10-02). EOR Scope, published by Trésor Kaya EI (Les Créavores), France. Licensed under CC BY 4.0. https://eorscope.com/methodology/
