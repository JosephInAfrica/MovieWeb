import webbrowser
import tomato
class Movie():
	"can this be a doc>"

	VALID_RATINGS=['G','PG','PG-13','R']
	def __init__(self,title,storyline,poster_image,trailer_youtube):
		self.title=title
		self.storyline=storyline
		self.poster_image_url=poster_image
		self.trailer_youtube_url=trailer_youtube

	def show_trailer(self):
		"doc for show_trailer"
		webbrowser.open(self.trailer_youtube_url)


IronMan=Movie('Ironman',
	'A scientist build himself an metal uniform to enable him to be the powerful Ironman to defend his city again bad guys',
	'https://upload.wikimedia.org/wikipedia/en/e/e0/Iron_Man_bleeding_edge.jpg','https://www.youtube.com/watch?v=uy6zdEbxjuU')


saving_private_ryan=Movie('saving private Ryan',
	'adventures of a group of soldiers sent to saving Private Ryan whose all 3 brothers got killed in battels',
	'https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg',
	'https://www.youtube.com/watch?v=mT3q8tba_lw')


brave_heart=Movie('Brave Heart','A scotish man who lead his people to fight agains English tyrant','http://img31.mtime.cn/mt/2014/02/22/230733.90049340_270X405X4.jpg','https://www.youtube.com/watch?v=pNuZIZOya78')


school_of_rock=Movie('School of Rock','A Rock Guitarist who teaches small kids to play rock music','http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg','https://www.youtube.com/watch?v=cwuZAaqcMfY')

movies=[IronMan,brave_heart,school_of_rock,saving_private_ryan]

tomato.open_movies_page(movies)

