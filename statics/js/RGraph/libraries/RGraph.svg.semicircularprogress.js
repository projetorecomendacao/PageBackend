
RGraph=window.RGraph||{isRGraph:true};RGraph.SVG=RGraph.SVG||{};(function(win,doc,undefined)
{var RG=RGraph;RGraph.SVG.SemiCircularProgress=function(conf)
{this.set=function(name,value)
{if(arguments.length===1&&typeof name==='object'){for(i in arguments[0]){if(typeof i==='string'){name=ret.name;value=ret.value;this.set(name,value);}}}else{var ret=RGraph.SVG.commonSetter({object:this,name:name,value:value});name=ret.name;value=ret.value;this.properties[name]=value;if(name==='colors'){this.originalColors=RGraph.SVG.arrayClone(value);this.colorsParsed=false;}}
return this;};this.get=function(name)
{return this.properties[name];};this.min=RGraph.SVG.stringsToNumbers(conf.min);this.max=RGraph.SVG.stringsToNumbers(conf.max);this.value=RGraph.SVG.stringsToNumbers(conf.value);this.id=conf.id;this.uid=RGraph.SVG.createUID();this.container=document.getElementById(this.id);this.layers={};this.svg=RGraph.SVG.createSVG({object:this,container:this.container});this.isRGraph=true;this.width=Number(this.svg.getAttribute('width'));this.height=Number(this.svg.getAttribute('height'));this.data=conf.data;this.type='semicircularprogress';this.colorsParsed=false;this.originalColors={};this.gradientCounter=1;this.nodes={};this.shadowNodes=[];if(this.value>this.max)this.value=this.max;if(this.value<this.min)this.value=this.min;RGraph.SVG.OR.add(this);this.container.style.display='inline-block';this.properties={centerx:null,centery:null,radius:null,width:60,marginLeft:35,marginRight:35,marginTop:35,marginBottom:35,backgroundStrokeLinewidth:0.25,backgroundStroke:'gray',backgroundFill:'Gradient(white:#aaa)',backgroundFillOpacity:0.25,colors:['#0c0'],textColor:'black',textFont:'Arial, Verdana, sans-serif',textSize:12,textBold:false,textItalic:false,scaleUnitsPre:'',scaleUnitsPost:'',scalePoint:'.',scaleThousand:',',scaleDecimals:0,scaleFormatter:null,labelsMin:true,labelsMinSpecific:null,labelsMinPoint:null,labelsMinThousand:null,labelsMinFormatter:null,labelsMinFont:null,labelsMinSize:null,labelsMinBold:null,labelsMinItalic:null,labelsMinColor:null,labelsMinDecimals:null,labelsMinUnitsPre:null,labelsMinUnitsPost:null,labelsMax:true,labelsMaxSpecific:null,labelsMaxPoint:null,labelsMaxThousand:null,labelsMaxFormatter:null,labelsMaxFont:null,labelsMaxSize:null,labelsMaxBold:null,labelsMaxItalic:null,labelsMaxColor:null,labelsMaxDecimals:null,labelsMaxUnitsPre:null,labelsMaxUnitsPost:null,labelsCenter:true,labelsCenterSpecific:null,labelsCenterPoint:null,labelsCenterThousand:null,labelsCenterFormatter:null,labelsCenterFont:null,labelsCenterSize:40,labelsCenterBold:true,labelsCenterItalic:null,labelsCenterColor:null,labelsCenterDecimals:null,labelsCenterUnitsPre:null,labelsCenterUnitsPost:null,linewidth:0,tooltips:null,tooltipsOverride:null,tooltipsEffect:'fade',tooltipsCssClass:'RGraph_tooltip',tooltipsEvent:'click',highlightStroke:'rgba(0,0,0,0)',highlightFill:'rgba(255,255,255,0.7)',highlightLinewidth:1,title:'',titleX:null,titleY:null,titleHalign:'center',titleValign:null,titleFont:null,titleSize:null,titleColor:null,titleBold:null,titleItalic:null,titleSubtitle:null,titleSubtitleSize:null,titleSubtitleColor:'#aaa',titleSubtitleFont:null,titleSubtitleBold:null,titleSubtitleItalic:null};RGraph.SVG.getGlobals(this);if(RGraph.SVG.FX&&typeof RGraph.SVG.FX.decorate==='function'){RGraph.SVG.FX.decorate(this);}
var prop=this.properties;this.draw=function()
{RGraph.SVG.fireCustomEvent(this,'onbeforedraw');this.nodes={};this.width=Number(this.svg.getAttribute('width'));this.height=Number(this.svg.getAttribute('height'));RGraph.SVG.createDefs(this);this.graphWidth=this.width-prop.marginLeft-prop.marginRight;this.graphHeight=this.height-prop.marginTop-prop.marginBottom;this.centerx=(this.graphWidth/2)+prop.marginLeft;this.centery=this.height-prop.marginBottom;this.radius=Math.min(this.graphWidth/2,this.graphHeight);this.centerx=typeof prop.centerx==='number'?prop.centerx:this.centerx;this.centery=typeof prop.centery==='number'?prop.centery:this.centery;this.radius=typeof prop.radius==='number'?prop.radius:this.radius;if(typeof prop.radius==='string'&&prop.radius.match(/^\+|-\d+$/))this.radius+=parseFloat(prop.radius);if(typeof prop.centerx==='string'&&prop.centerx.match(/^\+|-\d+$/))this.centerx+=parseFloat(prop.centerx);if(typeof prop.centery==='string'&&prop.centery.match(/^\+|-\d+$/))this.centery+=parseFloat(prop.centery);this.progressWidth=prop.width||(this.radius/3);RGraph.SVG.resetColorsToOriginalValues({object:this});this.parseColors();this.path=this.drawMeter();RGraph.SVG.drawTitle(this);this.drawLabels();RGraph.SVG.attribution(this);if(!RGraph.SVG.isNull(prop.tooltips)&&prop.tooltips[0]){var obj=this;this.path.addEventListener(prop.tooltipsEvent,function(e)
{obj.removeHighlight();RGraph.SVG.tooltip({object:obj,index:0,group:null,sequentialIndex:0,text:prop.tooltips[0],event:e});obj.highlight(e.target);},false);this.path.addEventListener('mousemove',function(e)
{e.target.style.cursor='pointer'},false);}
var obj=this;document.body.addEventListener('mousedown',function(e)
{obj.removeHighlight();},false);RGraph.SVG.fireCustomEvent(this,'ondraw');return this;};this.drawMeter=function()
{var path=RGraph.SVG.TRIG.getArcPath({cx:this.centerx,cy:this.centery,r:this.radius,start:RGraph.SVG.TRIG.PI+RGraph.SVG.TRIG.HALFPI,end:RGraph.SVG.TRIG.HALFPI,anticlockwise:false});var path2=RGraph.SVG.TRIG.getArcPath({cx:this.centerx,cy:this.centery,r:this.radius-this.progressWidth,end:RGraph.SVG.TRIG.PI+RGraph.SVG.TRIG.HALFPI,start:RGraph.SVG.TRIG.HALFPI,anticlockwise:true,moveto:false});var background=RGraph.SVG.create({svg:this.svg,type:'path',parent:this.svg.all,attr:{d:path+" L "+(this.centerx+this.radius-this.progressWidth)+" "+this.centery+path2+" L "+(this.centerx-this.radius)+" "+this.centery,fill:prop.backgroundFill||prop.colors[0],'stroke-width':0,'fill-opacity':prop.backgroundFillOpacity}});this.nodes.background=background;var angle=((this.value-this.min)/(this.max-this.min))*RGraph.SVG.TRIG.PI;angle-=RGraph.SVG.TRIG.HALFPI;var path=RGraph.SVG.TRIG.getArcPath({cx:this.centerx,cy:this.centery,r:this.radius,start:RGraph.SVG.TRIG.PI+RGraph.SVG.TRIG.HALFPI,end:angle,anticlockwise:false});var path2=RGraph.SVG.TRIG.getArcPath({cx:this.centerx,cy:this.centery,r:this.radius-this.progressWidth,start:angle,end:angle,anticlockwise:false,array:true});var path3=RGraph.SVG.TRIG.getArcPath({cx:this.centerx,cy:this.centery,r:this.radius-this.progressWidth,start:angle,end:RGraph.SVG.TRIG.PI+RGraph.SVG.TRIG.HALFPI,anticlockwise:true,moveto:false});var group=RGraph.SVG.create({svg:this.svg,type:'g',parent:this.svg.all,attr:{id:'indicator-bar-group'}});var path=RGraph.SVG.create({svg:this.svg,type:'path',parent:group,attr:{d:path+" L{1} {2} ".format(path2[1],path2[2])+path3+' z',fill:prop.colors[0],stroke:'black','stroke-width':prop.linewidth}});this.nodes.barGroup=group;this.nodes.bar=path;var backgroundStroke=RGraph.SVG.create({svg:this.svg,type:'path',parent:this.svg.all,attr:{d:this.nodes.background.getAttribute('d'),stroke:prop.backgroundStroke,fill:'rgba(0,0,0,0)','stroke-width':prop.backgroundStrokeLinewidth,'stroke-linecap':'square'},style:{pointerEvents:'none'}});this.nodes.backgroundStroke=backgroundStroke;return path;};this.drawLabels=function()
{if(prop.labelsMin){var min=RGraph.SVG.numberFormat({object:this,num:this.min.toFixed(typeof prop.labelsMinDecimals==='number'?prop.labelsMinDecimals:prop.scaleDecimals),prepend:typeof prop.labelsMinUnitsPre==='string'?prop.labelsMinUnitsPre:prop.scaleUnitsPre,append:typeof prop.labelsMinUnitsPost==='string'?prop.labelsMinUnitsPost:prop.scaleUnitsPost,point:typeof prop.labelsMinPoint==='string'?prop.labelsMinPoint:prop.scalePoint,thousand:typeof prop.labelsMinThousand==='string'?prop.labelsMinThousand:prop.scaleThousand,formatter:typeof prop.labelsMinFormatter==='function'?prop.labelsMinFormatter:prop.scaleFormatter});var text=RGraph.SVG.text({object:this,parent:this.svg.all,tag:'labels.min',text:typeof prop.labelsMinSpecific==='string'?prop.labelsMinSpecific:min,x:this.centerx-this.radius+(this.progressWidth/2),y:this.centery+5+prop.backgroundStrokeLinewidth,valign:'top',halign:'center',font:prop.labelsMinFont||prop.textFont,size:typeof prop.labelsMinSize==='number'?prop.labelsMinSize:prop.textSize,bold:typeof prop.labelsMinBold==='boolean'?prop.labelsMinBold:prop.textBold,italic:typeof prop.labelsMinItalic==='boolean'?prop.labelsMinItalic:prop.textItalic,color:prop.labelsMinColor||prop.textColor});this.nodes.labelsMin=text;}
if(prop.labelsMax){var max=RGraph.SVG.numberFormat({object:this,num:this.max.toFixed(typeof prop.labelsMaxDecimals==='number'?prop.labelsMaxDecimals:prop.scaleDecimals),prepend:typeof prop.labelsMaxUnitsPre==='string'?prop.labelsMaxUnitsPre:prop.scaleUnitsPre,append:typeof prop.labelsMaxUnitsPost==='string'?prop.labelsMaxUnitsPost:prop.scaleUnitsPost,point:typeof prop.labelsMaxPoint==='string'?prop.labelsMaxPoint:prop.scalePoint,thousand:typeof prop.labelsMaxThousand==='string'?prop.labelsMaxThousand:prop.scaleThousand,formatter:typeof prop.labelsMaxFormatter==='function'?prop.labelsMaxFormatter:prop.scaleFormatter});var text=RGraph.SVG.text({object:this,parent:this.svg.all,tag:'labels.max',text:typeof prop.labelsMaxSpecific==='string'?prop.labelsMaxSpecific:max,x:this.centerx+this.radius-(this.progressWidth/2),y:this.centery+5+prop.backgroundStrokeLinewidth,valign:'top',halign:'center',font:prop.labelsMaxFont||prop.textFont,size:typeof prop.labelsMaxSize==='number'?prop.labelsMaxSize:prop.textSize,bold:typeof prop.labelsMaxBold==='boolean'?prop.labelsMaxBold:prop.textBold,italic:typeof prop.labelsMaxItalic==='boolean'?prop.labelsMaxItalic:prop.textItalic,color:prop.labelsMaxColor||prop.textColor});this.nodes.labelsMax=text;}
if(prop.labelsCenter){var center=RGraph.SVG.numberFormat({object:this,num:this.value.toFixed(typeof prop.labelsCenterDecimals==='number'?prop.labelsCenterDecimals:prop.scaleDecimals),prepend:typeof prop.labelsCenterUnitsPre==='string'?prop.labelsCenterUnitsPre:prop.scaleUnitsPre,append:typeof prop.labelsCenterUnitsPost==='string'?prop.labelsCenterUnitsPost:prop.scaleUnitsPost,point:typeof prop.labelsCenterPoint==='string'?prop.labelsCenterPoint:prop.scalePoint,thousand:typeof prop.labelsCenterThousand==='string'?prop.labelsCenterThousand:prop.scaleThousand,formatter:typeof prop.labelsCenterFormatter==='function'?prop.labelsCenterFormatter:prop.scaleFormatter});var text=RGraph.SVG.text({object:this,parent:this.svg.all,tag:'labels.center',text:typeof prop.labelsCenterSpecific==='string'?prop.labelsCenterSpecific:center,x:this.centerx,y:this.centery,valign:'bottom',halign:'center',font:prop.labelsCenterFont||prop.textFont,size:typeof prop.labelsCenterSize==='number'?prop.labelsCenterSize:prop.textSize,bold:typeof prop.labelsCenterBold==='boolean'?prop.labelsCenterBold:prop.textBold,italic:typeof prop.labelsCenterItalic==='boolean'?prop.labelsCenterItalic:prop.textItalic,color:prop.labelsCenterColor||prop.textColor});this.nodes.labelsCenter=text;}};this.highlight=function(segment)
{this.removeHighlight();var highlight=RGraph.SVG.create({svg:this.svg,type:'path',parent:this.nodes.barGroup,attr:{d:this.path.getAttribute('d'),fill:prop.highlightFill,stroke:prop.highlightStroke,'stroke-width':prop.highlightLinewidth},style:{pointerEvents:'none'}});RGraph.SVG.REG.set('highlight',highlight);var obj=this;document.body.addEventListener('mousedown',function(e)
{obj.removeHighlight();},false);};this.removeHighlight=function()
{var highlight=RGraph.SVG.REG.get('highlight');if(highlight){highlight.parentNode.removeChild(highlight);highlight=null;}};this.parseColors=function()
{if(!Object.keys(this.originalColors).length){this.originalColors={colors:RGraph.SVG.arrayClone(prop.colors),highlightFill:RGraph.SVG.arrayClone(prop.highlightFill),backgroundColor:RGraph.SVG.arrayClone(prop.backgroundColor)}}
var colors=prop.colors;if(colors){for(var i=0;i<colors.length;++i){colors[i]=RGraph.SVG.parseColorLinear({object:this,color:colors[i],start:this.centerx-this.radius,end:this.centerx+this.radius,direction:'horizontal'});}}
prop.highlightFill=RGraph.SVG.parseColorLinear({object:this,color:prop.highlightFill,start:prop.marginLeft,end:this.width-prop.marginRight,direction:'horizontal'});prop.backgroundColor=RGraph.SVG.parseColorLinear({object:this,color:prop.backgroundColor,start:prop.marginLeft,end:this.width-prop.marginRight,direction:'horizontal'});};this.grow=function()
{var opt=arguments[0]||{},frames=opt.frames||30,frame=0,obj=this,value=opt.value;value=this.value;this.draw();var iterate=function()
{var multiplier=frame/frames
obj.value=value*multiplier;RGraph.SVG.redraw();if(frame++<frames){RGraph.SVG.FX.update(iterate);}else if(opt.callback){obj.value=value;RGraph.SVG.redraw();(opt.callback)(obj);}};iterate();return this;};this.on=function(type,func)
{if(type.substr(0,2)!=='on'){type='on'+type;}
RGraph.SVG.addCustomEventListener(this,type,func);return this;};this.exec=function(func)
{func(this);return this;};this.removeHighlight=function()
{var highlight=RGraph.SVG.REG.get('highlight');if(highlight&&highlight.parentNode){highlight.parentNode.removeChild(highlight);}
RGraph.SVG.REG.set('highlight',null);};for(i in conf.options){if(typeof i==='string'){this.set(i,conf.options[i]);}}};return this;})(window,document);