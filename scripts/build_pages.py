"""Builds docs/index.html, the sortable view of the EOR Scope dataset, from the public CSV.
Usage: python scripts/build_pages.py <eorscope-employer-charges.csv>
CSV: https://eorscope.com/data/eorscope-employer-charges.csv"""
import csv, html, os, sys
SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'docs', 'index.html')
rows = list(csv.DictReader(open(SRC, encoding='utf-8')))
latest = max(r['last_reviewed'] for r in rows)
trs = []
for r in rows:
    floor = r['rate_is_floor'] == 'yes'
    rate = float(r['employer_rate_pct'])
    trs.append(
        f'<tr><td data-v="{html.escape(r["country"])}"><a href="{html.escape(r["page_url"])}">{html.escape(r["country"])}</a></td>'
        f'<td>{r["iso"]}</td><td>{r["currency"]}</td>'
        f'<td class="n" data-v="{r["example_salary_usd_year"]}">${int(r["example_salary_usd_year"]):,}</td>'
        f'<td class="n" data-v="{rate}">{"at least " if floor else ""}{rate:g}%</td>'
        f'<td class="n" data-v="{r["employer_charges_usd_month"]}">{"at least " if floor else ""}${int(r["employer_charges_usd_month"]):,}</td>'
        f'<td class="n" data-v="{r["statutory_lines"]}">{r["statutory_lines"]}</td>'
        f'<td data-v="{r["last_reviewed"]}">{r["last_reviewed"]}</td></tr>')
page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Employer costs by country: open dataset, {len(rows)} countries</title>
<meta name="description" content="Sort and filter statutory employer charges for {len(rows)} countries at an example salary. Open data, CC BY 4.0, with a source and a read date on each country file.">
<meta name="robots" content="index,follow">
<link rel="canonical" href="https://eorscope.github.io/employer-costs/">
<style>
:root{{--i:#14201b;--m:#5b6a63;--l:#d8dfdb;--s:#0b6e4f;--b:#fff}}
@media (prefers-color-scheme:dark){{:root{{--i:#e8eeea;--m:#a3b0a9;--l:#33403a;--s:#5fd0a6;--b:#111816}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--b);color:var(--i);font:16px/1.5 system-ui,sans-serif}}
main{{max-width:64rem;margin:auto;padding:2rem 1rem}}h1{{font-size:1.7rem;line-height:1.2;margin:0 0 .5rem}}p{{margin:.4rem 0 .9rem;color:var(--m)}}a{{color:var(--s)}}
input{{width:100%;max-width:22rem;padding:.55rem .7rem;font:inherit;color:inherit;background:transparent;border:1px solid var(--l);border-radius:4px;margin-bottom:.8rem}}
.w{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;min-width:44rem;font-size:.92rem}}
th,td{{text-align:left;padding:.45rem .6rem;border-bottom:1px solid var(--l);white-space:nowrap}}
th button{{all:unset;cursor:pointer;font-weight:600}}th button:focus-visible{{outline:2px solid var(--s)}}.n{{text-align:right;font-variant-numeric:tabular-nums}}
</style></head><body><main>
<h1>Employer costs by country: open dataset</h1>
<p>Statutory employer charges for {len(rows)} countries at each country's example salary, before any provider fee. Latest country review: {latest}. Maintained by <a href="https://eorscope.com/">EOR Scope</a>; each country name opens its file, with every line, its source and its read date.</p>
<p><a href="https://eorscope.com/data/eorscope-employer-charges.csv">Download the CSV</a> · <a href="https://eorscope.com/data/">Dataset page and citation formats</a> · <a href="https://eorscope.com/methodology/">Methodology</a> · <a href="https://github.com/eorscope/employer-costs">Repository</a> · <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a></p>
<label for="q" style="display:block;font-weight:600">Filter by country</label>
<input id="q" type="search" placeholder="Germany, BR, EUR..." autocomplete="off">
<div class="w"><table id="t"><thead><tr>
<th><button data-k="0">Country</button></th><th><button data-k="1">ISO</button></th><th><button data-k="2">Currency</button></th>
<th class="n"><button data-k="3" data-n="1">Example salary (USD/yr)</button></th><th class="n"><button data-k="4" data-n="1">Employer charges</button></th>
<th class="n"><button data-k="5" data-n="1">Charges (USD/mo)</button></th><th class="n"><button data-k="6" data-n="1">Lines</button></th><th><button data-k="7">Reviewed</button></th>
</tr></thead><tbody>
{chr(10).join(trs)}
</tbody></table></div>
<p style="margin-top:1rem;font-size:.85rem">Statutory figures, not legal or tax advice. Provider fees are not in this dataset. Credit: EOR Scope, with a link to eorscope.com/data/.</p>
</main><script>
var b=document.querySelector('#t tbody'),q=document.getElementById('q'),d={{}};
q.addEventListener('input',function(){{var s=q.value.toLowerCase();[].forEach.call(b.rows,function(r){{r.hidden=r.textContent.toLowerCase().indexOf(s)<0}})}});
document.querySelectorAll('th button').forEach(function(x){{x.addEventListener('click',function(){{var k=+x.dataset.k,n=x.dataset.n,dir=d[k]=-(d[k]||-1);
function v(r){{var c=r.cells[k],t=c.dataset.v||c.textContent;return n?parseFloat(t):t}}
[].slice.call(b.rows).sort(function(a,c){{var p=v(a),o=v(c);return dir*(n?p-o:String(p).localeCompare(String(o)))}}).forEach(function(r){{b.appendChild(r)}})}})}});
</script></body></html>
'''
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(page)
print(len(rows), latest, len(page))
