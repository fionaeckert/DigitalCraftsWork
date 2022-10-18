const e = require('express');
const logger = require('./logger');
const express = require('express');
const app = express();
const { Sequelize } = require('sequelize');
const { students } = require('./models')

const sequelize = new Sequelize('postgres://fionaeckert@localhost:5432/digitalcrafts_cohort')

app.use(express.json())

app.all('*', (req, res, next) => {
    logger.info({
        "time" : new Date(),
        "path" : req.path,
        "body" : req.body,
        "method" : req.method
    })
    next()
})

// Get all students from the database
app.get('/', async (req, res) => {
    if (Object.keys(req.body).length == 0){
        const classroom = await students.findAll();
        console.log(classroom)
        res.send(classroom)
    }
    else {
        logger.error({
            "time" : new Date(),
            "message" : `User tried to pass a body, '${req.body}', into GET method.`,
            "path" : req.path,
            "method" : req.method
        })
        res.send('Bodies not allowed in GET request.')
    }
})

app.get('/students', async (req, res) => {
    if (Object.keys(req.body).length == 0){
        const student = await students.findOne({
            where: {
                id: req.query.id
            }
        });
        console.log(student)
        if (student === null){
            logger.error({
                "time" : new Date(),
                "message" : `User tried to search for a student with ID ${req.query.id}`,
                "path" : req.path,
                "method" : req.method
            })
            res.send('Student not found.')
        }
        else {
            res.send(student)
        }
    }
    else {
        logger.error({
            "time" : new Date(),
            "message" : `User tried to pass a body, '${req.body}', into GET method.`,
            "path" : req.path,
            "method" : req.method
        })
        res.send('Bodies not allowed in GET request.')
    }
})

// Add a student to the database
app.post('/students', async (req, res) => {
    console.log(req.body);
    if (req.body.first_name == null || req.body.last_name == null || req.body.birthdate == null || req.body.grade == null){
        logger.error({
            "time" : new Date(),
            "message" : `User tried to pass a body, '${req.body}', which did not have all required fields.`,
            "path" : req.path,
            "method" : req.method
        })
        res.send('Invalid body submitted.')
    }
    else{
        const student = await students.create({
            first_name: req.body.first_name, 
            last_name: req.body.last_name,
            birthdate: req.body.birthdate,
            grade: req.body.grade
        })
        let receipt = await students.findAll({
            where: {
                first_name: req.body.first_name,
                last_name: req.body.last_name
            }
        })
        res.send(receipt)
    }
})

app.put('/students/:id', async (req, res) => {
    const student = await students.findOne({
        where: {
            id: req.params.id
        }
    })
    if (student === null){
        logger.error({
            "time" : new Date(),
            "message" : `User tried to change student with ID ${req.params.id}, which was not found.`,
            "path" : req.path,
            "method" : req.method
        })
        res.send('Student not found.')
    }
    else {
        if (req.body.first_name != null){
            await student.update({
                first_name: req.body.first_name
            })
        }
        if (req.body.last_name != null){
            await student.update({
                last_name: req.body.last_name
            })
        }
        if (req.body.birthdate != null){
            await student.update({
                birthdate: req.body.birthdate
            })
        }
        if (req.body.grade != null){
            await student.update({
                grade: req.body.grade
            })
        }
        if (req.body.first_name == null && req.body.last_name == null && req.body.birthdate == null && req.body.grade == null){
            logger.error({
                "time" : new Date(),
                "message" : `User tried to pass a body, '${req.body}', which contained no valid changes.`,
                "path" : req.path,
                "method" : req.method
            })
            res.send('No valid changes where passed to the body.')
        }
        else{
            res.send(student)
        }
    }
})

app.delete('/students/:id', async (req, res) => {
    await students.destroy({
        where: {
          id: req.params.id
        }
      })
    if (student === null){
        logger.error({
            "time" : new Date(),
            "message" : `User tried to delete student with ID '${req.params.id}', which was not found.`,
            "path" : req.path,
            "method" : req.method
        })
        res.send('Student not found.')
    }
    let student = await students.findOne({
        where: {
            id: req.params.id
        }
    })
    if (student === null){
        res.send(req.params.id)
    }
    else {
        logger.error({
            "time" : new Date(),
            "message" : `User tried to delete student with ID '${req.params.id}', which was not properly deleted.`,
            "path" : req.path,
            "method" : req.method
        })
        res.send('Not properly deleted.')
    }
})

app.listen(3000, async () => {
    console.log('Server is running on http://localhost:3000');

    try {
        await sequelize.authenticate();
        console.log('Connection has been established successfully.');
      } catch (error) {
        console.error('Unable to connect to the database:', error);
      }
});