from typing import Dict
import streamlit as st


def setup(questions: Dict[str, dict], alex):
    # Initialize the current question index in the session state if it doesn't exist
    if "current_question_index" not in st.session_state:
        st.session_state.current_question_index = 0

    question_keys = list(questions.keys())
    current_key = question_keys[st.session_state.current_question_index]
    details = questions[current_key]
    answer = st.radio(details["question"], options=["Yes", "Not Sure", "No"])

    details["answer"] = 1 if answer == "Yes" else 0

    # Update flags with the current answers
    alex.update_flags(questions)

    if st.button("Next"):
        if answer == "Yes":
            for followup in details["followups"]:
                for dep_flag, dep_details in followup.items():
                    setup({dep_flag: questions[dep_flag]})
        st.session_state.current_question_index += 1
        st.experimental_rerun()

    # Check entity scores after updating flags
    scores = list(alex.entities_scores())
    if scores and scores[0][1] > 0.7:
        entity_name_to_description = {
            score[0].name: score[0].description for score in scores
        }
        legal_entities = [score[0].name for score in scores]
        selected_entity = st.selectbox(
            "We recommend this Legal Entity based on your answers:", legal_entities
        )
        st.write(entity_name_to_description[selected_entity])

        if st.button("Select"):
            alex.entity = [
                score[0] for score in scores if score[0].name == selected_entity
            ][0]
            st.session_state.finished_setup = True
            return questions

    return questions
