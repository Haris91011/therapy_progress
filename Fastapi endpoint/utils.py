import random
from operator import itemgetter
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()


def generate_unique_key(existing_keys):
    while True:
        key = random.randint(100, 999)  # generate a random no.  between 100 and 999
        if key not in existing_keys:
            return key
        


# Chain to reraank the session summaries
def ranker_chain(content):
    try:
        prompt_str="""     
        
        Analyze the following session summaries provided in the dictionary where the key represents the session number and the value represents the session summary text. Rank them in chronological order, with the oldest session receiving rank 1, followed by the next chronological session as rank 2, and so on. Your response should be in the format:
        1: <key of oldest session> \n\n 2: <key of next oldest session>\n\n  3: <key of most recent session>

        Ensure that you rank them based on how they appear chronologically, and return only the ranking and their associated keys.

        (((sessions summaries: {sessions})))
        """
        ranker_prompt = ChatPromptTemplate.from_template(prompt_str)
        chat_llm = ChatOpenAI(model="gpt-4o-mini",api_key=os.getenv("OPENAI_API_KEY"))
        setup={"sessions":itemgetter("sessions")}
        output_parser=StrOutputParser()
        ranker_chain = (setup|ranker_prompt|chat_llm|output_parser)
        response=ranker_chain.invoke({"sessions":content}).split("\n\n")
        return response
    except Exception as e:
        raise Exception(str(e))
    
# progress generation chain
def progress_genertaion_chain(content):
    try:
        prompt_str="""   
        You are a psychotherapist. Analyze the following session information across multiple sessions to predict the client's progress. Determine if the progress is positive or negative based on the comparison between the first session and the subsequent sessions. Provide a clear one liner explanation for your prediction.\n
        **Steps to Complete Task:**
        1-Read and analyze the content of each session.\n
        2-Compare the client's reported symptoms, behaviors, and progress between sessions.\n
        3-Determine if the overall progress is positive or negative.\n
        4-Provide a reason for the progress based on the client's behavior, responses to treatment, and any reported improvements or challenges.\n
        5-Use the first session as a baseline and compare subsequent sessions to identify trends or changes.\n
        6-Evaluate whether the client's stress, anxiety, or other key complaints have reduced or worsened.\n
        7-Include observations about the client's use of therapeutic strategies, changes in mood, and the impact on their daily functioning.\n

        Analyze the sessions and respond in the following format:
        Progress: (Positive Progress / Negative Progress) \n\n Reason:(Provide a reason for your evaluation based on changes in the client's symptoms, behaviors, and use of strategies.)

        (((**sessions data:** {sessions})))

        """
        progress_prompt = ChatPromptTemplate.from_template(prompt_str)
        chat_llm = ChatOpenAI(model="gpt-4o-mini",api_key=os.getenv("OPENAI_API_KEY"))
        setup={"sessions":itemgetter("sessions")}
        output_parser=StrOutputParser()
        progress_chain = (setup|progress_prompt|chat_llm|output_parser)
        response=progress_chain.invoke({"sessions":content})
        return response
    except Exception as e:
        raise Exception(str(e))






