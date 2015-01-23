var pages_loaded = [];
var highlighter;
var initialDoc;
var path = '';
var doc_posts = '/p/list/'+cluster_id+'/';
function retrieveAnnotations(){
	var xmlhttp=new XMLHttpRequest();
	xmlhttp.open("GET","p/pdf/"+cluster_id+"/",true);
	xmlhttp.send();
	xmlhttp.onreadystatechange = function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			annotation_data = JSON.parse(xmlhttp.responseText)
			highlighter.removeAllHighlights();
			len = pages_loaded.length;
			console.log(pages_loaded.length);
			for(var j=0; j<len; j++){
				loadAnnotationsForPage(pages_loaded[j]);
			}
		}
	}
}
window.onload = function() {
	rangy.init();

	highlighter = rangy.createHighlighter();

	highlighter.addClassApplier(rangy.createCssClassApplier("post", {
		ignoreWhiteSpace: true,
		tagNames: ["span", "a"]
	}));
	highlighter.addClassApplier(rangy.createCssClassApplier("temp", {
	}));
	annotation_data=null;
	retrieveAnnotations();
};
//get annotation data
function getSelectionText() {
	var text = "";
	if (window.getSelection) {
		text = window.getSelection().toString();
	} else if (document.selection && document.selection.type != "Control") {
		text = document.selection.createRange().text;
	}
	return text;
}

function newPost(containerNum){
	var context = getSelectionText();
	if (context.length>0){
		var highlighterTemp = rangy.createHighlighter();
		highlighterTemp.addClassApplier(rangy.createCssClassApplier("post", {
		}));
		var temp = highlighter.highlightSelection("temp",{containerElementId:'pageContainer'+containerNum});
		if (temp == null){
			alert("Intersects with existing range, please add post to the existing range or to a new non-intersecting range");
			return;
		}

		highlighterTemp.highlightSelection("post",{containerElementId:'pageContainer'+containerNum});

		console.log(highlighter.serialize());
		path = '/p/new/post?cluster='+cluster_id+'&annotated_text='+context+'&serialized_version='+highlighterTemp.serialize()+'&page_num='+containerNum;
		parent.window.frames['post_pane'].location = path;
	}else{
		if(parent.window.frames['post_pane'].location.pathname != doc_posts){
		parent.window.frames['post_pane'].location = doc_posts;
		}
	}
	
}
function pageLoadedCallback(pageNum){
	document.getElementById('pageContainer'+pageNum).addEventListener("mouseup",function() {
			newPost(pageNum);
			});
	loadAnnotationsForPage(pageNum);

}
function loadAnnotationsForPage(pageNum){
	if(annotation_data==null){
		console.log("Annotations not loaded");
	}

	for(var i=0;i<annotation_data.length;i++){
		if(annotation_data[i].page_num == pageNum){
			console.log(annotation_data[i].page_num);
			var link_path = '/p/'+annotation_data[i].post;
			highlighter.addClassApplier(rangy.createCssClassApplier("post", {
				elementTagName: "a",
				elementProperties: {
					href:"javascript:openPost('"+link_path+"');" 
				}
				
			}));
			highlighter.deserialize(annotation_data[i].serialized_version);
		}
	}
	pages_loaded.push(pageNum);
}
function openPost(link_path){
	parent.window.frames['post_pane'].location = link_path;
}

/*window.onload = function() {


	rangy.init();

	highlighter = rangy.createHighlighter();

	highlighter.addClassApplier(rangy.createCssClassApplier("post", {
		ignoreWhiteSpace: true,
		tagNames: ["span", "a"]
	}));

	highlighter.addClassApplier(rangy.createCssClassApplier("note", {
		ignoreWhiteSpace: true,
		elementTagName: "a",
		elementProperties: {
			href: "#",
			onclick: function() {
				var highlight = highlighter.getHighlightForElement(this);
				if (window.confirm("Delete this note (ID " + highlight.id + ")?")) {
					highlighter.removeHighlights( [highlight] );
				}
				return false;
			}
		}
		}
	));
	/*var annotationLoaderTimer = setInterval(function(){
		//var iframe = document.getElementById('pdf_viewer');
		//var innerDoc = document.contentDocument || document.contentWindow.document;
		//console.log(innerDoc);

		console.log(document.getElementById('viewer').children);
		if(document.getElementById('viewer').children>0){
			pdfLoadedCallback();
			clearInterval(annotationLoaderTimer);
			console.log('oho');
		}
		console.log('aha');
	},
	200);*/


	/*if (serializedHighlights) {
		highlighter.deserialize(serializedHighlights);
	}*/
//};

	/*highlighter.addClassApplier(rangy.createCssClassApplier("note", {
		ignoreWhiteSpace: true,
		elementTagName: "a",
		elementProperties: {
			href: "#",
			onclick: function() {
				var highlight = highlighter.getHighlightForElement(this);
				if (window.confirm("Delete this note (ID " + highlight.id + ")?")) {
					highlighter.removeHighlights( [highlight] );
				}
				return false;
			}
		}
		}
	));*/

