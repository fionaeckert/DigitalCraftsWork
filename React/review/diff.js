const counter = () => {
    let count = 0; 
    count = count + 1

    return count
}

let result = counter()
result = counter ()


class Count {
    constructor(){
        this.count = 0;
        }

    increement(){
        this.count++

        return this,count
    }
}

let count = new Count();
let result2 = count.increment() // 1
result2 = count.increment() //2

let count2 = new Count () //0