import os

import openai
import reflex as rx

openai.api_key = os.environ['OPENAI_API_KEY']


class QA(rx.Base):
    question: str
    answer: str


class State(rx.State):
    chats: dict[str, list[QA]] = {
        "Intros": [QA(question="안녕. 몇가지 물어봐도 될까?", answer="그럼요! 무엇이든 물어보세요!")],
    }
    current_chat = "Intros"
    question: str
    new_chat_name: str = ""

    def process_question(self, form_data: dict[str, str]):
        self.question = form_data["question"]
        if (
                self.chats[self.current_chat][-1].question == self.question
                or self.question == ""
        ):
            return

        messages = [
            {"role": "system", "content": "You are a friendly chatbot."}
        ]

        for qa in self.chats[self.current_chat][1:]:
            messages.append({"role": "user", "content": qa.question})
            messages.append({"role": "assistant", "content": qa.answer})

        messages.append({"role": "user", "content": self.question})

        session = openai.ChatCompletion.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=messages,
            stop=None,
            temperature=1,
            stream=True,
        )
        qa = QA(question=self.question, answer="")
        self.chats[self.current_chat].append(qa)

        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer_text = item.choices[0].delta.content
                self.chats[self.current_chat][-1].answer += answer_text
                self.chats = self.chats
                yield
