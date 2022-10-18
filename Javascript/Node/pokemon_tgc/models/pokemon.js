'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class pokemon extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  pokemon.init({
    id: { 
      type: DataTypes.STRING,
      primaryKey: true
    },
    name: DataTypes.STRING,
    level: DataTypes.INTEGER,
    type: DataTypes.STRING,
    hp: DataTypes.INTEGER,
    images: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'pokemon',
    freezeTableName:true
  });
  return pokemon;
};