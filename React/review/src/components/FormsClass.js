import React, { Component } from 'react'

class FormsClass extends Component {
  
  constructor(){
    super()
    this.state = {
      textValue:"",
      isValid: false,
      selectedValue: "Seattle",
      comments: []
    }
  }
  // componentWillMount(){
  //   console.log('component will mount') //only called once, called by React library
  // }

  //best place for an API call
 async componentDidMount(){
    console.log('component did mount') // only called once; called by React library; called after the component is rendered

    let result = await fetch ('https://jsonplaceholder.typicode.com/comments')
    let data = await result.json;
    console.log(data);

    this.setState({
      comments: data
    }, ()=>{

      console.log("current state", this.state.comments);
    })
  }
    handleChange = e => {
      //set state
      console.log(e.target.name)
      let targetType = e.target.type == 'checkbox' ? e.target.checked : e.target.value
      let name = e.target.name

      //value of input field is e.target.value
      //value of checkbox is e.target.checked
      //need to be able to handle both types hence the targetType variable

      this.setState({
        //putting brackets around name tells React to take the value of the name field rather than the field name itself
        [name]: targetType
      })
    }
  render() {
    let {textValue, isValid, selectedValue, comments} = this.state

    return (
      <>

      <h1>{textValue}</h1>
      <h1>{isValid ? "true":"false"}</h1>
      <h1>{selectedValue}</h1>
    
      <form>
        <input type="text" name="textValue" value={textValue} onChange={this.handleChange}/>
        <br />
        <input type="checkbox" name="isValid" value={isValid} onChange={this.handleChange}/>
        <br />
        <select name="selectedValue" value={selectedValue} onChange={this.handleChange}>
        <option value="NewYork">New York</option>
                <option value="Houston">Houston</option>
                <option value="Atlanta">Atlanta</option>
                <option value="Seattle">Seattle</option>
                <option value="Detroit">Detroit</option>
        </select>
      </form>
      <br />
      <br />

      <ul>
      {comments.map(obj =>{
        return <li key={obj.name}>{obj.name}</li>
      })}

      </ul>
      </>
    )
  }
}
export default FormsClass