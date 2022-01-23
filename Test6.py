import streamlit as st

# layouts and spacings

# default columns / Page layout wide

st.set_page_config(layout = 'wide', initial_sidebar_state='collapsed')

st.title('Registration Form')

first, last = st.columns(2)

first.text_input('Enter your first name')
last.text_input('Enter your last name')

first.text_input('Email ID')
last.text_input('Mobile/Telephone number')

first.checkbox('Accept the terms and condtions')

# spacing 

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1,2,.2,2,.1))

row0_1.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi facilisis, mi nec auctor finibus, augue nunc ultrices ligula, nec iaculis nunc metus vel metus. Nulla sed molestie enim. Nulla facilisi. Morbi eu lorem quis magna dapibus auctor ac eu ligula. Aliquam blandit venenatis nibh, eget porttitor justo accumsan sed. Morbi eget aliquam ante, sit amet vestibulum diam. Pellentesque a semper neque, nec laoreet eros. Etiam varius, tortor non faucibus pharetra, nibh neque venenatis justo, eget lacinia mauris neque ut lectus. Mauris efficitur id elit bibendum tristique. Sed ut nisi vel neque fringilla vehicula. Sed rutrum, sem eget congue sagittis, sem justo faucibus turpis, sed fermentum est nulla non mauris. Vivamus lacinia orci nec lacinia porttitor. ')
row0_2.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi facilisis, mi nec auctor finibus, augue nunc ultrices ligula, nec iaculis nunc metus vel metus. Nulla sed molestie enim. Nulla facilisi. Morbi eu lorem quis magna dapibus auctor ac eu ligula. Aliquam blandit venenatis nibh, eget porttitor justo accumsan sed. Morbi eget aliquam ante, sit amet vestibulum diam. Pellentesque a semper neque, nec laoreet eros. Etiam varius, tortor non faucibus pharetra, nibh neque venenatis justo, eget lacinia mauris neque ut lectus. Mauris efficitur id elit bibendum tristique. Sed ut nisi vel neque fringilla vehicula. Sed rutrum, sem eget congue sagittis, sem justo faucibus turpis, sed fermentum est nulla non mauris. Vivamus lacinia orci nec lacinia porttitor. ')

row1_spacer1, row1_1, row1_spacer2 = st.columns((.2,3,.2))

row1_1.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi facilisis, mi nec auctor finibus, augue nunc ultrices ligula, nec iaculis nunc metus vel metus. Nulla sed molestie enim. Nulla facilisi. Morbi eu lorem quis magna dapibus auctor ac eu ligula. Aliquam blandit venenatis nibh, eget porttitor justo accumsan sed. Morbi eget aliquam ante, sit amet vestibulum diam. Pellentesque a semper neque, nec laoreet eros. Etiam varius, tortor non faucibus pharetra, nibh neque venenatis justo, eget lacinia mauris neque ut lectus. Mauris efficitur id elit bibendum tristique. Sed ut nisi vel neque fringilla vehicula. Sed rutrum, sem eget congue sagittis, sem justo faucibus turpis, sed fermentum est nulla non mauris. Vivamus lacinia orci nec lacinia porttitor. ')

st.sidebar.checkbox('Hello')