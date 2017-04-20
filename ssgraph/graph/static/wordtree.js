google.charts.load('current', {packages:['wordtree']});

function Drawtree(word, data){

    setTimeout(Draw, 300, word,data);
}

function Draw(word, data){

    var data = addNodes(word, data[word])
    var options = {
        wordtree: {
        format: 'explicit',
        type: 'suffix'
        }
    };

    var chart = new google.visualization.WordTree(document.getElementById('wordtree'));
    chart.draw(data, options);
}

function addNodes(word, dests){
    var nodeListData = new google.visualization.arrayToDataTable([
          ['id', 'childLabel', 'parent', 'size', { role: 'style' }],
          [0, word, -1, 1, '#009688']
        ]);

    for(var i = 0 ; i < dests.length ; ++i){
        var node = [];
        node.push(i+1,dests[i],0,1,'#2196F3');
        nodeListData.addRow(node);
    }
    return nodeListData
}
