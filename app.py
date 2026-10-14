
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


# =====================================================
# PAGE SETTINGS — KEEP THIS NEAR THE TOP
# =====================================================

st.set_page_config(
    page_title="Happy Birthday Bubu 💗",
    page_icon="💗",
    layout="centered",
)


# =====================================================
# PERSONAL SETTINGS
# =====================================================

SEJU = "Bubu"
JIMMU = "JIMMU"

BASE_DIR = Path(__file__).resolve().parent
PHOTO_FOLDER = BASE_DIR / "photos"
MUSIC_FILE = BASE_DIR / "bg_music.mp3"


# =====================================================
# BACKGROUND MUSIC
# =====================================================

def romantic_background_music():
    """Display a music player for the birthday surprise."""

    if not MUSIC_FILE.is_file():
        st.info(
            "♫ Add bg_music.mp3 beside app.py "
            "to enable birthday music."
        )
        return

    try:
        audio_data = base64.b64encode(
            MUSIC_FILE.read_bytes()
        ).decode("utf-8")
    except OSError:
        st.warning("The birthday music file could not be read.")
        return

    components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <body style="margin:0;background:transparent;">
            <audio id="birthdayMusic"
                   loop
                   preload="auto"
                   src="data:audio/mpeg;base64,{audio_data}">
            </audio>

            <button id="musicButton"
                style="
                    border:1px solid #efb6cb;
                    border-radius:20px;
                    background:#fff0f5;
                    color:#9b4568;
                    padding:8px 15px;
                    font-size:13px;
                    cursor:pointer;
                ">
                ♫ Tap to play our song 💗
            </button>

            <script>
                const audio =
                    document.getElementById("birthdayMusic");
                const button =
                    document.getElementById("musicButton");

                audio.volume = 0.18;

                button.addEventListener("click", async () => {
                    try {
                        if (audio.paused) {
                            await audio.play();
                            button.textContent =
                                "♫ Playing for you 💗";
                        } else {
                            audio.pause();
                            button.textContent =
                                "♫ Play our song 💗";
                        }
                    } catch (error) {
                        button.textContent =
                            "♫ Tap to try again 💗";
                    }
                });
            </script>
        </body>
        </html>
        """,
        height=48,
    )


# =====================================================
# QUIZ QUESTIONS
# =====================================================

QUESTIONS = [
    {
        "title": "Level 1: The Birthday Queen 👑",
        "intro": (
            "Easy warm-up. Don't get too confident, "
            "birthday girl. 😂"
        ),
        "questions": [
            {
                "q": "Who is the main character today?",
                "options": [
                    "Me, obviously",
                    "Bubu, the birthday queen",
                    "The birthday cake",
                ],
                "correct": 1,
                "success": (
                    "Correct! The birthday queen has "
                    "entered the chat. 👑"
                ),
            },
            {
                "q": "What does the birthday girl deserve today?",
                "options": [
                    "A day full of happiness",
                    "Extra cuddles",
                    "Extra love & cuddles",
                ],
                "correct": 2,
                "success": (
                    "Exactly. Only happiness and lots "
                    "of love & cuddles. 💗"
                ),
            },
            {
                "q": "What is the official birthday rule?",
                "options": [
                    "No cake allowed",
                    "Extra love and extra cake",
                    "Do everyone's chores",
                ],
                "correct": 1,
                "success": (
                    "A rule I fully support. "
                    "Cake is compulsory. 🍰"
                ),
            },
        ],
    },
    {
        "title": "Level 2: Just Us 🫶",
        "intro": "This level is all about our memories.",
        "questions": [
            {
                "q": "Which one is our special inside joke?",
                "options": [
                    "When we met on our 2nd date, "
                    "you were watching...",
                    "Your chappal falls from the bike",
                    "I fell at your door that day",
                ],
                "correct": 0,
                "success": (
                    "HAHA, only we would understand that. 😂💗"
                ),
            },
            {
                "q": "What do I do that annoys you the most?",
                "options": [
                    "Touch your hair",
                    "Put my hands on your shoulder",
                    "Touch or do gudi-gudi on your stomach",
                ],
                "correct": 2,
                "success": "You know me a little too well. 😭",
            },
            {
                "q": "Which memory should we relive?",
                "options": [
                    "Our rainy-season dates (Dadar wali...)",
                    "Memories at our homes",
                    "Ganapati of 2025...",
                ],
                "correct": 0,
                "success": (
                    "Keeping this one in our forever folder. 🥹"
                ),
            },
        ],
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
                    "I am always right",
                ],
                "correct": 0,
                "success": (
                    "Correct. Although I may still ask "
                    "for your snacks. 😂"
                ),
            },
            {
                "q": "Which song belongs on your birthday playlist?",
                "options": [
                    "My voice...",
                    "Ek Din Teri Raahon Mein",
                    "Gujarati songs",
                ],
                "correct": 2,
                "success": "Birthday soundtrack unlocked. 🎶",
            },
            {
                "q": "Ready for your final surprise?",
                "options": [
                    "YES, SHOW ME!",
                    "Give me 47 more hints",
                    "Cake first, questions later",
                ],
                "correct": 0,
                "success": "That's my girl! 🎁",
            },
        ],
    },
]


# =====================================================
# BIRTHDAY LETTER
# =====================================================

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
# PINK ROMANTIC THEME
# =====================================================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            145deg, #FFF1F6, #F6EFFF, #FFFAF7
        );
    }

    h1, h2, h3, h4 {
        color: #B83268 !important;
    }

    .stApp p,
    .stApp label,
    .stApp li,
    .stMarkdown {
        color: #493447;
    }

    .stCaption,
    [data-testid="stCaptionContainer"] {
        color: #76546B !important;
    }

    .birthday-card {
        background: #FFFFFF;
        color: #493447 !important;
        padding: 22px;
        border-radius: 20px;
        border: 1px solid #FFD6E5;
        line-height: 1.9;
    }

    div.stButton > button {
        border-radius: 22px;
        min-height: 45px;
        background: #F8B4CE;
        color: #49283B !important;
        border: 1px solid #F08BB2;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background: #E98CB4;
        color: #FFFFFF !important;
        border-color: #D85C91;
    }

    [data-testid="stRadio"] label p {
        color: #493447 !important;
    }

    [data-testid="stProgressBar"] > div > div {
        background-color: #E77DA8;
    }

    .stApp a {
        color: #B83268 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =====================================================
# GAME STATE
# =====================================================

def reset_game():
    st.session_state.level = 0
    st.session_state.question = 0
    st.session_state.solved = set()
    st.session_state.hearts = 0
    st.session_state.started = False
    st.session_state.candle_blown = False
    st.session_state.ask_improvement = False
    st.session_state.improvement_answer = ""
    st.session_state.memories_revealed = False


if "level" not in st.session_state:
    reset_game()


def question_key(level, question):
    return f"{level}_{question}"


def show_progress():
    hearts = st.session_state.hearts

    st.write("### Your earned hearts")
    st.write(" ".join(
        ["💗"] * hearts + ["🤍"] * (3 - hearts)
    ))
    st.progress(hearts / 3)


# =====================================================
# WELCOME SCREEN
# =====================================================

if not st.session_state.started:
    st.markdown(
        "<h1 style='text-align:center;'>🎀🎂</h1>",
        unsafe_allow_html=True,
    )

    st.title(f"Happy Birthday, {SEJU}!")
    st.subheader(
        "Welcome to your little birthday adventure 💗"
    )

    st.write(
        "Okay birthday girl, your present isn't arriving "
        "in a box. It's arriving with questions, hearts, "
        "and a boyfriend who has clearly spent too much "
        "time coding. 🤓"
    )
    st.write(
        "Complete all three levels to unlock your surprise."
    )

    if st.button(
        "Start my birthday adventure ✨",
        use_container_width=True,
    ):
        st.session_state.started = True
        st.rerun()


# =====================================================
# QUIZ LEVELS
# =====================================================

elif st.session_state.level < len(QUESTIONS):
    level_index = st.session_state.level
    level_data = QUESTIONS[level_index]
    question_index = st.session_state.question
    question_data = level_data["questions"][question_index]
    key = question_key(level_index, question_index)

    st.caption(
        f"LEVEL {level_index + 1} OF {len(QUESTIONS)}"
    )
    st.title(level_data["title"])
    st.write(level_data["intro"])

    show_progress()

    st.progress(
        (question_index + 1)
        / len(level_data["questions"])
    )

    st.subheader(
        f"Question {question_index + 1}: "
        f"{question_data['q']}"
    )

    if key not in st.session_state.solved:
        choice = st.radio(
            "Choose your answer:",
            question_data["options"],
            key=f"choice_{key}",
        )

        if st.button(
            "Lock in my answer 💌",
            use_container_width=True,
            key=f"submit_{key}",
        ):
            selected_index = (
                question_data["options"].index(choice)
            )

            if selected_index == question_data["correct"]:
                st.session_state.solved.add(key)
                st.session_state[f"feedback_{key}"] = "correct"
                st.rerun()
            else:
                st.session_state[f"feedback_{key}"] = "wrong"

        if st.session_state.get(
            f"feedback_{key}"
        ) == "wrong":
            st.error(
                "Nope! Try again, birthday girl. 😏 "
                "Hint: you know this one!"
            )

    else:
        st.success(question_data["success"])

        if question_index < len(level_data["questions"]) - 1:
            if st.button(
                "Next question ➜",
                use_container_width=True,
                key=f"next_{key}",
            ):
                st.session_state.question += 1
                st.rerun()

        else:
            if st.button(
                "Complete this level 💗",
                use_container_width=True,
                key=f"complete_{level_index}",
            ):
                st.session_state.hearts = min(
                    3, st.session_state.hearts + 1
                )
                st.session_state.level += 1
                st.session_state.question = 0
                st.rerun()

    st.divider()
    st.caption(
        f"Complete Level {level_index + 1} "
        "to unlock the next one."
    )


# =====================================================
# CANDLE AND BIRTHDAY WISH
# =====================================================

elif not st.session_state.candle_blown:
    st.balloons()

    st.title(f"You did it, {SEJU}! 🎉")
    st.write("Three levels completed. Three hearts earned. 🩷")
    show_progress()

    st.markdown(
        "<h1 style='text-align:center;font-size:85px;'>🕯️</h1>",
        unsafe_allow_html=True,
    )

    st.subheader("Make a birthday wish ✨")
    st.write(
        "Take a tiny moment for yourself. You deserve "
        "good things, happy days, and cake. Especially cake."
    )

    if st.button(
        "Blow out the candle 💨",
        use_container_width=True,
    ):
        st.session_state.candle_blown = True
        st.session_state.ask_improvement = True
        st.rerun()


# =====================================================
# HEART-TO-HEART QUESTION
# =====================================================

elif st.session_state.ask_improvement:
    st.markdown(
        "<h1 style='text-align:center;'>💌🩷</h1>",
        unsafe_allow_html=True,
    )

    st.title(f"One little question, {SEJU}... 🥹💗")

    st.write(
        "Before I show you your final surprise, "
        "there's something I really want to ask you."
    )
    st.write(
        "I love you, and I want to keep learning how "
        "to love you better. You can be completely "
        "honest with me. ❤️"
    )

    options = [
        "Listen to you more and understand your feelings ❤️",
        "Give you more time, attention, and affection 🫂",
        "Be more patient during disagreements 🌷",
        "Communicate better and express my feelings 💬",
        "Understand you better instead of assuming things 🥹",
        "Respect your space and personal boundaries 🦋",
        "Show my love more through actions 💗",
        "Something else — let me tell you ✍️",
    ]

    custom_option = "Something else — let me tell you ✍️"

    improvement = st.radio(
        "What is one thing you'd like me to improve in my behaviour?",
        options,
        index=0,
        key="improvement_choice",
    )

    custom_answer = ""

    if improvement == custom_option:
        custom_answer = st.text_area(
            "Tell me honestly, meri jaan 💌",
            placeholder="I'll listen with an open heart...",
            key="custom_improvement_answer",
        )

    if st.button(
        "Continue to my surprise 🎁",
        use_container_width=True,
    ):
        if improvement == custom_option and not custom_answer.strip():
            st.warning(
                "Write your answer first, meri jaan. 🫶"
            )
        else:
            if improvement == custom_option:
                st.session_state.improvement_answer = (
                    custom_answer.strip()
                )
            else:
                st.session_state.improvement_answer = improvement

            st.session_state.ask_improvement = False
            st.rerun()


# =====================================================
# FINAL SURPRISE
# =====================================================

else:
    st.balloons()

    st.title(f"One last thing, {SEJU}... 🥹💗")
    st.write("You made it! Your final surprise is waiting.")
    st.write(
        "Thank you for sharing your honest answer with me. 🫶"
    )

    romantic_background_music()

    st.divider()

    if not st.session_state.memories_revealed:
        st.markdown(
            "<h1 style='text-align:center;'>🎁💌🎀</h1>",
            unsafe_allow_html=True,
        )

        st.subheader(
            "A little surprise is waiting for you..."
        )
        st.write(
            "Ready to unlock some of our favourite memories? "
            "This one's made just for you. 🥹💗"
        )

        if st.button(
            "💗 Open your memories 💗",
            use_container_width=True,
        ):
            st.session_state.memories_revealed = True
            st.rerun()

    else:
        st.markdown(
            "<h1 style='text-align:center;'>"
            "Happy Birthday, Mari jaan! 🥹❤️"
            "</h1>",
            unsafe_allow_html=True,
        )

        st.write(
            "A few little moments that became special "
            "because I got to share them with you. 💗"
        )

        captions = [
            "Our favourite photo 💗",
            "A cute memory 🫶",
            "Our silly side 😂",
            "One for the forever folder 💌",
        ]

        columns = st.columns(2)

        for i, caption in enumerate(captions, start=1):
            image_path = PHOTO_FOLDER / f"photo{i}.jpg"

            with columns[(i - 1) % 2]:
                if image_path.is_file():
                    st.image(
                        str(image_path),
                        caption=caption,
                        use_container_width=True,
                    )
                else:
                    st.warning(
                        f"Photo not found: photos/photo{i}.jpg"
                    )

        st.divider()
        st.subheader("A little letter for you 💌")

        # Escape HTML characters before displaying the letter.
        import html

        safe_letter = html.escape(BIRTHDAY_LETTER).replace(
            "\n", "<br>"
        )

        st.markdown(
            f"<div class='birthday-card'>{safe_letter}</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<h2 style='text-align:center;'>"
            "Happy birthday, my girl. 🩷"
            "</h2>",
            unsafe_allow_html=True,
        )

        if st.button(
            "Play the adventure again 🎊",
            use_container_width=True,
        ):
            reset_game()

            # Clear old answers so a replay starts fresh.
            for state_key in list(st.session_state.keys()):
                if (
                    state_key.startswith("choice_")
                    or state_key.startswith("feedback_")
                    or state_key.startswith("submit_")
                    or state_key.startswith("next_")
                    or state_key.startswith("complete_")
                    or state_key in (
                        "improvement_choice",
                        "custom_improvement_answer",
                    )
                ):
                    del st.session_state[state_key]

            st.rerun()
