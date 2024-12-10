# Protocol Specification

Messages between nodes shall contain a topic name and a value.

Topic names shall start with a `/` and may contain alphanumeric characters in addition to `_` and `/`. Topic names shall not include whitespace. Topic names should be structured with additional `/` separators to organize topics into logical groups.

## Serialization

### WebSocket

Messages sent via WebSocket shall be encoded as a JSON string. The underlying JSON object shall have the following fields:

- `topic`: The topic name as described above.
- `value`: Arbitrary JSON data to be sent on the topic.

Example:

```json
{"topic":"/cameras/mystream/enabled","value":true}
```

### ZMQ

Messages sent via ZMQ socket shall be encoded as a UTF-8 string. The string shall be comprised of the topic name followed by a single space and then a JSON string representing the value.

Example:

```python
"/cameras/mystream/enabled True"
```

## Topics

### Cameras

Camera topics shall follow the pattern `/cameras/<camera_id>/<subtopic>`.

#### Camera IDs

- `mystream`

#### Camera subtopics

- `/cameras/<camera_id>/enabled`: Set this value to True to enable the camera stream and False to disable the camera stream.


