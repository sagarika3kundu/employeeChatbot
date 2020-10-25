# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Action, Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT

class form_1(FormAction):
   """Example of a custom form action"""

   def name(self):
       # type: () -> Text
       """Unique identifier of the form"""

       return "form_1"
   
   @staticmethod
   def required_slots(tracker): # -&gt; List[Text] # type: () -&gt; List[Text]
    return ["region", "rel"]

   def slot_mapping(self, tracker):
       
       return {"region": self.from_entity(entity="region"), "rel": self.from_entity(entity="rel")}



   
   def submit(self, dispatcher, tracker, domain):
       # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
       """Define what the form has to do
           after all required slots are filled"""

       # utter submit template
       dispatcher.utter_template('utter_dot', tracker)
       return []

class form_2(FormAction):
   def name(self):
       return "form_2"

   @staticmethod
   def required_slots(tracker):
        return ["doc_desc"]

   def slot_mappings(self):
        return {"doc_desc": self.from_text()}

   def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_submit', tracker)
        return []