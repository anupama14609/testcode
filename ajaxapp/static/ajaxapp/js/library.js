window.onload = initAll 

var saveBookBtn;

function initAll(){
    saveBookBtn = document.getElementById('add_book');
    saveBookBtn.onclick = saveBook; 
}

function saveBook(){

    var name = document.getElementById('name').value; 
    var price = document.getElementById('price').value; 
    var pages = document.getElementById('pages').value; 

    var url = '/save-book?name='+name+'&price='+price+'&pages='+pages;
    alert(message)

    var req = XMLHttpRequest()
    req.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            
        }
    };
    req.open("GET", url, true);
    req.send();
}
