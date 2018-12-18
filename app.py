from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "2077"
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
	'state3',
	'state4',
	'state5',
	'state6',
	'state7'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
                'state3',
                'state4',
                'state5'
            ],
            'dest': 'user'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state6'
            ],
            'dest': 'user'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state7'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
