// Stage 5: Proposal. "Terms in Seven". F# minor (Dorian), 128 bpm, 7/8 grouped 2+2+3, 16 bars of 14 sixteenths.
// A (bars 0-7): F#m | A | E | B, two bars each. B (bars 8-15): D | E | F#m | C#sus4 C#.
SONGS[5]={
  name:'Proposal',
  title:'Terms in Seven',
  bpm:128,
  steps:224,
  play:(function(){
    var FM=[30,[61,66,69]],A=[33,[61,64,69]],E=[28,[59,64,68]],B=[35,[59,63,66]],
        D=[38,[62,66,69]],CSUS=[37,[61,66,68]],CS=[37,[61,65,68]];
    var BARS=[FM,FM,A,A,E,E,B,B, D,D,E,E,FM,FM,CSUS,CS];
    var BL=14;
    // lead: [bar, step, midi, length in sixteenths]; phrases run two bars (28 sixteenths)
    var LEAD=[
      [0,0,66,4],[0,4,69,4],[0,8,68,2],[0,10,66,2],[0,12,64,2],[1,0,66,6],[1,6,61,4],[1,10,64,4],
      [2,0,69,4],[2,4,73,4],[2,8,71,2],[2,10,69,2],[2,12,68,2],[3,0,69,6],[3,6,64,4],[3,10,66,4],
      [4,0,68,4],[4,4,71,4],[4,8,73,2],[4,10,71,2],[4,12,68,2],[5,0,64,6],[5,6,68,4],[5,10,71,4],
      [6,0,71,4],[6,4,75,4],[6,8,73,2],[6,10,71,2],[6,12,66,2],[7,0,68,6],[7,6,66,4],[7,10,63,4],
      [8,0,69,6],[8,6,74,4],[8,10,73,4],[9,0,71,6],[9,6,69,8],
      [10,0,68,6],[10,6,71,4],[10,10,76,4],[11,0,74,6],[11,6,71,8],
      [12,0,73,6],[12,6,69,4],[12,10,66,4],[13,0,68,6],[13,6,69,4],[13,10,73,4],
      [14,0,73,6],[14,6,71,4],[14,10,68,4],[15,0,65,8],[15,8,68,6]];
    var LM={};for(var k=0;k<LEAD.length;k++)LM[LEAD[k][0]*BL+LEAD[k][1]]=LEAD[k];
    // bass per bar: [step, 0 root / 1 high / 2 fifth, len]; follows the 2+2+3 groups
    var BASS=[[0,0,2],[2,0,1],[3,0,1],[4,1,2],[6,0,2],[8,0,2],[10,2,2],[12,1,2]];
    var ARP=[0,1,2, 1,2,3, 0,1,2,3, 2,3,1,2];          // 3+3+4+4 over the bar
    var n=-1;
    return function(i,t,d,h){
      if(i===0)n++;
      var bar=Math.floor(i/BL),s=i%BL,Bc=BARS[bar],r=Bc[0],c=Bc[1],I=h.intensity||0;
      var hiN=r+12>48?r+7:r+12,fifth=r+7;
      if(s===0&&(bar===0||BARS[bar-1]!==Bc)){
        h.chord(c);
        var len=1;while(bar+len<16&&BARS[bar+len]===Bc)len++;
        for(var v=0;v<3;v++)h.synth(c[v]-(v===1?12:0),t,d*BL*len-d,.022,{pad:true,att:.3,cut:600+700*I,q:3,bus:'pump',pan:(v-1)*.55});
      }
      // drums: eighths K h S h | K K S
      if(s===0||s===8)h.hit(t,'kick',.45);
      if(s===10)h.hit(t,'kick',.32);
      if(s===4||s===12)h.hit(t,'snare',.1);
      if(s===12&&bar%2===1)h.hit(t,'clap',.07);
      if(s%2===0)h.hit(t,'hat',s===0||s===4||s===8?.04:.026);
      else if(I>.45)h.hit(t,'hat',.014);
      if(bar===15&&s>=8)h.hit(t,'tom',.12+.015*(s-8));
      if(s===0&&(bar===8||(bar===0&&n>0)))h.hit(t,'crash',.05);
      // bass
      for(var b=0;b<BASS.length;b++)if(BASS[b][0]===s){
        var bn=BASS[b][1]===1?hiN:BASS[b][1]===2?fifth:r;
        h.synth(bn,t,d*BASS[b][2]*.85,.095,{voices:3,detune:10,cut:360+560*I,q:8,glide:BASS[b][1]===1?-2:0});
      }
      // arpeggio in 3+3+4+4
      var an=c.concat([c[0]+12])[ARP[s]];
      h.synth(an,t,d*.8,(s===0||s===3||s===6||s===10)?.034:.025,{voices:2,detune:6,cut:800+800*I,q:6,bus:'fx',pan:s%2?.3:-.3});
      // lead: always in section B; in A from the second loop or once the pipe is long
      var L=LM[i];
      if(L&&(bar>=8||n>0||I>.3)){
        h.synth(L[2],t,d*L[3]*.95,.05,{voices:3,detune:11,cut:1250+550*I,q:3,att:.02,bus:'fx',glide:L[3]>=6?-1:0});
        if(I>.6&&L[2]-12>=52)h.synth(L[2]-12,t,d*L[3]*.95,.028,{wave:'triangle',voices:1,cut:1000,q:2,bus:'fx'});
      }
      // deal: bright three-note counter cell running across the seven (it lands differently each bar)
      if(h.deal){
        var cell=[c[2]+12,c[1]+12,c[0]+12],dn=cell[i%3];if(dn>79)dn-=12;
        if(s%2===1||i%3===0)h.synth(dn,t,d*.65,.03,{wave:'square',voices:1,cut:2100,q:4,bus:'fx',pan:.45});
      }
    };
  })()
};
