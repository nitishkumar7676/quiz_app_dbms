import sqlite3

def questions():
    conn = sqlite3.connect("quiz_app.db")
    cursor = conn.cursor()


 questions = {
    "Science": {
        1: {
            "question": "What is the chemical symbol for water?",
            "options": ["A) H2", "B) O2", "C) H2O", "D) CO2"],
            "answer": "C"
        },
        2: {
            "question": "What planet is closest to the sun?",
            "options": ["A) Venus", "B) Earth", "C) Mercury", "D) Mars"],
            "answer": "C"
        },
        3: {
            "question": "What gas do plants primarily absorb for photosynthesis?",
            "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Methane"],
            "answer": "B"
        },
        4: {
            "question": "What part of the human body produces insulin?",
            "options": ["A) Liver", "B) Pancreas", "C) Stomach", "D) Kidney"],
            "answer": "B"
        },
        5: {
            "question": "Which organ is primarily responsible for filtering blood?",
            "options": ["A) Heart", "B) Liver", "C) Kidney", "D) Lungs"],
            "answer": "C"
        },
        6: {
            "question": "What is the process by which plants make their food called?",
            "options": ["A) Respiration", "B) Digestion", "C) Photosynthesis", "D) Fermentation"],
            "answer": "C"
        },
        7: {
            "question": "What is the boiling point of water at sea level?",
            "options": ["A) 50°C", "B) 100°C", "C) 200°C", "D) 150°C"],
            "answer": "B"
        },
        8: {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Jupiter", "B) Saturn", "C) Neptune", "D) Earth"],
            "answer": "A"
        },
        9: {
            "question": "What is the powerhouse of the cell?",
            "options": ["A) Nucleus", "B) Mitochondria", "C) Ribosome", "D) Cytoplasm"],
            "answer": "B"
        },
        10: {
            "question": "What is the basic unit of life?",
            "options": ["A) Atom", "B) Cell", "C) Tissue", "D) Organ"],
            "answer": "B"
        }
    },
    "Math": {
        1: {
            "question": "What is 7 + 6?",
            "options": ["A) 11", "B) 12", "C) 13", "D) 14"],
            "answer": "C"
        },
        2: {
            "question": "What is the square root of 64?",
            "options": ["A) 6", "B) 8", "C) 10", "D) 12"],
            "answer": "B"
        },
        3: {
            "question": "What is the value of π (pi) approximately?",
            "options": ["A) 3.14", "B) 2.72", "C) 1.62", "D) 3.67"],
            "answer": "A"
        },
        4: {
            "question": "What is 15% of 200?",
            "options": ["A) 20", "B) 30", "C) 15", "D) 25"],
            "answer": "B"
        },
        5: {
            "question": "What is 9 x 8?",
            "options": ["A) 64", "B) 72", "C) 81", "D) 90"],
            "answer": "B"
        },
        6: {
            "question": "What is 1/2 + 1/4?",
            "options": ["A) 1/2", "B) 1", "C) 3/4", "D) 5/4"],
            "answer": "C"
        },
        7: {
            "question": "What is the area of a rectangle with length 8 and width 5?",
            "options": ["A) 40", "B) 30", "C) 20", "D) 50"],
            "answer": "A"
        },
        8: {
            "question": "What is 100 divided by 4?",
            "options": ["A) 25", "B) 20", "C) 30", "D) 50"],
            "answer": "A"
        },
        9: {
            "question": "What is the result of 2³?",
            "options": ["A) 6", "B) 8", "C) 9", "D) 12"],
            "answer": "B"
        },
        10: {
            "question": "What is the perimeter of a square with side length 6?",
            "options": ["A) 24", "B) 18", "C) 36", "D) 12"],
            "answer": "A"
        }
    },
    "Social Science": {
        1: {
            "question": "Who is known as the Father of the Nation in India?",
            "options": ["A) Jawaharlal Nehru", "B) Mahatma Gandhi", "C) B. R. Ambedkar", "D) Subhas Chandra Bose"],
            "answer": "B"
        },
        2: {
            "question": "What is the capital of the United States?",
            "options": ["A) New York", "B) Washington, D.C.", "C) Los Angeles", "D) Chicago"],
            "answer": "B"
        },
        3: {
            "question": "Who wrote the Indian Constitution?",
            "options": ["A) Mahatma Gandhi", "B) B. R. Ambedkar", "C) Jawaharlal Nehru", "D) Sardar Patel"],
            "answer": "B"
        },
        4: {
            "question": "Which war ended in 1945?",
            "options": ["A) World War I", "B) World War II", "C) Cold War", "D) Vietnam War"],
            "answer": "B"
        },
        5: {
            "question": "What is the term for a system of government where citizens vote for representatives?",
            "options": ["A) Dictatorship", "B) Democracy", "C) Monarchy", "D) Oligarchy"],
            "answer": "B"
        },
        6: {
            "question": "What is the study of the past called?",
            "options": ["A) Archaeology", "B) History", "C) Sociology", "D) Anthropology"],
            "answer": "B"
        },
        7: {
            "question": "Which country is the largest by area?",
            "options": ["A) USA", "B) Canada", "C) Russia", "D) China"],
            "answer": "C"
        },
        8: {
            "question": "What does GDP stand for?",
            "options": ["A) Gross Domestic Product", "B) General Domestic Production", "C) Gross Development Plan", "D) General Development Plan"],
            "answer": "A"
        },
        9: {
            "question": "Who discovered America in 1492?",
            "options": ["A) Vasco da Gama", "B) Christopher Columbus", "C) Ferdinand Magellan", "D) Marco Polo"],
            "answer": "B"
        },
        10: {
            "question": "Which revolution is associated with the guillotine?",
            "options": ["A) Industrial Revolution", "B) Russian Revolution", "C) American Revolution", "D) French Revolution"],
            "answer": "D"
        }
    }
}


    for subject, subject_questions in questions.items():
        for question in subject_questions:
            cursor.execute("""
            INSERT INTO questions (subject, question, options, answer)
            VALUES (?, ?, ?, ?)""", (subject, question["q"], ", ".join(question["o"]), question["a"]))

    conn.commit()
    conn.close()
    print("Questions added successfully!")

if __name__ == "__main__":
    questions()
