# How to install project

# Install prometheus
Keep it simply, use docker!
```
docker run -p 9090:9090  prom/prometheus
```
After it, go to http://127.0.0.1:9090

# Install project
Clone and run it:
```
git clone ... tornad-prometheus
cd tornad-prometheus
pip install -r requirements.txt
python app/app.py
```
Then go to http://127.0.0.1:8888

# Prometheus stats
