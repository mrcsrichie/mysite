import course
import song

COURSES = [
    course.Course(period=1,
                  name='Intro to Computer Science',
                  teacher_name='Ms. Lee',
                  resource_name='repl.it',
                  resource_url='https://repl.it/'),
    course.Course(period=2,
                  name='Art history',
                  teacher_name='Mr. Long',
                  resource_name='ArtHistory.net',
                  resource_url='http://www.arthistory.net/'),
    course.Course(period=3,
                  name='English',
                  teacher_name='Mr. Moul',
                  resource_name='Spark Notes',
                  resource_url='http://www.sparknotes.com/'),
    course.Course(period=4,
                  name='Physics',
                  teacher_name='Ms. Davis',
                  resource_name='Interactive simulations',
                  resource_url='https://phet.colorado.edu/en/simulations/category/physics'),
    course.Course(period=5,
                  name='Geometry',
                  teacher_name='Ms. Friedeberg',
                  resource_name='Khan Academy',
                  resource_url='https://www.khanacademy.org/math/geometry'),
    course.Course(period=6,
                  name='Biology',
                  teacher_name='Mr. Poulsen',
                  resource_name='Wikipedia',
                  resource_url='https://en.wikipedia.org/wiki/Biology'),
]

TOP_TEN_SONGS = [
    song.Song(
        title='Call Out My Name',
        artist_name='The Weeknd',
        youtube_url='https://youtu.be/M4ZoCHID9GI'),
    song.Song(
        title='IDGAF',
        artist_name='Dua Lipa',
        youtube_url='https://youtu.be/Mgfe5tIwOj0'),
    song.Song(
        title='Perfect',
        artist_name='Ed Sheeran',
        youtube_url='https://youtu.be/2Vv-BfVoq4g'),
    song.Song(
        title='Havana',
        artist_name='Camila Camello',
        youtube_url='https://youtu.be/pz95u3UVpaM'),
    song.Song(
        title='Psycho',
        artist_name='Post Malone',
        youtube_url='https://youtu.be/au2n7VVGv_c'),
    song.Song(
        title='FRIENDS',
        artist_name='Marshmello & Anne-Marie',
        youtube_url='https://youtu.be/jzD_yyEcp0M'),
    song.Song(
        title='Colors',
        artist_name='Jason Derulo',
        youtube_url='https://youtu.be/jzD_yyEcp0M'),
    song.Song(
        title='Let Me',
        artist_name='ZAYN',
        youtube_url='https://youtu.be/J-dv_DcDD_A'),
    song.Song(
        title='New Rules',
        artist_name='Dua Lipa',
        youtube_url='https://youtu.be/k2qgadSvNyU'),
    song.Song(
        title="God's Plan",
        artist_name='Drake',
        youtube_url='https://youtu.be/xpVfcZ0ZcFM'),
]
