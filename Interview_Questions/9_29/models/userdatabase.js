'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class userDatabase extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  userDatabase.init({
    first_name: DataTypes.STRING,
    last_name: DataTypes.STRING,
    state: DataTypes.STRING,
    affected: DataTypes.BOOLEAN
  }, {
    sequelize,
    modelName: 'userDatabase',
  });
  return userDatabase;
};