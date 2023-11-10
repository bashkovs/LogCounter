<div align="center">
  <p>
    <a align="center" href="" target="_blank">
      <img
        width="100%"
        src="https://ltdfoto.ru/images/2023/11/10/banner.png"
      >
    </a>
  </p>
</div>

## 👋 hello

This api service provides the ability to count the number of wooden logs in the input image. The output is a json-formatted response with an outline of each log detected by the model.

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