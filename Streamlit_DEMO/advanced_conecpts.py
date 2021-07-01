import time

import numpy  # as np
import numpy as np
import pandas  # as pd
import streamlit as st

st.title("Advanced Concepts.")

st.subheader("Simple dataframe:")
dataframe = numpy.random.randn(10, 20)
st.dataframe(dataframe)

st.subheader("Simple dataframe with style 'highlight_max':")
dataframe = pandas.DataFrame(
    numpy.random.randn(10, 20), columns=("col %d" % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0))

st.subheader("Dataframe load as table format:")
dataframe = pandas.DataFrame(
    numpy.random.randn(10, 20), columns=("col %d" % i for i in range(20))
)
st.table(dataframe)

st.subheader("Insert elements out of order:")

st.text("This will appear first")
# Appends some text to the app.

my_slot1 = st.empty()
# Appends an empty slot to the app. We'll use this later.

my_slot2 = st.empty()
# Appends another empty slot.

st.text("This will appear last")
# Appends some more text to the app.

my_slot1.text("This will appear second")
# Replaces the first empty slot with a text string.

my_slot2.line_chart(np.random.randn(20, 2))
# Replaces the second empty slot with a chart.

st.subheader("Animate elements:")

if st.checkbox("Start animation!"):

    progress_bar = st.progress(0)
    status_text = st.empty()
    chart = st.line_chart(np.random.randn(10, 2))

    for i in range(100):
        # Update progress bar.
        progress_bar.progress(i)

        new_rows = np.random.randn(10, 2)

        # Update status text.
        status_text.text("The latest random number is: %s" % new_rows[-1, 1])

        # Append data to the chart.
        chart.add_rows(new_rows)

        # Pretend we're doing some computation that takes time.
        time.sleep(0.1)

    status_text.text("Done!")
    st.balloons()

if st.checkbox("Show dynamic chart!"):

    st.subheader("Append data to a table or chart:")

    # Get some data.
    data = np.random.randn(10, 2)

    # Show the data as a chart.
    chart = st.line_chart(data)

    # Wait 1 second, so the change is clearer.
    time.sleep(2)

    # Grab some more data.
    data2 = np.random.randn(10, 2)

    # Append the new data to the existing chart.
    chart.add_rows(data2)

st.subheader("Some interesting features:")

x = 10
"x =", x, "['x =', x ]"
