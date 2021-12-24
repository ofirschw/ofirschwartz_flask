
function func_name() {
    console.log('ofir schwartz');
}


function myFunction() {
    const name = document.getElementById("check");
    if (!name.checkValidity()) {
        document.getElementById("first").innerHTML = name.validationMessage;
    } else {
        document.getElementById("first").innerHTML = "Input your name is OK";
    }

    const text = document.getElementById("subject");
    if (!text.checkValidity()) {
        document.getElementById("second").innerHTML = text.validationMessage;
    } else {
        document.getElementById("second").innerHTML = "Input of your subject OK";
    }


}
