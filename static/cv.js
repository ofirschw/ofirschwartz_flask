fetch('https://reqres.in/api/users?page=2').then(
    response => response.json()
).then(
    responseJSON => createUserList(responseJSON.data)
)
    .catch(
        err =>console.log(err)
    );


function createUserList(users){
    console.log(users);
    const cMain = document.querySelector("main");
    for(let user of users){
       const section= document.createElement('section') ;
       section.innerHTML = `
           <div>
             ${user.first_name} ${user.last_name}
              <br>
              <a href="mailto:${user.email}">Send email</a>
           </div> ` ;
        cMain.appendChild(section);
    }
}












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
