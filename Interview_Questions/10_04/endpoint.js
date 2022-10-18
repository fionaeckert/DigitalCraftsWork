axios = require('axios')

function endpoint(){
    axios({
        method:'post',
        url: 'http://localhost:3000/newUser',
        Headers:{
            'Content-Type':'application/json'
        },
        data:{
            firstName: JSON.stringify({ firstName: 'firstName' })
        }
    });
}
module.exports = endpoint