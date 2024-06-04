from typing import Tuple
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import (
    Summary,
    IceBreaker,
    TopicOfInterest,
    summary_parser,
    ice_breaker_parser,
    topics_of_interest_parser,
)

def ice_break_with(name: str) -> Tuple[Summary, TopicOfInterest, IceBreaker, str]:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)

    summary_template = """
        given the information {information} about a person I want to create:
        1. a short summary
        2. two interesting facts about them
        \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm | summary_parser
    res: Summary = chain.invoke(input={"information": linkedin_data})

    topics_template = """
        given the information {information} about a person, list their topics of interest.
        \n{format_instructions}
    """
    
    topics_prompt_template = PromptTemplate(
        input_variables=["information"], template=topics_template,
        partial_variables={"format_instructions": topics_of_interest_parser.get_format_instructions()}
    )

    topics_chain = topics_prompt_template | llm | topics_of_interest_parser
    topics_of_interest: TopicOfInterest = topics_chain.invoke(input={"information": linkedin_data})

    ice_breakers_template = """
        given the information {information} about a person, suggest some ice breakers.
        \n{format_instructions}
    """
    
    ice_breakers_prompt_template = PromptTemplate(
        input_variables=["information"], template=ice_breakers_template,
        partial_variables={"format_instructions": ice_breaker_parser.get_format_instructions()}
    )

    ice_breakers_chain = ice_breakers_prompt_template | llm | ice_breaker_parser
    ice_breakers: IceBreaker = ice_breakers_chain.invoke(input={"information": linkedin_data})

    return res, topics_of_interest, ice_breakers, linkedin_data.get("profile_pic_url")

if __name__ == '__main__':
    load_dotenv()
    print('Ice Breaker')
    ice_break_with("Raul de Arriba jaume viladoms")
