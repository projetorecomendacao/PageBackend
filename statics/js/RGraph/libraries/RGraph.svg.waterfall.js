
RGraph=window.RGraph||{isRGraph:true};RGraph.SVG=RGraph.SVG||{};(function(win,doc,undefined)
{RGraph.SVG.Waterfall=function(conf)
{this.set=function(name,value)
{if(arguments.length===1&&typeof name==='object'){for(i in arguments[0]){if(typeof i==='string'){name=ret.name;value=ret.value;this.set(name,value);}}}else{var ret=RGraph.SVG.commonSetter({object:this,name:name,value:value});name=ret.name;value=ret.value;this.properties[name]=value;if(name==='colors'){this.originalColors=RGraph.SVG.arrayClone(value);this.colorsParsed=false;}}
return this;};this.get=function(name)
{var tmp=RGraph.SVG.propertyNameAlias({object:this,name:name});name=tmp.name;return this.properties[name];};this.id=conf.id;this.uid=RGraph.SVG.createUID();this.container=document.getElementById(this.id);this.layers={};this.svg=RGraph.SVG.createSVG({object:this,container:this.container});this.isRGraph=true;this.data=conf.data;this.type='waterfall';this.coords=[];this.colorsParsed=false;this.originalColors={};this.gradientCounter=1;RGraph.SVG.OR.add(this);this.container.style.display='inline-block';this.properties={marginLeft:35,marginRight:35,marginTop:35,marginBottom:35,marginInner:5,backgroundColor:null,backgroundImage:null,backgroundImageAspect:'none',backgroundImageStretch:true,backgroundImageOpacity:null,backgroundImageX:null,backgroundImageY:null,backgroundImageW:null,backgroundImageH:null,backgroundGrid:true,backgroundGridColor:'#ddd',backgroundGridLinewidth:1,backgroundGridHlines:true,backgroundGridHlinesCount:null,backgroundGridVlines:true,backgroundGridVlinesCount:null,backgroundGridBorder:true,backgroundGridDashed:false,backgroundGridDotted:false,backgroundGridDashArray:null,colors:['black','red','blue'],colorsSequential:false,colorsStroke:'#aaa',colorsConnector:null,total:true,linewidth:1,yaxis:true,yaxisTickmarks:true,yaxisTickmarksLength:5,yaxisColor:'black',yaxisScale:true,yaxisLabels:null,yaxisLabelsOffsetx:0,yaxisLabelsOffsety:0,yaxisLabelsCount:5,yaxisScaleUnitsPre:'',yaxisScaleUnitsPost:'',yaxisScaleStrict:false,yaxisScaleDecimals:0,yaxisScalePoint:'.',yaxisScaleThousand:',',yaxisScaleRound:false,yaxisScaleMax:null,yaxisScaleMin:0,yaxisScaleFormatter:null,yaxisLabelsColor:null,yaxisLabelsBold:null,yaxisLabelsItalic:null,yaxisLabelsFont:null,yaxisLabelsSize:null,xaxis:true,xaxisTickmarks:true,xaxisTickmarksLength:5,xaxisLabels:null,xaxisLabelsFont:null,xaxisLabelsSize:null,xaxisLabelsColor:null,xaxisLabelsBold:null,xaxisLabelsItalic:null,xaxisLabelsPosition:'section',xaxisLabelsPositionEdgeTickmarksCount:null,xaxisColor:'black',xaxisLabelsOffsetx:0,xaxisLabelsOffsety:0,labelsAbove:false,labelsAboveFont:null,labelsAboveSize:null,labelsAboveBold:null,labelsAboveItalic:null,labelsAboveColor:null,labelsAboveBackground:'rgba(255,255,255,0.5)',labelsAboveBackgroundPadding:2,labelsAboveUnitsPre:null,labelsAboveUnitsPost:null,labelsAbovePoint:null,labelsAboveThousand:null,labelsAboveFormatter:null,labelsAboveDecimals:null,labelsAboveOffsetx:0,labelsAboveOffsety:0,labelsAboveHalign:'center',labelsAboveValign:'bottom',labelsAboveSpecific:null,labelsAboveLastFont:null,labelsAboveLastBold:null,labelsAboveLastItalic:null,labelsAboveLastSize:null,labelsAboveLastColor:null,labelsAboveLastBackground:null,labelsAboveLastBackgroundPadding:null,textColor:'black',textFont:'Arial, Verdana, sans-serif',textSize:12,textBold:false,textItalic:false,tooltips:null,tooltipsOverride:null,tooltipsEffect:'fade',tooltipsCssClass:'RGraph_tooltip',tooltipsEvent:'click',highlightStroke:'rgba(0,0,0,0)',highlightFill:'rgba(255,255,255,0.7)',highlightLinewidth:1,title:'',titleX:null,titleY:null,titleHalign:'center',titleValign:null,titleSize:null,titleColor:null,titleFont:null,titleBold:null,titleItalic:null,titleSubtitle:null,titleSubtitleSize:null,titleSubtitleColor:'#aaa',titleSubtitleFont:null,titleSubtitleBold:null,titleSubtitleItalic:null,key:null,keyColors:null,keyOffsetx:0,keyOffsety:0,keyLabelsOffsetx:0,keyLabelsOffsety:-1,keyLabelsFont:null,keyLabelsSize:null,keyLabelsColor:null,keyLabelsBold:null,keyLabelsItalic:null};RGraph.SVG.getGlobals(this);if(RGraph.SVG.FX&&typeof RGraph.SVG.FX.decorate==='function'){RGraph.SVG.FX.decorate(this);}
var prop=this.properties;this.draw=function()
{RGraph.SVG.fireCustomEvent(this,'onbeforedraw');this.width=Number(this.svg.getAttribute('width'));this.height=Number(this.svg.getAttribute('height'));RGraph.SVG.createDefs(this);this.coords=[];this.graphWidth=this.width-prop.marginLeft-prop.marginRight;this.graphHeight=this.height-prop.marginTop-prop.marginBottom;RGraph.SVG.resetColorsToOriginalValues({object:this});this.parseColors();if(prop.total){var sum=RGraph.SVG.arraySum(this.data);this.data.push(sum);if(prop.xaxisLabels&&prop.xaxisLabels.length===(this.data.length-1)){prop.xaxisLabels.push('');}}
for(var i=0,max=0,runningTotal=0;i<this.data.length-(prop.total?1:0);++i){runningTotal+=this.data[i]
max=Math.max(Math.abs(max),Math.abs(runningTotal));}
if(typeof prop.yaxisScaleMax==='number'){max=prop.yaxisScaleMax;}
if(prop.yaxisScaleMin==='mirror'||prop.yaxisScaleMin==='middle'||prop.yaxisScaleMin==='center'){var mirrorScale=true;prop.yaxisScaleMin=0;}
this.scale=RGraph.SVG.getScale({object:this,numlabels:prop.yaxisLabelsCount,unitsPre:prop.yaxisScaleUnitsPre,unitsPost:prop.yaxisScaleUnitsPost,max:max,min:prop.yaxisScaleMin,point:prop.yaxisScalePoint,round:prop.yaxisScaleRound,thousand:prop.yaxisScaleThousand,decimals:prop.yaxisScaleDecimals,strict:typeof prop.yaxisScaleMax==='number',formatter:prop.yaxisScaleFormatter});if(mirrorScale){this.scale=RGraph.SVG.getScale({object:this,numlabels:prop.yaxisLabelsCount,unitsPre:prop.yaxisScaleUnitsPre,unitsPost:prop.yaxisScaleUnitsPost,max:this.scale.max,min:this.scale.max* -1,point:prop.yaxisScalePoint,round:false,thousand:prop.yaxisScaleThousand,decimals:prop.yaxisScaleDecimals,strict:typeof prop.yaxisScaleMax==='number',formatter:prop.yaxisScaleFormatter});}
this.max=this.scale.max;this.min=this.scale.min;prop.yaxisScaleMax=this.scale.max;prop.yaxisScaleMin=this.scale.min;RGraph.SVG.drawBackground(this);RGraph.SVG.drawXAxis(this);RGraph.SVG.drawYAxis(this);this.drawBars();this.drawLabelsAbove();if(typeof prop.key!==null&&RGraph.SVG.drawKey){RGraph.SVG.drawKey(this);}else if(!RGraph.SVG.isNull(prop.key)){alert('The drawKey() function does not exist - have you forgotten to include the key library?');}
RGraph.SVG.attribution(this);RGraph.SVG.fireCustomEvent(this,'ondraw');return this;};this.drawBars=function()
{this.graphWidth=this.width-prop.marginLeft-prop.marginRight;this.graphHeight=this.height-prop.marginTop-prop.marginBottom;var innerWidth=(this.graphWidth/this.data.length)-(2*prop.marginInner),outerWidth=(this.graphWidth/this.data.length);var y=this.getYCoord(0),total=0;for(var i=0;i<(this.data.length);++i){var prevValue=this.data[i-1],nextValue=this.data[i+1],currentValue=this.data[i],prevTotal=total;total+=parseFloat(this.data[i])||0;var height=Math.abs((this.data[i]/(this.scale.max-this.scale.min))*this.graphHeight);if(RGraph.SVG.isNull(prevValue)){if(currentValue>0){y=this.getYCoord(prevTotal)-height;}else{y=this.getYCoord(prevTotal);}}else{if(i==0&&this.data[i]>0){y=y-height;}else if(this.data[i]>0&&this.data[i-1]>0){y=y-height;}else if(this.data[i]>0&&this.data[i-1]<0){y=y+prevHeight-height;}else if(this.data[i]<0&&this.data[i-1]>0){}else if(this.data[i]<0&&this.data[i-1]<0){y=y+prevHeight;}}
var fill=this.data[i]>0?prop.colors[0]:prop.colors[1];if(prop.colorsSequential){fill=prop.colors[i];}
if(prop.total){if(i===(this.data.length-1)&&this.data[this.data.length-1]>=0){y=this.getYCoord(0)-height;if(!prop.colorsSequential){fill=prop.colors[2];}}else if(i===(this.data.length-1)&&this.data[this.data.length-1]<0){y=this.getYCoord(0);if(!prop.colorsSequential){fill=prop.colors[2];}}}
var x=prop.marginLeft+(outerWidth*i)+prop.marginInner;if(this.data[i]===null||typeof this.data[i]==='undefined'){var axisY=this.getYCoord(0);if(prevValue<0){y=prevY+prevHeight;}else{y=prevY;}
height=this.getYCoord(0)-this.getYCoord(total);if(!prop.colorsSequential){fill=prop.colors[3]||prop.colors[2];}
if(height<0){y+=height;height*=-1;}}
var rect=RGraph.SVG.create({svg:this.svg,type:'rect',parent:this.svg.all,attr:{x:x,y:y,width:innerWidth,height:height,stroke:prop.colorsStroke,fill:fill,'stroke-width':prop.linewidth,'shape-rendering':'crispEdges','data-index':i,'data-original-x':x,'data-original-y':y,'data-original-width':innerWidth,'data-original-height':height,'data-original-stroke':prop.colorsStroke,'data-original-fill':fill,'data-value':String(this.data[i])}});this.coords.push({object:this,element:rect,x:x,y:y,width:innerWidth,height:height});if(!RGraph.SVG.isNull(prop.tooltips)&&prop.tooltips[i]){var obj=this;(function(idx)
{rect.addEventListener(prop.tooltipsEvent.replace(/^on/,''),function(e)
{obj.removeHighlight();RGraph.SVG.tooltip({object:obj,index:idx,text:prop.tooltips[idx],event:e});obj.highlight(e.target);},false);rect.addEventListener('mousemove',function(e)
{e.target.style.cursor='pointer'},false);})(i);}
var prevX=x,prevY=y,prevWidth=innerWidth,prevHeight=height,prevValue=this.data[i];}
for(var i=0;i<this.coords.length;++i){if(this.coords[i+1]&&this.coords[i+1].element){var x1=Number(this.coords[i].element.getAttribute('x'))+Number(this.coords[i].element.getAttribute('width')),y1=parseInt(this.coords[i].element.getAttribute('y'))+(this.data[i]>0?0:parseInt(this.coords[i].element.getAttribute('height'))),x2=x1+(2*prop.marginInner),y2=parseInt(this.coords[i].element.getAttribute('y'))+(this.data[i]>0?0:parseInt(this.coords[i].element.getAttribute('height')));if(this.coords[i].element.getAttribute('data-value')==='null'){y1=parseFloat(this.coords[i].element.getAttribute('y'));y2=parseFloat(y1);}
var line=RGraph.SVG.create({svg:this.svg,type:'line',parent:this.svg.all,attr:{x1:x1,y1:y1+0.5,x2:x2,y2:y2+0.5,stroke:prop.colorsConnector||prop.colorsStroke,'stroke-width':prop.linewidth,'data-index':i,'data-original-x1':x1,'data-original-y1':y1+0.5,'data-original-x2':x2,'data-original-y2':y2+0.5}});}}};this.getYCoord=function(value)
{var prop=this.properties;if(value>this.scale.max){return null;}
var y,xaxispos=prop.xaxispos;if(value<this.scale.min){return null;}
y=((value-this.scale.min)/(this.scale.max-this.scale.min));y*=(this.height-prop.marginTop-prop.marginBottom);y=this.height-prop.marginBottom-y;return y;};this.highlight=function(rect)
{var x=rect.getAttribute('x'),y=rect.getAttribute('y'),width=rect.getAttribute('width'),height=rect.getAttribute('height');var highlight=RGraph.SVG.create({svg:this.svg,type:'rect',parent:this.svg.all,attr:{stroke:prop.highlightStroke,fill:prop.highlightFill,x:x,y:y,width:width,height:height,'stroke-width':prop.highlightLinewidth},style:{pointerEvents:'none'}});RGraph.SVG.REG.set('highlight',highlight);};this.parseColors=function()
{if(!Object.keys(this.originalColors).length){this.originalColors={colors:RGraph.SVG.arrayClone(prop.colors),backgroundGridColor:RGraph.SVG.arrayClone(prop.backgroundGridColor),highlightFill:RGraph.SVG.arrayClone(prop.highlightFill),backgroundColor:RGraph.SVG.arrayClone(prop.backgroundColor)}}
var colors=prop.colors;if(colors){for(var i=0;i<colors.length;++i){colors[i]=RGraph.SVG.parseColorLinear({object:this,color:colors[i]});}}
prop.backgroundGridColor=RGraph.SVG.parseColorLinear({object:this,color:prop.backgroundGridColor});prop.highlightFill=RGraph.SVG.parseColorLinear({object:this,color:prop.highlightFill});prop.backgroundColor=RGraph.SVG.parseColorLinear({object:this,color:prop.backgroundColor});};this.drawLabelsAbove=function()
{if(prop.labelsAbove){var total=0;for(var i=0;i<this.coords.length;++i){var num=this.data[i],total=total+num;if(typeof num==='number'||RGraph.SVG.isNull(num)){if(RGraph.SVG.isNull(num)){num=total;}
var str=RGraph.SVG.numberFormat({object:this,num:num.toFixed(prop.labelsAboveDecimals),prepend:typeof prop.labelsAboveUnitsPre==='string'?prop.labelsAboveUnitsPre:null,append:typeof prop.labelsAboveUnitsPost==='string'?prop.labelsAboveUnitsPost:null,point:typeof prop.labelsAbovePoint==='string'?prop.labelsAbovePoint:null,thousand:typeof prop.labelsAboveThousand==='string'?prop.labelsAboveThousand:null,formatter:typeof prop.labelsAboveFormatter==='function'?prop.labelsAboveFormatter:null});if(prop.labelsAboveSpecific&&prop.labelsAboveSpecific.length&&(typeof prop.labelsAboveSpecific[i]==='string'||typeof prop.labelsAboveSpecific[i]==='number')){str=prop.labelsAboveSpecific[i];}else if(prop.labelsAboveSpecific&&prop.labelsAboveSpecific.length&&typeof prop.labelsAboveSpecific[i]!=='string'&&typeof prop.labelsAboveSpecific[i]!=='number'){continue;}
var x=parseFloat(this.coords[i].element.getAttribute('x'))+parseFloat(this.coords[i].element.getAttribute('width')/2)+prop.labelsAboveOffsetx;if(this.data[i]>=0){var y=parseFloat(this.coords[i].element.getAttribute('y'))-7+prop.labelsAboveOffsety;var valign=prop.labelsAboveValign;}else{var y=parseFloat(this.coords[i].element.getAttribute('y'))+parseFloat(this.coords[i].element.getAttribute('height'))+7-prop.labelsAboveOffsety;var valign=prop.labelsAboveValign==='top'?'bottom':'top';}
if(i===(this.coords.length-1)){var font=prop.labelsAboveLastFont||prop.labelsAboveFont||prop.textFont,color=prop.labelsAboveLastColor||prop.labelsAboveColor||prop.textColor,background=prop.labelsAboveLastBackground||prop.labelsAboveBackground||null,padding=(typeof prop.labelsAboveLastBackgroundPadding==='number'?prop.labelsAboveLastBackgroundPadding:prop.labelsAboveBackgroundPadding)||0;if(typeof prop.labelsAboveLastSize==='number'){var size=prop.labelsAboveLastSize;}else if(typeof prop.labelsAboveSize==='number'){var size=prop.labelsAboveSize;}else{var size=prop.textBold;}
if(typeof prop.labelsAboveLastBold==='boolean'){var bold=prop.labelsAboveLastBold;}else if(typeof prop.labelsAboveBold==='boolean'){var bold=prop.labelsAboveBold;}else{var bold=prop.textBold;}
if(typeof prop.labelsAboveLastItalic==='boolean'){var italic=prop.labelsAboveLastItalic;}else if(typeof prop.labelsAboveItalic==='boolean'){var italic=prop.labelsAboveItalic;}else{var italic=prop.textItalic;}}else{var font=prop.labelsAboveFont||prop.textFont,size=typeof prop.labelsAboveSize==='number'?prop.labelsAboveSize:prop.textSize,color=prop.labelsAboveColor||prop.textColor,background=prop.labelsAboveBackground||null,padding=prop.labelsAboveBackgroundPadding||0;if(typeof prop.labelsAboveBold==='boolean'){var bold=prop.labelsAboveBold;}else{var bold=prop.textBold;}
if(typeof prop.labelsAboveItalic==='boolean'){var italic=prop.labelsAboveItalic;}else{var italic=prop.textItalic;}}
RGraph.SVG.text({object:this,parent:this.svg.all,tag:'labels.above',text:str,x:x,y:y,halign:prop.labelsAboveHalign,valign:valign,font:font,size:size,bold:bold,italic:italic,color:color,background:background,padding:padding});}}}};this.on=function(type,func)
{if(type.substr(0,2)!=='on'){type='on'+type;}
RGraph.SVG.addCustomEventListener(this,type,func);return this;};this.exec=function(func)
{func(this);return this;};this.removeHighlight=function()
{var highlight=RGraph.SVG.REG.get('highlight');if(highlight&&highlight.parentNode){highlight.parentNode.removeChild(highlight);}
RGraph.SVG.REG.set('highlight',null);};this.grow=function()
{var opt=arguments[0]||{},frames=opt.frames||30,frame=0,obj=this,data=[],height=null,seq=0;return this;};this.wave=function()
{return this;};for(i in conf.options){if(typeof i==='string'){this.set(i,conf.options[i]);}}};return this;})(window,document);