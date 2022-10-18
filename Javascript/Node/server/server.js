let axios = reqiure('axios').default;
let http = require('http');
// this is the numerical address for localhost
const host = '127.0.0.1'
const port = 8080;
const server = http.createServer((req,res)=>{
    res.statusCode = 200;
    res.setHeader('Content-Type','text/plain');
    res.end('You have reached my server');
});

server.listen(port,host,()=>{
    console.log(`Server is running at http:${host}:${port}`)
})
