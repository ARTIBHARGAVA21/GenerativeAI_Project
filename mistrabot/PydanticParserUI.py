import streamlit as st
from dotenv import load_dotenv
from typing import List, Optional
from pydantic import BaseModel

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

# Load environment variables
load_dotenv()

# Streamlit Page Configuration
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.movie-card {
    background-color: #f5f5f5;
    padding: 20px;
    border-radius: 12px;
    margin-top: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}

.title {
    text-align: center;
    color: #ff4b4b;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>🎬 Movie Information Extractor</h1>", unsafe_allow_html=True)
st.write("Enter a movie description and extract structured information using Mistral AI.")

# Initialize Model
model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.3
)

# Pydantic Model
class Movie(BaseModel):
    name: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[float] = None
    summary: str

# Parser
parser = PydanticOutputParser(pydantic_object=Movie)

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Extract movie information from the given paragraph.

{format_instruction}
"""
        ),
        (
            "human",
            "{paragraph}"
        )
    ]
)

# Text Input
paragraph = st.text_area(
    "📝 Enter Movie Paragraph",
    height=200,
    placeholder="""
Example:
Inception is a 2010 science fiction action film directed by Christopher Nolan.
The film stars Leonardo DiCaprio, Joseph Gordon-Levitt, and Ellen Page.
It has a rating of 8.8/10 and follows a thief who enters people's dreams to steal secrets.
"""
)

# Extract Button
if st.button("🚀 Extract Movie Information", use_container_width=True):

    if not paragraph.strip():
        st.warning("Please enter a movie description.")
    else:
        try:
            with st.spinner("Analyzing movie details..."):

                final_prompt = prompt.invoke(
                    {
                        "paragraph": paragraph,
                        "format_instruction": parser.get_format_instructions()
                    }
                )

                response = model.invoke(final_prompt)

                movie_data = parser.parse(response.content)

            st.success("Movie information extracted successfully!")

            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🎥 Basic Information")
                st.write(f"**Movie Name:** {movie_data.name}")
                st.write(f"**Release Year:** {movie_data.release_year}")
                st.write(f"**Director:** {movie_data.director}")
                st.write(f"**Rating:** ⭐ {movie_data.rating}")

            with col2:
                st.subheader("🎭 Genre & Cast")
                st.write("**Genres:**")
                st.write(", ".join(movie_data.genre))

                st.write("**Cast:**")
                st.write(", ".join(movie_data.cast))

            st.subheader("📖 Summary")
            st.write(movie_data.summary)

            st.markdown("</div>", unsafe_allow_html=True)

            with st.expander("📄 View JSON Output"):
                st.json(movie_data.model_dump())

        except Exception as e:
            st.error(f"Error: {str(e)}")