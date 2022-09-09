
let group = [];

form.addEventListener('submit',function(event){
    event.preventDefault();

    // const checkBox = document.getElementById('agreement')   
    // console.log(typeof(checkBox.value))

    // if (checkBox.value == "") {
    //     alert("Didn't check the box.");
    //     return console.log("CheckBox == False")
    // }
    let person = {
        first: "",
        last: "",
        num: "",
        email: "",
        pass: ""
    };
    const firstName = document.getElementById('firstName');
    const lastName = document.getElementById('lastName');
    const phoneNum = document.getElementById('phoneNum');
    const email = document.getElementById('email');
    const passWord = document.getElementById('pass');

    console.log(firstName, lastName, phoneNum, email, passWord);
    


    person.first = firstName.value;
    person.last = lastName.value;
    person.num = phoneNum.value;
    person.email = email.value;
    person.pass = passWord.value;
    console.log(person);

    group.push(person);
    console.log(group);

    let name = firstName.value +' '+ lastName.value;
        alert(name + " has been added to the group");

    form.reset();
    }
)