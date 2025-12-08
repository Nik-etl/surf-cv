# surfcam 


- architecture
	Remote sensing

- Server node (home server): 
	Raspi 5 running 24/7

- Command center (Laptop): 
	Laptop with access to server node

- Link (TailScale):
	Mesh VPN allowing SSH access to server node from
	anywhere without exposing ports to public

- Pipeline 
	exact specs TBD
	* CPU optimized
	* Python script scrapes a surf live stream

- Software
	exact specs TBD
	* capturing 1 frame every 5 - 10 seconds
	* OpenCV
	* YOLO

- Storage
	exact specs TBD
	* might be beneficial to use data warehouse techniques
	* utilize ssd on pi 

