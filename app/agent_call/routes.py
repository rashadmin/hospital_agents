from flask import Flask, request, jsonify
from app.agent_call.graph import graph
from app.agent_call.external import background_listener, active_thread_id
import threading
from app.agent_call import bp
# Start listener thread when app launches
listener_thread = threading.Thread(target=background_listener, args=(graph,), daemon=True)
listener_thread.start()

@bp.route("/agent", methods=["POST"])
# @app.route("/agent")
def run_agent():
    # global active_thread_id

    # data = request.json
    # user_input = data.get("message")
    # thread_id = data.get("thread_id", "default")
    # active_thread_id = thread_id

    # config = {"configurable": {"thread_id": thread_id}}

    # result = graph.invoke({"requests": [], "last_id": "0"}, config=config)
    return 'hello world'
    # return jsonify({
    #     "thread_id": thread_id,
    #     "response": result
    # })

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000, debug=True)
