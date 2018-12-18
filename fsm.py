from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state1'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state2'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state3'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state4'
        return False

    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state5'
        return False

    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state6'
        return False

    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state7'
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state1")
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state2")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state3")
        self.go_back()

    def on_exit_state3(self):
        print('Leaving state3')

    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state4")
        self.go_back()

    def on_exit_state4(self):
        print('Leaving state4')

    def on_enter_state5(self, event):
        print("I'm entering state5")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state5")
        self.go_back()

    def on_exit_state5(self):
        print('Leaving state5')

    def on_enter_state6(self, event):
        print("I'm entering state6")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state6")
        self.go_back()

    def on_exit_state6(self):
        print('Leaving state6')

    def on_enter_state7(self, event):
        print("I'm entering state7\nI'm entering state8\nI'm entering state9\nI'm entering state10")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state7\nI'm entering state8\nI'm entering state9\nI'm entering state10")
        self.go_back()

    def on_exit_state7(self):
        print('Leaving state10')

