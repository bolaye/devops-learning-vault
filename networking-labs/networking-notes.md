   #  Week 4: Networking Cheat Sheet

   ## Core Protocols
   - **DNS (Port 53):** Translates domain names (google.com) to IP addresses (142.250.190.46).
   - **HTTP (Port 80):** Unsecured web traffic.
   - **HTTPS (Port 443):** Secured web traffic (uses SSL/TLS encryption).
   - **SSH (Port 22):** Secure Shell. Used to remotely control Linux servers.

   ## Troubleshooting Commands
   - `nslookup <domain>`: Find the IP address of a domain.
   - `tracert <domain>`: See the router hops to a destination.
   - `curl -I <url>`: Check HTTP headers and server response.
   - `ipconfig`: View local network interfaces and private IP.
   - `netstat -an`: View active network connections and ports.