// Stage 3: Discovery. C minor, 122 bpm, 7/8 (grouped 2+2+3), 16-bar loop.
// The first odd meter: a limping, curious groove, arp cells that restart on each group, a Neapolitan Db for a darker turn.
SONGS[3]={
  name:'Discovery',
  title:'Seven Questions Deep',
  bpm:122,
  steps:224,                     // 16 bars x 14 sixteenths
  n:0,
  ch:[
    {b:36,v:[60,63,67,70,74]},   // Cm9
    {b:44,v:[60,63,67,72,74]},   // Abmaj7#11
    {b:41,v:[60,65,68,72,75]},   // Fm7
    {b:43,v:[60,62,65,67,72]},   // Gsus4 (bar 7 turns to G7b9)
    {b:39,v:[58,62,65,67,70]},   // Ebmaj9
    {b:38,v:[58,62,65,70,72]},   // Bbadd9/D
    {b:37,v:[61,65,68,72,75]},   // Dbmaj9 (Neapolitan)
    {b:43,v:[60,62,65,67,72]}    // Gsus4 (bar 15 turns to G7)
  ],
  g7b9:[59,62,65,68,71],
  g7:[59,62,65,67,71],
  // lead: [step,midi,len] per bar; back half every loop, the call (bars 2-3, 6-7) on alternate loops
  back:{8:[[0,70,4],[4,67,4],[8,74,6]],9:[[0,72,4],[4,70,4],[8,67,6]],
        10:[[0,65,4],[4,70,4],[8,72,3],[11,74,3]],11:[[0,74,8],[8,72,6]],
        12:[[0,72,4],[4,68,4],[8,65,6]],13:[[0,68,4],[4,72,4],[8,75,6]],
        14:[[0,74,8],[8,72,6]],15:[[0,71,14]]},
  call:{2:[[0,67,4],[4,72,4],[8,74,6]],3:[[0,72,14]],6:[[0,72,4],[4,67,4],[8,65,6]],7:[[0,68,6],[6,71,8]]},
  // bass riff in 7/8: [step, offset, len]
  riff:[[0,0,3],[3,0,1],[4,12,2],[6,0,2],[8,0,2],[10,7,2],[12,12,2]],
  // keep every bass note inside MIDI 28..48: fold by octaves, and if the jump folds onto the root use the fifth instead
  bn:function(r,o){var n=r+o;while(n>48)n-=12;while(n<28)n+=12;if(n===r&&o!==0)n=(r+7>48)?r-5:r+7;return n},
  cells:[[0,1,2,3],[1,2,3,4],[0,2,4,3,2,1]],
  play:function(i,t,d,h){
    var S=SONGS[3];if(i===0)S.n++;
    var bar=Math.floor(i/14),s=i%14,ci=bar>>1,I=h.intensity||0,c=S.ch[ci],k,p;
    var v=(bar===7)?S.g7b9:(bar===15)?S.g7:c.v;
    var grp=s<4?0:s<8?1:2,gs=s<4?s:s<8?s-4:s-8;          // which 2+2+3 group, and step within it
    if(s===0&&(bar%2===0||bar===7||bar===15)){
      h.chord(v.slice());
      var plen=(bar===6||bar===7||bar>=14)?14:28;
      for(k=0;k<v.length;k++)h.synth(v[k],t,d*plen,.019,{pad:true,cut:700+700*I,att:.35,q:2,detune:13,bus:'pump',pan:(k-2)*.25});
      if(i===0&&S.n>1)h.hit(t,'crash',.035);
    }
    // bass: thick saw riff, filter opens with intensity
    for(k=0;k<S.riff.length;k++)if(S.riff[k][0]===s){
      h.synth(S.bn(c.b,S.riff[k][1]),t,d*S.riff[k][2]*.9,s===0?.11:.085,{cut:280+800*I,q:9,detune:9});
    }
    // drums: kick on the 2+2+3 pulse, claps on 4 and 11
    if(s===0||s===8)h.hit(t,'kick',.45);
    if(I>.4&&s===10)h.hit(t,'kick',.28);
    if(s===4||s===11)h.hit(t,'clap',.075);
    if(s%2===0)h.hit(t,'hat',gs===0?.03:.018);
    if(I>.55&&s%2===1)h.hit(t,'hat',.01);
    if(s===12&&bar%2===1)h.hit(t,'openhat',.03);
    if(bar===15&&s>=8)h.hit(t,'tom',.16-(s-8)*.018);
    // arp: a cell that restarts on every group, so the pattern limps with the meter
    var cell=S.cells[grp];p=v[cell[gs%cell.length]];if(p>70)p-=12;
    if(I>.15||S.n>1||s%2===0)h.synth(p,t,d*.85,gs===0?.034:.024,{voices:1,cut:700+1100*I,q:8,bus:'fx',pan:grp===1?.35:-.25});
    // lead
    var ph=S.back[bar]||((S.n%2===0||I>.45)?S.call[bar]:null);
    if(ph)for(k=0;k<ph.length;k++)if(ph[k][0]===s)
      h.synth(ph[k][1],t,d*ph[k][2]*.93,.055,{voices:2,detune:11,cut:1100+600*I,q:4,att:.015,glide:(k===0?-1:0),bus:'fx'});
    // a low fifth drone under the second half once intensity is up
    if(I>.6&&bar>=8&&s===0&&bar%2===0)h.synth(c.b+19,t,d*28,.03,{pad:true,wave:'triangle',voices:1,cut:600,att:.8,bus:'pump'});
    // deal: three-against-seven counter-arp, bright but mid
    if(h.deal&&i%3===0){p=v[(Math.floor(i/3))%v.length];h.synth(p<64?p+12:p,t,d*2.6,.035,{wave:'square',voices:1,cut:2400,q:2,bus:'fx',pan:.45})}
  }
};
