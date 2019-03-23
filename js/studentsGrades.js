function loadGrades(){
    /* DB will be set up as, each student has a table
    num | exam | quiz | assignment
    -------------------------------
    1   |  56  | 34    | 90
    2   |  56  | 34    | 90
    3   |  56  | 34    | 90
    */

    //find student table

    //filling.
    for(let i = 0; i<11;i++){// loop till end of primary keys 
        var div = document.createElement('p');
        div.innerHTML = "Quiz "+(i+1)+" - "+"54";//put contents of feedback here// replace 54 with db
        if(i<4) document.getElementById('quizMark').append(div);
        var div = document.createElement('p');
        div.innerHTML = "Assignment "+(i+1)+" - "+"54";
        if(i<3) document.getElementById('assignmentMarks').append(div);

        var div = document.createElement('p');
        
        if(i===0) {
            div.innerHTML = "Midterm "+" - "+"54";
            document.getElementById('examMark').append(div);
        }
        else if(i===1){
            div.innerHTML = "Final"+" - "+"54";
            document.getElementById('examMark').append(div);
        }
    }

    
}