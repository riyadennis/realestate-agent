#!/usr/bin/env python
from realestate_agent.crew import RealestateAgentCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    RealestateAgentCrew().crew().kickoff(inputs=inputs)