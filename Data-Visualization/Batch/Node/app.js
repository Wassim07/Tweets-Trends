const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors')

app.use(cors())
//app.use(express.static(__dirname+'/client'));
app.use(bodyParser.json());

Hashtag =require('./hashtag');

// Connect to Mongoose
mongoose.connect('mongodb://wassimB:123456@ds129540.mlab.com:29540/bigdata');

var db = mongoose.connection;

app.get('/', (req, res) => {
	res.send('Please use /api/hashtags');
});

app.get('/api/hashtags', (req, res) => {
	Hashtag.getHashtags((err, hashtags) => {
		if(err){
			throw err;
		}
		res.json(hashtags);
	});
});


app.listen(3000);
console.log('Running on port 3000...');