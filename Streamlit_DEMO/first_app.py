import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy
import pandas
import time

st.title('My first app: test.')

st.write("Here's our first attempt at using data to create a table:")
st.write(pandas.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.title('Line chart, good?')
chart_data = pandas.DataFrame(
     numpy.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.title('Maps.')
map_data = pandas.DataFrame(
    numpy.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.title('Check box.')
if st.checkbox('Show dataframe'):
    chart_data = pandas.DataFrame(
       numpy.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

st.title('Side bar / Check box.')
if st.sidebar.checkbox('Show dataframe from side.'):
    chart_data = pandas.DataFrame(
       numpy.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

st.title('Select box.')
df = pandas.DataFrame({'first column': [1, 2, 3, 4], 'second column': [10, 20, 30, 40]})
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

st.title('Side bar / Select box.')
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option

st.title('Check time with side bar.')
'Wait user start the process...'
if st.sidebar.checkbox('Start long computation.'):
    'Starting a long computation...'
    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
    N = 1000
    for i in range(N):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}/{N}')
        bar.progress(round(100*(i + 1)/N))
        time.sleep(0.03)

    '...and now we\'re done!'


