function Readfile(filename) {
    //ajax request
     
    $.ajax({
        url: '/logreader/',
        data: {'name':filename},
        dataType: "json",
        success: function(filedata) {
            data = filedata.data;

            // Clear the logs
            $('#logs').text('');
            for(var i in data){
                var txt = document.createElement("p");  // Create with DOM
                txt.innerHTML = data[i];
                document.getElementById('logs').appendChild(txt);                   
            }    
        },
        failure: function() {
            $('#logs').text('');
            var txt = document.createElement("p");  // Create with DOM
            txt.innerHTML = 'Log Files Not Available !';
            document.getElementById('logs').appendChild(txt);
        }
    });
}