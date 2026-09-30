(function(){
var d=document,W=window;
function run(){var root=d.querySelector('.wgt');if(!root)return;
function $(s,c){return (c||d).querySelector(s)}
function $$(s,c){return Array.prototype.slice.call((c||d).querySelectorAll(s))}
// booking card goes into the WP Travel Engine sidebar, under the booking form
var side=$('#secondary'),card=$('.wgt-aside',root);
if(side&&card){side.appendChild(card)}
// "Book" buttons scroll to the booking form and make it glow
function bookBox(){return $('#secondary .wpte-bf-outer')||$('#secondary .widget')||side}
$$('.wgt-go-book').forEach(function(a){a.addEventListener('click',function(ev){
 var b=bookBox();if(!b)return;ev.preventDefault();
 var y=b.getBoundingClientRect().top+W.pageYOffset-110;W.scrollTo({top:y,behavior:'smooth'});
 b.classList.remove('wgt-flash');void b.offsetWidth;b.classList.add('wgt-flash');
})});
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
// ---------- route map (Leaflet, loaded when the map comes near the screen) ----------
var box=$('div.wgt-map',root),raw=$('#wgt-data');if(!box||!raw)return;
var R=JSON.parse(raw.textContent),map=null,dayLayers=[],pending=null,
 CLR={ride:'#E77717',hike:'#2f7d4f',drive:'#6b7280'},
 DASH={ride:null,hike:'1 9',drive:'7 9'};
// always use our own Leaflet 1.9.4: another plugin can put an older Leaflet on window.L,
// which breaks the route lines (bindTooltip / flyToBounds missing)
var L=null,LV='1.9.4',CDN=['https://unpkg.com/leaflet@'+LV+'/dist/','https://cdnjs.cloudflare.com/ajax/libs/leaflet/'+LV+'/'];
function fail(){box.innerHTML='<div class="wgt-map-err">The map could not load. The route is listed below.</div>'}
function load(cb,i){i=i||0;if(W.L&&W.L.version===LV){L=W.L;return cb()}
 if(i>=CDN.length)return fail();
 var c=d.createElement('link');c.rel='stylesheet';c.href=CDN[i]+'leaflet.css';d.head.appendChild(c);
 var s=d.createElement('script');s.src=CDN[i]+'leaflet.js';
 s.onload=function(){var x=W.L;if(!x||x.version!==LV)return load(cb,i+1);L=x.noConflict?x.noConflict():x;cb()};
 s.onerror=function(){load(cb,i+1)};d.head.appendChild(s)}
function safe(f){return function(){try{f.apply(this,arguments)}catch(e){if(W.console)console.error('wgt map',e)}}}
function pin(txt,cls){return L.divIcon({className:'',html:'<div class="wgt-pin '+(cls||'')+'">'+txt+'</div>',iconSize:[30,30],iconAnchor:[15,15]})}
function init(){
 box.innerHTML='';
 // canvas renderer: theme CSS on svg/path can't hide the route lines
 map=L.map(box,{scrollWheelZoom:false,zoomSnap:.25,preferCanvas:true,renderer:L.canvas({padding:.5,tolerance:6})});
 var base={
  'Map':L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',{maxZoom:19,subdomains:'abcd',attribution:'&copy; OpenStreetMap contributors &copy; CARTO'}),
  'Terrain':L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',{maxZoom:17,attribution:'&copy; OpenStreetMap contributors, SRTM | &copy; OpenTopoMap (CC-BY-SA)'}),
  'Satellite':L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',{maxZoom:18,attribution:'Tiles &copy; Esri'})};
 base['Map'].addTo(map);L.control.layers(base,null,{position:'topright'}).addTo(map);
 map.once('focus',function(){map.scrollWheelZoom.enable()});
 var all=[],stops={};
 R.days.forEach(function(D){var g=L.featureGroup();
  D.l.forEach(function(l){
   L.polyline(l.p,{color:'#fff',weight:l.m==='drive'?6:8,opacity:.9,lineCap:'round',lineJoin:'round'}).addTo(g);
   L.polyline(l.p,{color:CLR[l.m],weight:l.m==='drive'?3:5,dashArray:DASH[l.m],lineCap:'round',lineJoin:'round'})
    .bindTooltip('Day '+D.d+': '+D.t,{sticky:true,className:'wgt-tt'}).addTo(g);
   all=all.concat(l.p);
   l.n.forEach(function(n,i){var p=l.p[i+1];if(n===D.end)return;
    L.marker(p,{icon:L.divIcon({className:'',html:'<div class="wgt-dot"></div>',iconSize:[10,10],iconAnchor:[5,5]})})
     .bindTooltip(n,{direction:'top',offset:[0,-6],className:'wgt-tt'}).addTo(g)});
  });
  g.addTo(map);dayLayers[D.d]=g;
  var k=D.at.join(',');(stops[k]=stops[k]||{at:D.at,name:D.end,days:[]}).days.push(D);
 });
 var sk=R.at.join(',');
 L.marker(R.at,{icon:pin('Start','s'),zIndexOffset:1000}).bindPopup('<small>Start &amp; finish</small><b>'+R.start+'</b>').addTo(map);
 Object.keys(stops).forEach(function(k){if(k===sk)return;var S=stops[k],n=S.days.map(function(x){return x.d});
  L.marker(S.at,{icon:pin(n.join(',')),zIndexOffset:500})
   .bindPopup('<small>Night '+n.join(' &amp; ')+'</small><b>'+S.name+'</b>'+S.days.map(function(x){return 'Day '+x.d+': '+x.t}).join('<br>'))
   .bindTooltip(S.name,{direction:'top',offset:[0,-16],className:'wgt-tt'}).addTo(map)});
 var info=d.createElement('div');info.className='wgt-mapday';info.innerHTML='<span></span><button type="button">Show whole route</button>';
 box.parentNode.appendChild(info);
 // on treks the walking area is tiny next to the drive from Marrakech: start zoomed on it
 var wb=L.latLngBounds(all.length?all:[R.at]),act=[];
 R.days.forEach(function(D){D.l.forEach(function(l){if(l.m!=='drive')act=act.concat(l.p)})});
 function span(b){return Math.max(b.getNorth()-b.getSouth(),b.getEast()-b.getWest())}
 var ab=act.length?L.latLngBounds(act):null;
 if(ab&&span(ab)<span(wb)*.3){map.fitBounds(ab,{paddingTopLeft:[40,40],paddingBottomRight:[40,90],maxZoom:12});
  info.querySelector('span').textContent=(R.days.some(function(D){return D.l.some(function(l){return l.m==='ride'})})?'Riding':'Trekking')+' area';info.classList.add('on')}
 else map.fitBounds(wb,{padding:[30,30]});
 info.querySelector('button').addEventListener('click',function(){info.classList.remove('on');
  dayLayers.forEach(function(g){g&&g.setStyle&&g.eachLayer(function(x){x.setStyle&&x.setStyle({opacity:x.options.color==='#fff'?.9:1})})});
  map.flyToBounds(wb,{padding:[30,30],duration:.8})});
 map._wgtInfo=info;
 // the map box can change size after load (fonts, sidebar, rotation): redraw
 W.addEventListener('resize',function(){map.invalidateSize()});
 setTimeout(function(){map.invalidateSize()},400);
 if(pending)showDay(pending);
}
function showDay(n){
 var g=dayLayers[n];if(!g){return}
 dayLayers.forEach(function(x,i){x&&x.eachLayer(function(y){y.setStyle&&y.setStyle({opacity:i==n?(y.options.color==='#fff'?.9:1):.22})})});
 map.flyToBounds(g.getBounds(),{padding:[50,50],maxZoom:12,duration:.8});
 var D=R.days[n-1];map._wgtInfo.querySelector('span').textContent='Day '+D.d+' · '+D.t;map._wgtInfo.classList.add('on');
}
var started=false;function go(){if(started)return;started=true;load(safe(init))}
if('IntersectionObserver' in W){var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){io.disconnect();go()}},{rootMargin:'400px'});io.observe(box)}else go();
$$('.wgt-onmap',root).forEach(function(b){b.addEventListener('click',function(){var n=+b.getAttribute('data-day');
 W.scrollTo({top:box.getBoundingClientRect().top+W.pageYOffset-90,behavior:'smooth'});
 if(map)showDay(n);else{pending=n;go()}})});
}
if(d.readyState==='loading')d.addEventListener('DOMContentLoaded',run);else run();
})();
