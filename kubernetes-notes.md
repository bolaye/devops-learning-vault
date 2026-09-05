   # ☸️ Week 7: Kubernetes Cheat Sheet

   ## Core Concepts
   - **Pod:** The smallest unit. Wraps a single container.
   - **Deployment:** The "Boss". Manages replicas of Pods and handles self-healing.
   - **Service:** The permanent network address. Load balances traffic to Pods.
   - **Namespace:** Folders to organize cluster resources.

   ## Essential Commands
   - `kubectl get nodes`: See the servers in the cluster.
   - `kubectl get pods`: See running containers.
   - `kubectl get deployments`: See the "Bosses" managing the pods.
   - `kubectl get services`: See the network endpoints.
   - `kubectl describe pod <name>`: The X-ray machine. Shows events and errors.
   - `kubectl scale deployment <name> --replicas=3`: Scale up or down.
   - `kubectl delete deployment <name>`: Cleanly delete a workload.