from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool

# Uncomment the following line to use an example of a custom tool
# from realestate_agent.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class RealestateAgentCrew():
	"""RealestateAgent crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	scrape_tool = ScrapeWebsiteTool(
		website_url="https://www.rightmove.co.uk"
	)

	@agent
	def realestate_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['realestate_agent'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
		)

	@task
	def realestate_task(self) -> Task:
		return Task(
			config=self.tasks_config['realestate_task'],
			agent=self.realestate_agent(),
			tools=[self.scrape_tool]
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			agent=self.reporting_analyst(),
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the RealestateAgent crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			memory=True
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)