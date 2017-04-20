'use strict';

function Wordfetch(label){
	//Fetch word data
	var label = "<p>Name : <em>"+label+"</em></p>";
	var type = "<p>Type : <em>Word</em></p>";
	$("#Node")
	.html(label+type);
}

function Synsetfetch(label){
	//Fetch synset data
	var label = "<p>Name : <em>"+label+"</em></p>";
	var type = "<p>Type : <em>Synset</em></p>";
	$("#Node")
	.html(label+type);

/*	$.ajax({
    url: '/process_synset/',
    data:{'synset':label},
    dataType:'json',
    success:function(data){
    	console.log(JSON.stringify(data));
    },
    failure:function(){
      sweetAlert("Oops...", "Something went wrong!", "error");
    }
  });*/
	
}

function Includes(biglist, list){
	// See if lists of list contains a list
	for(var i in biglist){
		if(biglist[i].toString() == list.toString())
			return true;
	}
	return false;
}

function Issynset(node){
	// Tells if node a synset or not
	if(~node.indexOf(".")){
		return true;
	}else{
		return false;
	}
}

function Compact(word, data){
	// Clear Early Canvas
	var canvas = document.getElementById('similaritygraph');
	canvas.width = canvas.width;

	// Styling
	var root_font = 'bold 26px Verdana';
	var root_color = '#4169E1';
	var word_color = '#00BFFF';
	var synset_color = '#3CB371';
	var edge_colors = {'W2S':'#f44336','D2S':'#ff9800','S2W':'#009688','S2D':'#e91e63','S2E':'#2196F3','Hypernym':'#795548',
	'Hyponym':'#3f51b5','Meronym':'#9c27b0','Holonym':'#00bcd4','Similar':'#A9A9A9','Entailment':'#4CAF50'};

	// To take analysis data and form graph
	var graph = new Springy.Graph();	// Graph Instance
	var paths = data[word]
	var nodes = {} //Mapping between node names and node objects
	var edges = []
	var addededge = []	//To prevent re-creating same edges again

	//Creating Root Word node
	nodes[word] = graph.newNode({
		label: word,
		color: root_color,
		font: root_font
	});

	// First need to create node instances
	for (var i in paths){
		var path = paths[i]
		for (var j in path){
			var edge = path[j]
			var src = edge[0]
			var dest = edge[3]
			if(nodes[src] == undefined){
				// Key does not exists
				
				// Checking if word or synset
				var color = '';
				if(Issynset(src)){
					color = synset_color;
				}else{
					color = word_color;
				}

				nodes[src] = graph.newNode({
					label: src,
					color: color
				});
			}

			if(nodes[dest] == undefined){
				// Key does not exists
				
				// Checking if word or synset
				var color = '';
				if(Issynset(dest)){
					color = synset_color;
				}else{
					color = word_color;
				}

				nodes[dest] = graph.newNode({
					label: dest,
					color: color
				});
			}

			var edgedata = edge[2]+"<"+edge[1].toString()+">";	
			var srcnode = nodes[edge[0]]
			var destnode = nodes[edge[3]]
			if(!Includes(addededge, edge)){ 
				addededge.push(edge);
				var color = edge_colors[edge[2]];
				graph.newEdge(srcnode, destnode, {label: edgedata, color: color});
			}
		}
	}

	jQuery(function(){		
		var springy = window.springy = jQuery('#similaritygraph').springy({
			graph: graph,
			nodeSelected: function(node){
				var data = node.data;
				if(Issynset(data.label)){
					Synsetfetch(data.label);
				}else{
					Wordfetch(data.label);
				}
			}
		});
	});
}