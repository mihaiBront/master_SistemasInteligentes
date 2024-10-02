---
Subject: Cyber-physical and Robotic Intelligent Systems
Teacher: "@AngelPascualdelPobilFerré"
Topic: 
date: 2024-09-24
tags:
  - SJK001-Robotics
---
# 2.0 Notes
- Neural networks
- Neural networks representations
- Non-Feedforward neural networks

# 2.1 Paradigms

"*A paradigm is a universally recognizable scientific achievement that, for a time, provides model problems and solutions to a community of practitioners. Scientists accept the dominant paradigm until anomalies are thrown up.*"

>[!example] Pegging shaped holes as a robot:
>
>Two (almost) independent tasks:
>- **Identifying the shape of each object**: Can be "easily" solved with Computer Vision
>- **Correctly taking and placing the shape in its hole** Which is the most complex one, since involves:
>	- Pressure sensors to know when the figure, held by the arm, collides on (cylinder inside the robot's arm, plate made of some material that, by means of a transducer, it can detect pressures)
>	- Orientation of the piece

# 2.2 What is robotic intelligence?

![[Pasted image 20240924160121.png]]

## 2.2.1 Related names:
- **Cognitive robotics**: focused on how humans solve problems
- **Intelligent robotics**: stress on robotics
- **Robotic intelligence**: stress on intelligence
- **Embodied intelligence**: intelligence associated to a physical, biological shape
- **Physical agents**: 
- **Autonomous robot**: :LiEqualNot: Intelligent Robot :LiArrowRight: Explanation of:
	- ***Automated***: Programmed to do a task (like PLC-Controlled machines), wouldn't call it *autonomous* because it can't improvise
	- ***Autonomous***: can survive by itself, can improvise
	- ***Intelligent***: can perform intelligent tasks
	- We can say: $Autonomous \subset Intelligent \subset Automated$
		![[Pasted image 20240924162338.png]]
- 