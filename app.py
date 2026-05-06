"""A streamlit application for the 24-game solver."""

import base64
import random
import re

import streamlit as st

from media import FAIL_GIFS, SUCCESS_GIFS
from solver import solve_24

st.set_page_config(page_title="24-Inator", page_icon="ccbl_logo.svg")


def display_svg(svg_file_path, image_width="350px"):
    """Read an SVG, strips hardcoded dimensions, and encodes it."""
    try:
        with open(svg_file_path, "r", encoding="utf-8") as f:
            svg_content = f.read()

        svg_content = re.sub(r'\bwidth="[^"]+"', "", svg_content)
        svg_content = re.sub(r'\bheight="[^"]+"', "", svg_content)

        b64 = base64.b64encode(svg_content.encode("utf-8")).decode("utf-8")

        html_code = f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img
                    src="data:image/svg+xml;base64,{b64}"
                    style="width: {image_width}; max-width: 100%;
                    height: auto;"
                >
            </div>
        """
        st.markdown(html_code, unsafe_allow_html=True)

    except FileNotFoundError:
        st.warning(f"Could not find {svg_file_path}.")


display_svg("logo.svg", image_width="350px")

st.title("The CCBL 24-Inator")
st.write("Enter your cards below. Let the machine do the thinking.")

user_input = st.text_input(
    "Enter cards separated by spaces:", "4 7 8 8", key="card_input"
)


if st.button("Solve It!", type="primary"):
    try:
        cards = [int(x) for x in user_input.strip().split()]
        st.write(f"Running engine for: {cards}...")

        solutions = solve_24(cards)

        if solutions:
            st.success(f"Found {len(solutions)} solution(s):")

            for eq in solutions[:3]:
                st.code(f"{eq} = 24")

            if len(solutions) > 3:
                st.info(f"...and {len(solutions) - 3} more hidden solutions!")

            st.image(random.choice(SUCCESS_GIFS), width=400)

        else:
            st.error("No solutions found.")
            st.image(random.choice(FAIL_GIFS), width=400)

    except ValueError:
        st.warning("Please enter ONLY numbers separated by spaces.")
