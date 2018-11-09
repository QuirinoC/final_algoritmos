
const url = 'http://0.0.0.0:5000/'

tweet_data = null;


function tweet_response(response) {
    data = {
        'id':tweet_data['id'],
        'response':response
    }
    $.post(url,data, function(data,status){
    });
}

function update_tweet() {
    $.get(url, function(data,status){
        tweet_data = data;
        $('#tweet').text(tweet_data.text);
    });
}

$(document).ready(function () {
    update_tweet();

    $("#fake").click(function () {
        tweet_response('fake');
        update_tweet();
    });

    $("#real").click(() => {
        tweet_response('real');
        update_tweet();
    });
});

