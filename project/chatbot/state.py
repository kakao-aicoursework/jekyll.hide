import json
import chromadb
import reflex as rx
from langchain import LLMChain, ConversationChain
from langchain.chat_models import ChatOpenAI

from langchain.llms import OpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

from chatbot.datas import kakao_social, kakao_sync, kakaotalk_channel, parse_intent


class QA(rx.Base):
    question: str
    answer: str


def create_chain(llm, template, output_key):
    return LLMChain(
        llm=llm,
        prompt=ChatPromptTemplate.from_template(
            template=template
        ),
        output_key=output_key,
        verbose=True,
    )


def refine_data(data) -> str:
    splited = data.split("#")
    cate = splited[0].strip()
    res = {cate: {}}
    for data in splited[1:]:
        rows = [row.strip().strip(":") for row in data.split("\n") if row.strip() != ""]
        res[cate][rows[0]] = rows[1:]
    return json.dumps(res, ensure_ascii=False)


class State(rx.State):
    chats: dict[str, list[QA]] = {
        "Intros": [QA(question="안녕. 몇가지 물어봐도 될까?", answer="그럼요! 무엇이든 물어보세요!")],
    }
    current_chat = "Intros"
    question: str
    new_chat_name: str = ""

    def query_db(self, query: str, use_retriever: bool):

        _db = Chroma(
            persist_directory="chroma.db",
            embedding_function=OpenAIEmbeddings(),
            collection_name="chatbot",
        )
        _retriever = _db.as_retriever()
        if use_retriever:
            docs = self._retriever.get_relevant_documents(query)
        else:
            docs = self._db.similarity_search(query)
        str_docs = [doc.page_content for doc in docs]
        return str_docs

    @staticmethod
    def chain_factory(context: dict) -> LLMChain:
        llm = ChatOpenAI(temperature=0.1, max_tokens=4096, model="gpt-3.5-turbo")

        intent_chain = create_chain(
            llm=llm,
            template=parse_intent.format(msg=context['user_message'], intent_list=context['intent_list']),
            output_key="intent"
        )
        intent = intent_chain.run(context)

        if intent == "카카오싱크":
            return create_chain(llm=llm, template=refine_data(kakao_sync), output_key="sync")
        elif intent == "카카오소셜":
            return create_chain(llm=llm, template=refine_data(kakao_social), output_key="social")
        elif intent == "카카오톡채널":
            return create_chain(llm=llm, template=refine_data(kakaotalk_channel), output_key="kakaotalk")
        else:
            return ConversationChain(llm=llm, output_key="default")

    def process_question(self, form_data: dict[str, str]):
        context = {
            "user_message": form_data["question"],
            "intent_list": ["카카오싱크", "카카오소셜", "카카오톡채널", "etc"],
        }
        chain = self.chain_factory(context)

        self.question = form_data["question"]
        if (
                self.chats[self.current_chat][-1].question == self.question
                or self.question == ""
        ):
            return

        messages = [
            SystemMessage(content="You are a friendly chatbot."),
        ]

        for qa in self.chats[self.current_chat][1:]:
            messages.append(HumanMessage(content=qa.question))
            messages.append(AIMessage(content=qa.answer))

        messages.append(HumanMessage(content=self.question))
        # answer_text = chain.run(messages)
        #
        # qa = QA(question=self.question, answer="")
        # self.chats[self.current_chat].append(qa)
        #
        # print(answer_text)
        #
        # self.chats[self.current_chat][-1].answer += answer_text
        # self.chats = self.chats
        yield
