// Counter App
import React, { Component } from 'react'

export class Counter extends Component {
    // A constructor builds the template to define our class
    constructor(props) {
    // Super() calls the parent classes. In this case, the component class is the parent class. Then, it'll take any functions or props from the parent class and pass them to that class.
        super(props)

    //Default state for our counter. A state is a global variable to our component. In our case, it will display how many times a button is clicked

    //The "this" keyword refers to this instance of the class. Ther can be many instances of a single class in an app.
        this.state = {
            count: 0
        };
    }

    //Increment the value of the counter 
    increment = (num) => {
        // WE CANNOT DIRECTLY CHANGE THE VALUES OF THE STATE. WE HAVE TO DO SO USING A SETTER WHICH IS BUILT IN TO THE REACT COMPONENT
        // this.state = this.state 
        this.setState({
            count: this.state.count + num
        })
    }

    render() {
        return (
        <div>
            <span>{ this.props.name }</span>
            <span>{this.state.count}</span>
            <button onClick={() => this.increment(1)}>Add 1</button>
            <button onClick={() => this.increment(10)}>Add 10</button>
            <button onClick={() => this.increment(100)}>Add 100</button>
        </div>
            )
        }
    }
export default Counter