import re,sys,glob
files=sys.argv[1:]
OND="Anyone can ask. No SLA, so plan clients come first."
subs=[
 (r'\[2008\]','2008'),
 # contact hours (open hours 8 to 5); support-plan response hours stay 7 to 5
 (r'(0729(?:</a>)?,? (?:from )?|0729</a> \()7:00am to 5:00pm Central',r'\g<1>8:00am to 5:00pm Central'),
 (r'(Call us</span><span class="ds">1-844-264-0729, )7:00am',r'\g<1>8:00am'),
 (r'\[Brian sets: who can still use it, for example during a project\]',OND),
 (r'\[Brian to confirm: who can still use it, for example during a project\]',OND),
 (r'\[For current clients: Brian to confirm\]',OND),
 (r'(On-Demand</th><td class="pr">\$200 an hour</td><td>As needed, no retainer</td><td>)\[Brian to confirm\]',r'\g<1>'+OND),
 (r'typically takes \[Brian sets\] to \[Brian sets\] months','typically takes 8 to 16 weeks, and every project is quoted in writing'),
 (r'Typically \[Brian sets\] to \[Brian sets\] months','Typically 8 to 16 weeks'),
 (r'Typically \[N to N\] months','Typically 8 to 16 weeks'),
 (r'typically takes \[N to N\] months','typically takes 8 to 16 weeks'),
 (r'A rescue typically takes \[Brian sets\] months','A full rescue typically takes 8 to 16 weeks; a small fix can take days'),
 (r'Typically \[Brian sets\] months','Typically 8 to 16 weeks'),
]
n=0
for f in files:
    s=open(f).read(); o=s
    for a,b in subs: s=re.sub(a,b,s)
    if f.endswith('nine-packages.html'):
        q='<dt>Price</dt><dd>Quoted in writing after a short call</dd>'
        def setp(s,name,val):
            i=s.find(name); j=s.find(q,i)
            return s[:j]+'<dt>Price</dt><dd>'+val+'</dd>'+s[j+len(q):] if i>=0 and j>=0 else s
        s=setp(s,'Rescue and Repair</','$500 to $10,000, quoted in writing')
        s=setp(s,'Sales Accelerator</','$7,500')
        s=setp(s,'Service Accelerator</','$7,500')
    if f.endswith('nine-marketing.html'):
        s=re.sub(r'We also package Click for small teams as the <a class="lnk" href="https://www.encloud9.com/clickdimensions-powerpack/">ClickDimensions PowerPack, powered by enCloud9</a>\.',
                 'For small teams, the enCloud9 Marketing Accelerator is a $5,000 fixed fee: ClickDimensions set up, training, and your first email send.',s)
    if s!=o: open(f,'w').write(s); n+=1; print('changed',f)
print(n)
