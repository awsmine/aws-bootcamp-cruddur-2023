# Week 2 — Distributed Tracing

For this week 2, I have decided to **put the code for the homework tasks in the journal**, and write down and document how I completed all the tasks watching Andrew's Videos 2-3x.

I wrote down code for each task on the notepad, and went over the videos again to check and then executed them.

Did commit them to GitHub as and when neccessary.


# Homework Review

Followed instructions from https://github.com/omenking/aws-bootcamp-cruddur-2023/blob/week-2/journal/week2.md, watched videos, took notes carefully on the notepad, went over the videos again, compared them to my notes, and finally executed all the tasks step-wise.


## Videos

- [Week 2 -  AWS Cloud Project Bootcamp - Distributed Tracing - honeycomb.io set up](https://www.youtube.com/watch?v=2GD9xCzRId4)

- [Week 2 - Instrument XRay](https://www.youtube.com/watch?v=n2DTsuBrD_A)

- [Week 2 - CloudWatch Logs](https://www.youtube.com/watch?v=ipdFizZjOF4)

- [Week 2 - Rollbar](https://www.youtube.com/watch?v=xMBDAb5SEU4)

- [Week 2 - X-Ray Subsegments Solved](https://www.youtube.com/watch?v=4SGTW0Db5y0)

- [Week 2 - Observability vs Monitoring Explained in AWS](https://www.youtube.com/watch?v=bOf4ITxAcXc&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=31)

- [Week 2 - Pick the right cloud role: A beginners guide!](https://www.youtube.com/watch?v=E0haz6mymxY&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=35)

- [Week 2 - Honeycomb, Rollbar, AWS X-Ray and AWS Cloudwatch Logs pricing considerations](https://www.youtube.com/watch?v=2W3KeqCjtDY&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=38)

- [Week 2 - Github Codespaces Crash Course](https://www.youtube.com/watch?v=L9KKBXgKopA&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=36)

- [Week 2 - X-Ray Subsegments Solved](https://www.youtube.com/watch?v=4SGTW0Db5y0&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=37)


### 1. Week 2 - AWS Cloud Project Bootcamp - Distributed Tracing - honeycomb.io set up

**Honeycomb** is an opentelemetry standard service. By integrating Honeycomb into our application, we can observe and improve our code by tracing (monitor and analyze the behavior and performance of a system) issues that may occur while ruuning the application. It supports a wide range of data sources, including logs, metrics, and traces, and provides powerful visualization and analysis tools for exploring and understanding this data. 

Traces are a way of tracking the flow of requests through a distributed system. A trace is essentially a record of the interactions between the different components of the system as the request is processed. It includes information about the timing and duration of each interaction, as well as any errors or exceptions that occurred along the way.

**1. Created an anvironment for Cruddur in honeycomb.io to get the API_KEY**

**2. Setting environment variables for Gitpod with API Key for start up**

```
export HONEYCOMB_API_KEY=<"API KEY">
gp env HONEYCOMB_API_KEY=<"API KEY">
```

- Check if the environment variables have been set

```
env | grep HONEY
```

-  Jessica advised not to set honeycomb service name globally, instead to set it up for each service in docker-compose file. If you need to unset the service name,

run this command

```
unset SERVICE_NAME
```
 
**3.  OTEL (open telemetry) variables were added to docker compose for back-end service**

OpenTelemetry (OTEL) is an open source observability framework that assist in generating and capturing telemetry data and send it honeycomb.io

Add the following to the docker compose file for back-end service

```
OTEL_SERVICE_NAME: 'backend-flask'
OTEL_EXPORTER_OTLP_ENDPOINT: "https://api.honeycomb.io"
OTEL_EXPORTER_OTLP_HEADERS: "x-honeycomb-team=${HONEYCOMB_API_KEY}"
```

**4. Add open telemetry libraries (packages) to requirements.txt**

- This is to ensure that these packages are installed when deploying the application, and the backend application will have the necessary instrumentation to generate and export telemetry data to a tracing and monitoring backend service like Honeycomb.io

```
opentelemetry-api 
opentelemetry-sdk 
opentelemetry-exporter-otlp-proto-http 
opentelemetry-instrumentation-flask 
opentelemetry-instrumentation-requests
```

- cd into backend-flask and run the command

```
pip install opentelemetry-api 
```

```
pip install -r requirements.txt
```

**5. Importing required modules from the opentelemetry package for tracing and instrumentation**

- backend-flask/app.py, add

```
# Honeycomb -------
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor


# Honeycomb -------
# Honeycomb - Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)

# Honeycomb - Show spans in console standard output
simple_processor = SimpleSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(simple_processor)


trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)


# Create a flask and initialize automatic instrumentation with Flask
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
```



[commit link - week 2 - commit-instrument honeycomb.pdf]() shows adding the instrument honeycomb to app.py


- git commit -m "instrument honeycomb"

- git push 

**6. cd ../front-end**

```
npm i
```

**7. from root directory** 

```
docker compose up
```


**8. Update .gitpod.yml file to open ports**

```
ports:
  - name: frontend
    port: 3000
    onOpen: open-browser
    visibility: public
  - name: backend
    port: 4567
    visibility: public
  - name: xray-daemon
    port: 2000
    visibility: public
```

- git commit -m "adding ports to .gitpod.yml"

- git push 


- from backend URL, with /api/activities/home, you will see this Raw Data

```
[
  {
    "created_at": "2023-03-01T14:55:13.532950+00:00",
    "expires_at": "2023-03-08T14:55:13.532950+00:00",
    "handle": "Andrew Brown",
    "likes_count": 5,
    "message": "Cloud is very fun!",
    "replies": [
      {
        "created_at": "2023-03-01T14:55:13.532950+00:00",
        "handle": "Worf",
        "likes_count": 0,
        "message": "This post has no honor!",
        "replies_count": 0,
        "reply_to_activity_uuid": "68f126b0-1ceb-4a33-88be-d90fa7109eee",
        "reposts_count": 0,
        "uuid": "26e12864-1c26-5c3a-9658-97a10f8fea67"
      }
    ],
    "replies_count": 1,
    "reposts_count": 0,
    "uuid": "68f126b0-1ceb-4a33-88be-d90fa7109eee"
  },
  {
    "created_at": "2023-02-24T14:55:13.532950+00:00",
    "expires_at": "2023-03-12T14:55:13.532950+00:00",
    "handle": "Worf",
    "likes": 0,
    "message": "I am out of prune juice",
    "replies": [],
    "uuid": "66e12864-8c26-4c3a-9658-95a10f8fea67"
  },
  {
    "created_at": "2023-03-03T13:55:13.532950+00:00",
    "expires_at": "2023-03-04T02:55:13.532950+00:00",
    "handle": "Garek",
    "likes": 0,
    "message": "My dear doctor, I am just simple tailor",
    "replies": [],
    "uuid": "248959df-3079-4947-b847-9e0892d1bab4"
  }
]
```


**9. Create a custom span, added a tracer for this new span for home activities**

- Done as per [HoneyComb documentation](https://docs.honeycomb.io/getting-data-in/opentelemetry/python/)

- check to see your API Key

```
env|grep HONEY
```

- update - backend-flask/services/home_activities.py, with setting an attribute

- code demonstrates how OpenTelemetry can be used to trace and monitor a specific operation within an application by creating and updating spans with attributes and events

```
from opentelemetry import trace

tracer = trace.get_tracer("home.activities")

with tracer.start_as_current_span("home-activities-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
```

- Next I ran custom query grouped by trace.trace_id and chose a trace fron a span and see the expected results.


#### Images

- [week 2 -1-honeycomb-setup.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_2/week%202%20-1-honeycomb-setup.pdf)

- [week 2 -2-honeycomb-span.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_2/week%202%20-2-honeycomb-span.pdf))

- [week 2 -3-honeycomb-trace.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_2/week%202%20-3-honeycomb-trace.pdf)

- [week 2 -4-honeycomb-home-activities-mock-data-trace.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_2/week%202%20-4-honeycomb-home-activities-mock-data-trace.pdf)

- [week 2 -5-honeycomb-app-result_length.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_2/week%202%20-5-honeycomb-app-result_length.pdf)




### 2. Week 2 Instrument XRay
        
**AWS Xray** is similar to Honeycomb. It uses distributed tracing to your applications in order for you to gain insights on latency and performance of your applications. 

- [Github - AWS X-Ray SDK Python](https://github.com/aws/aws-xray-sdk-python)

 **1. Installing AWS X-RAY SDK to the backend-end flask**
 
 - From root directory, cd to backend-flask and add this to the requirents.txt file (to install python dependencies)

```
aws-xray-sdk
```

- then run from backend-flask

```
pip install -r requirements.txt
```

**2. Add to app.py**

- backend-flask/app.py

```
# import X-Ray modules for running the application
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

# configures the X-Ray SDK with the retrieved X-Ray URL for service "backend-flask"
xray_url = os.getenv("AWS_XRAY_URL")
xray_recorder.configure(service='backend-flask', dynamic_naming=xray_url)

# Adding X-Ray middleware
XRayMiddleware(app, xray_recorder)
```

**3. Setup AWS X-Ray Resources - xray.json**
     
- aws/json/xray.json - Create a file xray.json 

```
{
    "SamplingRule": {
        "RuleName": "Cruddur",
        "ResourceARN": "*",
        "Priority": 9000,
        "FixedRate": 0.1,
        "ReservoirSize": 5,
        "ServiceName": "backend-flask",
        "ServiceType": "*",
        "Host": "*",
        "HTTPMethod": "*",
        "URLPath": "*",
        "Version": 1
    }
  }
```

**4. Configuring AWS X-Ray to create a group for the "Cruddur" and filtering traces for the "backend-flask" service**

- from backend-flask, run cli command

```
aws xray create-group \
   --group-name "Cruddur" \
   --filter-expression "service(\"backend-flask\")"
```

- not used

```
FLASK_ADDRESS="https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}" 
```    
  
- **Note: The X-Ray Trace Groups are under X-Ray > New Console > CloudWatch > Settings > Traces > View Settings > Groups**

- [week-2-X-Ray group.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_2/week-2-X-Ray%20group.pdf)

**5. Configure the X-Ray sampling rules for the application with cli**

- run from aws/json

```
aws xray create-sampling-rule --cli-input-json file://xray.json
```

- OR

```
aws xray create-sampling-rule --cli-input-json file://aws/json/xray.json
```

- **Note: The Sampling rules are under CloudWatch > Settings > Traces > View Settings > Sampling rules**


- [week-2-Xray-Sampling rule.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_2/week-2-Xray-Sampling%20rule.pdf)



**6. Adding X-Ray Daemon Container to Docker Compose**

- need to set up a container to host the xray daemon that will be tracing our application

- add to docker-compose.yml

```
# AWS X-Ray Daemon Container
# https://hub.docker.com/r/amazon/aws-xray-daemon
  xray-daemon:
      image: "amazon/aws-xray-daemon"
      environment:
        AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
        AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
        AWS_REGION: ""us-east-1"
      command:
        - xray -o -b "xray-daemon:2000"
      ports:
        - 2000:2000/udp
```

- add these two env vars to our backend-flask in our docker-compose.yml file

```
AWS_XRAY_URL: "*4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}*"
AWS_XRAY_DAEMON_ADDRESS: "xray-daemon:2000"
```

- git commit -m "instrument x-ray"

- git push

[commit link - week 2-commit-instrument-Xray.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_2/week%202-commit-instrument-Xray.pdf) shows adding the instrument x-ray to docker-compose.yml
     
**7. ran docker compose up -d**

- Before you can see the x-ray trace 

- Connect to the Back-end URL from the Gitpod in the ports tab by appending /api/activities/home

- take you to the API page that is hosting the backend for our home_activities.py

- Refresh it few times

- **then Go AWS Console, X-Ray > New Console > CloudWatch > Traces > Run Query**

- X-Ray trace appeared in AWS X-Ray console 

- [week-2-xray-trace.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_2/week-2-xray-trace.pdf)

- Click on a trace 


- [week-2-xray-tracemap.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_2/week-2-xray-tracemap.pdf)

- [week-2-xray-tracemap-segments-timeline.pdf](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_2/week-2-xray-tracemap-segments-timeline.pdf)

**8. Instrumenting Segments and Subsegments code from Olley's article

- [Instrumenting Segments and Subsegments - Olley's article](https://olley.hashnode.dev/aws-free-cloud-bootcamp-instrumenting-aws-x-ray-subsegments)











## Homework Challenges



### 1. Instrument Honeycomb for the frontend-application to observe network latency between frontend and backend[HARD]



### 2. Add custom instrumentation to Honeycomb to add more attributes eg. UserId, Add a custom span



### 3. Run custom queries in Honeycomb and save them later eg. Latency by UserID, Recent Traces

**Images Saved Custom queries**

- [week-2-Heatmap-duration-1](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_2/week-2-Heatmap-duration-1.pdf)

- [week-2-Heatmap-duration-saved-query-2](https://github.com/awsmine/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week_2/week-2-Heatmap-duration-saved-query-2.pdf)




## Knowledge Challenges




## Cloud Technical Essays

### 1. [GitHub - most commonly used commands and sites](https://dev.to/aws-builders/github-most-commonly-used-commands-and-sites-5df7)

### 2.



