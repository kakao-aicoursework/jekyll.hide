import json
import reflex as rx
from langchain.chat_models import ChatOpenAI

from langchain.llms import OpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

with open("chatbot/project_data_카카오싱크.txt") as f:
    pre_load_data = f.read()
    f.close()


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
            SystemMessage(content="You are a friendly chatbot."),
            HumanMessage(content="카카오 싱크에 대해 설명해줘"),
            AIMessage(content=pre_load_data),
        ]

        for qa in self.chats[self.current_chat][1:]:
            messages.append(HumanMessage(content=qa.question))
            messages.append(AIMessage(content=qa.answer))

        messages.append(HumanMessage(content=self.question))
        llm = ChatOpenAI(temperature=1)
        session = llm(messages)

        qa = QA(question=self.question, answer="")
        self.chats[self.current_chat].append(qa)

        answer_text = session.content
        self.chats[self.current_chat][-1].answer += answer_text
        self.chats = self.chats
        yield
