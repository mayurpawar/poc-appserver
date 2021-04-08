# poc-appserver
 
This is POC project. This will will craete a web app that will insert a date time stamp in a MySQL database.

Use requiared name. In this example it is pluto.
Also we need a host port. This app listens on port 80. So make sure you use port 80 as a container port.

Below is the folder structure of this code.
```bash
.
├── Dockerfile
├── LICENSE
├── README.md
├── apis
│   ├── rules
│   │   ├── app.py
│   │   └── version.py
│   └── specs
│       └── swagger.yml
├── app.ini
├── buildspec.yaml
├── requirements.txt
└── server.py
```

## Installation as a docker container
```bash
docker build -t pluto .
docker run -p 5000:80 pluto
```
Access app at localhost:5000. This port is same that was used above. You can choose your preferred port. 
If app is enabled to use uwsgi protocol then you may need a proxy server in order to access it.

## Installation as a Flask App. Use python virtual environment if required.
```bash
pip install flask
export FLASK_APP=server.py
flask run
```
Access app at localhost:80 
If app is enabled to use uwsgi protocol then you may need a proxy server in order to access it.

## Contributing
Pull requests are welcome. This code is for very specific purpose and is kept here for evaluation.

This repository will be deleted in a week's time.

## License
[MIT](https://choosealicense.com/licenses/mit/)
