$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function(response) {
    var movies = response.results;
    for (var i = 0; i < movies.length; i++) {
      var title = movies[i].title;
      $('#list_movies').append('<li>' + title + '</li>');
    }
  }
});
