#!/usr/bin/env python
from realestate_agent.crew import RealestateAgentCrew
import os


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'Real estate trend',
        'postcode': os.getenv('POSTCODE')
    }
    RealestateAgentCrew().crew().kickoff(inputs=inputs)