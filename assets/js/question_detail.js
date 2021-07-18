function clicked(ans){
    if(ans === "True") {
        document.getElementById("sub").disabled = false;
    }else if(ans === "False"){
        document.getElementById("sub").disabled = true;
    }
}