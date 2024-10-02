---
Subject: Big Data Analytics
Teacher: "@RafaelBerlangaLlavori @RafaelBerlangaLlavori"
Topic: 
date: 
tags:
  - "#SJK006-BigDataAnalytics"
---
*Implementing Data Value Chains at large scale*

# 3.0 Concepts:
- Value chain: Transformaciones que dan valor a un producto
- Optimizar procesos así como servicio

# 3.1 Exercise: data chain values
*Caso del bicicas:*
``` c
anchors(uuid, bench_uuid, number) 
bans(uuid, use_uuid, date_start, date_expire, date_created, reason) 
benches_anchors(bench_uuid, anchor_uuid, anchor_number, 
				bicycle_number, date_created) 
benches(uuid, name, latitude, longitude, date_created) benches_notifications(uuid, bench_uuid, notification, priority, date_created) 
bench_messages(uuid, message, date_start, date_expire, date_created) 
bicycles(uuid, number, date_created, status) 
incidents(uuid, error_key, use_uuid, anchor_uuid, status, date_created, bike_uuid) 
loans(uuid, use_uuid, bicycle_uuid, anchor_uuid, date_created, type_access) 
putbacks(uuid, bicycle_uuid, anchor_uuid, date_created) 
users(change_uuid, uuid, document, name, surname, street, city, postcode, birthday, phone, email, gender, date_created, date_change, deleted) 
//processed
bench_status(bench_uuid, date_lastseen, ip, queue, version, number_loans)
loan_historical(uuid, loan_uuid, use_uuid, bicycle_uuid, loan_anchor_uuid, loan_date_created, putback_uuid, putback_anchor_uuid, putback_date_created, type_access, app_loan)
```

| **HISTORICAL**                             | **STREAMING**                                       |
| ------------------------------------------ | --------------------------------------------------- |
| Utilizaciones de cada bicicleta por año    | Bicicletas averiadas / bicicletas operativas        |
| Desplazamientos, de que bench a que bench  | Benches llenos y donde estan                        |
| Tiempo con picos de trafico en algun bench | Bicicletas disponibles en cada bench en tiempo real |
| Utilizaciones anuales por anchor           |                                                     |
| Uso de cada bench con tag de hora          |                                                     |

# 3.2 Value chains
