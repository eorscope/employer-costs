# EOR Scope: employer costs and EOR provider prices

Publisher: EOR Scope, published by Trésor Kaya EI (Les Créavores), France
Licence: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
Methodology: https://eorscope.com/methodology/
Export date: 2026-10-02
Source commit: d16e8e4961f0

**Cost comparison, not legal or tax advice.** Figures are an illustrative model of statutory employer charges and published provider prices; check with the provider and a local adviser before hiring.

## Files

| File | Rows | Content |
|---|---|---|
| `country_contributions.csv` | 542 | One row per employer contribution or statutory extra, with rate, base, floor/ceiling, source URL and date |
| `country_summary.csv` | 76 | One row per country: employer cost in % and USD per month at the example salary |
| `country_assumptions.csv` | 108 | One row per declared assumption: the case each country's lines and total are priced for |
| `providers.csv` | 35 | One row per provider and plan: monthly and annual prices, billing, deposit, add-ons, exclusions, source URL and date |

`employer_cost_pct` is produced by the same engine that prints the figure on eorscope.com (statutory contributions plus the statutory extras flagged `in_total`, at the example salary; EOR fees excluded). `employer_cost_pct_printed` is the figure as the site prints it (one decimal, half away from zero: 22.25 prints 22.3). Countries flagged `total_declared_floor` publish an "at least" figure, not a total. Under `total_declared_ceiling` the modelled contribution base is the highest the law allows; costs listed with `in_total=false` come on top.

Lines with `base = basic` apply to `basic_share_of_gross` × gross (`country_summary.csv`). Each total holds for the case described in `country_assumptions.csv`.

`employer_cost_pct` is not a social-security contribution rate. It adds statutory contributions, compulsory payments to private funds and statutory pay supplements (13th month, holiday pay, accrued severance), so it is not comparable with OECD Taxing Wages employer rates.

The `notes` columns reproduce the site's prose and may refer to "this page".

## Suggested citation

EOR Scope (2026). *EOR Scope: employer costs and EOR provider prices* (export 2026-10-02). EOR Scope, published by Trésor Kaya EI (Les Créavores), France. Licensed under CC BY 4.0. https://eorscope.com/methodology/
