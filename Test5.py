from cProfile import label
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import pydeck as pdk
import webbrowser



data = pd.DataFrame(np.random.randn(10,3), columns =['a','b','c'])

st.dataframe(data)

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)


fig1, mat = plt.subplots()
mat.scatter(data['a'],data['b'])
#mat.bar(data['a'],data['b'])
mat.set_title('Scatter Chart')
mat.set_xlabel('X axis')
mat.set_ylabel('Y axis')
st.pyplot(fig1)

fig2 , mat = plt.subplots()
mat.bar(data['a'],data['b'], edgecolor = 'Red', width = 0.7)
mat.set_title('Bar Chart')
mat.set_xlabel('X axis')
mat.set_ylabel('Y axis')
st.pyplot(fig2)

fig3 = alt.Chart(data).mark_circle().encode(
    x = 'a', y = 'b', tooltip = ['a','b']
)
st.altair_chart(fig3, use_container_width=True)

countrydata = {
    'lat':[28.6,55.75,38.883333,41.9,48.86666667,52.51666667],
    'lon':[77.2,37.6,-77,12.483333,2.333333,13.4],
    'range':[10,6,7,7,8,4]
}
countrydf = pd.DataFrame(countrydata)
#st.write(countrydata)
#st.dataframe(countrydf)
st.map(countrydf)

#pdkdf
# st.pydeck_chart(pdk.Deck(
#     map_style='mapbox://styles/mapbox/light-v9',
#      initial_view_state=pdk.ViewState(
#          latitude=37.76,
#          longitude=-122.4,
#          zoom=50,
#          pitch=50,
#      ),
#      layers=[
#          pdk.Layer(
#             'HexagonLayer',
#             data=countrydf,
#             get_position='[lat, lon]',
#             radius=200,
#             elevation_scale=4,
#             elevation_range=[0, 1000],
#             pickable=True,
#             extruded=True,
#          ),
#          pdk.Layer(
#              'ScatterplotLayer',
#              data=countrydf,
#              get_position='[lat, lon]',
#              get_color='[200, 30, 0, 160]',
#              get_radius=200,)]))

st.image('https://media.istockphoto.com/photos/sunrise-over-misty-fields-of-corn-picture-id1332712244?b=1&k=20&m=1332712244&s=170667a&w=0&h=jnTdEkp3nHw1X7LGiYICdTa1O9H4tug771D6U14VpOU=')

st.title('Widget time')
if st.button('Some Button'):
    st.write('Some text')

address = st.text_input('Enter your URL')
webbrowser.open_new_tab(address)

st.date_input('Enter a Date')

timeaddress = 'https://streamlit.io'
time = st.time_input('Da time ma man?')

if st.checkbox('I accept the terms and condtions'):
    st.write('Thank you for accepting')

st.radio('RickRoll!',['Never','Gonna','Give','You','Up'], index =0)

#Already worked with Selectbox

#Already worked with Slider

st.number_input('Enter your number')
st.file_uploader('Upload a file')
