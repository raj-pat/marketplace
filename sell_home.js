function getFormData(){
    var data = [] ; 
    var fill = "";
    for(i =0 ; i < 7 ;i++)
    {
        data[i] = document.getElementById("sell_home").elements[i].value;
        fill += data[i] + " "
    } 
    document.getElementById("fill").innerHTML = fill; 
}
function browse(){
document.getElementById("imageFile").click();
}