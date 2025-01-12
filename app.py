import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "e9fb112ca39f44ee815d060a9654a290"
CLIENT_SECRET = "7c46dceb59604ef4891434085ea61d39"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        artist = music.iloc[i[0]].artist
        print(artist)
        print(music.iloc[i[0]].song)
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_names.append(music.iloc[i[0]].song)

    return recommended_music_names,recommended_music_posters

st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">', unsafe_allow_html=True)
st.markdown('<span style="display: inline-block; font-size: 32px;"><i class="fa-brands fa-spotify"></i>   Spotify <span style="font-size: 11px;">MUSIC RECOMMENDATION SYSTEM</span></span>', unsafe_allow_html=True)
music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

music_list = music['song'].values
selected_music = st.selectbox(
    "Select a song for get recommendation :",
    music_list
)
c=0
if st.button('Show Recommendation'):
    c=1
    recommended_music_names,recommended_music_posters = recommend(selected_music)
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])
    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])

    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])
    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])
    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])

def img():
    image_style = """
    <style>
        img {
            width: 200px;
            height: auto;
            margin: 0 0 0 280px;
        }
    </style>
    """

    st.markdown(image_style, unsafe_allow_html=True)

    st.image('OAIEOU0-removebg-preview.png')

if c==0:
    img()
if c==1:
    image_style ="""
    <style>
        img {
            display: none;
        }
    </style>
    """

def main():
    footer_style = """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #000;
        color: #fff;
        padding: 10px;
        text-align: center;
        font-size: 14px;
    }
    </style>
    """

    st.markdown(footer_style, unsafe_allow_html=True)
    st.markdown('<div class="footer"><i class="fa-regular fa-copyright"></i> It is a proxy of Spotify and made for learning perpose .<div><i class="fa-regular fa-envelope"></i> sahupriyansu21@gmail.com</div></div>', unsafe_allow_html=True)

if True:
    main()