from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.gcp.compute import GKE
from diagrams.gcp.database import SQL
from diagrams.gcp.storage import Storage
from diagrams.gcp.network import LoadBalancing

with Diagram("Hybrid Architecture", filename="architecture_diagram", show=False):
    users = Users("Users")

    with Cluster("On-Premises"):
        on_prem_server = Server("App Server")
        on_prem_db = PostgreSQL("Local DB")

    with Cluster("Google Cloud"):
        gke = GKE("Kubernetes Cluster")
        cloud_sql = SQL("Cloud SQL")
        cloud_storage = Storage("Cloud Storage")
        load_balancer = LoadBalancing("Load Balancer")

    users >> Edge(label="HTTP") >> load_balancer >> gke
    gke >> Edge(label="SQL queries") >> cloud_sql
    gke >> Edge(label="File Storage") >> cloud_storage

    load_balancer >> Edge(label="Sync") >> on_prem_server
    on_prem_server >> Edge(label="DB Queries") >> on_prem_db
