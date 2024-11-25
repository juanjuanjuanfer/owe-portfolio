import streamlit as st
import random
import time
import datetime

# Questions data
QUESTIONS = [
    {
        "question": "What is the recommended length for an Executive Summary?",
        "options": ["5-10 pages", "1-2 pages (10% of original document)", "3-4 pages"],
        "correct": 1
    },
    {
        "question": "In a Business Letter, what comes immediately after the recipient's address?",
        "options": ["Opening paragraph", "Dear Mr./Ms. [Last Name]", "Subject line"],
        "correct": 1
    },
    {
        "question": "What is the primary purpose of a CV/Resume's professional summary?",
        "options": ["List all previous jobs", "Detail education history", "Highlight key qualifications in 2-3 sentences"],
        "correct": 2
    },
    {
        "question": "Which section appears first in a memo?",
        "options": ["Subject", "TO: line", "Purpose statement"],
        "correct": 1
    },
    {
        "question": "What should be included in a proposal's budget section?",
        "options": ["Only total cost", "Team salaries", "Direct and indirect costs with ROI analysis"],
        "correct": 2
    },
    {
        "question": "How should dates be formatted in Business Letters?",
        "options": ["Month Day, Year", "DD/MM/YY", "MM/DD/YYYY"],
        "correct": 0
    },
    {
        "question": "What is the recommended format for CV/Resume work experience?",
        "options": ["Alphabetical order", "Reverse chronological order", "Order of importance"],
        "correct": 1
    },
    {
        "question": "In an Executive Summary, what should follow the key findings?",
        "options": ["Background information", "Recommendations", "Team structure"],
        "correct": 1
    },
    {
        "question": "What element is mandatory in a memo's header?",
        "options": ["Company logo", "Department code", "Subject line"],
        "correct": 2
    },
    {
        "question": "What should be the first section of a business proposal?",
        "options": ["Problem statement", "Executive summary", "Budget breakdown"],
        "correct": 1
    },
    {
        "question": "What spacing should be used in Business Letters?",
        "options": ["Double space throughout", "Single-spaced with double space between paragraphs", "1.5 spacing throughout"],
        "correct": 1
    },
    {
        "question": "How should action items be presented in a memo?",
        "options": ["In paragraph form", "In alphabetical order", "With clear deadlines and responsibilities"],
        "correct": 2
    },
    {
        "question": "What's the appropriate length for an entry-level CV/Resume?",
        "options": ["3-4 pages", "1-2 pages", "5-6 pages"],
        "correct": 1
    },
    {
        "question": "How should financial data be presented in an Executive Summary?",
        "options": ["Detailed spreadsheets", "Brief cost/benefit summary", "Complete financial statements"],
        "correct": 1
    },
    {
        "question": "In a proposal, risk analysis should include:",
        "options": ["Only positive outcomes", "Historical data only", "Potential issues and mitigation strategies"],
        "correct": 2
    }
]

def save_result(name, score, time_taken):
    with open('quiz_results.txt', 'a') as f:
        f.write(f"{name},{score},{time_taken}\n")

def main():
    st.title("Executive Documents Quiz")
    
    # Initialize session state
    if 'state' not in st.session_state:
        st.session_state.state = 'start'
        st.session_state.start_time = None
        st.session_state.questions = None
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answers = {}
        st.session_state.randomized_options = {}

    if st.session_state.state == 'start':
        if st.button("Start Quiz"):
            st.session_state.state = 'quiz'
            st.session_state.start_time = time.time()
            # Randomize questions once at the start
            st.session_state.questions = random.sample(QUESTIONS, len(QUESTIONS))
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            # Create randomized options for all questions at the start
            st.session_state.randomized_options = {
                i: random.sample(list(range(len(q["options"]))), len(q["options"]))
                for i, q in enumerate(st.session_state.questions)
            }
            st.rerun()

    elif st.session_state.state == 'quiz':
        # Timer with auto-refresh
        elapsed_time = int(time.time() - st.session_state.start_time)
        remaining_time = max(300 - elapsed_time, 0)  # 5 minutes = 300 seconds
        
        time_placeholder = st.empty()
        progress_placeholder = st.empty()
        
        progress_placeholder.progress(remaining_time / 300)
        time_placeholder.write(f"Time remaining: {remaining_time // 60}:{remaining_time % 60:02d}")

        # Auto-submit when time runs out
        if remaining_time == 0:
            st.session_state.state = 'finish'
            st.rerun()

        # Display current question
        current_q = st.session_state.questions[st.session_state.current_question]
        st.write(f"Question {st.session_state.current_question + 1} of {len(QUESTIONS)}")
        st.write(current_q["question"])
        
        # Use pre-randomized options
        randomized_indices = st.session_state.randomized_options[st.session_state.current_question]
        options = [current_q["options"][i] for i in randomized_indices]
        
        answer = st.radio("Select your answer:", options, key=f"q_{st.session_state.current_question}")
        original_index = randomized_indices[options.index(answer)]
        
        if st.button("Next"):
            if original_index == current_q["correct"]:
                st.session_state.score += 1
            
            if st.session_state.current_question < len(QUESTIONS) - 1:
                st.session_state.current_question += 1
            else:
                st.session_state.state = 'finish'
            st.rerun()

    elif st.session_state.state == 'finish':
        time_taken = int(time.time() - st.session_state.start_time)
        formatted_time = f"{time_taken // 60}:{time_taken % 60:02d}"
        st.write(f"Quiz completed in {formatted_time}")
        st.write(f"Your score: {st.session_state.score}/{len(QUESTIONS)}")
        
        name = st.text_input("Enter your name to save result:")
        if name and st.button("Save Result"):
            save_result(name, st.session_state.score, formatted_time)
            st.success("Result saved!")
        
        if st.button("Retry Quiz"):
            st.session_state.state = 'start'
            st.rerun()

        # Display results table
        st.write("### Previous Results")
        try:
            with open('quiz_results.txt', 'r') as f:
                results = f.readlines()
            if results:
                st.table([r.strip().split(',') for r in results[-5:]])  # Show last 5 results
        except FileNotFoundError:
            st.write("No previous results found.")

if __name__ == "__main__":
    st.set_page_config(page_title="Executive Documents Quiz")
    main()