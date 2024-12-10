"""Camera server application."""

import json

import zmq


def main():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.bind("tcp://*:5555")

    print("Listening for camera topics")
    socket.setsockopt_string(zmq.SUBSCRIBE, "/cameras")

    while True:
        msg_str = socket.recv_string()
        topic, data_str = msg_str.split(" ", 1)
        data = json.loads(data_str)
        print(f"Received message: topic={topic} data={data}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Shutting down")
