"""Camera server application."""

import json
import shlex
import subprocess

import zmq


PIPELINES = {
    "mystream": [
        "v4l2src",
        "video/x-raw,width=640,height=480",
        "nvvidconv",
        "nvv4l2h264enc",
        "queue",
        "rtspclientsink location=rtsp://localhost:8554/mystream latency=0",
    ]
}

streams = {}


def main():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.bind("tcp://*:5555")

    print("Listening for camera topics")
    socket.setsockopt_string(zmq.SUBSCRIBE, "/cameras")

    while True:
        msg_str = socket.recv_string()
        topic, data_str = msg_str.split(" ", 1)
        value = json.loads(data_str)
        print(f"Received message: topic={topic} value={value}")

        camera_id, subtopic = topic.split("/")[2:4]
        if camera_id not in PIPELINES:
            print(f"Unknown stream {camera_id}")
            continue

        if subtopic == "enabled":
            enabled = value
            if enabled:
                start_stream(camera_id)
            else:
                stop_stream(camera_id)
        else:
            print(f"Unknown subtopic {subtopic}")
            continue


def start_stream(camera_id):
    global streams
    if camera_id in streams:
        print(f"Camera stream {camera_id} is already running")
    else:
        cmd = shlex.split(f"gst-launch-1.0 {' ! '.join(PIPELINES[camera_id])}")
        print(f"Starting camera pipeline for {camera_id}")
        print(cmd)
        streams[camera_id] = subprocess.Popen(cmd)


def stop_stream(camera_id):
    global streams
    if camera_id in streams:
        try_shutdown(camera_id)
        del streams[camera_id]
    else:
        print(f"Camera stream {camera_id} is not running")


def try_shutdown(camera_id):
    global streams
    print(f"Terminating pipeline for {camera_id}")
    streams[camera_id].terminate()
    try:
        streams[camera_id].wait(5)
    except subprocess.TimeoutExpired:
        print("ERROR: timed out waiting for pipeline to terminate")
    else:
        print("Stream terminated cleanly")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Shutting down")
    for stream in streams:
        try_shutdown(stream)
