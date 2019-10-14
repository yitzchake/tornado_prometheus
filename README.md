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

Basic metrics exported are:
* Garbage collector objects
* Endpoints number of time called
* Number of total requests
* Total seconds spend in each request

Examples:
```
 curl 127.0.0.1:8888/metrics
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 1376.0
python_gc_objects_collected_total{generation="1"} 364.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 172.0
python_gc_collections_total{generation="1"} 15.0
python_gc_collections_total{generation="2"} 1.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="6",patchlevel="5",version="3.6.5"} 1.0
# HELP tornado_http_request_duration_seconds HTTP request duration in seconds
# TYPE tornado_http_request_duration_seconds histogram
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="0.01",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="0.05",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="0.1",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="0.5",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="0.75",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="1.0",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="2.5",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="5.0",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="7.5",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="10.0",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="15.0",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="20.0",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="30.0",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MainHandler",le="+Inf",method="GET"} 1.0
tornado_http_request_duration_seconds_count{handler="MainHandler",method="GET"} 1.0
tornado_http_request_duration_seconds_sum{handler="MainHandler",method="GET"} 0.009666919708251953
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="0.01",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="0.05",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="0.1",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="0.5",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="0.75",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="1.0",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="2.5",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="5.0",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="7.5",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="10.0",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="15.0",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="20.0",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="30.0",method="GET"} 1.0
tornado_http_request_duration_seconds_bucket{handler="MetricsHandler",le="+Inf",method="GET"} 1.0
tornado_http_request_duration_seconds_count{handler="MetricsHandler",method="GET"} 1.0
tornado_http_request_duration_seconds_sum{handler="MetricsHandler",method="GET"} 0.004079103469848633
# TYPE tornado_http_request_duration_seconds_created gauge
tornado_http_request_duration_seconds_created{handler="MainHandler",method="GET"} 1.571094376741591e+09
tornado_http_request_duration_seconds_created{handler="MetricsHandler",method="GET"} 1.571094378345321e+09
# HELP tornado_http_requests_total Total of HTTP requests processed
# TYPE tornado_http_requests_total counter
tornado_http_requests_total{handler="MainHandler",method="GET",status="3xx"} 1.0
tornado_http_requests_total{handler="MetricsHandler",method="GET",status="2xx"} 1.0
# TYPE tornado_http_requests_created gauge
tornado_http_requests_created{handler="MainHandler",method="GET",status="3xx"} 1.571094376741933e+09
tornado_http_requests_created{handler="MetricsHandler",method="GET",status="2xx"} 1.5710943783455849e+09
```
