import React, {useEffect, useState} from 'react'

function App() {
  const [studentList, setStudentList] = useState([])
  useEffect(() => {
    const getData = async() => {
      try{
        let result = await fetch('/api')
        let data = await result.json()

        setStudentList(data)
      }
      catch(error){
        console.log(error)
      }
    }
    getData()
  }, [])
  
  return (
    <>
    <h2>Student Data</h2>

    {studentList.map(studentObj => {
      return <p key={studentObj.id}>{studentObj.name}</p>
    })}
    
    </>
  )
}

export default App
