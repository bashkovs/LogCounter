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

- [optional] setup python environment, activate it and install required dependencies

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    bash get_weights.sh
    ```

- or build docker container

    ```bash
    docker build -t log_counter .
    ```

## ⚙️ run

```bash
uvicorn main:app --host 0.0.0.0 --port 5005
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
@app.get("/")                   # Gradio-demo UI
@app.post("/recognize/")        # recognize image (image bytes)
@app.get("/healthcheck/")       # service health check
```

example of server response
```json
{
  "total": 94,
  "detections": {
    "0": [[513, 988], [561, 988], [513, 1052], [561, 1052]],
    "1": [[548, 1049], [593, 1049], [548, 1107], [593, 1107]],
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
- [done] mini web-ui interface for visual interaction with the model
- [done] visual sorting of contours for easy viewing
- some little fixes

```
A moment of self-reflection
Thanks for reading up to this point.
Yes, the depth of my knowledge is not enough to understand well how low-level model is organized, but I can independently do almost any task from zero to MVP and a little more. It will be a little while before I fill in the gaps in my knowledge.
```