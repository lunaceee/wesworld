var webpack = require('webpack');
var path = require('path');

var BUILD_DIR = path.resolve(__dirname, 'front_end/public');
var APP_DIR = path.resolve(__dirname, 'front_end/src');

var config = {
  entry: APP_DIR + '/App.js',
  output: {
    path: BUILD_DIR,
    filename: 'bundle.js'
  }
};

module.exports = config;
