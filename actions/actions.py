from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionCalculateIMC(Action):

	def name(self):
		return "action_calculate_imc"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: dict) -> list:

		weight = tracker.get_slot("weight")
		height = tracker.get_slot("height")

		if weight and height:
			try:
				imc = float(weight) / (float(height) ** 2)
				dispatcher.utter_message(text=f"Seu IMC é {imc:.2f}.")
				return []
			except ValueError:
				dispatcher.utter_message(text="Desculpe, os valores fornecidos não são válidos.")
		else:
			dispatcher.utter_message(text="Não consegui calcular seu IMC devido a valores ausentes.")

		# Pergunta novamente o peso ao final da interação
		dispatcher.utter_message(response="utter_ask_weight")

		return []
