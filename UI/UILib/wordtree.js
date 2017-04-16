google.charts.load('current', {packages:['wordtree']});

function Drawtree(word, data){

	destinations = data[word]
	var datatable = [['Phrases']];
	for(var i in destinations){
		var node = [];
		node.push(word+" "+destinations[i]);
		datatable.push(node);
	}
	console.log(datatable)

    var data = google.visualization.arrayToDataTable(datatable);

    var options = {
      wordtree: {
        format: 'implicit',
        word: word
      }
    };

    var chart = new google.visualization.WordTree(document.getElementById('wordtree'));
    chart.draw(data, options);
}