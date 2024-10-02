---
Subject: Cloud Computing
Teacher: "@Oscar"
Topic: Concepts
date: 2024-09-19
tags:
  - "#SJK005-CloudComputing"
---

# 1.0 Notes

# 1.1 Definitions
*"**Cloud computing** is a model for enabling ubiquitous, convenient, on- demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction. This cloud model is composed of five essential characteristics, three service models, and four deployment models."*

## 1.1 Actors of Cloud Computing

- Cloud Providers
- Cloud Consumers
- End Consumers

>[!quote] Keep in mind
>End Consumers = Consumers of the products of *Cloud Consumers* 

## 1.2 Characteristics of C.C.

- **Fast Provisioning**: Capacidad para el usuario (*Cloud Consumer* ) para cubrir sus necesidades básicas de manera rápida.
- **Auto Provisioning**: Mismo que antes, pero capacidad de que el propio usuario lo gestione
- **Scalability**: Poder ampliarse y reducirse 
- **Elasticity**: Escalabilidad sin que el usuario intervenga, escalabilidad programada
- **Availability**: Minimum down time
- **Security**: 
- **Modularity**:
- **Virtualization**:
- **Isolation**: No interfieren unos con otros

>[!note] Exercice
>***Compare the following scenarios in the "classic" and "cloud" worlds.***
> - *To provision new computers*
> - *To provision new storage*
> - *New software*
> 
> **RESPONSE:**
> 
> - **W/Cloud**: Enlarge subscription, no down time
> - **W/O Cloud**: Buy new devices, wait for delivery, more cost

# 1.2 Deployment models

### 1.2.1 Public cloud

[complete]

### 1.2.2 Private cloud

Equipos del que sirve la web

3 casos:
1. Owned and managed by company for the benefit of its customers
2. Owned by company but managed by a provider
3. Owned and managed by a public cloud provider but as a privet cloud for a client

>[!info] Aclaración 
>La diferencia entre el caso 3 y el publico es que la maquina de la cual se tiene "propiedad" es siempre la misma, no es volatil, ni se virtualiza en algun sitio. En el caso del publico nadie te garantiza que tengas la misma maquina todo el tiempo

### 1.2.3 Hybrid cloud

[complete]
### 1.2.4 Multi-cloud

Dependiendo de qué servicio es, o del usuario final, se puede servir en 2 copias. Una parte publica para el cliente final, y una privada para el uso interno, por ejemplo

>[!example] Ejercicio
>"*Think about the case of a software development company, the company needs: version control system, synchronous communications (on-line meetings) and asynchronous (messaging), document creation and management, payroll, customer relationship, and a long etcetera. Propose a possible solution and justify your choice of cloud for each of the services.*"
>
>SOLUCION:
>- **Version Control System**: Private, sensitive data
>- **Comms**: Public, Teams / Meet
>- **Document creation and management**: Public/Private depending on sensitivity of data
>- **Payroll**
>- **Customer relationship**
>
>`Worth mentioning that this is my choice but for all cases, it depends on the sensitivity of the data`

>[!example] 
>*Compare the results of the previous exercise with a "traditional" approach to provision the same infrastructure.*
>SVN



# 1.2 Modelos de servicios de CC

![[Pasted image 20240920154129.png]]

De abajo arriba:

- **INFRAESTRUCTURA COMO SERVICIO** (**IaaS**): 
	- Máquinas virtualizadas, la base, con ciertas características
	- El usuario se auto-aprovisiona de la potencia, almacenamiento y las capacidades de red
	- User can scale the services on demand: more computing, storage of networking.
	- Optionally, the services can auto-scale: they are elastic, when more is needed, they automatically scale.
	- The user is in charge of:
		- Computing: Selecting the operative system, install all packages needed.
		- Storage: Selecting HD size and king.
		- Networking: Define networking characteristics.
	**POSIBLE GRACIAS A LA VIRTUALIZACION**
	
- **PLATFORM as a SERVICE** (**PaaS**): Libera al usuario de Cloud de desplegar muchas aplicaciones y todas las extensiones, libraries...
	- The user can use different computer languages.
	- The user can choose between different databases, queue frameworks, version control systems, and so on.
	- Deployments can be automatized.
	**POSIBLE GRACIAS A LOS CONTENEDORES**
	
- **SOFTWARE as a SERVICE** (**SaaS**):