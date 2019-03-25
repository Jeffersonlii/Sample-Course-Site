
function loadFeedBack(){
    for(let i = 0; i<11;i++){// loop till database is empty??? 
        var div = document.createElement('p');
        div.innerHTML = i +"   blah blah sample lorem ";//put contents of feedback here
        document.getElementById('feedbacks').prepend(div);
    }
}

function loadGrades(){

}
