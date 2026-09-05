import streamlit as st
import json
import os


st.set_page_config(
    page_title="Bos Sony Carousel Machine",
    layout="wide"
)


st.title(
    "🚀 Bos Sony Carousel Machine"
)


st.subheader(
    "Content Production Dashboard"
)


database_file = (
    "database/content_database.json"
)


if os.path.exists(database_file):

    with open(database_file) as f:
        data = json.load(f)


    contents = data["contents"]


    col1, col2, col3 = st.columns(3)


    with col1:
        st.metric(
            "Total Carousel",
            len(contents)
        )


    with col2:
        st.metric(
            "Status",
            "Active"
        )


    with col3:
        st.metric(
            "Pipeline",
            "AI Automated"
        )


    st.divider()


    st.subheader(
        "Content History"
    )


    for item in contents:

        st.write(
            f"""
            📌 {item.get('title')}

            Date:
            {item.get('date')}

            Platform:
            {item.get('platform')}
            """
        )

else:

    st.warning(
        "Database belum tersedia"
    )
