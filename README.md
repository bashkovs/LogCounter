<div align="center">
  <p>
    <a align="center" href="" target="_blank">
      <img
        width="100%"
        src="https://github.com/bashkovs/assets/blob/main/LogCounter/banner.png"
      >
    </a>
  </p>
</div>

## 👋 hello

This api service allows you to count the number of wooden logs in the input image. The output is a json response with the number of each log detected by the model and its coordinates.

## 💻 install

- clone repository and navigate to example directory

    ```bash
    git clone https://github.com/bashkovs/LogCounter.git
    cd LogCounter
    ```

- download model weigts files

    ```bash
    bash ./get_weights.sh
    ```

- [optional] setup python environment, activate it and install required dependencies

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

- or build docker container

    ```bash
    docker build -t log_counter .
    ```

## ⚙️ run

```bash
python app.py
```
or start docker container

```bash
docker run -it --rm -p 5005:5005 log_counter
```

## 👨‍🔬 test
use `tests/check_worker.py` to push test requests to the server
```bash
cd tests
python check_worker.py
```

routers of service
```python
@app.route("/")                             # mini-webUI in future
@app.route("/recognize", methods=["POST"])  # recognize image (image bytes)
@app.route("/healthcheck")                  # service health check
```

example of server response
```json
{
  "total": 94,
  "detections": {
    "0": [
      [513.322265625,988.398193359375],
      [561.0213623046875,988.398193359375],
      [513.322265625,1052.563720703125],
      [561.0213623046875,1052.563720703125]
    ],
    "1": [
      [548.3073120117188,1049.979736328125],
      [593.6986694335938,1049.979736328125],
      [548.3073120117188,1107.452880859375],
      [593.6986694335938,1107.452880859375]
    ],
    ... ... ...
  }
}
```

## 🖼️ example of results
<div align="center">
  <p>
    <a align="center" href="" target="_blank">
      <img
        width="80%"
        src="https://github.com/bashkovs/assets/blob/main/LogCounter/results/test1_result.jpeg"
      >
    </a>
  </p>
</div>

## 🔮 in future
- mini web-ui interface for visual interaction with the model
- [done] visual sorting of contours for easy viewing
- some little fixes

```
A moment of self-reflection
Thanks for reading up to this point.
Yes, the depth of my knowledge is not enough to understand well how low-level model is organized, but I can independently do almost any task from zero to MVP and a little more. It will be a little while before I fill in the gaps in my knowledge.
```