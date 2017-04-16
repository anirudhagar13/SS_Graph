function Readfile(file){

	//API to read local files
	var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4){
        	// Clear the logs
        	$('#logs').text('');
            if(rawFile.status === 200 || rawFile.status == 0)
            {
            	var lines = rawFile.responseText.split("\n");
            	for(var i in lines){
            		var txt = document.createElement("p");  // Create with DOM
				    txt.innerHTML = lines[i];
				    document.getElementById('logs').appendChild(txt);            		
            	}    
            }
            else{
                var txt = document.createElement("p");  // Create with DOM
                txt.innerHTML = 'Log Files Not Available !';
                document.getElementById('logs').appendChild(txt);
            }
        }
    }
    rawFile.send();
}