(function(){
var d=document,W=window;
function run(){var root=d.querySelector('.wgt');if(!root)return;
function $(s,c){return (c||d).querySelector(s)}
function $$(s,c){return Array.prototype.slice.call((c||d).querySelectorAll(s))}
// booking card goes into the WP Travel Engine sidebar, under the booking form
var side=$('#secondary'),card=$('.wgt-aside',root);
if(side&&card){side.appendChild(card)}
function bookBox(){return null}
// mobile bar: show after the key facts, hide when the booking form is on screen
var bar=$('.wgt-mbar',root);
if(bar){d.body.appendChild(bar);var facts=$('.wgt-facts',root),bb=bookBox(),seenB=false,past=false;
 function upd(){bar.classList.toggle('on',past&&!seenB)}
 if('IntersectionObserver' in W){
  new IntersectionObserver(function(es){es.forEach(function(x){past=!x.isIntersecting&&x.boundingClientRect.top<0})
   ;upd()}).observe(facts);
  if(bb)new IntersectionObserver(function(es){es.forEach(function(x){seenB=x.isIntersecting});upd()}).observe(bb);
 }}
// section nav: highlight the section on screen
var links=$$('.wgt-nav a',root),secs=links.map(function(a){return $(a.getAttribute('href'))});
function spy(){var y=W.innerHeight*.3,cur=0;secs.forEach(function(s,i){if(s&&s.getBoundingClientRect().top<y)cur=i});
 links.forEach(function(a,i){a.classList.toggle('on',i===cur)})}
W.addEventListener('scroll',spy,{passive:true});spy();
links.forEach(function(a){a.addEventListener('click',function(ev){var s=$(a.getAttribute('href'));if(!s)return;ev.preventDefault();
 W.scrollTo({top:s.getBoundingClientRect().top+W.pageYOffset-80,behavior:'smooth'})})});
// itinerary: expand / collapse all
var days=$$('.wgt-day',root),ex=$('.wgt-expand',root);
if(ex)ex.addEventListener('click',function(){var open=ex.getAttribute('aria-pressed')!=='true';
 days.forEach(function(x){x.open=open});ex.setAttribute('aria-pressed',open);ex.textContent=open?'Collapse all days':'Expand all days'});
// ---------- route map: a map picture (tiles) with the route lines drawn on top, no map library ----------
var box=$('div.wgt-map',root),raw=$('#wgt-data');if(!box||!raw)return;
var R=JSON.parse(raw.textContent),NS='http://www.w3.org/2000/svg',
 CLR={ride:'#E77717',hike:'#2f7d4f',drive:'#6b7280'},DASH={ride:null,hike:'1 9',drive:'7 9'},
 TILE='https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}@2x.png',F='Plus Jakarta Sans,system-ui,sans-serif',
 dayLines=[],info=null;
// Web Mercator, world size 256 at zoom 0
function merc(p){var s=Math.sin(p[0]*Math.PI/180);return [(p[1]+180)/360*256,(.5-Math.log((1+s)/(1-s))/(4*Math.PI))*256]}
function el(n,a,p){var e=d.createElementNS(NS,n);for(var i in a)e.setAttribute(i,a[i]);if(p)p.appendChild(e);return e}
function draw(){
 var Wd=box.clientWidth||800,Ht=box.clientHeight||500,pad=Math.min(60,Wd*.08),pts=[R.at];
 R.days.forEach(function(D){D.l.forEach(function(l){pts=pts.concat(l.p)})});
 var m=pts.map(merc),xs=m.map(function(p){return p[0]}),ys=m.map(function(p){return p[1]});
 var x0=Math.min.apply(0,xs),x1=Math.max.apply(0,xs),y0=Math.min.apply(0,ys),y1=Math.max.apply(0,ys);
 var sc=Math.min((Wd-2*pad)/Math.max(x1-x0,1e-6),(Ht-2*pad)/Math.max(y1-y0,1e-6));
 sc=Math.min(sc,256*Math.pow(2,13)/256);
 var zf=Math.log(sc)/Math.LN2,z=Math.max(0,Math.min(18,Math.floor(zf))),ts=256*sc/Math.pow(2,z),
  ox=Wd/2-(x0+x1)/2*sc,oy=Ht/2-(y0+y1)/2*sc;
 function xy(p){var q=merc(p);return [q[0]*sc+ox,q[1]*sc+oy]}
 box.innerHTML='';box.style.position='relative';box.style.overflow='hidden';box.style.background='#efe8dc';
 // map picture
 var tl=d.createElement('div');tl.className='wgt-tiles';box.appendChild(tl);
 var n=Math.pow(2,z),tx0=Math.floor(-ox/ts),tx1=Math.floor((Wd-ox)/ts),ty0=Math.max(0,Math.floor(-oy/ts)),ty1=Math.min(n-1,Math.floor((Ht-oy)/ts)),sub='abcd';
 for(var tx=tx0;tx<=tx1;tx++)for(var ty=ty0;ty<=ty1;ty++){var im=d.createElement('img'),wx=((tx%n)+n)%n;
  im.alt='';im.decoding='async';im.src=TILE.replace('{s}',sub[(wx+ty)%4]).replace('{z}',z).replace('{x}',wx).replace('{y}',ty);
  im.style.cssText='left:'+(tx*ts+ox)+'px;top:'+(ty*ts+oy)+'px;width:'+(ts+.5)+'px;height:'+(ts+.5)+'px';
  im.onerror=function(){this.style.visibility='hidden'};tl.appendChild(im)}
 // route lines
 var svg=el('svg',{'class':'wgt-smap',viewBox:'0 0 '+Wd+' '+Ht,width:Wd,height:Ht,role:'img','aria-label':'Route map'});
 dayLines=[];
 [true,false].forEach(function(cas){R.days.forEach(function(D){D.l.forEach(function(l){
  var dr=l.m==='drive',a={points:l.p.map(function(p){return xy(p).join(',')}).join(' '),fill:'none','stroke-linecap':'round','stroke-linejoin':'round'};
  if(cas){a.stroke='#fff';a['stroke-width']=dr?6:8;a.opacity=.9}
  else{a.stroke=CLR[l.m];a['stroke-width']=dr?3:5;if(DASH[l.m])a['stroke-dasharray']=DASH[l.m]}
  var e=el('polyline',a,svg);e.setAttribute('data-day',D.d);dayLines.push(e);
  if(!cas)el('title',{},e).textContent='Day '+D.d+': '+D.t})})});
 // overnight stops and names
 var stops={},order=[],sk=R.at.join(','),placed=[],labels=[];
 R.days.forEach(function(D){var s=D.at.join(',');if(!stops[s]){stops[s]={at:D.at,name:D.end,days:[]};order.push(s)}stops[s].days.push(D.d)});
 function txt(x,y,t,a){var e=el('text',a,svg);e.setAttribute('x',x);e.setAttribute('y',y);e.setAttribute('font-family',F);e.textContent=t;return e}
 function label(p,t,off,force){var x=p[0],y=p[1];
  if(!force&&placed.some(function(q){return Math.abs(x-q[0])<90&&Math.abs(y-q[1])<24}))return;placed.push(p);
  var st=x<Wd-150;labels.push([st?x+off:x-off,y+5,t,st?'start':'end'])}
 var S0=xy(R.at);placed.push(S0);
 order.forEach(function(s){if(s===sk)return;var S=stops[s],p=xy(S.at);
  el('circle',{cx:p[0],cy:p[1],r:14,fill:'#1d2330',stroke:'#fff','stroke-width':3},svg);
  txt(p[0],p[1]+4,S.days.join(','),{'text-anchor':'middle','font-size':11,'font-weight':800,fill:'#fff'});
  label(p,S.name,20)});
 el('circle',{cx:S0[0],cy:S0[1],r:18,fill:'#E77717',stroke:'#fff','stroke-width':3},svg);
 txt(S0[0],S0[1]+4,'Start',{'text-anchor':'middle','font-size':10,'font-weight':800,fill:'#fff'});
 label(S0,R.start,24,true);
 labels.forEach(function(q){txt(q[0],q[1],q[2],{'text-anchor':q[3],'font-size':14,'font-weight':700,fill:'#1d2330',
  stroke:'#fff','stroke-width':4,'paint-order':'stroke'})});
 box.appendChild(svg);
 var at=d.createElement('div');at.className='wgt-attr';at.innerHTML='&copy; OpenStreetMap contributors &copy; CARTO';box.appendChild(at);
 if(!info){info=d.createElement('div');info.className='wgt-mapday';info.innerHTML='<span></span><button type="button">Show whole route</button>';
  box.parentNode.appendChild(info);info.querySelector('button').addEventListener('click',function(){showDay(0)})}
}
// "Show on map": highlight that day's lines
function showDay(n){
 dayLines.forEach(function(e){e.style.opacity=(!n||+e.getAttribute('data-day')===n)?'':'.2'});
 var D=R.days[n-1];if(n&&D){info.querySelector('span').textContent='Day '+D.d+' · '+D.t;info.classList.add('on')}else info.classList.remove('on');
}
try{draw()}catch(e){if(W.console)console.error('wgt map',e)}
var rt,lw=box.clientWidth;W.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(function(){
 if(box.clientWidth!==lw){lw=box.clientWidth;try{draw()}catch(e){}}},200)});
$$('.wgt-onmap',root).forEach(function(b){b.addEventListener('click',function(){
 W.scrollTo({top:box.getBoundingClientRect().top+W.pageYOffset-90,behavior:'smooth'});showDay(+b.getAttribute('data-day'))})});
}
if(d.readyState==='loading')d.addEventListener('DOMContentLoaded',run);else run();
})();
