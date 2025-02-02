"""This module contains the list of Authors"""
from awesome_streamlit.shared import models

Author = models.Author
# Authors
STREAMLIT_AUTHOR = Author(name="Streamlit", url="https://streamlit.io/")
STREAMLIT_EXAMPLE_AUTHOR = Author(
    name="Streamlit/.../examples/", url="https://streamlit.io/"
)
STREAMLIT_COMPONENT_AUTHOR = Author(
    name="Streamlit/.../api-examples-source", url="https://streamlit.io/"
)
KEVIN_ARVAI = Author(
    name="Kevin Arvai", url="https://github.com/arvkevi"
)
MARC_SKOV_MADSEN = Author(
    name="Marc Skov Madsen", url="https://datamodelsanalytics.com"
)
INES = Author(name="Ines Montani", url="https://gist.github.com/ines")
PARAS_PATIDAR = Author(name="Paras Patidar", url="https://github.com/patidarparas13")
AWESOME_STREAMLIT_ORG = Author(
    name="Awesome-Streamlit.org",
    url="https://github.com/marcskovmadsen/awesome-streamlit",
)
AUTHORS = [
    KEVIN_ARVAI,
    INES,
    MARC_SKOV_MADSEN,
    PARAS_PATIDAR,
    STREAMLIT_AUTHOR,
    STREAMLIT_COMPONENT_AUTHOR,
    STREAMLIT_EXAMPLE_AUTHOR,
]
