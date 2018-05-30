const mongoose = require('mongoose');

// Hashtag Schema
const hashtagSchema = mongoose.Schema({
	_id: String,
	value: String
});

const Hashtag = module.exports = mongoose.model('Hashtag', hashtagSchema);

// Get Hashtags
module.exports.getHashtags = (callback, limit) => {
	Hashtag.find(callback).limit(limit);
}