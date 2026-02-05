import streamlit as st

def main():
    st.title("Тест по История и География")
    st.write("Изберете по един отговор за всеки въпрос:")

    quiz_data = [
        {
            "question": "Коя е най-високата планина в България?",
            "options": ["Стара планина", "Пирин", "Рила", "Родопи"],
            "answer": "Рила"
        },
        {
            "question": "Кой град е бил столица на България преди София?",
            "options": ["Пловдив", "Велико Търново", "Варна", "Видин"],
            "answer": "Велико Търново"
        },
        {
            "question": "През кой месец честваме Деня на независимостта на България?",
            "options": ["Март", "Май", "Септември", "Ноември"],
            "answer": "Септември"
        },
        {
            "question": "Коя река е естествена граница между България и Румъния?",
            "options": ["Искър", "Марица", "Дунав", "Места"],
            "answer": "Дунав"
        },
        {
            "question": "Кой български владетел е приел християнството?",
            "options": ["Хан Аспарух", "Княз Борис I", "Цар Симеон Велики", "Хан Крум"],
            "answer": "Княз Борис I"
        }
    ]

    with st.form("quiz_form"):
        user_selections = []
        
        for i, item in enumerate(quiz_data):
            choice = st.radio(f"{i+1}. {item['question']}", item['options'], key=f"q{i}", index=None)
            user_selections.append(choice)
        
        submitted = st.form_submit_button("Провери резултата")

    if submitted:

        if None in user_selections:
            st.warning("Моля, отговорете на всички въпроси преди да изпратите!")
        else:
            score = 0
            st.divider()
            
            for i, item in enumerate(quiz_data):
                if user_selections[i] == item['answer']:
                    st.success(f"Въпрос {i+1}: Вярно!")
                    score += 1
                else:
                    st.error(f"Въпрос {i+1}: Грешно. Правилният отговор е: {item['answer']}")


            st.subheader(f"Общ резултат: {score}/5")
            if score == 5:
                st.balloons()
                st.success("Браво! Ти знаеш всичко!")
            elif score >= 3:
                st.info("Добър резултат!")
            else:
                st.warning("Имаш нужда от малко преговор.")


    main()

