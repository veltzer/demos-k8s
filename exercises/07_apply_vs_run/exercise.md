# Apply vs Run

The purpose of this exercise is to compare `kubectl apply` vs `kubectl run`

* Create a python web server that has two URLs:
    * `/` - just serves some content
    * `/crash` - causes the server to die
* run that python individually using:
    `$ kubectl run ...`
    now kill the container by accessing it's `/crash` URL
    What happened?
* run that python as a pod with replication level=1 in k8s with a deployment yaml
    file with the command:
    `$ kubectl apply -f [deployment.yaml]`
    now kill the container by accessing it's `/crash` URL
    What happened?
