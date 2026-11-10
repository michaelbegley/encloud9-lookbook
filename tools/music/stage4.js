// Stage 4: Demo. "Walkthrough". D minor, 122 bpm, 4/4, 16 bars.
// A (bars 0-7): Dm | Bb | C | Am, two bars each, under a 6-against-16 arpeggio. B (bars 8-15): Gm Gm Eb Eb Bb C Asus A, with the lead.
SONGS[4]={
  name:'Demo',
  title:'Walkthrough',
  bpm:122,
  steps:256,
  play:(function(){
    // per bar: [bass root, chord voicing (57..76)]
    var DM=[38,[62,65,69]],BB=[34,[58,62,65]],C=[36,[60,64,67]],AM=[33,[60,64,69]],
        GM=[31,[58,62,67]],EB=[39,[58,63,67]],ASUS=[33,[57,62,64]],A=[33,[57,61,64]];
    var BARS=[DM,DM,BB,BB,C,C,AM,AM, GM,GM,EB,EB,BB,C,ASUS,A];
    // lead for section B: [bar, step, midi, length in sixteenths]
    var LEAD=[[8,0,67,4],[8,4,70,4],[8,8,69,2],[8,10,67,2],[8,12,65,4],
      [9,0,62,6],[9,6,65,2],[9,8,67,8],
      [10,0,70,4],[10,4,67,4],[10,8,72,2],[10,10,70,2],[10,12,67,4],
      [11,0,63,6],[11,6,65,2],[11,8,67,8],
      [12,0,65,4],[12,4,69,4],[12,8,70,4],[12,12,74,4],
      [13,0,72,6],[13,6,70,2],[13,8,67,4],[13,12,64,4],
      [14,0,69,8],[14,8,67,4],[14,12,64,4],
      [15,0,61,8],[15,8,64,4],[15,12,67,2],[15,14,69,2]];
    var LM={};for(var k=0;k<LEAD.length;k++)LM[LEAD[k][0]*16+LEAD[k][1]]=LEAD[k];
    var ARP=[0,1,2,3,2,1, 0,1,2,3,2,1, 0,2,1,3];     // groups of six over sixteen: a rolling cross-rhythm
    var BASS=[[0,0,3],[3,0,2],[6,0,2],[8,0,2],[10,1,1],[11,0,2],[14,1,2]]; // [step, 0 root / 1 high, len]
    var n=-1;
    return function(i,t,d,h){
      if(i===0)n++;
      var bar=i>>4,s=i&15,B=BARS[bar],r=B[0],c=B[1],I=h.intensity||0,hiN=r+12>48?r+7:r+12;
      var change=s===0&&(bar===0||BARS[bar-1]!==B);
      if(change){
        h.chord(c);
        var len=1;while(bar+len<16&&BARS[bar+len]===B)len++;
        for(var v=0;v<3;v++)h.synth(c[v],t,d*16*len-d,.022,{pad:true,att:.25,cut:650+700*I,q:3,bus:'pump',pan:(v-1)*.5});
      }
      var intro=(n===0&&bar<2);
      // drums
      if(s%4===0)h.hit(t,'kick',intro&&s>0?.3:.44);
      if(!intro&&(s===4||s===12))h.hit(t,'clap',.11);
      if(s%4===2)h.hit(t,'hat',.04);
      else if(I>.4&&s%2===1)h.hit(t,'hat',.016);
      if(s===14&&bar%4===3)h.hit(t,'kick',.3);
      if((bar===7||bar===15)&&s>=12){h.hit(t,'tom',.18-.02*(s-12));}
      if(s===0&&(bar===8||(bar===0&&n>0)))h.hit(t,'crash',.05);
      // bass: thick filtered saw, syncopated
      for(var b=0;b<BASS.length;b++)if(BASS[b][0]===s){
        h.synth(BASS[b][1]?hiN:r,t,d*BASS[b][2]*.9,.095,{voices:3,detune:9,cut:330+520*I,q:7});
        if(BASS[b][1]===0&&s===0)h.synth(r-12>=28?r-12:r,t,d*3,.03,{wave:'sine',voices:1});
      }
      // arpeggio (the engine of the track)
      var an=c.concat([c[0]+12])[ARP[s]];
      h.synth(an,t,d*.85,s%6===0?.034:.026,{voices:2,detune:5,cut:850+750*I,q:5,bus:'fx',pan:s%2?.25:-.25});
      // section B lead
      var L=LM[i];
      if(L){
        h.synth(L[2],t,d*L[3]*.95,.055,{voices:3,detune:10,cut:1300+500*I,q:3,att:.015,bus:'fx'});
        if(I>.55&&L[2]-12>=52)h.synth(L[2]-12,t,d*L[3]*.95,.03,{wave:'square',voices:1,cut:900,q:2,bus:'fx'});
      }
      // section A counter motif: from the second loop, or once the pipe is long
      if(bar<8&&bar%2===1&&(n>0||I>.35)){
        if(s===10)h.synth(c[2],t,d*2,.04,{wave:'triangle',voices:1,cut:1600,bus:'fx'});
        if(s===12)h.synth(c[1],t,d*2,.04,{wave:'triangle',voices:1,cut:1600,bus:'fx'});
        if(s===14)h.synth(c[0]+(bar%4===3?12:0),t,d*2,.04,{wave:'triangle',voices:1,cut:1600,bus:'fx'});
      }
      // deal: a high counter-arpeggio on the offbeat sixteenths
      if(h.deal&&s%2===1){
        var dn=[c[0]+12,c[1]+12,c[2]+12,c[1]+12][(s>>1)%4];if(dn>79)dn-=12;
        h.synth(dn,t,d*.7,.034,{wave:'square',voices:1,cut:2200,q:4,bus:'fx',pan:.4});
      }
    };
  })()
};
