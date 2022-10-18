'use strict';

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up (queryInterface, Sequelize) {
     await queryInterface.bulkInsert('students', [
      {
       first_name: 'John',
       last_name: 'Doe',
       birthdate: '1998-08-14',
       grade: 87,
       createdAt: new Date(),
       updatedAt: new Date()
     },
    {
      first_name: 'Jane',
      last_name: 'Doe',
      birthdate: '1998-12-14',
      grade: 98,
      createdAt: new Date(),
      updatedAt: new Date()
    },
    {
      first_name: 'Lala',
      last_name: 'Schmooney',
      birthdate: '1990-01-01',
      grade: 82,
      createdAt: new Date(),
      updatedAt: new Date()
    }
    ], {});
  },

  async down (queryInterface, Sequelize) {
     await queryInterface.bulkDelete('students', null, {});
  }
};
