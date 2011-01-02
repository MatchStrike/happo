
// The ID of the most recent tweet currently being displayed on the page. Used for polling.
var most_recent_tweet = [];

$(document).ready(function(){
	
	load_champions();
	
	if ($('#city').length > 0) {
		get_new_city_tweets();
		get_new_happo_tweets();
		//setInterval(get_new_city_tweets, 30000);
		//setInterval(get_new_happo_tweets, 30000);
	}
	
	// Google Analytics
	$.ga("UA-10208886-6");
});

function get_new_city_tweets() {
	get_new_tweets('#city_query');
}

function get_new_happo_tweets() {
	get_new_tweets('#happo_query');
}

function get_new_tweets(feed_id) {
	$.get(get_query_url(feed_id),{}, function(data) {
		var stream_id = feed_id+'_tweets';
		if('results' in data) {
			if (data.results.length > 0) {
				most_recent_tweet[feed_id] = data.results[0].id;
				$(stream_id+'>.loading_message, '+stream_id+'>.no_tweets_message, '+stream_id+'>.error_message').fadeOut('fast', function(){ $(this).remove(); });
				for (i in data.results) {
					$(stream_id).append(
						"<li><a href='http://twitter.com/"+data.results[i].from_user+"'><img src='"+data.results[i].profile_image_url+"' alt='twitter user image' /></a><a href='http://twitter.com/"+data.results[i].from_user+"'>"+data.results[i].from_user+"</a> "+twitterize(data.results[i].text)+"<br /><span class='timestamp'>"+relative_time(data.results[i].created_at)+"</span></li>"
					);
				}
			} else {
				if($(stream_id+'>.loading_message').length > 0){
					$(stream_id+'>.loading_message, '+stream_id+'>.error_message').fadeOut('slow', function(){ $(this).remove(); });
					$(stream_id).append('<li class="no_tweets_message"><img src="/assets/img/message.png" alt="HAPPO message" />Sorry. We couldn\'t find any tweets in this category.</li>');
				}
			}
		} else {
			$(stream_id).append('<li class="error_message"><img src="/assets/img/message.png" alt="HAPPO message" />Sorry. We encountered an error while retrieving tweets from Twitter. We\'ll try again in a few seconds.</li>');
		}
	}, "json");
}

function get_query_url(feed_id) {
	var query_url = $(feed_id).attr('href').replace('atom', 'json');
	if (feed_id in most_recent_tweet){
			query_url=query_url+'&since_id='+most_recent_tweet[feed_id];
	}	
	return query_url+'&callback=?';
}

function twitterize(tweet) {
	var link = /((ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?)/gi; 
	var atmentions = /[\@]+([A-Za-z0-9-_]+)/gi;
	var hashtags = / [\#]+([A-Za-z0-9-_]+)/gi;
	
	tweet = tweet.replace(link,"<a href=\"$1\">$1</a>");
	tweet = tweet.replace(atmentions,"@<a href=\"http://twitter.com/$1\">$1</a>");
	tweet = tweet.replace(hashtags, ' <a href="http://search.twitter.com/search?q=%23$1">#$1</a>');
	
	return tweet;
}

function load_champions(){
	$('#champions>li').each(function(){
		insert_profile($(this).attr('id'));
	});
}

function insert_profile(champion){
	var champion_id = '#'+champion
	$.get('http://api.twitter.com/1/users/show/'+champion+'.json?callback=?',{}, function(data) {
		if('id' in data) {
			$('#champs').append('<h3><a href="http://twitter.com/'+data.screen_name+'">'+data.name+'</a></h3><img src="'+data.profile_image_url+'" alt="image of '+data.screen_name+'" /><p class="champ_info"><a href="http://twitter.com/'+data.screen_name+'">@'+data.screen_name+'</a></p><p class="champ_info"><a href="'+data.url+'">Website</a></p><p>'+data.description+'</p>');
			$(champion_id).fadeOut('slow').fadeIn('slow');
		} else {
			// Failed
		}
	}, "json");
}

// Taken from http://tweet.seaofclouds.com/
function relative_time(time_value) {
	var parsed_date = Date.parse(time_value);
	var relative_to = (arguments.length > 1) ? arguments[1] : new Date();
	var delta = parseInt((relative_to.getTime() - parsed_date) / 1000);
	if(delta < 60) {
		return 'less than a minute ago';
	} else if(delta < 120) {
		return 'about a minute ago';
	} else if(delta < (45*60)) {
		return (parseInt(delta / 60)).toString() + ' minutes ago';
	} else if(delta < (90*60)) {
		return 'about an hour ago';
	} else if(delta < (24*60*60)) {
		return 'about ' + (parseInt(delta / 3600)).toString() + ' hours ago';
	} else if(delta < (48*60*60)) {
		return '1 day ago';
	} else {
		return (parseInt(delta / 86400)).toString() + ' days ago';
	}
}
