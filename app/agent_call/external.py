import redis
import threading
import time
from langchain_core.runnables.config import RunnableConfig
from langgraph.checkpoint.memory import MemorySaver

# Redis client
r = redis.Redis(host="localhost", port=6379, decode_responses=True)
STREAM_NAME = "requests"
active_thread_id = None  # updated per session
checkpointer = MemorySaver()

def background_listener(graph):
    """Continuously listen for Redis stream messages and update graph state."""
    last_id = "0"
    config = RunnableConfig(configurable={"thread_id": active_thread_id})  # trace tag

    while True:
        try:
            messages = r.xread({STREAM_NAME: last_id}, block=0, count=50)
            if messages:
                print(messages)
                for stream, entries in messages:
                    for entry_id, fields in entries:
                        graph.update_state(
                            values={
                                "requests": [{"id": entry_id, "data": fields}],
                                "last_id": entry_id
                            },
                            config=config   # 👈 traced in LangSmith if enabled
                        )
                        last_id = entry_id

            time.sleep(0.1)
        except Exception as e:
            print("Listener error:", e)
            time.sleep(1)
