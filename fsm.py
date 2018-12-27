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
            return text.lower() == 'song1'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'song2'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'song3'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'song4'
        return False

    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'Hi'
        return False

    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'tell me a joke'
        return False

    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'news'
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Pantera - Cowboys from Hell")

    #def on_exit_state1(self):
        #print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Machine Head - Locust")

    #def on_exit_state2(self):
        #print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "DOWN - Stone the Crow")

    #def on_exit_state3(self):
        #print('Leaving state3')

    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Bush - Glycerine")
        self.go_back()

    def on_exit_state4(self):
        print('Leaving state4')

    def on_enter_state5(self, event):
        print("I'm entering state5")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Hello, world!")
        self.go_back()

    def on_exit_state5(self):
        print('Leaving state5')

    def on_enter_state6(self, event):
        print("I'm entering state6")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "How many tickles does it take to make an octupus laugh? Ten. Tentacles!")
        self.go_back()

    def on_exit_state6(self):
        print('Leaving state6')

    def on_enter_state7(self, event):
        print("I'm entering state7")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "https://www.reuters.com")
        self.go_back()

    def on_exit_state7(self):
        print('Leaving state10')

