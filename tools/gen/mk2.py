from rep import run
P='/home/claude/lb/pages/nine-marketing.html'
run(P,[
('@media (min-width:1081px){body.p-marketing .plans-grid.flip',
'''/* support table: stacked rows on phones instead of a clipped four-column table */
@media (max-width:640px){
  body.p-marketing .plans-grid .tbl{min-width:0}
  body.p-marketing .plans-grid .tbl thead{display:none}
  body.p-marketing .plans-grid .tbl tbody tr{display:grid;grid-template-columns:1fr auto;column-gap:16px;padding:14px 0;border-bottom:1px solid var(--line)}
  body.p-marketing .plans-grid .tbl tbody th,body.p-marketing .plans-grid .tbl tbody td{display:block;border:0;padding:0}
  body.p-marketing .plans-grid .tbl tbody td.pr{text-align:right}
  body.p-marketing .plans-grid .tbl tbody td:nth-child(n+3){grid-column:1/-1;font-size:15px;color:var(--muted);margin-top:4px}
  body.p-marketing .plans-grid .tbl tbody td:empty{display:none}
}
@media (min-width:1081px){body.p-marketing .plans-grid.flip'''),
])
