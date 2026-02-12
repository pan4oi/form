import streamlit as st

def main():
    st.title("Тест по История и География")
    st.write("Напишете правилните отговори в полетата под всеки въпрос:")

    quiz_data = [
        {
            "question": "Коя е най-високата планина в България?",
            "answer": "Рила"
        },
        {
            "question": "Кой град е бил столица на България преди София?",
            "answer": "Велико Търново"
        },
        {
            "question": "През кой месец честваме Деня на независимостта на България? (напишете само месеца)",
            "answer": "Септември"
        },
        {
            "question": "Коя река е естествена граница между България и Румъния?",
            "answer": "Дунав"
        },
        {
            "question": "Кой български владетел е приел християнството?",
            "answer": "Княз Борис I"
        }
    ]

    with st.form("quiz_form"):
        user_answers = []
        
        for i, item in enumerate(quiz_data):
            ans = st.text_input(f"{i+1}. {item['question']}", key=f"q{i}")
            user_answers.append(ans)
        
        submitted = st.form_submit_button("Провери отговорите")

    if submitted:
        score = 0
        st.divider()
        
        for i, item in enumerate(quiz_data):
            user_ans = user_answers[i].lower()
            correct_ans = item['answer'].lower()

            if user_ans == correct_ans:
                st.success(f"Въпрос {i+1}: Правилно! ({item['answer']})")
                score += 1
            elif user_ans == "":
                st.warning(f"Въпрос {i+1}: Не сте дали отговор.")
            else:
                st.error(f"Въпрос {i+1}: Грешно. Правилният отговор е: {item['answer']}")

        st.subheader(f"Общ резултат: {score}/{len(quiz_data)}")
        
        if score == len(quiz_data):
            st.balloons()
            st.success("Отличен! Ти си експерт!")
        elif score >= 3:
            st.info("Много добре!")
        else:
            st.warning("Опитай пак за по-добър резултат.")

if __name__ == "__main__":
    main()
