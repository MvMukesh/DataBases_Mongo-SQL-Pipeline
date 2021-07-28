# CAP Theorem
#### `CAP Theorem states that a distributed system can only have 2 out of these 3 properties at any given time `
---
![image](https://user-images.githubusercontent.com/26667491/127171483-3a0f2dc9-8ae2-4a73-8ac3-a71a3806452c.png)
* This problem of distributed systems, of choosing b/w either Case-1 or 2 is governed by CAP Theorem

![image](https://user-images.githubusercontent.com/26667491/127172233-79e1dcc6-0670-440d-8098-928d49b079cf.png)

* `Partiton Tolerance`
  * Work despite of partiton or networ failure
  * When Partiton occurs System either provide Consistency or Availability

* `Consistency`
  * No 2 nodes will ever return outdated data
  * Outdated node will wait for a problem to be fixed before processing any request 

* `Availability`
  * Even if partiton b/w nodes, Outdated node can still process requests, although it will return outdated information




