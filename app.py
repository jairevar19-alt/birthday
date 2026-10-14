import streamlit as st
from pathlib import Path

# =====================================================
# BUBU'S BIRTHDAY ADVENTURE
# PERSONALISE EVERYTHING IN THIS SECTION
# =====================================================

SEJU = "Bubu"                 # Or "Mari jaan"
JIMMU = "JIMMU"

QUESTIONS = [
    {
        "title": "Level 1: The Birthday Queen 👑",
        "intro": "Easy warm-up. Don't get too confident, birthday girl. 😂",
        "questions": [
            {
                "q": "Who is the main character today?",
                "options": [
                    "Me, obviously",
                    "Bubu, the birthday queen",
                    "The birthday cake"
                ],
                "correct": 1,
                "success": "Correct! The birthday queen has entered the chat. 👑"
            },
            {
                "q": "What does the birthday girl deserve today?",
                "options": [
                    "A day full of happiness",
                    "Extra cuddles.",
                    "Extra love & cuddles"
                ],
                "correct": 2,
                "success": "Exactly. Only happiness and alots of love & cuddles. 💗"
            },
            {
                "q": "What is the official birthday rule?",
                "options": [
                    "No cake allowed",
                    "Extra love and extra cake",
                    "Do everyone's chores"
                ],
                "correct": 1,
                "success": "A rule I fully support. Cake is compulsory. 🍰"
            }
        ]
    },
    {
        "title": "Level 2: Just Us 🫶",
        "intro": "This level is about our memories. Replace the sample answers with your own!",
        "questions": [
            {
                "q": "Which one is our special inside joke?",
                "options": [
                   "When we met on our 2nd date you were watching....",
                    "your chappal falls from bike",
                    "I fall on your door at that day."
                ],
                "correct": 0,
                "success": "HAHA, only we would understand that. 😂💗"
            },
            {
                "q": "What do I do that annoys you the most?",
                "options": [
                    "Touch your hairs.",
                    "Put hands on your shoulder.",
                    "Touch or gudi-gudi on stomach"
                ],
                "correct": 2,
                "success": "You know me a little too well. 😭"
            },
            {
                "q": "Which memory should we relive?",
                "options": [
                    "Our rainy season dates.(dadar wali.....)",
                    "Memories at our homes",
                    "Ganapati of 2025..."
                ],
                "correct": 0,
                "success": "Keeping this one in our forever folder. 🥹"
            }
        ]
    },
    {
        "title": "Level 3: Birthday Boss Battle 🎮",
        "intro": "Final round. Your surprise is almost unlocked!",
        "questions": [
            {
                "q": "What do I hope you always remember?",
                "options": [
                    "You deserve happiness and kindness",
                    "You must share every snack",
                    "I am always right"
                ],
                "correct": 0,
                "success": "Correct. Although I may still ask for your snacks. 😂"
            },
            {
                "q": "Which song belongs on your birthday playlist?",
                "options": [
                    "My voice...",
                    "Ek din teri raahon mei",
                    "Gujarati songs"
                ],
                "correct": 2,
                "success": "Birthday soundtrack unlocked. 🎶"
            },
            {
                "q": "Ready for your final surprise?",
                "options": [
                    "YES, SHOW ME!",
                    "Give me 47 more hints",
                    "Cake first, questions later"
                ],
                "correct": 0,
                "success": "That's my girl! 🎁"
            }
        ]
    }
]

BIRTHDAY_LETTER = f"""
Happy birthday, my {SEJU}. 🩷

I wanted to make you something of my own instead of
just sending another birthday message. It has some
silly questions and questionable jokes, but I made
it thinking of you.

I hope this year brings you peaceful days, reasons
to smile, new memories, and things that genuinely
make you happy. I hope you enjoy today, eat something
really good, and laugh a lot.

I will probably continue annoying you, stealing your
attention, and asking for one more minute with you.
That part of the present is unfortunately non-refundable. 😂

Thank you for being you. I'm really happy I get to
celebrate you today.

Happy birthday, mari jaan. I love you. 💗

— {JIMMU}
"""

# =====================================================
# GAME INTERFACE
# =====================================================

st.set_page_config(
    page_title=f"Happy Birthday {SEJU} 💗",
    page_icon="💗",
    layout="centered"
)


st.markdown("""
<style>
/* Soft romantic birthday background */
.stApp {
    background: linear-gradient(
        145deg,
        #FFF1F6,
        #F6EFFF,
        #FFFAF7
    );
}

/* Rose-pink headings */
h1, h2, h3, h4 {
    color: #B83268 !important;
}

/* Main text */
.stApp p,
.stApp label,
.stApp li,
.stMarkdown {
    color: #493447;
}

/* Captions */
.stCaption,
[data-testid="stCaptionContainer"] {
    color: #76546B !important;
}

/* Birthday letter card */
.birthday-card {
    background: #FFFFFF;
    color: #493447 !important;
    padding: 22px;
    border-radius: 20px;
    border: 1px solid #FFD6E5;
    line-height: 1.9;
}

/* Romantic pink buttons */
div.stButton > button {
    border-radius: 22px;
    min-height: 45px;
    background: #F8B4CE;
    color: #49283B !important;
    border: 1px solid #F08BB2;
    font-weight: 600;
    transition: all 0.2s ease;
}

/* Button hover effect */
div.stButton > button:hover {
    background: #E98CB4;
    color: #FFFFFF !important;
    border-color: #D85C91;
}

/* Quiz answer text */
[data-testid="stRadio"] label p {
    color: #493447 !important;
}

/* Text input fields */
.stTextInput input,
.stTextArea textarea {
    color: #493447 !important;
    background-color: #FFFFFF !important;
    border: 1px solid #F0B7CF;
}

/* Progress bar */
[data-testid="stProgressBar"] > div > div {
    background-color: #E77DA8;
}

/* Links */
.stApp a {
    color: #B83268 !important;
}

/* Checkboxes */
[data-testid="stCheckbox"] label p {
    color: #493447 !important;
}
</style>
""", unsafe_allow_html=True)





def reset_game():
    st.session_state.level = 0
    st.session_state.question = 0
    st.session_state.solved = set()
    st.session_state.hearts = 0
    st.session_state.started = False
    st.session_state.candle_blown = False


if "level" not in st.session_state:
    reset_game()


def question_key(level, question):
    return f"{level}_{question}"


def level_completed(level):
    return all(
        question_key(level, i) in st.session_state.solved
        for i in range(len(QUESTIONS[level]["questions"]))
    )


def show_progress():
    st.write("### Your earned hearts")
    hearts = st.session_state.hearts
    st.write(" ".join(["💗"] * hearts + ["🤍"] * (3 - hearts)))
    st.progress(hearts / 3)


# =====================================================
# WELCOME SCREEN
# =====================================================

if not st.session_state.started:
    st.markdown("<h1 style='text-align:center;'>🎀🎂</h1>",
                unsafe_allow_html=True)
    st.title(f"Happy Birthday, {SEJU}!")
    st.subheader("Welcome to your little birthday adventure 💗")

    st.write(
        "Okay birthday girl, your present isn't arriving in a box. "
        "It's arriving with questions, hearts, and a boyfriend who "
        "has clearly spent too much time coding. 🤓"
    )
    st.write("Complete all three levels to unlock your surprise.")

    if st.button("Start my birthday adventure ✨", use_container_width=True):
        st.session_state.started = True
        st.rerun()

# =====================================================
# LEVELS
# =====================================================

elif st.session_state.level < len(QUESTIONS):
    level_index = st.session_state.level
    level_data = QUESTIONS[level_index]
    question_index = st.session_state.question
    question_data = level_data["questions"][question_index]
    key = question_key(level_index, question_index)

    st.caption(f"LEVEL {level_index + 1} OF {len(QUESTIONS)}")
    st.title(level_data["title"])
    st.write(level_data["intro"])
    show_progress()

    st.progress(
        (question_index + 1) / len(level_data["questions"])
    )

    st.subheader(
        f"Question {question_index + 1}: {question_data['q']}"
    )

    if key not in st.session_state.solved:
    choice = st.radio(
        "Choose your answer:",
        question_data["options"],
        key=f"choice_{key}"
    )

    if st.button("Lock in my answer 💌", use_container_width=True):
        selected_index = question_data["options"].index(choice)

        if selected_index == question_data["correct"]:
            st.session_state.solved.add(key)
            st.session_state[f"feedback_{key}"] = "correct"
            st.rerun()
        else:
            st.session_state[f"feedback_{key}"] = "wrong"

    if st.session_state.get(f"feedback_{key}") == "wrong":
        st.error("Nope! Try again, birthday girl. 😏 Hint: you know this one!")

    else:
        st.success(question_data["success"])

        if question_index < len(level_data["questions"]) - 1:
            if st.button("Next question ➜", use_container_width=True):
                st.session_state.question += 1
                st.rerun()
        else:
            if st.button("Complete this level 💗", use_container_width=True):
                st.session_state.hearts += 1
                st.session_state.level += 1
                st.session_state.question = 0
                st.rerun()

    st.divider()
    st.caption(
        f"Level {level_index + 1} must be completed to unlock the next one."
    )

# =====================================================
# CANDLE AND WISH
# =====================================================

elif not st.session_state.candle_blown:
    st.balloons()
    st.title(f"You did it, {SEJU}! 🎉")
    st.write("Three levels completed. Three hearts earned. 🩷")
    show_progress()

    st.markdown(
        "<h1 style='text-align:center;font-size:85px;'>🕯️</h1>",
        unsafe_allow_html=True
    )
    st.subheader("Make a birthday wish ✨")
    st.write(
        "Take a tiny moment for yourself. You deserve good things, "
        "happy days, and cake. Especially cake."
    )

    if st.button("Blow out the candle 💨", use_container_width=True):
        st.session_state.candle_blown = True
        st.session_state.improvement_answer = ""
        st.session_state.ask_improvement = True
        st.rerun()
    # =====================================================
# ONE HEART-TO-HEART QUESTION 💌
# =====================================================

elif st.session_state.get("ask_improvement", False):
    st.title("One little question, Bubu... 🥹💗")

    st.write(
        "Before I show you your final surprise, "
        "there's something I really want to ask you."
    )

    st.write(
        "I love you, and I want to keep learning how to love "
        "you better. You can be completely honest with me. ❤️"
    )

    improvement = st.radio(
        "What is one thing you'd like me to improve in my behaviour?",
        [
            "Listen to you more and understand your feelings ❤️",
            "Give you more time, attention, and affection 🫂",
            "Be more patient during disagreements 🌷",
            "Communicate better and express my feelings 💬",
            "Understand you better instead of assuming things 🥹",
            "Respect your space and personal boundaries 🦋",
            "Show my love more through actions 💗",
            "Something else — let me tell you ✍️"
        ],
        index=None,
        key="improvement_choice",
        placeholder="Choose the one that feels right..."
    )

    custom_answer = ""

    if improvement == "Something else — let me tell you ✍️":
        custom_answer = st.text_area(
            "Tell me honestly, meri jaan 💌",
            placeholder="I'll listen with an open heart...",
            key="custom_improvement_answer"
        )

    if st.button("Continue to my surprise 🎁", use_container_width=True):
        if improvement is None:
            st.warning("Choose an answer first, Bubu. 💗")
        elif (
            improvement == "Something else — let me tell you ✍️"
            and not custom_answer.strip()
        ):
            st.warning("Write your answer first, meri jaan. 🫶")
        else:
            st.session_state.improvement_answer = (
                custom_answer.strip()
                if improvement == "Something else — let me tell you ✍️"
                else improvement
            )
            st.session_state.ask_improvement = False
            st.rerun()
# =====================================================
# FINAL SURPRISE
# =====================================================

else:
    st.balloons()
    st.title(f"One last thing, {SEJU}... 🥹💗")
   # =====================================================
# FINAL SURPRISE — UNLOCK PHOTOS ONLY AT THE END
# =====================================================

else:
    st.balloons()

    st.title(f"One last thing, {SEJU}... 🥹💗")
    st.write("No more questions. Promise.")
    st.write("You've completed all three levels and earned all your hearts! 💗")

    # Start with memories locked
    if "memories_revealed" not in st.session_state:
        st.session_state.memories_revealed = False

    st.divider()

    if not st.session_state.memories_revealed:
        st.markdown(
            "<h1 style='text-align:center;'>🎁💌🎀</h1>",
            unsafe_allow_html=True
        )

        st.subheader("A little surprise is waiting for you...")
        st.write(
            "You've made it this far, birthday girl. "
            "Ready to unlock some of our favourite memories? 🫶"
        )

        if st.button(
            "💗 Open your memories 💗",
            use_container_width=True
        ):
            st.session_state.memories_revealed = True
            st.rerun()

    else:
        from pathlib import Path

        BASE_DIR = Path(__file__).resolve().parent
        photo_folder = BASE_DIR / "photos"

        st.markdown(
            "<h1 style='text-align:center;'>"
            "Happy Birthday, Mari jaan! 🥹❤️"
            "</h1>",
            unsafe_allow_html=True
        )

        st.write(
            "A few little moments that became special "
            "because I got to share them with you. 💗"
        )

        captions = [
            "Our favourite photo 💗",
            "A cute memory 🫶",
            "Our silly side 😂",
            "One for the forever folder 💌"
        ]

        cols = st.columns(2)

        for i, caption in enumerate(captions, start=1):
            image_path = photo_folder / f"photo{i}.jpg"

            with cols[(i - 1) % 2]:
                if image_path.exists():
                    st.image(
                        str(image_path),
                        caption=caption,
                        use_container_width=True
                    )
                else:
                    st.info(
                        f"📷 Photo {i} goes here\n\n"
                        f"Add it as photos/photo{i}.jpg"
                    )

        st.divider()

        st.subheader("A little letter for you 💌")

        st.markdown(
            "<div class='birthday-card'>"
            + BIRTHDAY_LETTER.replace("\n", "<br>")
            + "</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<h2 style='text-align:center;'>"
            "Happy birthday, my girl. 🩷"
            "</h2>",
            unsafe_allow_html=True
        )

        if st.button(
            "Play the adventure again 🎊",
            use_container_width=True
        ):
            reset_game()
            st.session_state.memories_revealed = False
            st.rerun()
            st.session_state.improvement_answer = ""
            
