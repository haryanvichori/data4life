


<!-- PROJECT LOGO -->
<br />


  <h3 align="center">NEO Explorer </h3>

  <p align="center">
     Near earth object explorer by Preeti for Data4life
    <br />
      </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About">About NEO Exlorer</a></li>
    <li><a href="#Techstack">Techstack</a></li>
    <li><a href="#System-architecture">System architecture</a></li>
    <li><a href="#API-definitions">API definitions</a></li>
    <li><a href="#Getting-Started">Getting Started</a></li>
    <li><a href="#Testing">Testing</a></li>
    <li><a href="#Contact">Contact</a></li>
  </ol>
</details>




## About


NEO Explorer is a backend application which helps you search near earth objects with [RESTFUL APIs](https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/)

### Techstack 

All programming language, web frameworks, databases are the 
tools for a craftsperson called software engineer.
Most of these tools fits well for certain type of business problems.
Here the use case was to develop a small webserver with no specific 
scalability requirements.
I have used mentioned stack 


* [Python 3.8.2](https://www.python.org/downloads/release/python-382/) As Programming language for web server and client
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) As Web Framework
* [SQlite](https://www.sqlite.org/index.html) As database
* [docker](https://www.docker.com/) For containerisation
* [Kubernetes](https://kubernetes.io/) For containerised deployment
* [HELM](https://helm.sh/docs/topics/charts/) As Kubernetes package manager

## System architecture
![plot](system_arch.jpg)


## API definitions
I have created six endpoints 
1. "/" - Root, always returns OK
2. "/probes/liveness" - liveness always returns OK
3. "/probes/readiness" - Tests DB connection Returns OK is server is ready to serve traffic
4. "/neo", methods=['POST'] - POST neo object
5. "/neo/week", methods=['GET'] - Returns count of how many NEO will happen this week
6. "/neo/next", methods=['GET'] - Returns next NEO

**1. Root endpoint**
----
  Always returns OK response

* **URL**

  /

* **Method:**

  `GET`
  
*  **URL Params**
  None

* **Data Params**
  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `OK`
 
* **Error Response:**

  No response from server


**2. Liveness endpoint**
----
  Always returns OK response

* **URL**

  /probes/liveness

* **Method:**

  `GET`
  
*  **URL Params**
  None

* **Data Params**
  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `OK`
 
* **Error Response:**

  No response from server


**3. Readiness endpoint**
----
  Returns OK response if database is serving requests

* **URL**

  /probes/readiness

* **Method:**

  `GET`
  
*  **URL Params**
  None

* **Data Params**
  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `OK`
 
* **Error Response:**

  No response from server


**4. Near earth objects endpoint**
----
  Post data about near earth object using post request.

* **URL**

  /neo

* **Method:**

  `POST`
  
*  **URL Params**
  None

* **Data Params**
 close_approach_date - date in str format
 id - id in integer format
 name - name of object in string format
 nasa_jpl_url - url of object for more info
 is_potentially_hazardous_asteroid - Boolean if asteroid is hazardous

 * **Sample data** 
  {
   "close_approach_date":"2015-Sep-10 08:30",
   "id":3532365,
   "name":"(2010 MH1)",
   "nasa_jpl_url":"http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3532365",
   "is_potentially_hazardous_asteroid":false
  }

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `OK`
 
* **Error Response:**

   * **Code:** 500 <br />
    **Content:** `IntegrityError`
     

**5. Count of Near earth objects next week endpoint**
----
  Get count of NEO next week.

* **URL**

  /neo/week

* **Method:**

  `GET`
  
*  **URL Params**
  None

* **Data Params**
  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** int
 
* **Error Response:**

   * **Code:** 404 <br />
    **Content:** `no obejct found`
     

**6. Next Near earth object endpoint**
----
  Get count of NEO next week.

* **URL**

  /neo/next

* **Method:**

  `GET`
  
*  **URL Params**
  hazardous: boolean 

* **Data Params**
  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** neo object json
 
* **Error Response:**

   * **Code:** 404 <br />
    **Content:** `no object found`
## Getting Started 
## Setting up Neo explorer server
### With docker 

I have pushed latest version of this app to docker hub repository. 
If you do not have docker installed on your system install it from [here](https://docs.docker.com/get-docker/).

Use below commands to pull and run docker container on port 80 of localhost

```
docker pull preety26/data4life:latest
docker run -p 80:80 preety26/data4life 
```

Now you should have application running on your local host.

To verify that docker instances are running use this command to check docker containers.
```
docker ps
```

### WIthout docker

1. If you do not want to use docker ensure you have python3.8 version 
installed on your system form [here](https://www.python.org/downloads/release/python-382/)

2. It's always a good practice to isolate environment of different applications.
For python applications virtual environment is a good way to ensure just that
Install [virtualenv from here](https://pypi.org/project/virtualenv/).

3. Once installed, create a virtualenv and activate it follow this [documentation](https://virtualenv.pypa.io/en/latest/#)

4. Install project dependencies using pip with this command

```
pip install -r requirements.txt
```

5. Use  below command to run flask application on default 5000
   ```sh
   flask run
   ```


## Setting up Client for NASA API server

1. Extract data4life.zip and change your directory to data4life
2. Set up virtual environment and install dependencies using
   ```shell
   pip install -r requirements.txt
   ```
3. Get a free API Key at [https://api.nasa.gov](hhttps://api.nasa.gov)
4. Clone the repo
   set above received api as environment variable using below command
   ```shell
   export NASA_API_KEY=<your_api_key_goes_here>
   ```

5. Please ensure correct endpoint of server is set using `NEO_SERVER_POST_ENDPOINT` 
environment variable.
   ```
   export NEO_SERVER_POST_ENDPOINT=<neo_server_post_endpoint_goes_here>
   ```

6. Run client app to populate database using API endpoints with data from NASA
   ```shell
   python main.py
   ```

## Testing
A wise engineer once said that `Something that is untested is broken.`
Well not always but most often.

I have used [pytest](https://docs.pytest.org/en/6.2.x/) to test the app.

Run tests with below command in project root and relax, pytest will do the job for you
```shell
pytest
```

I have not written extensive test cases, I would to add more tests here.

### Deployment 
This application has been tested with deployment on kubernetes.
I have tried with minikube setup on my mac system.
Use [this link](https://minikube.sigs.k8s.io/docs/start/) to setup minikube cluster on your client machine.


## Deployment with helm charts
Helm claims "Helm is the best way to find, share, and use software built for Kubernetes."
This was my first interaction with helm. 

Please find helm chart files in deployment directory to deploy using helm.

To deploy using helm, use this command inside deployment directory
   ```shell
  helm install neo data4life 
   ```
Above command should return results as below
   ```shell
NAME: neo
LAST DEPLOYED: Fri Jul 16 23:33:10 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=data4life,app.kubernetes.io/instance=neo" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
   ```
To confirm that deployment has actually happened 
Use this command to check if pods actually got deployed 
   ```shell
   kubectl get pods
   ```
This command should response like below
   ```shell
  NAME                             READY   STATUS    RESTARTS   AGE
  neo-data4life-5fff775d67-9pnl5   1/1     Running   0          30s
  neo-data4life-5fff775d67-m5xfx   1/1     Running   0          30s
   ```

We received two parameters because we set 
`replicaCount: 2` in `deployment/data4life/values.yaml`


## Contact

Preeti Bhardwaj - [LinkedIn](www.linkedin.com/in/bhardwaj-preeti) - sharma.pittu101@gmail.com
